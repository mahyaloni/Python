from datetime import datetime
import pandas_datareader.data as web
import pandas as pd
start = datetime(2018,1,1)
end = datetime(2019,1,1)
df = web.DataReader('AAPL','yahoo', start, end)
print(df.head())

# output
              High        Low       Open      Close       Volume  Adj Close
Date                                                                          
2018-01-02  43.075001  42.314999  42.540001  43.064999  102223600.0  41.248268
2018-01-03  43.637501  42.990002  43.132500  43.057499  118071600.0  41.241089
2018-01-04  43.367500  43.020000  43.134998  43.257500   89738400.0  41.432655
2018-01-05  43.842499  43.262501  43.360001  43.750000   94640000.0  41.904377
2018-01-08  43.902500  43.482498  43.587502  43.587502   82271200.0  41.748734

