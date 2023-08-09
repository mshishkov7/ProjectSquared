its a game about squares, get to the red square with your square.
its written in python and pygame.

how to build it.

1. instal pip install pyinstaller
2. run in terminal in the main.py folder -> pyinstaller --onefile --name SquareTap --collect-data assets/chars --collect-data assets/tiles --collect-data assets/fonts --noconsole --icon=main.ico main.py
3. run in terminal -> pyinstaller SquareTap.spec
4. move main.exe from folder "dist" to the main folder.