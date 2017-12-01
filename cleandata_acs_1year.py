#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests

#age
a0 = "DP05_0004PE,DP05_0005PE,DP05_0006PE,DP05_0007PE,DP05_0008PE,DP05_0009PE,DP05_0010PE,DP05_0011PE,DP05_0012PE,DP05_0013PE,DP05_0021PE"
#sex, race, employment status
a1 = "DP05_0002PE,DP05_0072PE,DP05_0073PE,DP05_0066PE,DP03_0001PE"
#income
a2 = "DP03_0062E,DP03_0052PE,DP03_0053PE,DP03_0054PE,DP03_0055PE,DP03_0056PE,DP03_0057PE,DP03_0058PE,DP03_0059PE,DP03_0060PE,DP03_0061PE"
#educational attainment
a3 = "DP02_0059PE,DP02_0060PE,DP02_0061PE,DP02_0062PE,DP02_0063PE,DP02_0064PE"
#health insurance coverage
a4 = "DP03_0096PE,DP03_0097PE,DP03_0098PE,DP03_0099PE"
a5 = "DP03_0101PE,DP03_0106PE,DP03_0107PE,DP03_0108PE"
a6 = "DP03_0111PE,DP03_0112PE,DP03_0113PE,DP03_0116PE,DP03_0117PE,DP03_0118PE"

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

for year in range(2012, 2017):
    d0_year = pd.DataFrame(data = get_data("county",year,a0)[1:],columns = get_data("county",year,a0)[0])
    d1_year = pd.DataFrame(data = get_data("county",year,a1)[1:],columns = get_data("county",year,a1)[0])
    d2_year = pd.DataFrame(data = get_data("county",year,a2)[1:],columns = get_data("county",year,a2)[0])
    d3_year = pd.DataFrame(data = get_data("county",year,a3)[1:],columns = get_data("county",year,a3)[0])
    d4_year = pd.DataFrame(data = get_data("county",year,a4)[1:],columns = get_data("county",year,a4)[0])
    d5_year = pd.DataFrame(data = get_data("county",year,a5)[1:],columns = get_data("county",year,a5)[0])
    d6_year = pd.DataFrame(data = get_data("county",year,a6)[1:],columns = get_data("county",year,a6)[0])
        
    data_year = pd.merge(d0_year,d1_year,how='left',on=['NAME','state','county'])
    data_year = pd.merge(data_year,d2_year,how='left',on=['NAME','state','county'])
    data_year = pd.merge(data_year,d3_year,how='left',on=['NAME','state','county'])
    data_year = pd.merge(data_year,d4_year,how='left',on=['NAME','state','county'])
    data_year = pd.merge(data_year,d5_year,how='left',on=['NAME','state','county'])
    data_year = pd.merge(data_year,d6_year,how='left',on=['NAME','state','county'])
    
    filename = "acs_" + str(year) + ".csv"
    data_year.to_csv(filename)
