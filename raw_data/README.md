# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) General Assembly DSI Group Project: Health Outcomes Modeled Over Multiple CalEnviroScreen Reporting Periods

---
> ## Data Cleaning & Detailed Dictionaries
> Detailed description of raw data and sources below. 
> All data in this directory is unprocessed: not scaled, not imputed. 
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



### <b>Data:</b> US Census Business Survey: Warehouse Counts, Density
**Description:**  The US Census counts ... 

<a href = "https://www2.census.gov/programs-surveys/cbp/datasets/"> US Census Bureau  </a> 
<a href = " "> Data Descriptions </a> Datasets were collected from ___?????

year(s) | name/link     | description                  | size 
---     | ---           | ---                          | ---
2012    |   xxx         |  business by type in county  | row x col 
2012    |   xxx         |  business counts by zip      | row x col 


name        | description 
---         | --- 
est total   | total number of warehouses in class 
est ag      | total number of warehouse for agricultural 

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