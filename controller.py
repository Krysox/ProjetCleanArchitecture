import model
import auth
import display

from data_source.iuser import IUser
from data_source.iprice import IPrice
from data_source.iproduct import IProduct
from data_source.isellHistory import ISellHistory
from auth.iauth import IAuth
from display.idisplay import IDisplay

class Controller:

    def __init__(self, iuser: IUser, iprice: IPrice, iproduct: IProduct, ihistory: ISellHistory, iauth: IAuth, idisplay: IDisplay):
        self.iuser = iuser
        self.iprice = iprice
        self.iproduct = iproduct
        self.ihistory = ihistory
        self.iauth = iauth
        self.idisplay = idisplay

    def display_product(self, product_id, user_id):

        connected = self.iauth.isAuth(user_id);
        product = self.iproduct.getOne(product_id)
        price = self.iprice.get_last_price_for_product(product_id)

        # A séparer dans un autre service
        if connected:
            history_product_user = self.ihistory.get_history_by_product_and_user_last_year(user_id, product_id)
            history_user = self.ihistory.get_history_by_user_last_six_months(user_id)

            if len(history_product_user) > 5:
                price.price *= 1.05

            elif len(history_user) >= 3:
                print("reduction")
                price.price *= 0.9

        return self.idisplay.displayProduct({
            "isConnected": connected,
            "username": self.iuser.find_one(user_id).name if connected else {},
            "product": {
                "name": product.name,
                "description": product.description,
                "category": product.category,
                "details": product.details,
                "price": price.price
            }
        })