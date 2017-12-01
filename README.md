# Introduction to Programming for Public Policy (30550)
## Final Project
#### Group Members: Shiyin Jiao, Siyu Wu

### Research Question
Health insurance coverage in the US, and the effect of ACA, income and other demographic variables on health insurance coverage

【TO BE DONE】

### Past Work     

【TO BE DONE】

### Data Sources
Check-out scripts for the data used in our analysis can be found in my [data repository](https://github.com/wusiyu94/final_project/tree/master/data).  

* County-level health insurance coverage data, by selected economic and demographic characteristics

   * Small Area Health Insurance Estimates (SAHIE) [State and County 2006-2015]  
   csv files: https://www2.census.gov/programs-surveys/sahie/datasets/time-series/estimates-acs/  
   
   API information: api.census.gov/data/timeseries/healthins/sahie.html
   
   The U.S. Census Bureau’s Small Area Health Insurance Estimates program produces the only source of data for single-year estimates of health insurance coverage status for all counties in the U.S. by selected economic and demographic characteristics. The SAHIE model-based estimates are a vital source of information for assessing year-to-year change in health insurance coverage at the county level.

* State-level health insurance coverage data, with income and other demographic information: age, sex, race/ethnicity, etc

   * American Community Survey 1-Year Data (2011-2016)  
   https://api.census.gov/data/2016/acs/acs1/profile/  

   The American Community Survey (ACS) is an ongoing survey that provides data every year -- giving communities the current information they need to plan investments and services. Data files are available for the nation, all 50 states, the District of Columbia, Puerto Rico, every congressional district, every metropolitan area, and all counties and places with populations of 65,000 or more.  
&nbsp;<details><summary>Counties Not Published in ACS 1-Year Data</summary>
Approximately 74 percent or 2,323 of U.S. counties do not have 1-year estimates of health insurance coverage. However, the ACS 1-year county-level estimates cover 85 percent of the total U.S. population.  
Counties Not Published in the ACS 1-Year Estimates, 2015:
![alt text](https://github.com/wusiyu94/final_project/blob/master/Counties%20Not%20Published%20in%20the%20ACS%201-Year%20Estimates%2C%202015.png "Counties Not Published in the ACS 1-Year Estimates, 2015")  
</details>

### Data Cleaning

We collect data directly from ACS API. We uses more than 50 variables in both state and county level, from 2012 to 2016.

The data cleaning work could be found at:

https://github.com/wusiyu94/final_project/blob/master/cleandata_acs_1year.py
https://github.com/wusiyu94/final_project/blob/master/relabel.py


### Exploratory Analysis

* Fisrt of all, we create choropleth map on health insurance coverage in state level from 2012 to 2016.

The code for this map is included in a jupyter notebook:
https://github.com/wusiyu94/final_project/blob/master/persent_insurance_2012_2016.ipynb 

And the map is presented in web format, which could be found at here:
https://github.com/wusiyu94/final_project/blob/master/persent_insurance_2012_2016.html

* Next, we create map to show the persent of change in public and private health insurance coverage in state level from 2012 to 2016.

The code for the map of public health insurance is included in a jupyter notebook:
https://github.com/wusiyu94/final_project/blob/master/persent_insurance_public.ipynb

And the map is presented in web format, which could be found at here: 
https://plot.ly/~wusiyu94/20

The code for the map of private health insurance is included in a jupyter notebook:
https://github.com/wusiyu94/final_project/blob/master/persent_insurance_private.ipynb

And the map is presented in web format, which could be found at here: 
https://plot.ly/~wusiyu94/18

* Finanly, we look at the persent of no health insurance coverage based on different age group and employment status in 2016. 

The code for the map is included in a jupyter notebook:
https://github.com/wusiyu94/final_project/blob/master/persent_no_insurance_category.ipynb
And the map is presented in web format, which could be found at here: 
https://github.com/wusiyu94/final_project/blob/master/persent_no_insurance_category.html


### Regression Analysis

【TO BE DONE】

### Conclusions

【TO BE DONE】

*	Baseline functionality

We propose to examine annual trends in health insurance coverage for all US counties, and demographic and economic differences in coverage status for years 2009-2015, using SAHIE. We will create visual presentations of health insurance coverage by county, and stratify by age group and income level. We will then clean up and merge data from 2009-2015 on health insurance coverage with data on income and other relevant demographics in ACS, on a county level (we wanted to do census tract level but couldn’t find census tract level health insurance data). To investigate the association between coverage status and income, we will examine descriptive statistics and develop a sensible regression model based on relevant demographic variables and income measured as mean/median income, categorized income group, or poverty rate, as well as other alternative specifications. Because Medicaid covers low income and disabled people while Medicare covers people aged 65 and older, we will evaluate which population group is actually the most uninsured, and could benefit from policy changes.

* Possible extensions
  * Animated map showing changes over the years in uninsured rates by county
  * Graphs showing uninsured rates across age groups and income levels
  * Build a navigable website to present all visualizations and data analyses  
  * Others as we get to learn more
