from gui.frames import MainFrame
from gui import *


def main():
    """
    This function simply creates the main frame and displays it.
    :return:
    """
    app = MyTk()  # instantiate the app

    m = MainFrame(app)  # instantiate the app's main frame
    m.show()  # show the main frame
    m.mainloop()  # keep it on the screen

