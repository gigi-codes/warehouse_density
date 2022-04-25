# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Health Outcomes: Proximity to Distributions Hubs
---

> #  TO DO 
> * CLEAN `all_processed` file in `processed_data` directory: 
>   * all four ES datasets
>   * warehouse-data for 4 years from census 
>   * still has `NaN`, etc. but otherwise ready for modelling
> * SLLIDES 
> * CLEAN UP `REPOSITORY`
>   * I am happy to volunteer to do this: 
>       * one directory with all our sheets, renumbered
>       * remove superflous direcetories 
>       * I've had a mini-TOC at the top of each of my nb for previous projects, I can do this for ours as well 

> # NOTES
> #### _4/24_
> * `processed_data` directory has all files ready for `imputing`, etc. 
> * `05_merged` nb in `Giovanna` directory has some initial EDA
>
> #### _4/22_ 
> * I messed up <b>David's</b> initial EDA notebook trying to add my last name. Don't know how to fix it right now, but can confirm previous versions ARE saved and accessible via github's version /revision history. Will look into this later. 

---
---
---


## Model health outcomes given traffic volumes, density of warehouse/fulfilment centers
* Predict 2021 given 2013, 2014, 2018 data? 
* Specifically rate of hospitalization per 10,000 for: 
    * asthma
    * _low birth weight_ ?
* MEASURABLE: incidence change over four time periods 
* Relevant: YES. We care about the cost of our online shopping? 
* Time-bound: YES: We have to select the period/ years we wish to model.
* NOVEL: really good work, David, in compiling # of warehouses !!! 

## _Target? Goal_
We are 
* regressing, 
* classifying, 
* using some forests
* using (un)/supervised neural network to
* model health outcomes  

---
## Data: _CA Enviornmental & Health_

 Source                                                      | File          | Date  |
 ---                                                         | ---           | ---   |
 <a href = "https://oehha.ca.gov/calenviroscreen/report-general-info/calenviroscreen-10"> CalEnviroScreen 1 </a> |  <a href = "https://github.com/gigi-codes/CO2_modelling/blob/g_branch/raw_data/calenviroscreendatav11.xls"> Data (xlsx) </a> | April 2013 
 <a href = "https://data.ca.gov/dataset/calenviroscreen-2-0"> CalEnviroScreen 2 </a> |  <a href = "https://oehha.ca.gov/media/downloads/calenviroscreen/report/ces20updateoct2014.xlsx"> Data (xlsx) </a> | Oct 2014 
<a href = "https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-30"> CalEnviroScreen 3 </a>  | <a href =  "https://oehha.ca.gov/media/downloads/calenviroscreen/document/ces3results.xlsx"> Data (xlsx) </a>     | June 2018 
 <a href = "https://calenviroscreen-oehha.hub.arcgis.com"> CalEnviroScreen 4 </a> | <a href = "https://calenviroscreen-oehha.hub.arcgis.com"> Data, Dictionarty ZIP </a>| Oct 2021 
 
**Dataset Description:** data from State of California including health outcomes, zip codes, traffic volumes, and hospitalization rates. Dictionaries below. 

## Data: _Warehouse Density_
<a href = "https://www2.census.gov/programs-surveys/cbp/datasets/"> US Census Bureau  </a> 
<a href = " "> Data Descriptions </a> 



## Data: _Dictionaries_
Data dictionary (describe every feature in your data set, or at least those features that were prominent in your final model)

variable name   | Type      | Description 
---             | ---       | ---   
asthma          | numeric   | incidence rate, cases/ 10k population
cardiovasccular | numeric   | incidence rate, cases/ 100 population
low birth weight| numeric   | % born `< 2500 g`
diesel pm       | numeric   | particulate matter, spatially modelled
ozone           | numeric   | concentration
traffic         | numeric   | volume: vehicles per length of time over fixed distance


## _Exploratory Data Analyses_ 
Consider including a plot or two from your EDA

