def to_flo(df, cols):
    
    """ convert user-specified columns of a data from object to float"""
    """ input: df - data, cols - a list of numbers (which cols to convert)"""
    
    for i in range(len(cols)):
        df.iloc[:,cols[i]] = df.iloc[:,cols[i]].apply(float)
