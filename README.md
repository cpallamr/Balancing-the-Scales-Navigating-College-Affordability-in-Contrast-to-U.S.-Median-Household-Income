# TEAM KAIZEN (Balancing the Scales Navigating College Affordability in Contrast to U.S.Median Household Income)
Higher education  affordability and accessibility within the  context of socioeconomic disparities.

Project Abstract:This research tackles the urgent problem of rising tuition prices and how they affect 
accessibility in US higher education. Rising tuition has outpaced increase in household 
income over the last two decades, causing social mobility to be hampered and economic 
inequality to worsen. The suggested remedy is creating a sophisticated interactive 
dashboard that compares the growth of tuition and fees with median household income 
across different geographic locations by utilizing cloud-based infrastructure and analytics. 
With the use of transparent data visualizations and real-time analytics, this user-friendly 
platform seeks to empower stakeholders, including researchers, politicians, and students, 
to support policy changes, make informed decisions, and create a more accessible and 
affordable higher education environment. The goal of the project is to offer a special degree 
of in-depth research and openness, acting as a useful tool for students and families 
navigating the challenges of affording college as well as a potent lobbying tool for 
legislative change.

**POWER BI:**

![dashboard](https://github.com/cpallamr/Balancing-the-Scales-Navigating-College-Affordability-in-Contrast-to-U.S.Median-Household-Income/assets/159217518/4a6a74c9-6ed7-43bb-977b-98c4b8dc6362)
![dashboard 1](https://github.com/cpallamr/Balancing-the-Scales-Navigating-College-Affordability-in-Contrast-to-U.S.Median-Household-Income/assets/159217518/5b6cba8e-5664-4c35-9143-4c961974efcc)
![dashboard 2](https://github.com/cpallamr/Balancing-the-Scales-Navigating-College-Affordability-in-Contrast-to-U.S.Median-Household-Income/assets/159217518/0996b273-a033-4820-b546-d96156f8c84f)



**Tableau link:**
1.https://public.tableau.com/app/profile/chaitanya.pallamreddy/viz/TuitionFeeVsMedianIncome/Dashboard1 
2.https://public.tableau.com/app/profile/chaitanya.pallamreddy/viz/Top10UniversitiesinEachState/Dashboard1
3.https://public.tableau.com/app/profile/chaitanya.pallamreddy/viz/AVERAGETUITIONFEEVSSTATE/Dashboard1

**overview**
Using tuition prices and median income levels from 2002 to 2022 as its main points of focus, this thorough analysis offers an interesting look at higher education institutions across the country. By employing diverse data visualization techniques such as line graphs, bar plots, and histograms, the study proficiently depicts the financial metrics and distribution of colleges. The ability to customize views according to state, degree level, and sector through an interactive dashboard that provides both broad and in-depth perspectives improves user engagement. Some of the most important conclusions are that private nonprofit organizations predominate, out-of-state tuition has increased disproportionately when compared to median income, and geographical differences in tuition offer useful data for scholars, politicians, and students.
This forecast section describes the development and assessment of two alternative machine-learning techniques designed to anticipate tuition costs based on historical data. In the beginning, a Linear Regression framework was created via pandas for data management and sklearn for analysis. The regression model was validated on a dataset of tuition prices across time, with 'Year' serving as the variable that is independent with 'Out_of_State_Tuition' as the variable that is dependent. The model performed well on a test set, with an R² value of 0.88 showing good explanatory power. However, errors such as RMSE and MAE indicated probable flaws caused by anomalies or breaches of the linear model's assumptions.
Subsequently, an ARIMA framework was used to forecast prospective expenditures on tuition with training determined by the discovery of optimum characteristics using ACF and PACF plots. The sequence was evaluated for linearity using the Augmented Dickey-Fuller test to ensure that the model hypotheses were valid. The above framework was used to project tuition for the decade to come, with forecasts including average tuition prices and confidence intervals. The model's performance varied; in-state tuition forecasting were relatively accurate with a lower MAPE, whereas tuition from other states forecasts had high errors, suggesting the need for model reassessment, the incorporation of additional variables, or the exploration of more complex models such as SARIMA to improve prediction accuracy.

