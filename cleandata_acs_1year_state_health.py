#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests

def get_health_state_data(year):
    #the address of API are different in different years
    if (year > 2014): 
        addr = "https://api.census.gov/data/{}/acs/acs1/profile?get=DP03_0096PE,NAME&for=state:*&key=fec0e41eb606865dc911dc580210adf7e94fac80".format(year)
    else:
        addr = "https://api.census.gov/data/{}/acs1/profile?get=DP03_0096PE,NAME&for=state:*&key=fec0e41eb606865dc911dc580210adf7e94fac80".format(year)
    
    return requests.get(addr).json()

#save state level health insurance coverage data from 2012 to 2016
for i in range(2012,2017):
    temp = get_health_state_data(i)
    temp2 = pd.DataFrame(data = temp[1:],columns = temp[0])
    file_name = "state_health_{}.csv".format(i)
    temp2.to_csv(file_name)




