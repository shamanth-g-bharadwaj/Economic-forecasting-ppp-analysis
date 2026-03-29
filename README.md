# Economic Forecasting PPP Analysis

A business forecasting project focused on analysing exchange rates and testing Purchasing Power Parity (PPP) between **Switzerland** and **Singapore** using time series analysis and ARIMA forecasting.

## Project Overview

This project examines the relationship between exchange rates and price levels between Switzerland and Singapore. The main aim was to test whether **Purchasing Power Parity (PPP)** holds in practice and to build a forecasting model for the **real exchange rate (REER)**.

The analysis combines economic theory with practical forecasting methods. Using monthly data, the project explores the behaviour of inflation, nominal exchange rates, and real exchange rates through data preparation, visual analysis, statistical testing, and time series modelling.

## Objectives

- Analyse exchange rate behaviour between Switzerland and Singapore
- Test **Absolute PPP** and **Relative PPP**
- Examine the statistical properties of the time series data
- Build and compare ARIMA models for forecasting the real exchange rate
- Generate practical forecasting insights from the selected model

## Dataset

The project uses monthly macroeconomic and exchange rate data from **January 1999 to February 2025**.

### Variables used
- Consumer Price Index (CPI) for Switzerland
- Consumer Price Index (CPI) for Singapore
- Nominal Exchange Rate
- Real Exchange Rate (REER)

### Data sources
- Swiss National Bank (SNB)
- Federal Statistical Office
- Department of Statistics Singapore
- RateInflation

## Data Preparation

Before analysis, the raw data was restructured and cleaned to make it suitable for time series modelling.

Key preparation steps included:

- Transforming CPI data from wide format to long format
- Merging separate datasets into one monthly time series
- Renaming variables for consistency and clarity
- Checking for missing values and data quality issues
- Converting date fields into proper time format
- Applying log transformations to support interpretation and modelling

The final dataset contained **314 monthly observations** with no missing values.

## Analytical Approach

The project followed a structured forecasting workflow:

1. **Initial data inspection**  
   Reviewed completeness, variable types, and summary statistics.

2. **Exploratory analysis**  
   Examined distributions, skewness, and time series plots.

3. **Log transformation**  
   Applied natural logs to stabilise variance and interpret changes more meaningfully.

4. **Stationarity testing**  
   Used the **Augmented Dickey-Fuller (ADF) test** to check whether the variables were stationary.

5. **PPP testing**  
   Tested both:
   - **Absolute PPP** using OLS regression on log exchange rates and price differentials
   - **Relative PPP** using OLS regression on first differences

6. **ARIMA modelling**  
   Estimated multiple ARIMA models using the Box-Jenkins approach and compared them using:
   - coefficient significance
   - residual diagnostics
   - Ljung-Box test
   - AIC / BIC

7. **Forecasting**  
   Generated out-of-sample forecasts for the real exchange rate and interpreted the projected trend and uncertainty bands.

## Key Findings

- All key variables were found to be **non-stationary in levels** but **stationary after first differencing**
- Neither **Absolute PPP** nor **Relative PPP** held for Switzerland and Singapore in this sample
- Among the candidate forecasting models, **ARIMA (0,1,1)** was selected as the best fit
- The forecast suggested a relatively **stable future path** for the real exchange rate, but with **widening uncertainty over time**

## Tools Used

- **Python**
- **pandas**
- **matplotlib**
- **statsmodels**
- **NumPy**
- **Jupyter Notebook**
