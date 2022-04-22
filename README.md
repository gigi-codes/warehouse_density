# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Health Outcomes: Proximity to Online-Shopping Distribution Hubs
---
_Template modelled from capstone guidelines._
# NOTES: 
* I messed up david's initial EDA notebook trying to add my last name. Don't know how to fix it right now, but can confirm previous versions ARE saved and accessible via github's version /revision history. Will look into this later. 
* I try to keep this README updated with our combined data sources and work, will add links to all the ZIP code/census data David has added by year, or just append to tables below. 
* Thank you for the ZIP translations @David: 
* Thank you for the combined ES file @ Marshall: 
* I will concact these files tomorrow and plot on tableau to see if we can share something pretty for our presenation, or on tableau itself. Even before the modelling, combining all the years into an 'interactive' map is really good work we can be proud to share.
* Won't be in class but have some free time in the AM. 

## Model health outcomes given traffic volumes, density of warehouse/fulfilment centers. 
> * Specifically rate of hospitalization per 10,000 for: 
>    * asthma
>    * cardiovascular
> * Also lso _low birth weight_ 
* MEASURABLE: incidence change over four time periods 
* Relevant: YES. We care about the cost of our online shopping? 
* Time-bound: YES: We have to select the period/ years we wish to model. 

## Data: _CA Enviornmental_

 Source                                                      | File          | Date  |
 ---                                                         | ---           | ---   |
 <a href = "https://oehha.ca.gov/calenviroscreen/report-general-info/calenviroscreen-10"> CalEnviroScreen 1 </a> |  <a href = "https://github.com/gigi-codes/CO2_modelling/blob/g_branch/raw_data/calenviroscreendatav11.xls"> Data (xlsx) </a> | April 2013 
 <a href = "https://data.ca.gov/dataset/calenviroscreen-2-0"> CalEnviroScreen 2 </a> |  <a href = "https://oehha.ca.gov/media/downloads/calenviroscreen/report/ces20updateoct2014.xlsx"> Data (xlsx) </a> | Oct 2014 
<a href = "https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-30"> CalEnviroScreen 3 </a>  | <a href =  "https://oehha.ca.gov/media/downloads/calenviroscreen/document/ces3results.xlsx"> Data (xlsx) </a>     | June 2018 
 <a href = "https://calenviroscreen-oehha.hub.arcgis.com"> CalEnviroScreen 4 </a> | <a href = "https://calenviroscreen-oehha.hub.arcgis.com"> Data, Dictionarty ZIP </a>| Oct 2021 

## Data: _Fulfilment Center Locations_
Fulfilment  | Centers
---         | --- 
<a href = "https://www.mwpvl.com/html/amazon_com.html"> amazon  </a> | 
<a href = "https://www.mwpvl.com/html/walmart.html"> walmart </a> |  
<a href = "https://www.mwpvl.com/html/target.html"> target </a> | 

> **Dataset Description:** Data Desccribe 


----

## _Target?Goal_
We are regressing, classifying, using a un supervised netowkr to say yes or no, or quantify a change. 

## _Data Dictionary_
Data dictionary (describe every feature in your data set, or at least those features that were prominent in your final model)

variable name   | Type        | Description 
---             | ---         | ---   
CO2             | numeric     | $CO_2$ in ppm 
asthma          | binary      | asthma yes = 1
asthma          | rate        | incidence rate, cases/ 100 population

## _Exploratory Data Analyses_ 
Consider including a plot or two from your EDA

---
## _Model Performance_ 
Model performance on training/test data
Did you fit many models? Feel free to summarize some of your scores here.
Consider useing a markdown table to make results easy to review.
It should be clear which model you chose for production and why.

## _Model Selection and Findings_
Primary findings/conclusions/recommendations
These should follow from your project

### _Conclusion_
You should provide an answer to your problem statement

---
## _Next Steps_
Always focus on the positive (it's not what you did wrong, it's what you look forward to improving).
Is your model ready for production? Probably not, but you can comment on how it might get there.
Does this project demonstrate skills that you think could be applied to similar problems?

> ### LINKS 
* <a href ="https://www.epi.org/publication/unfulfilled-promises-amazon-warehouses-do-not-generate-broad-based-employment-growth/"> EPI: Warehouses Do Not Generate Broad-Based Employment </a> (cites the source I have for fulfillment center locations)
* <a href = https://www.cbre.com/insights/local-response/2022-north-america-industrial-big-box-los-angeles-county> CBRE: 2022 North America Industrial Big Box Review & Outlook: Los Angeles County</a>
> 

--- 
### ADDENDUM: _make reusable functions_
Writing code in functions serves many purposes, but for the purpose of these projects I want to focus on two.

Writing functions to perform individual tasks will clarify, to you as well as the reader, what each line of code is doing. Just like how we use separate notebooks to allow readers to keep distinct tasks separated in their minds, functions can serve an identically helpful organizational purpose.
When you are interviewing, you will absolutely be expected to write functions since that is how code is, in practice, written and used. It is genuinely a very important part of writing code.

---
## CALENDAR

> ### April, PDT


| monday | tuesday | wednesday | thursday | friday | saturday | sunday
|--------|---------|-----------|----------|--------|----------|--------
| 11     | 12      | 13        | 14       | 15     | 16       | 17 
| /      | /       |  /        |   /      |   /    |          | MTG
| /      | /       |  /        |   /      |   /    |          | Final Data Select
| 18     | 19      | 20        | 21       | 22     | 23       | 24 
|        |         |           |          |        |          | MTG
|        |         |           |          |        |          | Final Models
| 25     | 26      | 27        | 28             | 29     |          |
|        |         |Prez Prep, I           | Prez Prep II  |  <b>*DUE*</b>      |
|        |         |Final Edits           |          |        |          | 


> ### Link: <a href = "https://docs.google.com/spreadsheets/d/1ANNmWiE-c8f3_PcVUyNqUl5LC-RZKtLLuI6cJGyq0Hc/edit?usp=sharing"> Timeline/ Checklist </a>