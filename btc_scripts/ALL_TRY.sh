echo "500 EURO'luk BTC aliminda" > test.txt
BTCEUR=`curl --fail --silent --show-error  -XGET https://www.bitstamp.net/api/v2/ticker/btceur | awk -F"," '{print$2}' | tr -d '"' | awk '{print$2}'`
echo "BTCEUR: $BTCEUR" >> test.txt
BTCTRY=`curl --fail --silent --show-error -XGET https://api.btcturk.com/api/v2/ticker?pairSymbol=BTC_TRY | awk -F"," '{print$4}' | tr -d '"' | awk -F":" '{print$2}'`
echo "BTCTRY: $BTCTRY" >> test.txt
EURTRY=`curl --fail --silent --show-error -XGET https://api.exchangeratesapi.io/latest?symbols=TRY | awk -F"," '{print$1}' | tr -d '"' | tr -d '}'| awk -F":" '{print$3}'`
echo "EURTRY: $EURTRY" >> test.txt
BTCAlim=`echo "500 / $BTCEUR" | bc -l`
echo "BTC alim: 0$BTCAlim" >> test.txt
BTCAlim2=`echo 0$BTCAlim`
EURTRYValue=`echo "500 * $EURTRY" | bc -l`
echo "Euro karsiligi = $EURTRYValue TRY" >> test.txt
BTCTRYValue=`echo "$BTCAlim2 * $BTCTRY" | bc -l`
echo "BTC karsiligi = $BTCTRYValue TRY" >> test.txt
echo "----------------------------------------------------------" >> test.txt
echo "500 EURO'luk XRP aliminda" >> test.txt
XRPEUR=`curl --fail --silent --show-error -XGET https://www.bitstamp.net/api/v2/ticker/xrpeur | awk -F"," '{print$2}' | tr -d '"' | awk '{print$2}'`
echo "XRPEUR: $XRPEUR" >> test.txt
XRPTRY=`curl --fail --silent --show-error -XGET https://api.btcturk.com/api/v2/ticker?pairSymbol=XRP_TRY | awk -F"," '{print$4}' | tr -d '"' | awk -F":" '{print$2}'`
echo "XRPTRY: $XRPTRY" >> test.txt
XRPAlim=`echo "500 / $XRPEUR" | bc -l`
echo "XRP alim: $XRPAlim" >> test.txt
echo "Euro karsiligi = $EURTRYValue TRY" >> test.txt
XRPTRYValue=`echo "$XRPAlim * $XRPTRY" | bc -l`
echo "XRP karsiligi = $XRPTRYValue TRY" >> test.txt
echo "----------------------------------------------------------" >> test.txt
echo "500 EURO'luk ETH aliminda" >> test.txt
ETHEUR=`curl --fail --silent --show-error -XGET https://www.bitstamp.net/api/v2/ticker/etheur | awk -F"," '{print$2}' | tr -d '"' | awk '{print$2}'`
echo "ETHEUR: $ETHEUR" >> test.txt
ETHTRY=`curl --fail --silent --show-error -XGET https://api.btcturk.com/api/v2/ticker?pairSymbol=ETH_TRY | awk -F"," '{print$4}' | tr -d '"' | awk -F":" '{print$2}'`
echo "ETHTRY: $ETHTRY" >> test.txt
ETHAlim=`echo "500 / $ETHEUR" | bc -l`
echo "ETH alim: $ETHAlim" >> test.txt
echo "Euro karsiligi = $EURTRYValue TRY" >> test.txt
ETHTRYValue=`echo "$ETHAlim * $ETHTRY" | bc -l`
echo "ETH karsiligi = $ETHTRYValue TRY" >> test.txt
echo "----------------------------------------------------------" >> test.txt
echo "500 EURO'luk LTC aliminda" >> test.txt
LTCEUR=`curl --fail --silent --show-error -XGET https://www.bitstamp.net/api/v2/ticker/ltceur | awk -F"," '{print$2}' | tr -d '"' | awk '{print$2}'`
echo "LTCEUR: $LTCEUR" >> test.txt
LTCTRY=`curl --fail --silent --show-error -XGET https://api.btcturk.com/api/v2/ticker?pairSymbol=LTC_TRY | awk -F"," '{print$4}' | tr -d '"' | awk -F":" '{print$2}'`
echo "LTCTRY: $LTCTRY" >> test.txt
LTCAlim=`echo "500 / $LTCEUR" | bc -l`
echo "LTC alim: $LTCAlim" >> test.txt
echo "Euro karsiligi = $EURTRYValue TRY" >> test.txt
LTCTRYValue=`echo "$LTCAlim * $LTCTRY" | bc -l`
echo "LTC karsiligi = $LTCTRYValue TRY" >> test.txt
cat test.txt
rm -f test.txt
