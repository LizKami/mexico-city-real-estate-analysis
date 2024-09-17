# mexico-city-real-estate-analysis
The goal is to determine whether sale prices are influenced more by property size or location.

**Problem-Statement**

The real estate market in Mexico is influenced by various factors, with property size and location often seen as key determinants of sale price. However, the relative influence of these factors remains unclear. This project aims to analyze a dataset of properties for sale from Properati.com to determine whether sale prices are more influenced by property size or location. By leveraging Python data structures and libraries such as pandas, I will clean and organize the data, visualize key relationships using scatter and box plots, and examine correlations to assess the impact of these variables on property prices. The findings from this analysis will provide insights into the primary drivers of real estate prices in Mexico, helping potential buyers and sellers make informed decisions.



**Results and Conclusions**

The provided Python script performs a comprehensive data cleaning and exploratory data analysis (EDA) of Mexico City real estate data, merging multiple datasets, cleaning them, and performing visual and statistical analysis. Below is a summary of the results and conclusions:

Results:
Data Loading and Cleaning:

Three CSV files were loaded containing real estate data.
Missing values were dropped from all dataframes (df1, df2, df3).
For the price_usd column in df1 and the price_mxn column in df2, characters (like $ and ,) were removed, and values were converted to floats. For df2, prices in pesos (MXN) were converted to USD using a 19:1 exchange rate.
In df3, latitude, longitude, and state columns were extracted from existing columns. The datasets were then concatenated into a single dataframe.
Exploratory Data Analysis (EDA):

Visualizing Home Sizes:

A histogram and boxplot showed that home sizes ("area_m2") are right-skewed (many smaller homes and a few larger ones), leading to a mean area larger than the median.
Mean Price by State:

A bar chart showed that Querétaro initially appeared as the state with the highest average real estate prices.
Price per Square Meter:

After accounting for home size (price_per_m2), Mexico City (Distrito Federal) emerged as the most expensive market by a large margin. Many of the top GDP states were also high in real estate prices.
Price vs. Area Correlation:

A scatter plot showed a positive correlation between home size (area_m2) and price (price_usd), meaning larger homes tend to be more expensive.
The correlation coefficient for the entire dataset was about 0.5, indicating a moderate relationship between house size and price.
State-Specific Analysis (Morelos and Mexico City):

For Morelos, the correlation between home size and price was stronger with a correlation coefficient close to 1, showing a strong positive relationship.
In Mexico City, the correlation was weaker (lower correlation coefficient), suggesting other factors, besides size, drive prices in the country's most economically powerful urban center.
Conclusions:
Home Size Distribution:

Home sizes in Mexico City's real estate market tend to be right-skewed, with many homes being smaller than average, but a few significantly larger homes pushing up the mean size.
Mean House Price by State:

While Querétaro initially appeared to have the most expensive real estate, this was misleading due to differences in house sizes. Mexico City (Distrito Federal) was found to have the highest real estate prices per square meter, aligning better with its economic status.
Relationship Between Size and Price:

Larger homes tend to be more expensive. This holds true across most states, with a moderate correlation for the entire dataset.
In Morelos, there is a strong relationship between size and price, while in Mexico City, the relationship is weaker, possibly due to other factors like location, amenities, or demand influencing prices more than just size.
Market Insights:

Mexico City's real estate market is highly competitive, with price influenced by factors other than size, making it distinct from other regions like Morelos, where home size plays a more direct role in pricing.
In conclusion, the analysis shows that home prices in Mexico vary widely by state, and the relationship between home size and price is stronger in some regions (like Morelos) than others (like Mexico City). Understanding regional market dynamics and accounting for variables like price per square meter provides a more accurate view of real estate trends.
