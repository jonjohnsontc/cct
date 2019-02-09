import numpy as np
import pandas as pd 



class Clean:
    def __init__(self):
        self.clean_terms = cleaning_dict
    

    def clean_series(self, series, terms, substitute=''):
    '''
    Iterates through pandas series of strings and applies regex
    based substitutions for items passed into cleaning_dictionary
    
    Parameters:
    -----------
    series : pandas series, a series of strings to perform operations on
    terms : list, items to substitute 
    substitute : str default='', Item to substitue in place of string
    '''
    for item in cleaning_dictionary:
        series = series.iloc[:].apply(lambda x: re.sub(\
                                                cleaning_dictionary[item],
                                                substitute))
        return series
        
    


cleaning_dict = {
    'single quote mark': r"\"",
    'dbl quote mark': r"\'",
    'brackets': r' \[.*',
    'parenthesis': r'(\s\(.*\))',
    'feat artist': r'( feat\..*)',
    'hyphens' : r' -.*',
}