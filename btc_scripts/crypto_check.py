import requests

def get_cryeur(token):    
    url_bitstamp="https://www.bitstamp.net/api/v2/ticker/"
    request_bitstamp = requests.get(url_bitstamp + token)
    json_bitstamp = request_bitstamp.json()
    print(token + ":" + json_bitstamp['last'])
    return json_bitstamp['last']

def get_crytry(token):
    url_btcturk="https://api.btcturk.com/api/v2/ticker?pairSymbol="
    request_btcturk = requests.get(url_btcturk + token)
    json_btcturk = request_btcturk.json()
    print(token + ":", json_btcturk.get("data")[0].get("last"))
    return json_btcturk.get("data")[0].get("last")

apikey="xxx"
url_exchange="http://api.currencylayer.com/live?access_key=" + apikey + "&currencies=EUR,TRY&format=1"
request_exchange = requests.get(url_exchange)
json_exchange = request_exchange.json()
usdtry = float(json_exchange["quotes"]["USDTRY"])
usdeur = float(json_exchange["quotes"]["USDEUR"])
eurtry = usdtry / usdeur

amount = float(input("Amount: "))
eur_try_amount = (amount * 0.95) * eurtry


btceur = float(get_cryeur("btceur"))
btc_amount = (amount-5) / btceur
print("BTC amount with", amount, ":%.6f"%btc_amount)
btctry = float(get_crytry("BTC_TRY"))
btc_try_amount = btc_amount * btctry

xrpeur = float(get_cryeur("xrpeur"))
xrp_amount = (amount-5) / xrpeur
print("XRP amount with ", amount, ":%.6f"%xrp_amount)
xrptry = float(get_crytry("XRP_TRY"))
xrp_try_amount = xrp_amount * xrptry

ltceur = float(get_cryeur("ltceur"))
ltc_amount = (amount-5) / ltceur
print("LTC amount with ", amount, ":%.6f"%ltc_amount)
ltctry = float(get_crytry("LTC_TRY"))
ltc_try_amount = ltc_amount * ltctry


etheur = float(get_cryeur("etheur"))
eth_amount = (amount-5) / etheur
print("ETH amount with ", amount, ":%.6f"%eth_amount)
ethtry = float(get_crytry("ETH_TRY"))
eth_try_amount = eth_amount * ethtry


print("-----RESULT-----\nEUR to TRY amount:", int(eur_try_amount))
print("TRY amount with BTC %.6f"%btc_amount ,":", int(btc_try_amount))
print("TRY amount with XRP %.6f"%xrp_amount, ":", int(xrp_try_amount))
print("TRY amount with LTC %.6f"%ltc_amount, ":", int(ltc_try_amount))
print("TRY amount with ETH %.6f"%eth_amount, ":", int(eth_try_amount))
