import sys
from controller import Controller
from data_source.test_price import TestPrice
from data_source.test_user import TestUser
from data_source.test_product import TestProduct
from data_source.test_history import TestHistory
from auth.auth_user_id import AuthUserId
from display.display_console import DisplayConsole

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Product id required", file=sys.stderr)
        exit

    
    product_id = int(sys.argv[1])
    user_id = int(sys.argv[2]) if len(sys.argv) >= 3 else None

    testUser = TestUser()
    testPrice = TestPrice()
    testProduct = TestProduct()
    testHistory = TestHistory()
    testAuth = AuthUserId()
    consoleDisplay = DisplayConsole()

    controller = Controller(testUser, testPrice, testProduct, testHistory, testAuth, consoleDisplay)

    controller.display_product(product_id, user_id)