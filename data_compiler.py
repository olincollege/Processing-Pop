import pandas as pd

# Read in your .csv files as dataframes using pd.read_csv()
df_1960s = pd.read_csv("1960s.csv")
df_1970s = pd.read_csv("1970s.csv")
df_1980s = pd.read_csv("1980s.csv")
df_1990s = pd.read_csv("1990s.csv")
df_2000s = pd.read_csv("2000s.csv")
df_2010s = pd.read_csv("2010s.csv")



# This method combines a list of pandas dataframes into one dataframe
master_dataframe = pd.concat([df_1960s, df_1970s, df_1980s, df_1990s, df_2000s, df_2010s])
