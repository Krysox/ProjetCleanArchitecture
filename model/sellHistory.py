from model.user import User
from model.productCatalog import ProductCatalog

class SellHistory:

    def __init__(self, id, user: User, product: ProductCatalog, date):
        self.id = id
        self.user = user
        self.product = product
        self.date = date
        