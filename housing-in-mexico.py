!pip install pandas
import pandas as pd
# Loading CSV files into DataFrames

# Try with 'ISO-8859-1' encoding
df1 = pd.read_csv("C:/Users/User/Desktop/mexico real estate data 1.csv", encoding='ISO-8859-1')
df1.info()
df2 = pd.read_csv("C:/Users/User/Desktop/mexico real estate data 2.csv", encoding='ISO-8859-1')
df2.info()
df3 = pd.read_csv("C:/Users/User/Desktop/mexico real estate data 3.csv", encoding='ISO-8859-1')
df2.info()

#cleaning df1
# Drop null values from df1
df1.dropna(inplace=True)
df1.info()

# Clean "price_usd" column in df1
df1.dropna( inplace=True)
df1 = df1.dropna(subset=["price_usd"]) # Specify column to avoid dropping entire rows
# Remove characters and convert to float
df1["price_usd"] = df1["price_usd"].str.replace("$", "", regex=False).str.replace(",", "").astype(float)

#cleaning df2
df2.info()
# Drop null values from df2
df2.dropna(inplace=True)
# Remove characters and convert to float
df2["price_mxn"] = df2["price_mxn"].str.replace("$", "", regex=False).str.replace(",", "").astype(float)
# Create "price_usd" column for df2 (19 pesos to the dollar in 2014)
df2["price_usd"] = ((df2["price_mxn"]/19).round(2))
# Drop "price_mxn" column from df2
df2.drop(columns=["price_mxn"],inplace=True)

#cleaning df3
df3.info()
df3.dropna(inplace= True)
# Create "lat" and "lon" columns for df3
df3[["lat", "lon"]] = df3["lat-lon"].str.split(",", expand=True)
# Create "state" column for df3
df3["state"] = df3["place_with_parent_names"].str.split("|",expand=True)[2]
# Drop "place_with_parent_names" and "lat-lon" from df3
df3.drop(columns=["place_with_parent_names","lat-lon"],inplace=True)
df3.head()

#Concatenate df1, df2, and df3
df = pd.concat([df1,df2,df3])

# Save df as a CSV
df.to_csv("C:/Users/User/Desktop/mexico real estate clean.csv",index=False)



#EXPLORATORY DATA ANALYSIS (EDA)
!pip install matplotlib
!pip install plotly
import matplotlib.pyplot as plt
import plotly.express as px
#location data visualization using "lat" & "lon"
# Use plotly express to create figure
fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat="lat",
    lon="lon",
    center={"lat": 19.43, "lon": -99.13},  # Map will be centered on Mexico City
    width=600,  # Width of map
    height=600,  # Height of map
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)

# Add mapbox_style to figure layout
fig.update_layout(mapbox_style="open-street-map")

# Show figure
fig.show()



#categorical data "state"
# Get value counts of "state" column
df["state"].value_counts().head()

#Numerical Data: "area_m2" and "price_usd"
# Describe "area_m2", "price_usd" columns (descriptive statistics)
df[["area_m2", "price_usd"]].describe()

#Let's start by looking at "area_m2". It's interesting that the mean is larger than the median (another name for the 50% 
#quartile). Both of these statistics are supposed to give an idea of the "typical" value for the column, so why is there a 
#difference of almost 15 m2 between them? To answer this question, we need to see how house sizes are distributed in our 
#dataset. Let's look at two ways to visualize the distribution: a histogram and a boxplot.

# Use Matplotlib to create histogram of "area_m2"
plt.hist(df["area_m2"]);
# Add x-axis label
plt.xlabel("Area [sq meters]")
# Add y-axis label
plt.ylabel("Frequency")
# Add title
plt.title("Distribution of Home Sizes")
# Show the plot
plt.show()
#Looking at our histogram, we can see that "area_m2" skews right. In other words, there are more houses at the lower end of the 
#distribution (50-200m2) than at the higher end (250-400m2). That explains the difference between the mean and the median.

# Use Matplotlib to create boxplot of "area_m2"
# Clear previous plot settings
plt.clf()
plt.boxplot(df["area_m2"],vert=False);
# Add x-axis label
plt.xlabel("Area [sq meters]")
# Add title
plt.title("Distribution of Home Sizes")
plt.show()


