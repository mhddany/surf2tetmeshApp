# loading_dialog.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import Qt


class LoadingDialog(QDialog):
    """Simple modal loading progress dialog."""

    def __init__(self, message="Processing...", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Please Wait")
        self.setModal(True)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)

        layout = QVBoxLayout(self)

        label = QLabel(message)
        label.setAlignment(Qt.AlignCenter)

        self.progress = QProgressBar()
        self.progress.setRange(0, 0)  # Indeterminate progress
        self.progress.setTextVisible(False)

        layout.addWidget(label)
        layout.addWidget(self.progress)

        self.setFixedSize(300, 100)

        # Optional: Style to match your app
        self.setStyleSheet("""
            QDialog {
                background-color: #FFFFFF;
                border: 1px solid #A0A0A0;
            }
            QLabel {
                color: #000000;
                font-size: 14px;
            }
            QProgressBar {
                border: 1px solid #A0A0A0;
                border-radius: 3px;
                background: #F0F0F0;
            }
            QProgressBar::chunk {
                background-color: #66BB6A;
                width: 10px;
            }
        """)
