import mock

symbol = 'GOOGL'

data, meta_data = mock.get_daily_mock()


data_day = data['2019-06-14']

data_day_open = data_day['1. open']


print(symbol + ' Open @ $' + data_day_open)


