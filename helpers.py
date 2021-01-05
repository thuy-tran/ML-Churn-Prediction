import pandas as pd
import numpy as np

def load_data(file,verbose=False):
    data=pd.read_csv('{0}.csv'.format(file))
    if verbose:
        print('\n*'*100)
        print('\n')
        print(data.info())
        print('\n')
        print('\n*'*100)
        print('\n')
        print(data.shape())
        print('\n')
        print('\n*'*100)
        print('\n')
        print(data.head())
        
    return data