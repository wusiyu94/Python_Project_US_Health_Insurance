#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests


a0 = "DP05_0004PE,DP05_0005PE,DP05_0006PE,DP05_0007PE,DP05_0008PE"
a1 = "DP05_0009PE,DP05_0010PE,DP05_0011PE,DP05_0012PE,DP05_0013PE,DP05_0021PE"
a2 = "DP05_0002PE,DP05_0072PE,DP05_0073PE,DP05_0066PE,DP03_0001PE"
a3 = "DP03_0062PE,DP03_0052PE,DP03_0053PE,DP03_0054PE,DP03_0055PE,DP03_0056PE"
a4 = "DP03_0057PE,DP03_0058PE,DP03_0059PE,DP03_0060PE,DP03_0061PE,DP03_0059PE"
a5 = "DP03_0060PE,DP03_0061PE,DP02_0062PE,DP03_0063PE,DP03_0064PE"
a6 = "DP03_0096PE,DP03_0097PE,DP03_0098PE,DP03_0099PE"

variable_list = [a0,a1,a2,a3,a4,a5,a6]

def get_data(level,year,variable):
    if (level == "county"):
        if (year > 2014):
            addr = "https://api.census.gov/data/{}/acs/acs1/profile?get=".format(year)
            addr = addr+variable+",NAME&for=county:*&in=state:*&key=fec0e41eb606865dc911dc580210adf7e94fac80"
        else:
            addr = "https://api.census.gov/data/{}/acs1/profile?get=".format(year)
            addr = addr+variable+",NAME&for=county:*&in=state:*&key=fec0e41eb606865dc911dc580210adf7e94fac80"
    else:
        if (year > 2014):
            addr = "https://api.census.gov/data/{}/acs/acs1/profile?get=".format(year)
            addr = addr+variable+",NAME&for=state:*&key=fec0e41eb606865dc911dc580210adf7e94fac80"
        else:
            addr = "https://api.census.gov/data/{}/acs1/profile?get=".format(year)
            addr = addr+variable+",NAME&for=state:*&key=fec0e41eb606865dc911dc580210adf7e94fac80"
    return requests.get(addr).json()


d0 = pd.DataFrame(data = get_data("county",2012,a0)[1:],columns = get_data("county",2012,a0)[0])
d1 = pd.DataFrame(data = get_data("county",2012,a1)[1:],columns = get_data("county",2012,a1)[0])
d2 = pd.DataFrame(data = get_data("county",2012,a2)[1:],columns = get_data("county",2012,a2)[0])
d3 = pd.DataFrame(data = get_data("county",2012,a3)[1:],columns = get_data("county",2012,a3)[0])
d4 = pd.DataFrame(data = get_data("county",2012,a4)[1:],columns = get_data("county",2012,a4)[0])
d5 = pd.DataFrame(data = get_data("county",2012,a5)[1:],columns = get_data("county",2012,a5)[0])
d6 = pd.DataFrame(data = get_data("county",2012,a6)[1:],columns = get_data("county",2012,a6)[0])
        

data_2012 = pd.merge(d0,d1,how='left',on=['NAME','state','county'])
data_2012 = pd.merge(data_2012,d2,how='left',on=['NAME','state','county'])
data_2012 = pd.merge(data_2012,d3,how='left',on=['NAME','state','county'])
data_2012 = pd.merge(data_2012,d4,how='left',on=['NAME','state','county'])
data_2012 = pd.merge(data_2012,d5,how='left',on=['NAME','state','county'])
data_2012 = pd.merge(data_2012,d6,how='left',on=['NAME','state','county'])

data_2012.to_csv("acs_2012.csv")

