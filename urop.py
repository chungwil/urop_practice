#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:01:45 2020

@author: williamchung
"""

import pandas as pd

from zipfile import ZipFile

file_names  = []

# Opens Zip File
with ZipFile('names.zip', 'r') as zipObj:
   file_names = zipObj.namelist()

# Gets lists of dataframes from each individual txt file
df_list = []  
for txt_file in file_names:
    if txt_file[6:14] != "National":
        df = pd.read_csv(txt_file, names=["Name", "Sex", "Count"])
        df["Year"] = txt_file[9:13]
        df_list.append(df)
        

# Combines the dataframes
main_dataframe = pd.concat(df_list, sort = False).reset_index()

# Unisex names: .5 < boys/girls < 2

 # Group by the name and sex, and adds up the number of times they occur, 
 # getting a total count
groups = main_dataframe.groupby(['Name', 'Sex'], sort=True).sum().reset_index()

#names = [i for i in groups['Name']]


# Loop through the dataframe to calculate if the names are unisex
data = []

for i in range (0, len(groups)-1):
    if groups['Name'][i] == groups['Name'][i+1]:
        if groups['Sex'][i] == "M":
            num_boys = groups['Count'][i]
            num_girls = groups['Count'][i+1]
        else:
            num_boys = groups['Count'][i+1]
            num_girls = groups['Count'][i]
            
        final_value = num_boys / num_girls
        i+1
        if final_value > 0.5 and final_value < 2:
            dic = {}
            dic['Name'] = groups['Name'][i]
            dic['Number'] = num_boys + num_girls
            data.append(dic)
            
new_list = sorted(data, key = lambda i: i['Number'], reverse = True)

final_data = []

for i in range(0,10):
    final_data.append(new_list[i]['Name'])

# Final data has the top ten unisex names since 1880
print(final_data)
    



        


'''for i in groups['Name']:
    filtered = groups.loc[groups['Name'] == i]
    filtered.reset_index()
    if filtered.count ==2 and i not in final_data:
        if filtered['Sex'][0] == "M":
            num_boys = filtered['Count'][0]
            num_girls = filtered['Count'][1]
        else:
            num_boys = filtered['Count'][1]
            num_girls = filtered['Count'][0]
            
        final_value = num_boys / num_girls
        if final_value > 0.5 and final_value < 2:
            final_data.append(i)'''




'''for index, i in enumerate(names):
    temp = i
    #names.pop(0)
    try:
        position = names.index(temp, index+1, len(names))
        if position != -1:
            if groups['Sex'][index] == "M":
                num_boys = groups['Count'][index]
            else:
                num_girls = groups['Count'][index]
        
            if groups['Sex'][position] == "M":
                num_boys = groups['Count'][position]
            else:
                num_girls = groups['Count'][position]
                
            final_value = num_boys / num_girls
            
            if final_value > 0.5 and final_value < 2:
                final_data.append(temp)
    except:
        continue'''

    
        





    
    




