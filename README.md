> # 4/26
> #  TO DO 
> * SLIDES 
> * #### SLIDES
> * ### SLIDES
> * ## SLIDES
> * # SLIDES
> * # **SLIDES**
> * CLEAN UP `REPOSITORY`, with following structure: 
>    1. `code` directory with all notebooks
>       * $TOC$ at top of each notebooks 
>       1. combining all ES
>       2. extracting from census
>       3. combing ES + census 
>       4. initial EDAs (4_1, 4_2, 4_3, etc.)
>       5. David's LRs
>       6. G's RFs, SVR, XGB
>       7. Marshalls's XGB? 
>       8. Final Model & Conclusion 
>    2. `raw_data` 
>       * ES data
>       * census business survey 
>    3. `processed_data`
>    4. `ES` PDFs
>    5. `other` PDFs, links, etc. 
> 
> <br>
> 
> * ~~CLEAN `all_processed` file in `processed_data` directory:~~
>   * ~~all four ES datasets~~
>   * ~~warehouse-data for 4 years from census~~ 


> # NOTES
> #### _4/24_
> * `processed_data` directory has all files ready for `imputing`
> * `05_merged` nb in `Giovanna` directory has some initial EDA
>
> #### _4/22_ 
> * $G$ messed up $David's$ initial EDA notebook trying to add my last name. Don't know how to fix it right now, but can confirm previous versions ARE saved and accessible via github's version /revision history. Will look into this later. 

---
---
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Health Outcomes Modeled Over Multiple CalEnviroScreen Reporting Periods

---
## ***Summary***  We aggregated data from `four` <a href = "https://oehha.ca.gov/calenviroscreen/about-calenviroscreen">CA OEHHA CalEnviro Screen</a> reports, appended warehouse numbers from <a href = "link"> US Census Business Counts</a>  and trained `54` estimators to model health outcomes from collected data: `THE NN/XGB/RFR MODEL`, performed the best, accurately predciting `100%` of the health outcomes on `new data.` 
---


## Background 
California Office of Environmental Health Hazard Assessment (<a href = "https://oehha.ca.gov/calenviroscreen/about-calenviroscreen">CA OEHHA</a>) has compiled data from various government agencies to create a mapping tool used to identifying communities most affected by various pollution sources, producing four reports total in years 2013, 2014, 2018 and 2021. 

---
## Data Acquisition & Cleaning 
---
### <b>Data:</b> CalEnviroScreen 
**Description:** CA OEHHA compiles data specfically regarding pollutants and the communities affected by them. 


 Source  | File  | Report Date  | Shape | 
 ---     | ---   |  ---         |  ---  |
 <a href = "https://oehha.ca.gov/calenviroscreen/report-general-info/calenviroscreen-10"> CalEnviroScreen 1 </a> |  <a href = "https://github.com/gigi-codes/CO2_modelling/blob/g_branch/raw_data/calenviroscreendatav11.xls"> Data (xlsx) </a> | April 2013 | FILLIN |
 <a href = "https://data.ca.gov/dataset/calenviroscreen-2-0"> CalEnviroScreen 2 </a> |  <a href = "https://oehha.ca.gov/media/downloads/calenviroscreen/report/ces20updateoct2014.xlsx"> Data (xlsx) </a> | Oct 2014 | (8035, 51) |
 <a href = "https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-30"> CalEnviroScreen 3 </a>  | <a href =  "https://oehha.ca.gov/media/downloads/calenviroscreen/document/ces3results.xlsx"> Data (xlsx) </a>     | June 2018 |  (8035, 51) |
 <a href = "https://calenviroscreen-oehha.hub.arcgis.com"> CalEnviroScreen 4 </a> | <a href = "https://calenviroscreen-oehha.hub.arcgis.com"> Data, Dictionarty ZIP </a>| Oct 2021 |  (8035, 51) |
 |   | |  Combined Data   | (25444, 62) |
 |   | |   **Used Data**   | (14912, 59) |


 * `ozone` data from CalEnviroScreen (CAES) 4: converted from yearly units to daily units
 * `low birth rate` in CAES 2: converted from fraction to percent
 * `others` ? 

 * `99%` of observations were ommitted: 
    * feature/column only reported for one year
    * `Nan` were `DROPPED` `FILLED WITH MEDIAN`
 
