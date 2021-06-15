from display.idisplay import IDisplay

class DisplayConsole(IDisplay):

    def displayProduct(self, param):
        if param['isConnected']:
            print(f"As user {param['username']}")
        else:
            print("As public user (not logged)")

        print("Product:")
        print(f"    Name: {param['product']['name']}")
        print(f"    Description: {param['product']['description']}")
        print(f"    Price: {param['product']['price']}")
        print("    Details")
        for key, value in param['product']['details'].items():
            print(f"      Key: {key}, Name: {value}")
