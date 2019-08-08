def check_null(df):
    total_null = df.isnull().sum().sum()
    if total_null > 0:
        print('Total:', total_null)
        return total_null
    else:
        print('No nulls')
        return 0
        
def add_column(name, lst, df):
    df[name] = lst