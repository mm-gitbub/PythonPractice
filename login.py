
def login(user_name, password):
    if (user_name == "user" and password == "passwd"):
        return True
    else:
        return False
assert login("user", "patsswd") == True, "Login is failed!"
