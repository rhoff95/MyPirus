import mock

kSymbol = '01. symbol'
kPrice = '05. price'
kChangePercent = '10. change percent'

quote, ignore = mock.get_global_quote_mock()

symbol = quote[kSymbol]
price = quote[kPrice]
changePercent = quote[kChangePercent]

print("{:4.4s} {:^4.4s} {:4.4s}".format(symbol, str(price), str(changePercent)))
