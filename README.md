# Introduction to Programming for Public Policy (30550)
## Final Project
#### Group Members: Shiyin Jiao, Siyu Wu

### Research Question
**Health Insurance Coverage in the US and Income, and the Impact of the Affordable Care Act**

Medicaid is the largest funding source for medical services for people of all ages with insufficient income and resources to pay for health care, so income level plays a major role in determining eligibility for Medicaid.

Medicaid is jointly funded by the state and federal goverments, and states have some flexibility in deciding who qualifies for coverage.
The Patient Protection and Affordable Care Act (ACA/"Obamacare"), most which took effect in 2014, significantly expanded eligibility for Medicaid, but states have the option of participating in the expansion or not.

What are the impacts of the ACA on health insurance coverage?

### Past Work     

In a Current Population Report by Barnett, Jessica C. and Edward R. Berchick: [Health Insurance Coverage in the United States: 2016](https://www.census.gov/content/dam/Census/library/publications/2017/demo/p60-260.pdf), it was found that people with lower household
income had lower overall health insurance coverage rates than people with higher income. The coverage rate increased by 1.1 percentage points to 86.3 percent for people with household income of less than $25,000, which was the only income group with a statistically
significant change in health insurance coverage between 2015 and 2016.

The Massachusetts insurance market reform of 2006 is a state coverage expansion that has received a great deal of attention. Using a set of policies similar to the ACA, the Massachusetts law decreased the state’s uninsured rate by about 6 percentage points ([Courtemanche & Zapata, 2014](http://onlinelibrary.wiley.com/doi/10.1002/pam.21737/abstract); [Long, Stockley, & Yemane, 2009](http://pubs.aeaweb.org/doi/pdfplus/10.1257/aer.99.2.508)). Using data from the Urban Institute Health Reform Monitoring Survey, Long et al. (2014) compared coverage rates in September 2013 to September 2014 and found an overall increase in coverage of 5.3 percentage points among nonelderly adults. The increase in insurance coverage in Medicaid expansion states was estimated to be 5.8 percentage points, compared to 4.8 percentage points in non-expansion states.

### Data Source
Check-out scripts for the data used in our analysis can be found in my [repository](https://github.com/wusiyu94/final_project).  

* State- and county-level health insurance coverage data, with income and other demographic information

   * American Community Survey 1-Year Data (2011-2016)   
   
     Health insurance coverage is not available in 2011 data.  
   
     2012-14:  
     https://api.census.gov/data/2012/acs1/profile  
     https://api.census.gov/data/2013/acs1/profile   
     https://api.census.gov/data/2014/acs1/profile   
     2015-16:  
     https://api.census.gov/data/2015/acs/acs1/profile/  
     https://api.census.gov/data/2016/acs/acs1/profile/  

   The American Community Survey (ACS) is an ongoing survey that provides data every year -- giving communities the current information they need to plan investments and services. Data files are available for the nation, all 50 states, the District of Columbia, Puerto Rico, every congressional district, every metropolitan area, and all counties and places with populations of 65,000 or more.  
&nbsp;<details><summary>Counties Not Published in ACS 1-Year Data</summary>
Approximately 74 percent or 2,323 of U.S. counties do not have 1-year estimates of health insurance coverage. However, the ACS 1-year county-level estimates cover 85 percent of the total U.S. population.  
Counties Not Published in the ACS 1-Year Estimates, 2015:
![alt text](https://github.com/wusiyu94/final_project/blob/aa0e15d2b528670bc5faea1eecfe2ed8a6f0a359/img/Counties%20Not%20Published%20in%20the%20ACS%201-Year%20Estimates%2C%202015.png "Counties Not Published in the ACS 1-Year Estimates, 2015")  
</details>
    In consideration of the data coverage, we decided to use state-level data for mapping and county-level data for regression analyses.   
    
### Data Cleaning

We collected data directly from ACS API. We queried more than 50 variables from both state- and county-level, from 2012 to 2016.

The data cleaning work could be found at:

https://github.com/wusiyu94/final_project/blob/master/cleandata_acs_1year.py
https://github.com/wusiyu94/final_project/blob/master/relabel_combine.py


### Exploratory Analysis

* All analysis code for our exploratory analyses is included in a single jupyter notebook:
  [exploratory_analysis.ipynb](https://github.com/wusiyu94/final_project/blob/master/exploratory_analysis.ipynb)
  
The analysis is based on maps and graphs that derived from health insurance coverage data from ACS from 2012 to 2016. We expect to find the trend of change in health insurance coverage, look for features and characteriscs of health insurance data, and make some descriptive statistics for the regression analysis.

The analysis includes four parts. 
  
In the first part, we create choropleth maps on precent of health insurance coverage in state level from 2012 to 2016. The map is stored in web format [percent_insurance_2012_2016.html](https://github.com/wusiyu94/final_project/blob/master/img/percent_insurance_2012_2016.html). Should download the whole folder and then open the html.
  
In the second part, we create graph to show the percent of change in private health insurance coverage in state level from 2012 to 2016. The map is stored in web format [percent of change in private health insurance coverage](https://plot.ly/~wusiyu94/22.embed).
  
In the third part, we create graph to show the percent of change in public health insurance coverage in state level from 2012 to 2016. The map is stored in web format [percent of change in public health insurance coverage](https://plot.ly/~wusiyu94/26.embed).   
we also consider the impact of ACA expansion on health insurance coverage, and plot the trend for [ACA's effect](https://github.com/wusiyu94/final_project/blob/master/img/aca_effect.png).
  
In the final part, we create choropleth maps of the percent of no health insurance coverage based on different age group and employment status in 2016. [percent_no_insurance_category.html](https://github.com/wusiyu94/final_project/blob/master/img/percent_no_insurance_category.html). Please download the whole folder and then open the html.


### Regression Analysis

* All analysis code for our regression analyses is included in a single jupyter notebook:
  [Health_Insurance_Coverage.ipynb](https://github.com/wusiyu94/final_project/blob/master/Health_Insurance_Coverage.ipynb)

  To investigate the relationship between income and uninsured rate, we make [scatter plots](https://github.com/wusiyu94/final_project/tree/master/img) with fitted regression lines, with the total population and subpopulations of age groups and employment status. We then develop a OLS regression model based on relevant demographic variables and income measured as median household income, or refined categories of income group.   
  
  To evaluate the effects of the ACA, we use a difference-in-diffence model, comparing changes in uninsured rates at year 2014 in states participating in the Medicaid expansion vs states not participating.
  
### Conclusions

From our OLS regression model, we found statistically significant differences in uninsured rates between our comparison groups, although all are quite small in manitude. Factors we found to have a beneficial effect of decreasing county-level uninsured rates: having higher median income, being male, and having high school diploma or Bachelor's degree compared to >Bachelor's.

Although the directions of effect for some variables are not quite in line with our expectation, we should note that our sample size is very large (>800 counties in 5 years) which could make any small change statistically significant.
From our diff-in-diff model, we found a 4.09 percentage points decrease in uninsured rate, that represents the effect of the fully implemented ACA. Within this 4.09 percentage points decrease, 3.21 percentage points is from the non-Medicaid components of the ACA (insurance market reforms, individual mandate, subsidies, exchanges), and 0.88 (percentage points) is the effect of the Medicaid expansion.

Our findings are consistent with past work that Medicaid expansion did improve health insurance coverage.


