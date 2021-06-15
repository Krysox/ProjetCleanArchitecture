from data_source.isellHistory import ISellHistory
from model.sellHistory import SellHistory
from model.productCatalog import ProductCatalog
from model.user import User
from typing import List

class TestHistory(ISellHistory):

    def get_history_by_product_and_user_last_year(self, idUser, idProduct) -> List[SellHistory]:

        product = ProductCatalog(idProduct, "test", "test", "test", "test")
        user = User(idUser, "Test", "test25")

        userHistory = [
            SellHistory(1, user, product, "2021-06-12"),
            SellHistory(2, user, product, "2021-05-12"),
            SellHistory(3, user, product, "2021-04-28"),
            SellHistory(4, user, product, "2021-04-22"),
            SellHistory(5, user, product, "2021-04-16"),
        ]

        if idUser == 2:
            userHistory.append(SellHistory(5, user, product, "2021-04-16"))

        return userHistory

    def get_history_by_user_last_six_months(self, idUser) -> List[SellHistory]:
        product1 = ProductCatalog(1, "test1", "test1", "test1", "test1")
        product2 = ProductCatalog(2, "test2", "test2", "test2", "test2")
        product3 = ProductCatalog(3, "test3", "test3", "test3", "test3")
        user = User(idUser, "Test", "test25")

        userHistory = [
            SellHistory(1, user, product1, "2021-06-12"),
            SellHistory(2, user, product2, "2021-05-12"),
        ]

        if idUser == 1:
            userHistory.append(SellHistory(3, user, product1, "2021-04-22"))

        return userHistory