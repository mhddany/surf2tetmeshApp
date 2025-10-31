from PySide6.QtWidgets import QProgressDialog, QWidget
from PySide6.QtCore import QThread, Signal, Qt


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
class FunctionProgressDialog(QProgressDialog):
    def __init__(self, parent=None, label="Working..."):
        super().__init__(label, "Cancel", 0, 0, parent)
        self.setWindowModality(Qt.WindowModal)
        self.setMinimumDuration(0)
        self.setAutoClose(True)
        self.setAutoReset(True)

    def run(self, func, *args, **kwargs):
        self.show()

        self.worker = Worker(func, *args, **kwargs)
        self.worker.finished.connect(self.close)
        self.worker.start()
        return self.worker  # can connect to finished if you want result
