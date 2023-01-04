'''a 'close' is the value that the stock price closes on on a particular day. the volume is the number of stocks traded. 
the goal is to find the values for each year for each ticker where the volume values were the greatest, and save that data to csv. 
Then do the same with close values'''
import os
import pandas as pd
import glob

def get_ticker(inpath):
    filename = inpath.split(os.path.sep)[-1]
    return filename.split(".")[0]
def money_to_float(x):
    x = x.replace("$", "")
    return float(x)
def to_datetime(x):
    return pd.to_datetime( x, format="%m/%d/%Y")

def grab_highest_value(df, col: str):
    '''input: df dataframe of stock records
    col: str identifying the column
    for the col given, it grabs the highest value for each year. 
    if the value occurs twice, it grabs both'''
    high_per_year = df[["year", col]].groupby("year").max()
    df_high = df.merge(high_per_year, how='inner', on=["year", col])
    df_high.sort_values('year', inplace=True, ignore_index=True)
    return df_high

if __name__=='__main__':
    data_dir = "stock_data"
    list_files = os.listdir(data_dir)
    list_paths = [filepath for filepath in glob.glob(os.path.join(data_dir,"*.csv"))]
    file_path = list_paths[0]
    final_cols = ['ticker',"date", 'close', 'vol', 'open', 'high', 'low', 'year']
    high_close = pd.DataFrame([], columns=final_cols)
    high_vol = pd.DataFrame([], columns=final_cols)
    for file_path in list_paths:
        ticker = get_ticker(file_path)
        print("ticker: ", ticker)
        conv = {"date":to_datetime, 'close': money_to_float, 'vol':int, 'open':money_to_float, 'high':money_to_float, 'low':money_to_float}
        df = pd.read_csv(file_path, names=["date", 'close', 'vol', 'open', 'high', 'low'], skiprows=1, converters =conv)
        df["year"] = df['date'].apply(lambda x: x.year)
        df_vol = grab_highest_value(df, 'vol')
        df_vol.insert(0, 'ticker', ticker)
        high_vol=pd.concat([high_vol, df_vol])
        df_close = grab_highest_value(df, 'close')
        df_close.insert(0, 'ticker', ticker)
        high_close=pd.concat([high_close, df_close])

    high_close.to_csv(os.path.join(data_dir,'results', "highest_close_pyear_pticker.csv"))
    high_vol.to_csv(os.path.join(data_dir,'results', "highest_vol_pyear_pticker.csv"))
