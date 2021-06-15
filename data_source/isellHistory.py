from model.sellHistory import SellHistory
from typing import List

class ISellHistory:

    def get_history_by_product_and_user_last_year(self, idUser, idProduct) -> List[SellHistory]:
        pass

    def get_history_by_user_last_six_months(self, idUser) -> List[SellHistory]:
        pass