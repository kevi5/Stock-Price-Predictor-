import pandas as pd
import numpy as np
import pandas_datareader as pdr

def get_data():
    df = pdr.get_data_yahoo("RELIANCE.NS", start="2015-01-01", end="2022-01-01")
    new_col=np.ones(df.shape[0])
    df["x0"]=new_col
    return df

def drop_data(df):
    df=df.drop([ "High", "Low", "Volume", "Adj Close"],axis=1)
    return df

def min_max(df):
    # df["orginal_Close"]=df["Close"]
    for i in df.columns:
        # df["original"+str(i)]=df[i]
        min_close=df[i].min()
        max_close=df[i].max()
        if min_close!=max_close:
            df[i]=(df[i]-min_close)/(max_close-min_close)
    return df

def denormalize(pred,max_close,min_close):
    pred=pred*(max_close-min_close)+min_close
    return pred

def denormalize_ema(d1,min_close,max_close,a):
    if a==0:
        d1["EMA_unnormalized"]=denormalize(d1["EMA"],max_close,min_close)
        d1["pred_EMA"]=denormalize(d1["pred"],max_close,min_close)
    else:
        d1["EMA_unnormalized"]=d1["EMA"]
        d1["pred_EMA"]=d1["pred"]
    d1['EMA_unnormalized'] = d1['EMA_unnormalized'].shift(-1)
    d1['pred_EMA'] = d1["pred_EMA"].shift(-1)
    d1=d1.dropna()
    return d1
    