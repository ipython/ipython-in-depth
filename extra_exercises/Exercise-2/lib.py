"""
Some tools to change a pandas datafrae colum to categories. 
"""
from pandas import Categorical

def categorify(df, keys):
    if isinstance(keys, str):
        keys = (keys, )
        
    for key in keys:
        ## Attempt 1 to make  the column a categorical column
        df[key] = Categorical(df[key])
        ## Attempt 2
        # cat_map = {cat:i for i,cat in enumerate(set(df[key]))}
        # df[key] = df[key].apply(lambda x:cat_map[x])