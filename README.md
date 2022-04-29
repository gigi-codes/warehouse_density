# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Health Outcomes Modeled Over Multiple CalEnviroScreen Reporting Periods

---
We aggregated data from `4` <a href = "https://oehha.ca.gov/calenviroscreen/about-calenviroscreen">CA OEHHA CalEnviro Screen</a> reports, appended warehouse counts extracted from <a href = "link"> US Census Business Data</a> and trained numerous estimators, however none reliably modelled health outcomes using the aggregated data.

---

## Background 
California Office of Environmental Health Hazard Assessment (<a href = "https://oehha.ca.gov/calenviroscreen/about-calenviroscreen">CA OEHHA</a>) has compiled data from various government agencies to create a mapping tool used to identifying communities most affected by various pollution sources, producing four reports total in years 2013, 2014, 2018 and 2021 with scores to for each identified disadvantaged community that was disproportionally facing enviornmental impacts. We sought to create models to answer the following questoins: 

* Is effect of increased warehouse presence on health outcomes quantifiable ?
* What are primary mitigating factors the State can address in response to increased warehouse density?
* How well do the CalEnviroScreen scores reflect emergency healthcare counts?
* What indicators from the CalEnviroScreen dataset best determine the number of emergency healthcare visits?

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

From this data, we used the following for our model: 

 * `ozone` data from CalEnviroScreen (CAES) 4: converted from yearly units to daily units
 * `low birth rate` in CAES 2: converted from fraction to percent
 * `others` ? 

 * `99%` of observations were ommitted: 
    * feature/column only reported for one year
    * `Nan` were `DROPPED` `FILLED WITH MEDIAN`
 
<br>

### <b>Data:</b> <a href = "https://www2.census.gov/programs-surveys/cbp/datasets/"> US Census Business Survey: Warehouse Counts, Density </a>
**Description:**  The US Census counts ... 


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


### Data: _Model Features_
variable name   | type      | description 
---             | ---       | ---   
diesel pm       | numeric   | particulate matter, spatially modelled
ozone           | numeric   | concentration
traffic         | numeric   | volume: vehicles per length of time over fixed distance
traffic         | numeric   | volume: vehicles per length of time over fixed distance

## _Target_

We trained multiple estimators to model the following health outcomes: 

variable name   | type      | description 
---             | ---       | ---   
asthma hospitalization         | numeric   | incidence rate, cases/ 10k population
heat attack hospitalizatoin   | numeric   | incidence rate, cases/ 100 population
low birth weight| numeric   | % newborns weighing `< 2.5 kg` (#/100 live births)


## _Exploratory Data Analyses_ 

<img src = " " > INCLUDE CORR MATRIX IMAGES HERE

![](/Giovanna/images/asthma.png)
<img src = 'Giovanna/images/asthma.png'>



---
## _Model Performance_ 

> ### Giovanna: Random Forest & SVR 

Model   | Estimator                 | $n-estimator$  | $max  depth$ | $max features$  | $max leaf nodes$ | $R^2$
---     |---                        | ---            | ---         | ---             | ---            | --- 
1*      | Decision Tree Regressor   | 100            | 10          | auto            | 10             | -1.5


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
We saw saw no meaningful relationship to create robust models for health outcomes using our warehouse-aggregated data. _Cal EnviroScreen_ scores highly reflect `asthma` and `pollution burden` but not `hospitalization rates`. Socioeconomic factors aggregated in _Cal EnviroScreen_ built best predictive models for negative health outcomes, highlighting the need for the State to address root causes for pollution burden. 

---
## _Next Steps_
We will continue to aggregate more data with finer ganularity, and explore the raw data from which the CalEnviroScreen was sourced and modelled. Furthemore, spatial and temporal analyses will provide more robust models for projecting and adddressing communites to support. 

> ### Background: From the Press 
* <a href ="https://www.epi.org/publication/unfulfilled-promises-amazon-warehouses-do-not-generate-broad-based-employment-growth/"> EPI: Warehouses Do Not Generate Broad-Based Employment </a> (cites the source I have for fulfillment center locations)
* <a href = https://www.cbre.com/insights/local-response/2022-north-america-industrial-big-box-los-angeles-county> CBRE: 2022 North America Industrial Big Box Review & Outlook: Los Angeles County</a>
> 