# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Health Outcomes Modeled Over Multiple CalEnviroScreen Reporting Periods

---
We aggregated data from `4` <a href = "https://oehha.ca.gov/calenviroscreen/about-calenviroscreen">CA OEHHA CalEnviro Screen</a> reports, appended warehouse counts extracted from <a href = "link"> US Census Business Data</a> and trained numerous estimators, however none reliably modelled health outcomes using the aggregated data.

---

## Background 
California Office of Environmental Health Hazard Assessment (<a href = "https://oehha.ca.gov/calenviroscreen/about-calenviroscreen">CA OEHHA</a>) has compiled data from various government agencies to create a mapping tool used to identifying communities most affected by various pollution sources, producing four reports total in years 2013, 2014, 2018 and 2021 with scores to for each identified disadvantaged community that was disproportionally facing enviornmental impacts. Because trasportation of goods and people continues to be the primary source of emissions, and because increased commerce requires increased warehousing and associated transportation, we sought to create models to answer the following questoins: 

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

<br >

variable name   | type      | description 
---             | ---       | ---   
diesel pm       | numeric   | particulate matter, spatially modelled
ozone           | numeric   | concentration
traffic         | numeric   | volume: vehicles per length of time over fixed distance

## *_Target_*

We trained multiple estimators to model the outcomes reported in the _CalEnviroScreen_ reports to build upon that work: 

<br>

variable name   | type      | description 
---             | ---       | ---   
asthma hospitalization         | numeric   | incidence rate, cases/ 10k population
heat attack hospitalizatoin   | numeric   | incidence rate, cases/ 10k population
low birth weight| numeric   | % newborns weighing `< 2.5 kg` (#/100 live births)

---

## _Exploratory Data Analyses_ 

<img src = " " > INCLUDE CORR MATRIX IMAGES HERE

<img src = Giovanna/images/asthmaa.png><br>


---
## _Modeling_

> ### David: Linear Models
The linear models give us a sense of which of the features to focus on if we want to address these health issues.

large coefficients ---(relative to that feature scale. Divide these by corresponding feature stds or scale data ahead of time for direct comparison of importance. not as fancy as PCR or other importance techniques)---
large coefficients on high R^2 models indicate features to work on if we wish to reduce ER visits for these three health types.

* warehouses alone are very poor indicators.
* socio-economi metrcs not as good as the caes modified scores (which also account for social and pollution), but some relationship here.
* the caes scores are actually decent.
CAES scores alone (train/test)
the caes scores are decent.
asthma
(0.4832395083165938, 0.4807148307370688)
lbw
(0.23950857499514167, 0.2515350979968135)
cvd
(0.2364798467342505, 0.23122365100217368)


Model   | Features                              | Target | $R^2_train$  | $R^2_test$
---     |---                                    | ---    | ---          | --- 
1       | selected: no time, space or CES scores| Asthma | 0.59292      | 0.59249
2       | selected: no time, space or CES scores| CVD    | 0.49659      | 0.50636
3       | selected: no time, space or CES scores| LBW    | 0.38478      | 0.40500
4       | warehouse counts only                 | Asthma | 0.02162      | 0.02139
5       | warehouse counts only                 | CVD    | 0.00419      | 0.00404
6       | warehouse counts only                 | LBW     | 0.02167     | 0.02177
7       | socio-economic only                   | Asthma | 0.02162      | 0.02139
8       | warehouse counts only                 | CVD    | 0.10994      | 0.11001
9       | warehouse counts only                 | LBW    | 0.13333      | 0.13754






comparing these, as well as with correlations alone, gives a sense of the importance of the social features.
<br> 

> ### Giovanna: Random Forest & SVR 
<br> 

`Random Forest Regression` over a Gridsearch to find optimal values returned the following importances and low-performance scores, indicating that the metrics we used to model health outcomes are insufficient, and highlighting that socioeconomic factors are much more predictive. Specifically, the number of warehouses in a given zip code does not reflect the outcomes in that zip code. 

Model   | Estimator                | Features   | Target    |  $R^2$
---     |---                       | ---        | ---       | --- 
1      | Decision Tree Regressor   | all | asthma           | -0.07
2      | Decision Tree Regressor   | all | heart attack     | -0.07
3      | Decision Tree Regressor   | all | low birth weight | -0.07
4      | Decision Tree Regressor   | non-se | asthma           | -0.07
5      | Decision Tree Regressor   | non-se | heart attack     | -0.07
6     | Decision Tree Regressor    | non-se | low birth weight | -0.07

<br> 

<img src = Giovanna/images/asthmaa.png><br>
_Features importances with all features, model target is `asthma`._

<img src = Giovanna/images/caridoa.png><br>
_Features importances with all features, model target is `heart-attacke` hospitalization._ 

<img src = Giovanna/images/lbwa.png><br>
_Features importances with all features, model target is `low birth-weight`._

<img src = Giovanna/images/asthmanse.png><br>
_Features importances without socio-economic features, model target is `asthma`._

<img src = Giovanna/images/heartnse.png><br>
_Features importances without socio-economic features, model target is `heart-attacke` hospitalization._ 

<img src = Giovanna/images/lbwnse.png><br>
_Features importances without socio-economic features, model l target is low birth-weight`._

<br > 

> ### Marshall: XGBOOST

Features used: 
| total population, ozone, pm2.5, diesel pm, pesticides, traffic, cleanup sites, groundwater threats, haz. waste, imp. water bodies, solid waste, pollution burden, low birth weight, education, linguistic isolation, poverty, pop. char. , drinking water, tox. release, unemployment, ces_per, cardiovascular disease, housing burden, est total, est gen, est cold, est farm, est other | gradient boosting supervised regression |
| Model         | features used  type   | evaluation metric  | Train Accuracy  | Test Accuracy | RMSE score | MAE test score |
| ---        | ---  | --- | --- | ---| ---| ---
| XGBoost       | R2, RMSE, & MAE | 0.9139 | 0.7853 | 13.6915  | 9.3296       |
| Random Forest  meta estimator regression               | R2, RMSE, & MAE | 0.9634 | 0.7503 | 14.7307  | 9.9952       |


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
We will continue to aggregate more data with finer granularity, and explore the raw data from which the CalEnviroScreen was sourced and modeled. Furthemore, spatial and temporal analyses will provide more robust models for projecting and adddressing communites to support. 
<br> 

---
> ### Background: From the Press 
* <a href ="https://www.epi.org/publication/unfulfilled-promises-amazon-warehouses-do-not-generate-broad-based-employment-growth/"> EPI: Warehouses Do Not Generate Broad-Based Employment </a> (cites the source I have for fulfillment center locations)
* <a href = https://www.cbre.com/insights/local-response/2022-north-america-industrial-big-box-los-angeles-county> CBRE: 2022 North America Industrial Big Box Review & Outlook: Los Angeles County</a>
> 