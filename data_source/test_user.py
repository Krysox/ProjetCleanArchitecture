from data_source.iuser import IUser
from model.user import User

class TestUser(IUser):

    def find_one(self, user_id) -> User:
        return User(user_id, f"test{user_id}", f"test{user_id}")