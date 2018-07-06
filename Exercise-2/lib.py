from pandas import Categorical

def categorify(df, keys):
    if isinstance(keys, str):
        keys = (keys, )
        
    for key in keys:
        #df[key] = Categorical(df[key])
        cat_map = {cat:i for i,cat in enumerate(set(df[key]))}
        df[key] = df[key].apply(lambda x:cat_map[x])