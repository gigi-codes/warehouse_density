# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Health Outcomes: Proximity to Online-Shopping Distribution Hubs
---
_Template modelled from capstone guidelines._

## Does increase in _NOx_, _SOx_, _PPMx_ predict incidence of _asthma_, _COPD_ or related disease? 
> * SPECIFIC-select: 
>    * diseases
>    * emissions
>    * time frame
>    * location(s)
* MEASURABLE: incidence before, after specified time period. 
* Achievable: can we get the data? 
* Relevant: YES. We care about the cost of our online shopping? 
* Time-bound: YES: We have to select the period/ years we wish to model. 

## _Data: Sources_

|Source                            | File     | Date  |
|---                               | ---                  | ---   |

|<a href = "https://data.ca.gov/dataset/calenviroscreen-2-0"> CalEnviroScreen 2 </a>     |  <a href = "https://oehha.ca.gov/media/downloads/calenviroscreen/report/ces20updateoct2014.xlsx"> Data (xlsx) </a> | Oct 2014  |


|<a href = "https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-30"> CalEnviroScreen 3 </a>  | <a href =  "https://oehha.ca.gov/media/downloads/calenviroscreen/document/ces3results.xlsx"> Data (xlsx) </a>     | June 2018 |


|<a href = "https://calenviroscreen-oehha.hub.arcgis.com"> CalEnviroScreen 4 </a> | <a href = "https://calenviroscreen-oehha.hub.arcgis.com"> Data (xlsx) </a>| Oct 2021  |



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

---
### ADDENDUM: make reusable functions
Writing code in functions serves many purposes, but for the purpose of these projects I want to focus on two.

Writing functions to perform individual tasks will clarify, to you as well as the reader, what each line of code is doing. Just like how we use separate notebooks to allow readers to keep distinct tasks separated in their minds, functions can serve an identically helpful organizational purpose.
When you are interviewing, you will absolutely be expected to write functions since that is how code is, in practice, written and used. It is genuinely a very important part of writing code.