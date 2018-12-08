import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv("{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols = ['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close' : symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])

    return df

def normalize_data(df):
    #return (df -df.mean()) / (df.max()- df.min())
    return df / df.ix[0,:]

def plot_data(df):
    ax = df.plot(title="Stock Prices", fontsize=12)
    ax.set(xlabel="Date", ylabel = "Price")
    myFmt = mdates.DateFormatter("%m/%y")
    ax.xaxis.set_major_formatter(myFmt)
    plt.show()

def test_run():
    dates = pd.date_range('2010-01-01', '2010-12-31')
    symbols = ['GOOG', 'IBM', 'GLD']
    df = get_data(symbols, dates)
    df = normalize_data(df)
    #print(df)
    #print(df.loc['2010-01-01':'2010-01-31']) #slice rows between 2 dates - note df.ix is depreciated use df.loc
    #slice by column (symbols)
    #print(df['GOOG']) #print only one col
    #print(df[['IBM', 'GLD']]) #print multiple cols
    #print(df.loc['2010-01-01':'2010-01-31', ['SPY', 'IBM']]) #print SPY and IBM for only jan 2010
    #df = df.loc['2010-03-01':'2010-04-01', ['SPY', 'IBM']] #select SPY and IBM for only march 2010 and then plot
    plot_data(df)
    
    
if __name__ == "__main__":
    test_run()
        