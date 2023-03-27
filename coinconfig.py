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
    "profit_percent":0.0018,
    "risk":0.0014,
    "balance_part":0.1,
    "compensation":0.7
}

BTCUSDT= {
    "symbol":"BTCUSDT",
    "asset":"USDT",
    "leverage":50,
    "roundity":3,
    "profit_percent":0.006,
    "risk":0.0016,
    "balance_part":0.25,
    "compensation":0.5
}

DOGEUSDT= {
    "symbol":"DOGEUSDT",
    "asset":"USDT",
    "leverage":50,
    "roundity":0,
    "profit_percent":0.0068,
    "risk":0.0017,
    "balance_part":0.25,
    "compensation":0.2
}

DOGEBUSD= {
    "symbol":"DOGEBUSD",
    "asset":"BUSD",
    "leverage":20,
    "roundity":0,
    "profit_percent":0.0064,
    "risk":0.0018,
    "balance_part":0.5,
    "compensation":0.3
}

EOSUSDT= {
    "symbol":"EOSUSDT",
    "asset":"USDT",
    "leverage":75,
    "roundity":1,
    "profit_percent":0.006,
    "risk":0.0016,
    "balance_part":0.25,
    "compensation":0.5
}

ETHBUSD= {
    "symbol":"ETHBUSD",
    "asset":"BUSD",
    "leverage":50,
    "roundity":3,
    "profit_percent":0.006,
    "risk":0.002,
    "balance_part":0.1,
    "compensation":0.0015,
    "price_divergence":0.0035
}

ETHUSDT= {
    "symbol":"ETHUSDT",
    "asset":"USDT",
    "leverage":50,
    "roundity":3,
    "profit_percent":0.006,
    "risk":0.002,
    "balance_part":0.3,
    "compensation":0.5
}

LTCUSDT= {
    "symbol":"LTCUSDT",
    "asset":"USDT",
    "leverage":75,
    "roundity":1,
    "profit_percent":0.006,
    "risk":0.0018,
    "balance_part":0.25,
    "compensation":0.5
}

BNBBUSD= {
    "symbol":"BNBBUSD",
    "asset":"BUSD",
    "leverage":20,
    "roundity":2,
    "profit_percent":0.006,
    "risk":0.002,
    "balance_part":0.5,
    "compensation":0.5
}
coinlist=[BTCBUSD, BTCUSDT, DOGEUSDT, DOGEBUSD, ETHBUSD, ETHUSDT, EOSUSDT, LTCUSDT, BNBBUSD]