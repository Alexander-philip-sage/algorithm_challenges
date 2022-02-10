import os
import pandas as pd
import numpy as np

def get_ticker(inpath):
    filename = inpath.split(os.path.sep)[-1]
    return filename.split(".")[0]
def money_to_float(x):
    x = x.replace("$", "")
    return float(x)
def to_datetime(x):
    return pd.to_datetime( x, format="%m/%d/%Y")

def get_high_vol(df):
    high_vol_sm = df[["year", 'vol']].groupby("year").max()
    return df.merge(high_vol_sm, how='inner', on=["year", 'vol'])

def get_high_close(df):
    max_close_sm = df[["year", "close"]].groupby("year").max()
    good = []
   
    year_to_close = {}
    for index, data in max_close_sm.iterrows():
        year_to_close[int(index)]= data[0]

    for index, data in df.iterrows():
        close = year_to_close[data["year"]]
        if close==data["close"]:
            good.append(True)
        else:
            good.append(False)
    return df[good]


if __name__=='__main__':
    data_dir = "./data/"
    list_files = os.listdir(data_dir)
    list_paths = [data_dir + file for file in list_files]
    file_path = list_paths[0]
    all_answers = []
    for file_path in list_paths:
        print("ticker: ", get_ticker(file_path))
        conv = {"date":to_datetime, 'close': money_to_float, 'vol':int, 'open':money_to_float, 'high':money_to_float, 'low':money_to_float}
        df = pd.read_csv(file_path, names=["date", 'close', 'vol', 'open', 'high', 'low'], skiprows=1, converters =conv)
        df["year"] = df['date'].apply(lambda x: x.year)

        all_answers.append([get_high_vol(df), get_high_close(df)])
    
