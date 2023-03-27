#!/usr/bin/env python
# coding: utf-8

# In[ ]:

tradeconfig={
    "dualSidePosition":True,
    "marginType":"CROSSED",
    "recvWindow":5000
}

BTCBUSD= {
    "symbol":"BTCBUSD",
    "asset":"BUSD",
    "leverage":50,
    "roundity":3,
    "profit_percent":0.006,
    "diference":0,
    "balance_part":0.4,
    "compensation":0.002,
    "ingebit":2
}

BTCUSDT= {
    "symbol":"BTCUSDT",
    "asset":"USDT",
    "leverage":125,
    "roundity":3,
    "profit_percent":0.006,
    "diference":0.002,
    "balance_part":0.25,
    "compensation":0.15,
    "ingebit":2.5
}

DOGEUSDT= {
    "symbol":"DOGEUSDT",
    "asset":"USDT",
    "leverage":50,
    "roundity":0,
    "profit_percent":0.005,
    "diference":0.002,
    "balance_part":0.2,
    "compensation":0.2,
    "ingebit":2.5
}

DOGEBUSD= {
    "symbol":"DOGEBUSD",
    "asset":"BUSD",
    "leverage":20,
    "roundity":0,
    "profit_percent":0.006,
    "diference":0,
    "balance_part":0.7,
    "compensation":0.15,
    "ingebit":2
}

EOSUSDT= {
    "symbol":"EOSUSDT",
    "asset":"USDT",
    "leverage":20,
    "roundity":0,
    "profit_percent":0.005,
    "diference":0.002,
    "balance_part":0.7,
    "compensation":0.2,
    "ingebit":2
}

ETHBUSD= {
    "symbol":"ETHBUSD",
    "asset":"BUSD",
    "leverage":50,
    "roundity":3,
    "profit_percent":0.0036,
    "diference":0,
    "balance_part":0.5,
    "compensation":0.0015,
    "ingebit":2
}

ETHUSDT= {
    "symbol":"ETHUSDT",
    "asset":"USDT",
    "leverage":50,
    "roundity":3,
    "profit_percent":0.006,
    "diference":0.002,
    "balance_part":0.3,
    "compensation":0.5
}

LTCUSDT= {
    "symbol":"LTCUSDT",
    "asset":"USDT",
    "leverage":75,
    "roundity":1,
    "profit_percent":0.006,
    "diference":0.002,
    "balance_part":0.25,
    "compensation":0.5
}

BNBBUSD= {
    "symbol":"BNBBUSD",
    "asset":"BUSD",
    "leverage":20,
    "roundity":2,
    "profit_percent":0.006,
    "diference":0.002,
    "balance_part":0.5,
    "compensation":0.5
}
coinlist=[BTCBUSD, BTCUSDT, DOGEUSDT, DOGEBUSD, ETHBUSD, ETHUSDT, EOSUSDT, LTCUSDT, BNBBUSD]