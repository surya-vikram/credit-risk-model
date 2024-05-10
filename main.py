from src.data_preprocessing import *
from src.feature_selection import *
from src.model import *

if __name__ == "__main__":
    df1, df2 = load_data()
    df1, df2 = remove_nulls(df1, df2)
    df = merge_dataframes(df1, df2)
    df = process_dataframe(df)
    train_model(df.iloc[:, 1:])
    
