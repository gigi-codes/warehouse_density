# David's log

[GitHub repo](https://github.com/gigi-codes/CO2_modelling)

Spring 2022
DSIR 222
Group project

---
---
4/9
---
Performed EDA with the EnviroScreen 4 data, familiarized myself with each column.
Practiced with cartopy to visualize each of the census tracts

---
---
4/11
---

Marshall performed a linear regression on the CES data 3 and obtained a poor score
Giovanna performed EDA on CES data 2
G shared the CES 1, noting it's much different

feeling uneasy about problem statement progress --- we gotta get movin!

---
---
4/14
---

Meeting

    - There are open /transparent data sets, but they're difficult to navigate.
    - Sorted out git organization
    - keep altered data in a separate folder. only raw_data should go in raw_data. I'm being a real curmudgeon about this.
    - shared our EDAs from last weekend
    - considering a predictive neural net
    - agreed to:
        - treat sets 3 and 4 the same.
        - Apply some more comprehensive EDA, and compare 3 and 4.
        - continue with cleaning and comparison.
        - look up business permit data by tract and merge with CES 3 and/or 4.

To do:

~~- read warehouse-best-practices PDF -- Xavier Becerra CA attorney general~~

    - Inland Empire - mojave, riverside, lots of warehouse, smog, highway traffic (rts 15 to Las Vegas, 40 to Flagstaff, 10 to Phoenix)
    - Good neighbors policies:
        - four counties riverside country, the city of riverside, the city of moreno valley, watern riverside council of governments
        - what the heck are good neighbor policies
        - 300 meters from warehouse to "sensitive receptors": western riverside council
        - vehicles entering area must adhere to CARB guidelines
    - recommends proactive planning:
        - zoning -- industrial districts near major highways and rail corridors
    - community engagement
        - communicate in meetings, posts, mail, translation services,
        - ample warning and access info for meetings
        - get feedback and support
        - create a benefits agreement
        - community advisory board of residents
        - assign community liason to operations
    - Warehouse siting
        - lcation location location
        - CARB: 1000+ ft from sensitive receptors
        - barriers 
        - adequate parking, strategic placement of docks
        - clear signage with use info for trucks and awareness info for everyone
        - long term viability awareness
    - Greenhouse gases best practices:
        - analyze project impacts thoroughly. CEQA guidelines sec. 15369
        - prepare a quantitative air study
        - don't label as CARB compliant. Everyone must be CARB compliant. ("legal sea foods")
        - analyze truck trips thoroughly
        - account for all GHGs, CA's Cap-and-Trade Program
    - lots of suggestions for mitigating GHGs
    - noise considerations
    - traffic impact
    - other best practices:
        - appoint compliance officer
        - create a fund to mitigate impacts in community
        - sweep surrounding streets
        - light only the site directly, reduce pavement heating, high quality climate control fro worksersd
    - conclusion: claifornia is great

- read "a multivariate analysis of cal enviroscreen..."
- collect references in the two above --- news articles, papers

- I have no clue how Markdown/jupyter decides how to color these things. What's going on with this green ones down there! Why aren't they all blue like above? Is it the links? 

    - read and shared a couple articles
        - used [this article](https://www.pe.com/2021/09/29/inland-empire-is-warehouse-central-but-how-did-it-happen) to find a couple of the statista sets [number of big box warehouses](https://www.statista.com/statistics/757252/number-of-big-box-buildings-inland-empire/) and [area of big box warehouses](https://www.statista.com/statistics/757290/existing-space-size-of-big-box-buildings-inland-empire-ca/) and [vacancy rate of big box warehouses](https://www.statista.com/statistics/757309/vacancy-rate-of-big-box-buildings-inland-empire-ca/) in the Inland Empire. These sets look like garbage --- only a number for each year from 2009 to 2020. The site hides the sources behind its paywall.
    - Inland Empire: Riverside and San Bernardino counties
    
- begin looking through business permit data
    - It would be great if we had [a version of this building permit dataset for Los Angeles](https://data.lacity.org/A-Prosperous-City/Building-Permits/nbyu-2ha9) for Riverside and San Bernardino counties.
    - [CA Open Data Portal](https://data.ca.gov/) could be valuable.
    - [CIRB](https://www.cirbreport.org/reports/) may have the data we want, but it's 1100 dollars.
    - How about the [CA Dept. Commerce](https://data.commerce.gov/)?
    - [This Census page](https://www.census.gov/data/developers/data-sets/cbp-nonemp-zbp/cbp-api.html) may be our ticket. it involves an api call. Strangtely enough, it looks like maybe census tract isn't given, but zip code is. Is Uniform Census Geography Identifier clause (UCGID) the census tract?
    - [Here's the census FTP server](https://www2.census.gov/) to download the entire dataset.
    - [CBP data page](https://www.census.gov/programs-surveys/cbp.html)
    - [Getting closer??](https://www.census.gov/programs-surveys/cbp/data/datasets.html)
        - these include industry codes, which could allow us to filter out the storage facilities
        - I'm glad it made this green in jupyter because it's important.
    - [Census Industry Classifications](https://www2.census.gov/programs-surveys/cbp/technical-documentation/reference/naics-descriptions/naics2017.txt)
    
- combine the data sets by tract
- get statistics by types, groupbys. pivot table?
    
---
---
4/15
---

- quick meet -- G will poke around the FTP server and API
- census industry codes
    - added naics2017.txt to raw_data
    - saved a copy as naics2017_UTF8.txt to read
    - making a new notebook, NAICS, to look at it for some reason. It's practice.
    
	- G looked through the CBP data page. It really seems like the right data. It is divided into congressional districts, zip codes, and counties. They don't all have the same information --- but we ought to be able to link them together.
    - G downloading and looking over 2013 data.
- downloaded .zips for all CBP and ZBP datas 2012 through 2019. This hopefully covers all the data we'll ever need. I may unzip only as needed, and try to remember to add the unzipped file to .gitignore. unzipping one of the ZBP increased it from ~30MB to ~110MB --- don't wanna go over GitHub's limits.
- feeling like we have a project here.

---
---
4/17
---

Looking at Gs aggregate EDA. Differences in distributions for the emergency room visits. low birth weights and heart attack ED visits are striking.

Called [my sis](https://www.linkedin.com/in/smtbrokaw/) to ask about lifestyle diseases and wildfires. Asked about striking changes in these emergency room visits after 2015. She focused on diabetes in Montana, but is well aware of wildfire PM and other environmental risks to other long term diseases. She said these kinds of changes were observed in MT, but agreed it's strange that heart disease went up rather than asthma first if we're attributing the change to PM2.5 and other air pollutants.

unpacked the zbp19 data and added the expanded file to .gitignore.

familiarizing myself with zbp19 data, writing in [this notebook](./2_zbpandcbpData.ipynb)

---
---
4/20
---

Meeting this morning. I will add up business data by zip code and export a CSV. I agreed to make a sample with my expected format.

Others will work on merging the data from at least the CAES 3 and 4 sets, but maybe 1, 2, 3, and 4 for some critical columns (health related, basic pollution)

The set of zip codes is different from CAES to CAES. Zip codes apparently change often, with 10-20 being added each year. The majority are in overlap, so we could just do an inner join with these.

made a pair of dicts that translate between zip codes and tracts

---
---
4/21
---
gonna make a thing

---
---
4/22
---

Met this morning, sorted more git problems. we merged extra branches to main and agreed to just push and pull from main.

Still planning on making a thing.

GG and MC have been working with CAES data directly. exporting a single consolidated file. Looking at that now.

Looks cool. gonna finally make that zip-warehouse counter.


---
---
4/24
---
warehouse types counted by zip. that's in `processed_data/business_counts_by_zip/`

---
---
4/25
---
The zip-warehouse counter was used by others to make a merged set. Made some initial linear regressions with each of the health data. These are just with time and space, just with warehouse counts, and with most of the physical measurements including warehouse counts and pollution levels.

---
---
4/26 - 4/27
---

- fleshed out linear regressions on multiple sets of parameters. worked on interpretation. began a clean rewrite.
- met about troubles with git, coordination
- began as a group making slides and coordinating talk. hope to be confident about it tonight, with a practice. at least one friday morning.

---
---
4/28
---
- finishing rewrite of linear regression notebook, with details on interpretation. picking out "best models"
- make coefficient comparisons
- adding those to the slides. should add data source descriptions to slides.

---
---
4/29
---
We met this morning and finished our slides, compared them, practiced twice, and spoke to the class.
Two of us met in the breakout room at the end of the day to discuss organizing and commenting on this repo.
replaced group project slides with dog-free version.
removed my linear_models.txt description from the top directory
to do:
    

    - readme:
        - add linear model results
        - add make flow chart or description of notebook order, with links to notebooks
        - include description of the zbp data source and type.
    - notebooks to clean up:
        -1
        -2
        -3
        -4
        -5
        -6
        -7