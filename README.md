# Final project for PPHA 30550 by Shilin, Joyce and Richard.

Our project studies the relationship between political system status and social development.


How to open our website
======
Welcome to Shilin, Joyce and Richard's baby project! Here is how you access it:

1. Open a directory where you want to save the files, e.g. Desktop, in _terminal_.
2. Enter the code `git clone git@github.com:jxie4/project-SJR` into _terminal_; this will download the repository "project-SJR".
3. Move towards the directory in the file ___SJR___: `cd project-SJR/SJR`
4. Enter the code `python manage.py runserver` into _terminal_.
5. Load the page http://127.0.0.1:8000/dev/, this will lead you to our starting page!
6. For the access to each page, see the guide beneath.

Manual Guide
======
Once the server is running on _terminal_, click on the interested title and you will be directed to the page you're looking for. Links are also shown so you can copy + paste once the server is running.


## About

- [x] __[Research Question] (http://127.0.0.1:8000/dev/question/)__

This page explains our research question in more details and the motives behind our research question. It lists all the indicators used in our study and explains how these indicators are selected. We also state the indicator used for political system status and explain the mechanism behind this score.

```
http://127.0.0.1:8000/dev/question/
```


- [x] __[Dataset Sources] (http://127.0.0.1:8000/dev/datasetsource)__

An introduction to the two data sources and the providers used in our research: World Development Indicator by World Bank & the Polity IV Project by Integrated Network for Societal Conflict Research

```
http://127.0.0.1:8000/dev/datasetsource
```

- [x] __[Our Team] (http://127.0.0.1:8000/dev/team)__

A basic introduction of the 3 team members: Shilin Liu, Juanyou Xie & Richard Han.

```
http://127.0.0.1:8000/dev/team
```

## Key Findings
Our data collected were presented in three different dimensions: country overview, indicator overview and political system & social development.

- [x] __[Country Overview] (http://127.0.0.1:8000/dev/location/)__

This page presents the data for each country from World Development Indicators and the Polity IV Project. Users can select whichever country they are interested in and get the data we have. The purpose is to help users get a general sense of each country's situation, including the social indicators and the political system status.

```
http://127.0.0.1:8000/dev/location/
```

- [x] __[Indicator Overview] (http://127.0.0.1:8000/dev/indicator/)__

This page provides the function of comparing cross-country data in one single indicator. The multiple choice form allows users to choose multiple countries; the drop down bar allows users to pick the interested indicator.
The table section will present the data of the selected countries for the specific indicator over the past 20 years (1994-2014).
The graph plots the changes in the indicator for each country. Each country will have different colors.
This will help users understand how each country performs in specific indicators while comparing to one another.

```
http://127.0.0.1:8000/dev/indicator/
```

- [x]  __[Political System & Social Development] (http://127.0.0.1:8000/dev/correlate/)__

This page contains the key answers to our research question: how political system status is correlated with social development.
The page is composed of 2 parts: the result summary table and regressions between political system status score and the one single indicator (by choosing the social development indicator from the drop down bar).
The regression uses the aggregated data of all countries over the whole time span, meaning each data point represents the indicator of one country in one single year.

```
http://127.0.0.1:8000/dev/correlate/
```

##  Resources
Direct links to the resources we've used: World Development Indicators & the Polity IV Project.
