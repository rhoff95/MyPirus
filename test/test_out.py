#!/usr/bin/env python

from papirus import PapirusTextPos
import mock

kSymbol = '01. symbol'
kPrice = '05. price'
kChangePercent = '10. change percent'

quote, ignore = mock.get_global_quote_mock()

symbol = quote[kSymbol]
price = quote[kPrice]
changePercent = quote[kChangePercent]

line = "{:4.4s} {:^4.4s} {:4.4s}".format(symbol, str(price), str(changePercent))

print(line)

# Same as calling "PapirusTextPos(True [,rotation = rot])"
text = PapirusTextPos(False, 0)
text.Clear()

text.AddText(line, 0, 0, 24, Id="Start1")
text.AddText("ATRS 3.03 +2.4", 0, 24, 24, Id="Start2")
text.AddText("NVDA _145 +.27", 0, 48, 24, Id="Start3")
text.AddText("__MU 32.5 -0.7", 0, 72, 24, Id="Start4")

text.WriteAll()
