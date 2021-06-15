from data_source.iprice import IPrice
from model.price import Price
from model.productCatalog import ProductCatalog

class TestPrice(IPrice):

    def get_last_price_for_product(self, productId) -> Price:
        return Price(
            2, 
            ProductCatalog(5, "jjgjgjg", "jgjgjgj", "jfjfjf", {}),
            "2021-06-12",
            52.16
        )