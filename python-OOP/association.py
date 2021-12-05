# In Object Oriented Approach, when an object of a class is used as a local variable in another class,
# it is called as "uses-a" relationship or ASSOCIATION.

class Account:
    def __init__(self, acct_no, acct_type):
        self.acct_no = acct_no
        self.acct_type = acct_type

    def authenticate_user(self, user):
        if user.password == 12345 and user.name == "Ebo":
            return "User " \
                   + user.name \
                   + " is logged in " \
                   + self.acct_type + " account no." \
                   + str(self.acct_no) \
                   + " with the right password " \
                   + str(user.password)
        else:
            return "incorrect user name or password"


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


user_a = User("Ebo", 12345)
user_b = User("Sega", 99887)

account_a = Account(110022, "checking")
account_b = Account(336699, "investment")

print("account_a with the RIGHT user name and password: ", account_a.authenticate_user(user_a))
print("account_a with the WRONG user name and password: ", account_a.authenticate_user(user_b))
print("account_b with the RIGHT user name and password: ", account_b.authenticate_user(user_a))
print("account_b with the WRONG user name and password: ", account_b.authenticate_user(user_b))