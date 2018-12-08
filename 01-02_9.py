import pandas as pd
import matplotlib.pyplot as plt

#read in csv, plot both the close and adjusted close prices
"""
def test_run():
    df = pd.read_csv("AAPL.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show()
"""

#read in csv, print head, tail, rows 10-20, max close value, and mean of volume
"""
def test_run():
    df = pd.read_csv("AAPL.csv")
    print(df.head())
    print(df.tail())
    print(df[10:21])
    print(df['Close'].max())
    print(df['Volume'].mean())
"""

#declare empty df with indexes of dates
"""
def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    df1 = pd.DataFrame(index=dates)
    print(df1)
"""

#join dfs
def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)

    #declare empty df with index = dates
    df1 = pd.DataFrame(index=dates)

    #read SPY data in
    dfSPY = pd.read_csv("SPY.csv", index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    #join the empty df and SPY df using DataFrame.join() - inner to only keep records that appear in both
    df1 = df1.join(dfSPY, how = 'inner')

    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols = ['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close' : symbol})
        df1 = df1.join(df_temp)


    print(df1)

if __name__ == "__main__":
    test_run()
        