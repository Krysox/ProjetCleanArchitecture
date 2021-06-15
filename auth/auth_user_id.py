from auth.iauth import IAuth

class AuthUserId(IAuth):

    def isAuth(self, user_id: int):
        if user_id != None:
            return True

        return False