#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:44:35 2020

@author: williamchung
"""

import pandas as pd
from zipfile import ZipFile



def mary_count(df):
    count = 0
    for index, name in enumerate(df['Name']):
        if str(name) == "Mary" and str(df['Sex'][index]) == 'F':
            count += df['Count'][index]
            
    return count

file_names  = []

with ZipFile('names.zip', 'r') as zipObj:
   file_names = zipObj.namelist()

   

def sarah_count(df):
    count = 0
    for index, name in enumerate(df['Name']):
        if str(name) == "Sarah" and str(df['Sex'][index]) == 'F':
            count += df['Count'][index]
            
    return count

def vir_count(df):
    count = 0
    for index, name in enumerate(df['Name']):
        if str(name) == "Vir" and str(df['Sex'][index]) == 'M':
            count += df['Count'][index]
            
    return count

def harley_count(df):
    count = 0
    for index, name in enumerate(df['Name']):
        if str(name) == "Harley" and str(df['Sex'][index]) == 'F':
            count += df['Count'][index]
            
    return count
df_list = []
   
for i in file_names:
    if i[6:14] != "National":
        df = pd.read_csv(i, names=["Name", "Sex", "Count"])
        df["Year"] = i[9:13]
        df_list.append(df)
        

main_dataframe = pd.concat(df_list, sort = False).reset_index()


print(harley_count(main_dataframe))


