import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QFileDialog, QLabel
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


class MP3Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reproductor MP3")
        self.setGeometry(300, 300, 300, 150 )

        self.player = QMediaPlayer()#Motor de reproduccion de la aplicacion

        self.label = QLabel("Archivo no cargado")

        # Botones
        self.open_button = QPushButton("Cargar MP3")
        self.play_button = QPushButton("Reproducir")
        self.pause_button = QPushButton("Pausar")
        self.stop_button = QPushButton("Detener")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.open_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        # Conectar botones a funciones
        self.open_button.clicked.connect(self.open_file)
        self.play_button.clicked.connect(self.player.play)
        self.pause_button.clicked.connect(self.player.pause)
        self.stop_button.clicked.connect(self.player.stop)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo MP3", "", "Archivos MP3 (*.mp3)")
        if file_path:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.label.setText(f"Archivo: {file_path.split('/')[-1]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MP3Player()
    window.show()
    sys.exit(app.exec_())