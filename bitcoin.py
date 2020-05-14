import requests
import json
import time


#      __  ______    ____  ______   ______  __        _____ __    _____  __
#     /  |/  /   |  / __ \/ ____/  / __ ) \/ /  _   _|__  // /   /  _/ |/ /
#    / /|_/ / /| | / / / / __/    / __  |\  /  | | / //_ </ /    / / |   / 
#   / /  / / ___ |/ /_/ / /___   / /_/ / / /   | |/ /__/ / /____/ / /   |  
#  /_/  /_/_/  |_/_____/_____/  /_____/ /_/    |___/____/_____/___//_/|_|  
#                                                                          



response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot") #Requete sur l'api de Coinbase
data = response.json() #Indiquer le type de reponse
currency = data["data"]["base"] #recuperer les info
price = data["data"]["amount"]
print(f"Devise : {currency} ( ETHEREUM ) Prix: {price}") #afficher les info
time.sleep(5)
response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
data = response.json()
currency = data["data"]["base"]
price = data["data"]["amount"]
print(f"Devise : {currency} ( BITCOIN ) Prix: {price}")



    