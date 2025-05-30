# Store Sales Analysis Task

## Overview
This project analyzes sales data to uncover insights into revenue trends, product performance, customer demographics, and market distribution. The analysis focuses on identifying key patterns, seasonality, and correlations to inform business strategies.

## Key Insights

### Revenue Analysis
- **Growth**: Revenue increased from ~$10M in 2011 to ~$20M in 2016, a 100% growth over 5 years.
- **Peak**: $22M in 2015.
- **Highest Growth Period**: 2012-2013 with a 70% increase from $10M to $17M.
- **Volatility**: Significant fluctuations between 2013-2015.
- **Trend Summary**:
  - 2011-2012: Stable at ~$10M.
  - 2013: Surge to $17M.
  - 2014: Decline to $15.5M.
  - 2015: Recovery to $22M.
  - 2016: Moderate decline to $19.5M.
- **Conclusion**: Strong growth potential but inconsistent revenue trends suggest a need for stabilization strategies.

### Business Analysis
1. **Product Category Analysis**:
   - **Accessories**: Dominate with ~1M total order quantity (>80% of orders).
   - **Bikes**: Low order quantity (~50K).
   - **Clothing**: Moderate (~250K).
   - **Summary**: Accessories drive volume, indicating high demand for supplementary products.

2. **Monthly Revenue Trends**:
   - **Peak Months**: May ($10M) and December ($10.2M).
   - **Lowest Months**: July-August (~$6.4M each).
   - **Pattern**: Strong Q4 performance with a summer dip.
   - **Summary**: Clear seasonality with holiday peaks and summer slowdowns.

3. **Revenue by Age Group**:
   - **Top Performer**: Adults (35-64) with ~$47M.
   - **Second**: Young Adults (25-34) with ~$35M.
   - **Lowest**: Youth (<25) with ~$13M; Seniors (64+) show no revenue.
   - **Summary**: Middle-aged adults are the core customer base with the highest purchasing power.

4. **Profit by Sub-Category**:
   - **Highest Profit**: Road Bikes ($14M), Mountain Bikes ($10.5M).
   - **Moderate Profit**: Helmets ($4M), Tires and Tubes ($3M).
   - **Lowest Profit**: Socks, Caps, Cleaners (<$1M each).
   - **Summary**: Bikes offer the highest profit margins despite lower order volumes.

5. **Top 10 Products by Revenue**:
   - **Top Performer**: Road-150 Red, 62 (~$4.2M).
   - **Key Products**: Mountain-200 series and Road-150 variants dominate.
   - **Summary**: Premium bike models are the primary revenue drivers.

6. **Revenue by Country**:
   - **Dominant Market**: United States (~$30M, >40% of total).
   - **Second Tier**: Australia (~$25M).
   - **Third Tier**: UK ($11M), Germany ($10M), France (~$10M).
   - **Smallest**: Canada (~$8M).
   - **Summary**: Strong US market presence with notable international sales in English-speaking countries.

7. **Correlation Analysis**:
   - **Strong Correlations**: Cost-Revenue (0.99), Revenue-Profit (0.99).
   - **Perfect Correlation**: Unit_Cost-Unit_Price (1.0).
   - **Negative Correlation**: Order_Quantity vs Unit_Cost/Price (-0.52).
   - **Summary**: Higher-priced, lower-volume products drive profitability, with an inverse relationship between volume and price.

## Conclusion
The analysis reveals robust growth potential tempered by revenue volatility. Accessories dominate order volume, while premium bikes drive profitability. Seasonality affects sales, with strong holiday peaks. The US is the largest market, and middle-aged adults are the primary customers. Strategic focus on stabilizing revenue and leveraging high-margin products could enhance business performance.

## Repository Structure
- `Europe_Bike_Store_Sales.csv`: Raw dataset containing sales data for analysis.
- `main.ipynb`: Jupyter notebook with data cleaning, preparation, analysis, and visualizations.
- `README.md`: This file, summarizing the project and insights.

## How to Use
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Open `main.ipynb` in Jupyter Notebook to explore data cleaning, analysis, and visualizations.
4. Ensure `Europe_Bike_Store_Sales.csv` is in the same directory as `main.ipynb` for the notebook to run correctly.

## Visualizations
All visualizations (e.g., revenue trends, product performance, and demographic breakdowns) are generated within `main.ipynb`. To view them, run the notebook in a Jupyter environment.
