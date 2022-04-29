# GIGI'S LOG
<br> 

> 4/26
#### updated `my_metrics` to print importances with labels, additional errors and include `max_depth` in f(`arguments`)
* the module/function scales: no need to do it before-hand
* module has two functions: 
    1. gs_svr (X, y)
    2. gs_rf (X, y, params)

> 4/25
#### I was gonna do a basic linear regression but I spent too much time this afternoon troublesehooting a dumb error... and now that I've trained myself to `git pull upstream main` before starting significant work on the group project, I see $David$ has already done a thorough job so I'll be focusing on a random forests regression.

### got a random forest using the columns from David's `06_nb`
* got output, interpret feature importances
* what to do with residuals? 
* which other errors to check? 

> 4/24
- ~~compile all data into one mega dataset from all 4 reports and David's ZIP/census counts~~
- ~~Find change in `ozone`, `birth weight` reporting to ensure metrics are on same scale~~
- ~~modify data given above findings~~
- NO: David has better data ~~extract distribution center list from that site~~

> 4/23
- ~~get lat/long/city/county from zip for ES2~~
- ~~compile all 4 datasets together~~

> 4/22
* cleaned up ES2: extracted city, zip, lat long from one location 
* compiled all data, with zip as ID ... one doesn't have census tract, but we can easily get it with David's scripts
* re-did some EDA with cleaner data, kept David's supplementary analysis to
* ALL DATA has NO DUPLICATES, but I kept nulls - we can imput otherwise later 

> 4/14
* duplicated David's EDA for 3.0, minus _cartopy_ - mostly the same stuff
* extracting center list from that site 

> 4/12 
aggregate eda

> 4/10:
check:  
Emergency Department and Patient Discharge Datasets from the
State of California, Office of Statewide Health Planning and
Development (OSHPD)
