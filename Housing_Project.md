# Housing Selling Prices & Renovation

**Authors**: David Tian, Christopher de la Cruz

## Overview

Our analysis currently reflects what types of renovations (based on a home's grade and condition) are most worth the increase in selling price. We take a deep dive into the specific relationship that grade and price share with sales price. Our project currently shows that DECIDE ON A MAIN CONCLUSION WITH DAVID. This analysis can be used by any real estate agency or prospective home seller to guide them on what kinds of renovations they should be making.

## Business Problem

We are a Seattle-based real estate agency that specializes in helping prospective real estate sellers make the best possible choices to increase the value of their homes before putting them on the market. Among the homes in Seattle, Washington, homes are graded by both their grade (1 - 10; 10 being the highest possible condition) and condition (1 - 5; 5 being the highest quality condition). Our project aims to look at what types of renovations are worth the improvement in price (for example if a home has a grade of 1, is the change in selling price worth it to renovate to a 3 or does it have to renovate to a 5 in order to be worth the renovation?). We chose to focus on renovations because there are the most straight-forward changes that you can make to a home (for example, you cannot simply add a waterfront view to a home).

## Data

Our dataset contains house sale prices for King County. It includes homes sold and the characteristics of those homes. For the sake of our regression model, we limited our houses specifically to Seattle and specifically looked closely at:

- Price<br>
- Grade<br>
- Condition<br>

## Methods

We mainly stuck to the observations of films in the past 5 years in order to stay relevant to today's trends. We observed mainly how different factors affected a film's profitability and popularity which are the two main driving sources behind any investment. A film's profitability is a large short-term profit but its popularity means more payments for domestic and international licensing fees meaning there is more long term profit to be made.

## Result 1

We have two main key results which are that there is a preferential budget range for movies that are both highly rated and popular

### Visual 1
![budget_sd](https://user-images.githubusercontent.com/77891283/113523642-ef653900-9576-11eb-9cd0-43f22f14e078.png)

## Result 1
Our second main result is that the genres performing best individually and in combination are action, adventure, and sci-fi

### Visual 2
![genre_ind](https://user-images.githubusercontent.com/77891283/113523656-158ad900-9577-11eb-8e14-d7ba4ac637b3.png)

![genre_pairs](https://user-images.githubusercontent.com/77891283/113523659-1d4a7d80-9577-11eb-8fef-89c56c9a2ba6.png)

## Conclusions

These are our business recommendations for a future film:<br>

1. We stick to a budget of 12m - 67.6m. The grand majority of films that are popular and perform well are in this range. Higher budgets are justifiable on a case by case scenario (mainly a film designed to be a blockbuster hit)<br>

2. Action, Adventure and Sci - Fi are all outperforming all the other genres both individually and combined and we highly recommend doing our first film in one or a combination of these genres.<br>

3. We aim for release during what the film industry calls the "slump months" (Jan - Feb & Aug - Sept). These two periods are when quality of movie releases are at their lowest (due to the month before these periods being considered prime time for mega blockbusters). We recommend aiming for a release during one of the slump months as a) we are not equipped to compete with an established blockbuster and 2) there will be less competition, giving our film a higher chance of standing out

4. Keep all story lines high stakes, with strong familial-like relationships and familiar themes

These are the next steps we believe we should take:

1. Franchises are enormously profitable but almost all already owned by other movie studios. We advise doing a deep dive into any existing unowned franchises and potential for creating our own franchise

2. Each genre and genre combination will require its own personal deep dive into further details such as the current hottest actors and directors in each genre, the runtimes that perform best, audience rating that performs best, etc

3. Our research also showed that the profit for online TV streaming and internet content rivals film profits and we advise doing a special deep dive into also creating online streaming television shows and online content
![Revenue_Sources](https://user-images.githubusercontent.com/77891283/113523592-6e0da680-9576-11eb-9ba7-5a2333f18165.png)


## For More Information

Please review our full analysis in our Jupyter Notebook (Microsoft_Film_Industry_Analysis.ipynb located in the code folder) or our [Presentation](https://github.com/cdlc01/Microsoft-Film-Industry-Analysis/files/6255838/Powerpoint_film_analysis.pdf)

For any additional questions, please contact **Christopher de la Cruz at cdelacruz2013@gmail.com, NEED DAVID'S EMAIL**

## Repository Structure

```
├── __init__.py                                  <- .py file that signals to python these folders contain packages
├── README.md                                    <- The top-level README for reviewers of this project
├── Powerpoint_film_analysis.pdf                 <- PDF version of project presentation
├── code
│   ├── __init__.py                              <- .py file that signals to python these folders contain packages
│   ├── visualizations.py                        <- .py script to create finalized versions of visuals for project
│   ├── Data_Cleaning.py                         <- .py script used to pre-process and clean data from the IMDbpy module
│   ├── Dataframe_Cleaning.py                    <- .py script used to clean the dataframe directly
│   ├── Data_Collection-DO NOT RUN.py            <- .py script used to gather data using the IMDbpy module. The process takes a full day. We advise not running
│   ├── Analysis.py                              <- .py script for specific genre analysis (courtesy of George)
│   ├── eda_notebook.ipynb                       <- Notebook containing data exploration
|   ├── Microsoft_Film_Industry_Analysis.ipynb   <- Narrative documentation of analysis in Jupyter notebook 
|       ├── data                                 <- Both sourced externally and generated from code
└── images                                       <- Both sourced externally and generated from code
```
