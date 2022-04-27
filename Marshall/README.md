4/10
- Familiarized myself with team and proceeded to look around the first viable dataset(Enviroscreen)

4/11
- Inital score with regression is quite poor, but teammates are quite good at EDA. 
- thinking about executive summary and what our "theater" goal is for this project to make it seem real

4/14
Met with team
- All focused on figuring out my Github
- taking noted from both David and Giovanna to make sure my pushes are communicated
Needing structure on: 

- understanding the zip and warehouse data connection with data.
- continue drawing inference on deatailed reports for health conditions. 
- Using my knowledge of growing up in CA to infer certain ares as being prone to higher pollution and contamination from heavy warehouse or buisness interaction. (first thought is that so many cars are Environmentally stringent with big corps(CA is so strict with regulations, imagine Texas or the midwest). Will warehouses show a big impact with pollution? im sure higher than average, but its not a coal plant in Oklahoma. 
- What health effect will be the target? asthma seems the most obvious for me.

4/16
- busy day
- I merged together the Datasets from EnviroScreen but it did not include census and tract info like how Giovana and David collected.
- understanding the impact of the census data. 
4/18
- Great processed dataset with all EnviroScreens and CEAS data. This is what I will use to model effectively. 
- Lots of good learned process from the team with how to deal with missing data in this merged and processed dataset, I have a tendancy to drop and make similar which would ruin integrity. 

4/20
- I have regression models that are not great (.60 R2 roughly)
- Have tried multiple different types of models, diving into GridSearch CV heavily and trying to tackle the XGboost Regression modle.


4/26
- I have completed multiple GridSearch models. 
- My XGboost Reg I think has the best score with .85-.87 R2 score so far but i need to follow up with team to make sure my target health outcome is correctly formatted. 
- confident with the GS I made we can feed in a any of the processed data and achieve a pretty good score!



### TODO: append to main READ.md:
Background on the data what each of the sets are, Big picture(where it came from, how we obtained it, why it is useful). Describe how it was transformed, and what were the general results. Explaination of data dictionary. 

How we encountered percentiles and values in values. initial findings with barebones models. Findings in EDA with location, industry, traffic and connection to health problems. Why its relevant now for someone analyzing this. 

Methodology for why certain models were choosen. 


## Background

#### Cal Enviroscreen
- CalEnviroScreen is a mapping tool that helps identify California communities that are most affected by many sources of pollution, and where people are often especially vulnerable to pollution’s effects.
- CalEnviroScreen uses environmental, health, and socioeconomic information to produce scores for every census tract in the state.
- The scores are mapped so that different communities can be compared. An area with a high score is one that experiences a much higher pollution burden than areas with low scores.
- CalEnviroScreen ranks communities based on data that are available from state and federal government sources. (Source: https://oehha.ca.gov/calenviroscreen/about-calenviroscreen)

#### model types
- SVR (description and implementation)
- Random forest Regressor (description and implementation)
- Elastic Net (description and implementation)

- XGboost regressor with brew install in jupyter lab (description and implementation)

#### Health effects and Pollutants

- Data dictionary 
- 

## Summary of Methodology and Results

- waiting to compile model results

- 

## Executive Summary

   It's time to prepare the California Environmental Protection Agency's Office of Environmental Health Hazard's for a successful auditing process on industry leading companies within the state. California is the home to many successful industry leading companies that supply on a global scale. It is crucial that no area of any company has oversight by the OEHHA and is inefficient or unorganized as to ensure no health hazards are unrecognized for the public. Our aim is to capitalize on the meticulous data gathered in the yearly Enviro-Screen report and be prepared to answer confidently and questions about pollution production and correation with public health. When it comes to the health of our citizens there is no room for error.

   We are a team of data scientist's that specialize in exactly that and have found atleast 5 points of interest so that the OEHHA will be able to accurately label and have predictive strength to monitor adverse health effects caused by pollution in industry and beyond. First-hand, there are insightful correlations (both negative and positive) between asthma, cardiovascular disease, Diesel particulates, and Ozone(add more here*). Secondly, I have a plan of action for how to increase citizen awareness and highlight specific area prone to health complication factors from pollution. These two factors in conjunction will pave the way for predictive/preventitive techniques so that California remains the Golden State for future generations. 

   Through our Regression modeling techniques, the team can determine a statistically correct predictive algorithm that can Identify future and current 'hot spots' of heavy pollution and how they impact the population. With millions of industry dense areas 


   This data science team has experience and the energy to see this project through to the final stages of success. There is no better time than the present to educate and potentially prevent future detriment to the populous and enviroment. With the growing state of California on a local and global scale the clock is ticking and we have not only identified the issues but put together a comprehensive plan to visualize and execute a preventitive and insightful plan for medical and government agencies.

   Let's make it happen and leave no doubt that the beautiful beaches, mountains, and valleys stay pure and continue to bring joy not health issues to our wonderful citizens. We have the chance to change and impact future generations and policy makers accross the globe. 

