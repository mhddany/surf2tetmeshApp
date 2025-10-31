from pathlib import Path
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QThread, Signal



# Generic worker that runs any function
class Worker(QThread):
    progress = Signal(int)   # optional progress updates
    finished = Signal(object)  # result of the function

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        # The function can optionally accept a `progress_callback` kwarg
        if "progress_callback" in self.kwargs:
            self.kwargs["progress_callback"] = self.progress.emit

        result = self.func(*self.args, **self.kwargs)
        self.finished.emit(result)


# Reusable progress dialog
class FunctionProgressDialog(QDialog):
    def __init__(self, parent=None, label: str = "Working..."):
        super().__init__(parent)
        self.setWindowTitle("")
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(220, 220)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)

        # Set background to white
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # Hard-coded GIF relative to app directory
        app_dir = Path(__file__).parent
        gif_path = app_dir / "loading_anim_resized.gif"  # make sure loading_anim.gif is in same folder as this script

        self.label_gif = QLabel(self)
        self.movie = QMovie(str(gif_path))
        self.label_gif.setMovie(self.movie)
        self.label_gif.setStyleSheet("border: none;")
        self.movie.start()
        layout.addWidget(self.label_gif)

        self.label_text = QLabel(label, self)
        self.label_text.setAlignment(Qt.AlignCenter)
        
        # Set text color to semi-gray
        self.label_text.setStyleSheet("color: #555555; border: none; font-size: 16px;")
        
        layout.addWidget(self.label_text)

    def run(self, func, *args, **kwargs):
        self.show()

        self.worker = Worker(func, *args, **kwargs)
        self.worker.finished.connect(self.close)
        self.worker.start()
        return self.worker  # can connect to finished if you want result