---
## _Model Performance_ 
* Model performance on training/test data
* Did you fit many models? Feel free to summarize some of your scores here.
* Consider useing a markdown table to make results easy to review.
* It should be clear which model you chose for production and why.

> PLACEHOLDER TABLE FOR RESULTS 

Model   | Transformer       | Regularization        | $n$  | Train   
---     |---                | ---                   | ---  | ---     
1       | Linear Regression | Logistic Regressor    | 2605 | 0.7373  
2       | Count Vectorizer  | Logistic Regressor    | 4537 | 0.7111  
3       | Count Vectorizer  | Random Forest	        | 4537 | 0.7569  


## _Model Selection and Findings_
Primary findings/conclusions/recommendations
These should follow from your project

## _Discussion_ 
* Some confounding factors: 
    * overall inrease in ppm in CA because of fires
    * overal increase in VMT in CA because of ... our poor planning 


## _Conclusion_
You should provide an answer to your problem statement

---
## _Next Steps_
Always focus on the positive (it's not what you did wrong, it's what you look forward to improving).
Is your model ready for production? Probably not, but you can comment on how it might get there.
Does this project demonstrate skills that you think could be applied to similar problems?

> ### Background: From the Press 
* <a href ="https://www.epi.org/publication/unfulfilled-promises-amazon-warehouses-do-not-generate-broad-based-employment-growth/"> EPI: Warehouses Do Not Generate Broad-Based Employment </a> (cites the source I have for fulfillment center locations)
* <a href = https://www.cbre.com/insights/local-response/2022-north-america-industrial-big-box-los-angeles-county> CBRE: 2022 North America Industrial Big Box Review & Outlook: Los Angeles County</a>
> 

--- 
### ADDENDUM: _make reusable functions_
Writing code in functions serves many purposes, but for the purpose of these projects I want to focus on two.

Writing functions to perform individual tasks will clarify, to you as well as the reader, what each line of code is doing. Just like how we use separate notebooks to allow readers to keep distinct tasks separated in their minds, functions can serve an identically helpful organizational purpose.
When you are interviewing, you will absolutely be expected to write functions since that is how code is, in practice, written and used. It is genuinely a very important part of writing code.

---
---

> ## Data Dictionaries, _cont._
<br>

> ### For `ZBP[YR]DETAIL.TXT` files

| Name     | Data Type | Description                                                 |
|----------|------|-------------------------------------------------------------|
| ZIP      | C    | ZIP Code                                                    |
| NAICS    | C    | Industry Code - 6-digit NAICS code.                         |
| EST      | N    | Total Number of Establishments                              |
| N1_4     | N    | Number of Establishments: 1-4 Employee Size Class           |
| N5_9     | N    | Number of Establishments: 5-9 Employee Size Class           |
| N10_19   | N    | Number of Establishments: 10-19 Employee Size Class         |
| N20_49   | N    | Number of Establishments: 20-49 Employee Size Class         |
| N50_99   | N    | Number of Establishments: 50-99 Employee Size Class         |
| N100_249 | N    | Number of Establishments: 100-249 Employee Size Class       |
| N250_499 | N    | Number of Establishments: 250-499 Employee Size Class       |
| N500_999 | N    | Number of Establishments: 500-999 Employee Size Class       |
| N1000    | N    | Number of Establishments: 1,000 or More Employee Size Class |  

> ### For `ZBP[YR]TOTALS.TXT` files 

| Name    | Data Type | Description           |
|---------|------|-----------------------|
| ZIP     | C    | ZIP Code              |
| NAME    | C    | ZIP Code Name         |
| EMPFLAG | C    | Data Suppression Flag |
| EMP_NF   | C | Total Mid-March Employees Noise Flag (flat definitions in table below) |
| EMP      | N | Total Mid-March Employees with Noise                                                           |
| QP1_NF   | C | Total First Quarter Payroll Noise Flag                                                         |
| QP1      | N | Total First Quarter Payroll ($1,000) with Noise                                                |
| AP_NF    | C | Total Annual Payroll Noise Flag                                                                |
| AP       | N | Total Annual Payroll ($1,000) with Noise                                                       |
| EST      | N | Total Number of Establishments                                                                 |
| CITY     | C | ZIP City Name                                                                                  |
| STABBR   | C | ZIP State Abbreviation                                                                         |
| CTY_NAME | C | ZIP County Name                                                                                |

