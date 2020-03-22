from voters.security import RSA
import hashlib
from chain.trunk import database

keygen = RSA

notfound = "username or password does not exist/is incorrect."


def hash_it(tohash):
    return hashlib.sha512(tohash.encode('utf-8')).hexdigest()


class Rolls:
    def __init__(self):
        self.r = database.Database(pw="yumyum").instance()

    def register(self, u, p):
        userid = hash_it(u)
        password = hash_it(p + userid)
        if userid not in [x.decode() for x in self.r.keys()]:
            self.r.set(userid, password)
        else:
            return print("username already exists. try again, or login.")
        return print("registration completed for user: {}".format(u))

    def reset_password(self, u, op, np):
        userid = hash_it(u)
        password = userid + hash_it(op)
        newpassword = hash_it(np + userid)
        if password == self.r.get(userid).decode():
            self.r.delete(userid)
            self.r.set(userid, newpassword)
        else:
            return print(notfound)
        return print("password change completed for user: {}".format(u))


class Voter:
    def __init__(self):
        self.logged_in = False
        self.u = None
        self.r = database.Database(pw="yumyum").instance()

    def login(self, u, p):
        userid = hash_it(u)
        password = hash_it(p + userid)
        if password == self.r.get(userid).decode():
            self.logged_in = True
            self.u = u
            return print("logged in")
        else:
            return print(notfound)

    def username(self):
        return self.u
