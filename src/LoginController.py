class LoginController:
    def __init__(self):
        print("Login controller created")

    def login(self, app):
        usr = app.getEntry("UserID")
        print("User: ", usr)