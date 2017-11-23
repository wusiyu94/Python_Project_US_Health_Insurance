#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


def sahie_data_import(year):
    string_year = str(year)
    filename = "sahie_"+string_year+".csv"
    sahie = pd.read_csv(filename,skiprows=78,
                             usecols=[0,2,3,4,5,6,7,8,9,11,13,15,17,19,21,23,24],
                             low_memory=False)
    sahie["state_name"]= sahie["state_name"].map(str.strip)
    sahie["county_name"]= sahie["county_name"].map(str.strip)
    return sahie


#append data from 2009 to 2015
sahie_data = sahie_2009
for i in range(2010,2016):  
    sahie_data = sahie_data.append(sahie_data_import(i))

sahie_data.to_csv("sahie_data.csv")
