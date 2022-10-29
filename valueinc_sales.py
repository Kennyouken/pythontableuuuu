# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:51:59 2022

@author: kenny
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') format

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep = ';')

#summary of the data

data.info()

#Defining variables 

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operation on tableu

ProfitPerItem = 21.11 - 11.73
ProfitPerItem  = SellingPricePerItem - CostPerItem  

ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column Calculation
# variable  = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased


#adding a new column

data['CostPerTransaction'] = CostPerTransaction

#sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']



#rounding

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'],2)


#combining fields

#check data type column

print(data['Time'].dtype)

#change column type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)

my_date = day + '-' + data['Month']+ '-' + year

data['date'] = my_date

#using iloc to view specific columns

data.iloc[3] #run row 3

data.iloc[0] #run row 0

data.iloc[-5:] #last five rows

data.iloc[1000] #row 1000

data.head(5) #brings in 1st 5 rows

data.iloc[:,2] #brings in all rows the 2nd column

data.iloc[4,2] #brings in 4th row 2nd column


data.iloc[0,3]


data.iloc[4:] #brings all the rows except the last four

data.iloc[-4:] #brings the last 4 rows


#see everything on console

pd.options.display.max_columns = None

#reset console to default 

pd.reset_option('display.max_columns')



#using split to split the client keywords field
#new_var = dataframe[column].str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new columns for the split columns for ClientKeywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

data['ItemDescription'] = data['ItemDescription'].str.lower()


#how to merge files 

#bring in new dataset

seasons = pd.read_csv('value_inc_seasons.csv' , sep=";")

#merge_files: merge_df = pd.merge(df_old ,df_new, on = 'key')


data = pd.merge(data,seasons, on='Month')

#drop columns

# df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords' , axis=1) 
data = data.drop('Day' , axis=1) 
data = data.drop(['Year' , 'Month'] , axis=1) 


#export into csv

data.to_csv('ValueInc_Cleaned.csv', index = False)


































