#!/usr/bin/env python

import pandas as pd

insurance_combined = pd.DataFrame()
for year in range(2012,2017):
    filename = "acs_" + str(year) + ".csv"
    insurance_year = pd.read_csv("data/" + filename, index_col = ["county"])
    insurance_year.rename(columns = {"NAME":"County, State", "state":"State FIPS",
        #age
        "DP05_0004PE":"Under 5 years", "DP05_0005PE":"5 to 9 years", "DP05_0006PE":"10 to 14 years", 
        "DP05_0007PE":"15 to 19 years", "DP05_0008PE":"20 to 24 years", "DP05_0009PE":"25 to 34 years", 
        "DP05_0010PE":"35 to 44 years", "DP05_0011PE":"45 to 54 years", "DP05_0012PE":"55 to 59 years",
        "DP05_0013PE":"60 to 64 years", "DP05_0021PE":"65 years and over", "DP05_0018PE":"18 years and over",
        #sex, 
        #race (values missing for 57,74,49 counties in 2012,13,14, won't use in regression), 
        #employment status
        "DP05_0002PE":"Male", "DP05_0072PE":"Non-Hispanic White", "DP05_0073PE":"Non-Hispanic Black", 
        "DP05_0066PE":"Hispanic or Latino", "DP03_0005PE":"Unemployed (>=16 years,In civilian labor force)",
        #income
        "DP03_0062E":"Median household income", "DP03_0052PE":"Less than $10,000", "DP03_0053PE":"$10,000 to $14,999", 
        "DP03_0054PE":"$15,000 to $24,999", "DP03_0055PE":"$25,000 to $34,999", "DP03_0056PE":"$35,000 to $49,999", 
        "DP03_0057PE":"$50,000 to $74,999", "DP03_0058PE":"$75,000 to $99,999", "DP03_0059PE":"$100,000 to $149,999", 
        "DP03_0060PE":"$150,000 to $199,999", "DP03_0061PE":"$200,000 or more", 
        #educational attainment
        "DP02_0059PE":"Less than 9th grade", "DP02_0060PE":"9th to 12th grade, no diploma", "DP02_0061PE":"High school graduate", 
        "DP02_0062PE":"Some college, no degree", "DP02_0063PE":"Associate's degree", "DP02_0064PE":"Bachelor's degree",
        #health insurance coverage
        "DP03_0096PE":"With health insurance coverage", "DP03_0097PE":"With private health insurance", 
        "DP03_0098PE":"With public health insurance", "DP03_0099PE":"No health insurance coverage",
        "DP03_0101PE":"<18 years, No insurance", "DP03_0106PE":"18-64, Employed, With private insurance", 
        "DP03_0107PE":"18-64, Employed, With public insurance", "DP03_0108PE":"18-64, Employed, No insurance",
        "DP03_0111PE":"18-64, Unmployed, With private insurance", "DP03_0112PE":"18-64, Unmployed, With public insurance", 
        "DP03_0113PE":"18-64, Unmployed, No insurance", "DP03_0116PE":"18-64, Not in labor force, With private insurance", 
        "DP03_0117PE":"18-64, Not in labor force, With public insurance", "DP03_0118PE":"18-64, Not in labor force, No insurance"
        }, inplace = True)
    insurance_year.drop('Unnamed: 0', axis=1, inplace=True)
    insurance_year["Year"] = year
    
    #insurance_norace_year = insurance_year[insurance_year["Non-Hispanic White"]=="N"]
    #print(len(insurance_norace_year))
    
    # Re-Categorize
    insurance_year["Under 18 years"] = 100 - insurance_year["18 years and over"]
    insurance_year["18 - 64 years"] = insurance_year["18 years and over"] - insurance_year["65 years and over"]
    insurance_year["< High school"] = insurance_year["Less than 9th grade"] + insurance_year["9th to 12th grade, no diploma"]
    insurance_year["Associate's/Bachelor's degree"] = insurance_year["Associate's degree"] + insurance_year["Bachelor's degree"]
    insurance_year = insurance_year.apply(pd.to_numeric, errors='coerce')
        
    insurance_combined = insurance_combined.append(insurance_year)

insurance_2012 = insurance_combined[insurance_combined["Year"] == 2012]
insurance_2013 = insurance_combined[insurance_combined["Year"] == 2013]
insurance_2014 = insurance_combined[insurance_combined["Year"] == 2014]
insurance_2015 = insurance_combined[insurance_combined["Year"] == 2015]
insurance_2016 = insurance_combined[insurance_combined["Year"] == 2016]
