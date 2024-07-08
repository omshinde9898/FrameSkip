import os
import pandas as pd
from pandas import DataFrame


def jsonLoader(path):
    """
    Function for loading json data files for experiment
    """
    pass

def imageLoader(path):
    """
    Function for loading image files of folders of images
    """
    pass

def textLoader(path):
    """
    Function for loading plaintext data from .txt file
    """
    pass

def pickleLoader(path):
    """
    Implementation On hold
    """
    pass

def excelLoader(path):
    """
    Function to load excel files
    """
    pass

def csvLoader(path:str) -> (DataFrame | list):
    """
    function to load multiple csv files from directory
    path : path to csv file or directory containing multiple csv files
    args : none
    """
    
    if os.path.isfile(path):
        print(f"Reading Single CSV file from {path}")
        try:
            return pd.read_csv(path)
        except Exception as e:
            print(e)
            exit()
    elif os.path.isdir(path):
        print(f"Reading files from Directory {path}")
        try:
            frames = []
            for file in os.listdir(path):
                frames.append(pd.read_csv(os.path.join(path,file)))
            return frames
        except Exception as e:
            print(e)
            exit()
    else:
        raise FileNotFoundError


def xmlLoader(path):
    """
    Implementation On hold
    """
    pass

def pdfLoader(path):
    """
    Implementation On hold
    """
    pass


def simulateIO():
    path = input("Enter path to data file or directory : ")
    if os.path.isdir(path) or os.path.isfile(path):
        print("choose a file type used to store data : ")
        types= ['pdf','csv','txt','xml','json','images','xls','pickle',]
        for i in types:
            print(f"{i+1} {i}")
        ty = int(input("Enter Index Number : ")) - 1
        match ty:
            case 0:
                return pdfLoader(path)
            case 1 :
                return csvLoader(path)
            case 2 :
                return textLoader(path)
            case 3 :
                return xmlLoader(path)
            case 4 :
                return jsonLoader(path)
            case 5 :
                return imageLoader(path)
            case 6 :
                return excelLoader(path)
            case 7 :
                return pickleLoader(path)
            case _ :
                raise Exception

    else:
        print("Cannot find such path")
        return
    