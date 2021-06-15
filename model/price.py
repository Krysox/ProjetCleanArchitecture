import model.productCatalog

class Price:

    def __init__(self, id, product: ProductCatalog, updateDate, price):
        self.id = id
        self.product = product
        self.updateDate = updateDate
        self.price = price