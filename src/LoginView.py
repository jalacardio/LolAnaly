from appJar import gui
from LoginController import LoginController


class LoginView:
    app = gui("Login", "400x200")
    lc = LoginController()

    def __init__(self):
        self.app.addLabel("title", "Welcome To LOL Analysis")
        self.app.setLabelBg("title", "grey")

        self.app.addEntry("UserID")

        self.app.setEntryDefault("UserID", "Your Summoner ID")

        self.app.addButtons(["Submit", "Cancel"], self.__press)

        #self.app.setFocus("UserID")

    def __press(self, button):
        if button == "Cancel":
            self.app.stop()
        else:
            self.lc.login(self.app)

    def run(self):
        self.app.go()


if __name__ == '__main__':
    lw = LoginView()
    lw.run()
