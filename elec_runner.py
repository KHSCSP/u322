# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['United States', 'Zimbabwe','Cuba', 'Caribbean small states', "Cameroon", "Burundi"]

# Load in the data with read_csv()
df = pd.read_csv("u322/elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()


# TIP:
# make a list of markers, line types, and colors
# and custom line types
# when configuring the plot, use random.choice to get from your list


# Plot the data on a line graph
for c in unique_countries:
    if c in my_countries:
      
        # match country to one of our we want to look at and get a list of years
        years = df[df['Entity'] == c]['Year']
        # This line of code is setting years equal to a list of years for a specific country
        # more info about this in the book

        # match country to one of our we want to look at and get a list of electriciy values
        sum_elec = df[df['Entity'] == c]['Access']

        # add each countries data to the graph
        plt.plot(years, sum_elec, label=c)

  
plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()
