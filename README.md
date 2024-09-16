# mexico-city-real-estate-analysis
The goal is to determine whether sale prices are influenced more by property size or location.

**Problem-Statement**

The real estate market in Mexico is influenced by various factors, with property size and location often seen as key determinants of sale price. However, the relative influence of these factors remains unclear. This project aims to analyze a dataset of properties for sale from Properati.com to determine whether sale prices are more influenced by property size or location. By leveraging Python data structures and libraries such as pandas, I will clean and organize the data, visualize key relationships using scatter and box plots, and examine correlations to assess the impact of these variables on property prices. The findings from this analysis will provide insights into the primary drivers of real estate prices in Mexico, helping potential buyers and sellers make informed decisions.


#DAta wrangling with pandas

#data wrangling with pandas
import pandas as pd

# Loading CSV files into DataFrames
df1 = pd.read_csv("data/mexico-real-estate-1.csv")
df2 = pd.read_csv("data/mexico-real-estate-2.csv")
df3 = pd.read_csv("data/mexico-real-estate-3.csv")

# Drop null values from df1
df1.dropna(inplace=True)
df1.info()
# Clean "price_usd" column in df1
df1.dropna( inplace=True)
df1 = df1.dropna(subset=["price_usd"]) # Specify column to avoid dropping entire rows

# Remove characters and convert to float
df1["price_usd"] = df1["price_usd"].str.replace("$", "", regex=False).str.replace(",", "").astype(float)

<class 'pandas.core.frame.DataFrame'>
Int64Index: 583 entries, 0 to 699
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   property_type  583 non-null    object 
 1   state          583 non-null    object 
 2   lat            583 non-null    float64
 3   lon            583 non-null    float64
 4   area_m2        583 non-null    float64
 5   price_usd      583 non-null    object 
dtypes: float64(3), object(3)
memory usage: 31.9+ KB

df1.head()


# Drop null values from df2
df2.dropna(inplace=True)

# Create "price_usd" column for df2 (19 pesos to the dollar in 2014)
df2["price_usd"] = ((df2["price_mxn"]/19).round(2))

# Drop "price_mxn" column from df2
df2.drop(columns=["price_mxn"],inplace=True)

df2.head()

# Drop null values from df3
df3.dropna(inplace=True)
# Create "lat" and "lon" columns for df3
df3[["lat", "lon"]] = df3["lat-lon"].str.split(",", expand=True)

# Create "state" column for df3
df3["state"] = df3["place_with_parent_names"].str.split("|",expand=True)[2]
# Drop "place_with_parent_names" and "lat-lon" from df3
df3.drop(columns=["place_with_parent_names","lat-lon"],inplace=True)

df3.head()

# Concatenate df1, df2, and df3
df = pd.concat([df1,df2,df3])

# Save df as a CSV
df.to_csv("data/mexico-real-estate-clean.csv",index=False)

