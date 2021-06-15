import model.sellHistory

class ISellHistory:

    def get_history_by_product_and_user_last_year(self, idUser, idProduct) -> list[SellHistory]:
        pass

    def get_history_by_user_last_six_months(self, idUser) -> list[SellHistory]:
        pass