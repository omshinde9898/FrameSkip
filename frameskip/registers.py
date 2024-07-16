from pandas import DataFrame
import pandas as pd

def frameRegister(frame : DataFrame):
    meta_data = {}
    for i in frame.columns:
        if isCategorical(frame[i]):
            meta_data[i] = 'catagorical'
        else:
            meta_data[i] = 'Numerical'

    return meta_data



def isCategorical(col):
    isNumeric =  col.dtype != pd.Int64Dtype or col.dtype != pd.Float64Dtype or col.dtype != pd.Int32Dtype or col.dtype != pd.Float32Dtype
    isNumeric =  not isNumeric
    isThreshhold = col.nunique() < (len(col)/10)
    return  isThreshhold and isNumeric