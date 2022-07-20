import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import csv
import numpy as np


df = pd.read_csv (r'jan.csv')

filename = 'jan.csv'
with open('jan.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)



#df.dtypes
#pd.to_datetime(df['Date'])
#df['Date'] = pd.to_datetime(df['Date'])

#col_list = ["fifties", "sixties"]
#print(df["fifties"])
#print(df["sixties"])
#avg works!!!!
#date works!!


df2 = df['fifties'].mean()
print(df2)

df2 = df['sixties'].mean()
print(df2)

df2 = df['seventies'].mean()
print(df2)

df2 = df['eighties'].mean()
print(df2)

df2 = df['nineties'].mean()
print(df2)

df2 = df['twok'].mean()
print(df2)

df2 = df['twenty ten'].mean()
print(df2)

close = ('jan.csv')

dict = {


}


'''

df3 = pd.read_csv (r'feb.csv')


filename = 'feb.csv'
with open('feb.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df2)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)