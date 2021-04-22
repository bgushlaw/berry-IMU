from sklearn import preprocessing
import math
import pandas as pd
import os.path
from os import path
import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import signal
import scipy.signal as scisig
import scipy.stats
import time

def butter_lowpass(cutoff, fs, order=3):
    # Filtering Helper functions
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, 'low', analog=True)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=3):
    # Filtering Helper functions
    cutoff=3
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = scisig.lfilter(b, a, data)
    return y

def butter_highpass(cutoff, fs, order=3):
    # Filtering Helper functions
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, 'high', analog=True)
    return b, a


def butter_highpass_filter(data, cutoff, fs, order=5):
    # Filtering Helper functions
    b, a = butter_highpass(cutoff, fs, order=order)
    y = scisig.lfilter(b, a, data)
    return y

def get_window_stats(data, label=-1):
    mean_features = np.mean(data)
    std_features = np.std(data)
    min_features = np.amin(data)
    max_features = np.amax(data)
    
    features = {'mean': mean_features, 'std': std_features, 'min': min_features, 'max': max_features,
                'label': label}
    return features
  
 def filter_Acc(df):
    global Old_Feature_list
    global New_Feature_list
    
    for x in range(0,3):
        df[New_Feature_list[x]] = butter_lowpass_filter(df[Old_Feature_list[x]], 3.0, 50, 3)
        df[New_Feature_list[x+3]] = butter_highpass_filter(df[Old_Feature_list[x]], 3.0, 50, 3)
        df=df.drop([Old_Feature_list[x]], axis=1)
    return df
  
  def window_feature_extraction(df):
    lower=-1
    upper=1

 
    
    # Remove Subject and activity IDs so we can run the get_windows_stats 
    # function without doing all data manipulation on these values
    df2=df

    
    w=df2.loc[df2.index[0:len(df)]]
        #w = w /w.abs()
        #w = normalize_data(w,lower,upper)
    names = w.columns
    w = preprocessing.normalize(w, axis=0)
    w = pd.DataFrame(w, columns=names)

        #These values shouldnt need to be averaged but this will double check a non integer isnt present
        # which would mean the windowing is wrong.
    
    
    wstats=get_window_stats(w)
    wstats=pd.DataFrame(pd.DataFrame(wstats).drop('label', axis=1))
    wstats=wstats.sort_index()
    wdf = pd.DataFrame(wstats.values.flatten()).T
        
     
        
    #Fix the header to the appropriate names and clean up the indexing  
    wdf.columns=Final_Feature_list
    wdf=wdf.reset_index(drop=True)
    return wdf
  
  def normalize_data(df,lower,upper):
    scaler = preprocessing.MinMaxScaler(feature_range=(lower, upper))
    names = df.columns
    d = scaler.fit_transform(df)
    scaled_df = pd.DataFrame(d, columns=names)
    return scaled_df
  
  def Create_Features(df,file_name,Old_Feature_list,New_Feature_list,Final_Feature_list):
    df=filter_Acc(df)
    wf=window_feature_extraction(df)
    wf.to_csv(file_name+'.csv', mode='a', header=False)
    
    return wf
  
  
  