> ### For `CBP[YR]CO.TXT` files 

| Name     | Data Type | Description                         |
|----------|------|-------------------------------------|
| FIPSTATE | C    | FIPS State Code                     |
| FIPSCTY  | C    | FIPS County Code                    |
| NAICS    | C    | Industry Code - 6-digit NAICS code. |
| EMPFLAG  | C    | Data Suppression Flag               |
| EMP_NF                  | C | Total Mid-March Employees Noise Flag (Noise Flag below)
| EMP                     | N | Total Mid-March Employees with Noise                                                           |
| QP1_NF                  | C | Total First Quarter Payroll Noise Flag                                                         |
| QP1                     | N | Total First Quarter Payroll ($1,000) with Noise                                                |
| AP_NF                   | C | Total Annual Payroll Noise Flag                                                                |
| AP                      | N | Total Annual Payroll ($1,000) with Noise                                                       |
| EST                     | N | Total Number of Establishments                                                                 |
| N1_4                    | N | Number of Establishments: 1-4 Employee Size Class                                              |
| N5_9                    | N | Number of Establishments: 5-9 Employee Size Class                                              |
| N10_19                  | N | Number of Establishments: 10-19 Employee Size Class                                            |
| N20_49                  | N | Number of Establishments: 20-49 Employee Size Class                                            |
| N50_99                  | N | Number of Establishments: 50-99 Employee Size Class                                            |
| N100_249                | N | Number of Establishments: 100-249 Employee Size Class                                          |
| N250_499                | N | Number of Establishments: 250-499 Employee Size Class                                          |
| N500_999                | N | Number of Establishments: 500-999 Employee Size Class                                          |
| N1000                   | N | Number of Establishments: 1,000 or More Employee Size Class                                    |
| N1000_1                 | N | Number of Establishments: Employment Size Class: 1,000-1,499 Employees                         |
| N1000_2                 | N | Number of Establishments: Employment Size Class: 1,500-2,499 Employees                         |
| N1000_3                 | N | Number of Establishments: Employment Size Class: 2,500-4,999 Employees                         |
| N1000_4                 | N | Number of Establishments: Employment Size Class: 5,000 or More Employees                       |
| CENSTATE                | C | Census State Code                                                                              |
| CENCTY                  | C | Census County Code                                                                             |

<br>

| CLASS | # EMPLOYEES | - |
|---|-----------------|---|
| A | 0-19            |   |
| B | 20-99           |   |
| C | 100-249         |   |
| E | 250-499         |   |
| F | 500-999         |   |
| G | 1,000-2,499     |   |
| H | 2,500-4,999     |   |
| I | 5,000-9,999     |   |
| J | 10,000-24,999   |   |
| K | 25,000-49,999   |   |
| L | 50,000-99,999   |   |
| M | 100,000 or More |   |

<br>

> * Employer Flag: denotes employment size class for data withheld to avoid disclosure (confidentiality) or withheld because data do not meet publication standard
>* NOTE: Noise Flag definitions (fields ending in _NF) are:

| CODE | Noise Definition | - | 
|-------------------------------|------------------------------------------------------------------------------------------------------------------|---|
| G                             | 0 to < 2% noise (low noise)                                                                                      |   |
| H                             | 2 to < 5% noise (medium noise)                                                                                   |   |
| D                             | Withheld to avoid disclosing data for individual companies; data are included in higher level totals. Employment or payroll field set to zero. |    |
| S                             | Withheld because estimate did not meet publication standards. Employment or payroll field set to zero.           |   |