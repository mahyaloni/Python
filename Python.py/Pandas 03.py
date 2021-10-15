import pandas_datareader.wb
from datetime import datetime
import matplotlib.pyplot as plt
start = datetime(2015, 1, 1)
end = datetime(2019, 1, 1)
indicator_id = 'FP.CPI.TOTL'
Consumer_price_index = pandas_datareader.wb.download(indicator=indicator_id, start=start, end=end, country=['US', 'CA', 'IRN'])
print(Consumer_price_index)
Consumer_price_index.plot(figsize=(15,8))
plt.ylabel('CPI')
plt.grid()
plt.show()

# output
                        FP.CPI.TOTL
country            year             
Canada             2019   116.757298
                   2018   114.524900
                   2017   111.984831
                   2016   110.224671
                   2015   108.672009
Iran, Islamic Rep. 2019   550.929425
                   2018   393.781630
                   2017   333.673322
                   2016   308.828318
                   2015   287.964094
United States      2019   117.244195
                   2018   115.157303
                   2017   112.411557
                   2016   110.067009
                   2015   108.695722









