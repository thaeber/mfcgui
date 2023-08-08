import sys
from PyQt6 import QtGui, QtQml
from pathlib import Path

def main():
    app = QtGui.QGuiApplication(sys.argv)
    
    engine = QtQml.QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    
    path = Path(__file__).parent / 'views' / 'main.qml'
    engine.load(path.as_uri())

    sys.exit(app.exec())

if __name__ == '__main__':
    main()