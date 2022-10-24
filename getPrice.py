#!/usr/bin/env python3



#Libraries needed below... 
#coinmarketcap api credentials stored in coincreds.py file called by import coincreds


import pygsheets
import json
import coincreds
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


#function to get price of crypto current price... 
def getPrice():	
	#enter coin symbols.. ex. BTC
	coins = ["XRP","HBAR","SAND","VET","SOLO","HNT","BTC","XLM","WLUNC","LRC","ETH","ANKR","GALA","SHIB","ADA","NU","COMP","GRT","FORTH","CVC","BUSD", "AVAX","BR34P","SAFUU","OHM","DRIP","DOGS","AFP","KAVA","CRO","LUNC","FLUX"]
	cell = 3 
	
	#api call to loop through list of coin symbols current prices.... 
	for i in coins:
		url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
		parameters = {
			'symbol': i
		}
		headers = {
			'Accepts': 'application/json',
			'X-CMC_PRO_API_KEY': f"{coincreds.key}",
		}
		
		session = Session()
		session.headers.update(headers)
		
		try:
			response = session.get(url, params=parameters)
			data = json.loads(response.text)
			listing = (data['data'])
			
			#check against crypto symbol using coin name...
			for j in listing[i]:
				#enter coin name.. ex. Bitcoin
				names = ["XRP", "Hedera", "The Sandbox", "VeChain", "Sologenic", "Helium",  "Bitcoin", "Stellar", "Wrapped LUNA Classic", "Loopring", "Ethereum", "Ankr", "Gala", "Shiba Inu", "Cardano", "NuCypher", "Compound", "The Graph", "Ampleforth Governance Token", "Civic", "Binance USD", "Avalanche", "BR34P", "Safuu", "Olympus v2", "Drip Network", "Dogs Token", "Animal Farm Pigs", "Kava", "Cronos", "Terra Classic", "Flux"]
				
				#update google sheet with current prices of crypto symbols.. 
				for k in names:
					if j['name'] == k:
						price=(j['quote']['USD']['price'])
						gc = pygsheets.authorize(service_file='/Users/dbanks/client_secret.json')
						sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/18X4ZyLaYfk6kFQ-waXKGCRfhmxvhheOP2D63q1pniNU/edit#gid=2088748637')
						earnings = sh.worksheet('title', 'Earnings')
						cell += 1
						print("Updating " f"{i} column "  f"H{cell}" + " with price " f"{price}")
						earnings.update_value(f"H{cell}", price)
				
		except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)
			
getPrice()