#Which state has the most expensive real estate market?

#Use the groupby method to create a Series named mean_price_by_state, where the index contains each state in the dataset and the 
#values correspond to the mean house price for that state.

# Declare variable `mean_price_by_state`
mean_price_by_state = df.groupby("state")["price_usd"].mean().sort_values(ascending=False)

# Create bar chart from `mean_price_by_state` using pandas
mean_price_by_state.plot(
kind="bar",
xlabel="State",
ylabel="Mean Price [USD]",
title="Mean House Price by State"
);
plt.show()


#It seems odd that Querétaro would be the most expensive real estate market in Mexico when, according to recent GDP numbers, 
#it's not in the top 10 state economies. With all the variations in house sizes across states, a better metric to look at would 
#be price per m2. In order to do that, we need to create a new column

# Create "price_per_m2" column
df["price_per_m2"] = df["price_usd"]/df["area_m2"]
# Group `df` by "state", create bar chart of "price_per_m2"
(
    df
    .groupby("state")
    ["price_per_m2"].mean()
    .sort_values(ascending=False)
    .plot(
        kind="bar",
        xlabel="State",
        ylabel="Mean Price per M^2[USD]",
        title="Mean House Price per M^2 by State"
    )
)
plt.show()
#Now we see that the capital Mexico City (Distrito Federal) is by far the most expensive market. Additionally, many of the top 10 
#states by GDP are also in the top 10 most expensive real estate markets. So it looks like this bar chart is a more accurate 
#reflection of state real estate markets.

#Is there a relationship between home size and price?
# Clear previous plot settings
plt.clf()
# Create scatter plot of "price_usd" vs "area_m2"
plt.scatter(x=df["area_m2"],y=df["price_usd"]);
# Add x-axis label
plt.xlabel("Area [sq metres]")
# Add y-axis label
plt.ylabel("Price [USD]")
# Add title
plt.title("Price vs Area");
plt.show()
#While there's a good amount of variation, there's definitely a positive correlation - in other words, the bigger the house, 
#the higher the price.

#Quantifying this correlation
#Calculate correlation of "price_usd" and "area_m2"
p_correlation = df["area_m2"].corr(df["price_usd"])
p_correlation
#The correlation coefficient is over 0.5, so there's a moderate relationship house size and price in Mexico. But does this 
#relationship hold true in every state? Let's look at a couple of states, starting with Morelos.

# Declare variable `df_morelos` by subsetting `df`
df_morelos = df[df["state"]=="Morelos"]
# Create scatter plot of "price_usd" vs "area_m2" in Morelos
plt.clf()
plt.scatter(x=df_morelos["area_m2"], y=df_morelos["price_usd"])
# Add x-axis label
plt.xlabel("Area sq meters")
# Add y-axis label
plt.ylabel("price_usd")
# Add title
plt.title("Morelos: Price vs. Area")
plt.show()
#It looks like the correlation is even stronger within Morelos. Let's calculate the correlation 
#coefficient and verify that that's the case.
# Calculate correlation of "price_usd" and "area_m2" in `df_morelos`
p_correlation = df_morelos["area_m2"].corr(df_morelos["price_usd"])
p_correlation
#With a correlation coefficient that high, we can say that there's a strong relationship between house size and price in Morelos.

#To conclude, I'll look at the capital Mexico City (Distrito Federal)
# Declare variable `df_mexico_city` by subsetting `df`
df_mexico_city = df[df["state"]=="Distrito Federal"]
# Create a scatter plot "price_usd" vs "area_m2" in Distrito Federal
plt.clf()
plt.scatter(df_mexico_city["area_m2"], df_mexico_city["price_usd"]) ; 
# Add x-axis label
plt.xlabel("Area [sq meters]")  
plt.ylabel("Price [USD]")  
# Add title
plt.title("Mexico City: Price vs. Area")  
plt.show()
# Calculate correlation of "price_usd" and "area_m2" in `df_mexico_city`
p_correlation = df_mexico_city["area_m2"].corr(df_mexico_city["price_usd"])
p_correlation
#One interpretation is that the relationship we see between size and price in many states doesn't hold true in the country's 
#biggest and most economically powerful urban center because there are other factors that have a larger influence on price.