<br>

### <b>Data:</b> US Census Business Survey: Warehouse Counts, Density
**Description:**  The US Census counts ... 

<a href = "https://www2.census.gov/programs-surveys/cbp/datasets/"> US Census Bureau  </a> 
<a href = " "> Data Descriptions </a> Datasets were collected from 

datasets: 

year(s) | name/link     | description                  | size 
---     | ---           | ---                          | ---
2012    |   xxx         |  business by type in county  | row x col 
2012    |   xxx         |  business counts by zip      | row x col 


name        | description 
---         | --- 
est total   | total number of warehouses in class 
est ag      | total number of warehouse for agricultural 


### Additional cleaning steps: 
* filled medians? 

* MEASURABLE: incidence change over four time periods 
* Relevant: YES. We care about the cost of our online shopping? 
* Time-bound: YES: We have to select the period/ years we wish to model.
* NOVEL: really good work, David, in compiling # of warehouses !!! 

### Data: _Dictionary for Model Features_


variable name   | Type      | Description 
---             | ---       | ---   
asthma          | numeric   | incidence rate, cases/ 10k population
cardiovasccular | numeric   | incidence rate, cases/ 100 population
low birth weight| numeric   | % newborns weighing `< 2500 g`
diesel pm       | numeric   | particulate matter, spatially modelled
ozone           | numeric   | concentration
traffic         | numeric   | volume: vehicles per length of time over fixed distance
traffic         | numeric   | volume: vehicles per length of time over fixed distance

## _Target? Goal_
We are 
* regressing, 
* classifying, 
* using some forests
* using (un)/supervised neural network to
* model health outcomes  


## _Exploratory Data Analyses_ 

<img src = " " > INCLUDE CORR MATRIX IMAGES HERE

---
## _Model Performance_ 

> ### Giovanna: Random Forest & SVR 

Model   | Transformer       | Regularization        | $n$  | Train   
---     |---                | ---                   | ---  | ---     
1       | Linear Regression | Logistic Regressor    | 14000 | 0.7373  
2       | Random Forest Regressor  | none   | 14000 | 0.55
3       | SVR | None	        | 1400 | 0.44 



Include Feature Importances Plot here from RFR
<img src = " ">

> ### Marshall: XGBOOST: table hidden for now, truncate values on accuracy scores

<!-- reinclude after truncating values 
| Model         | features used                                                                                                                                                                                                                                                                                                                                                                             | type                                    | evaluation metric           | Train Accuracy     | Test Accuracy      | RMSE score | r_2 score |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|-----------------------------|--------------------|--------------------|------------|-----------|
| XGBoost       | total population, ozone, pm2.5, diesel pm, pesticides, traffic, cleanup sites, groundwater threats, haz. waste, imp. water bodies, solid waste, pollution burden, low birth weight, education, linguistic isolation, poverty, pop. char. , drinking water, tox. release, unemployment, ces_per, cardiovascular disease, housing burden, est total, est gen, est cold, est farm, est other | gradient boosting supervised regression | Accuracy, r_2 score, & RMSE | 0.9472151826696329 | 0.7639090300436409 | 14.376141  | 0.7       |
| Random Forest | total population, ozone, pm2.5, diesel pm, pesticides, traffic, cleanup sites, groundwater threats, haz. waste, imp. water bodies, solid waste, pollution burden, education, linguistic isolation, poverty, pop. char. , drinking water, tox. release, unemployment, ces_per, housing burden, est total, est gen, est cold, est farm, est other                                           | meta estimator regression               | Accuracy, r_2 score, & RMSE | 0.9631357268516347 | 0.7488496371839088 | 14.739432  | 0.6       |
|               |                                                                                                                                                                                                                                                                                                                                                                                           |                                         |                             |                    |                    |            |           |
 -->


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