# Final project for PPHA 30550 by Shilin, Joyce and Richard.

Our project studies the relationship between politcal system status and social development.


How to open our website
======
1. Open a directory where you want to save the files, e.g. Desktop etc.
2. Open `https://github.com/jxie4/project-SJR`
3. Type `git clone git@github.com:jxie4/project-SJR` into _terminal_; this will download the file "project-SJR"
4. Move towards the directory in the file ___SJR___
5. Type `python manage.py runserver` into _terminal_
6. Load the page `http://127.0.0.1:8000/dev/`, this will lead you to our starting page
7. For the access to each page, see the guide beneath

Manual Guide
======
Once the server is running, click on the interested title and you will be directed to the page you're looking for.


## About

- [x] ___[Research Question] (http://127.0.0.1:8000/dev/question/)___

This page explains our research question in more details. This page explains the motives behind our research question. It includes all the indicators used in our study and explains how these indicators are selected. We also state the indicator used for political system status and explain the mechanism behind this score.


- [x] ___[Dataset sources] (http://127.0.0.1:8000/dev/datasetsource)___

An introduction to the two data sources and the providers used in our research: World Development Indicator by the world bank & Polity IV by Integrated Network for Societal Conflict Research

- [x] ___[Our Team] (http://127.0.0.1:8000/dev/team)___

A basic introduction of the 3 team members: Shilin Liu, Juanyou Xie & Richard Han

## Key Findings
Our data collected were presented in three different ways: country overview, indicator overview & political system & social development.

- [x] ___[Country overview] (http://127.0.0.1:8000/dev/location/)___

This page presents the data for each country from World Development Indicators and Project Polity IV. Users can select whichever country they are interested it and get the data we have. The purpose is to help users get a general sense of each country's situation, including the social indicators and political system status.


- [x] ___[Indicator overview] (http://127.0.0.1:8000/dev/indicator/)___

This page provides the function of comparing cross-country data in one single indicator. The multiple choice form allows users to choose multiple countries; the drop down bar allows users to pick the interested indicator.
The table section will present the data for the selected countries for the specific indicator over the 20 years.
The graph plots the changes in the indicator for each country. Each country will have different colours.
This will help users understand how each country performs in specific indicators while comparing to one another.

- [x]  ___[Political system & social development] (http://127.0.0.1:8000/dev/correlate/)___

This page contains the key answers to our research question: how political system status affects development.
The page is composed by 2 parts: the result summary table & regressions between political system status score & the one single indicator.
The regression uses the aggregated data of all countries over the whole time span, meaning each data point represents the indicator of one country in one single year.

##  Resources
Direct links to the resources we've used: World Development Indicator & Project Polity IV
