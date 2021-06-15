from data_source.iproduct import IProduct
from model.productCatalog import ProductCatalog

class TestProduct(IProduct):

    def getOne(self, id) -> ProductCatalog:
        return ProductCatalog(id, "Test", "Ceci est un article de test", "jouet", {"taile": "23*24", "matiere": "plastqye"})