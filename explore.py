import matplotlib.pyplot as plt
import pandas as pd


# the main difference between this activity and the last one:
# 3.2.1 graphs all data
# 3.2.2 chooses a portion of the data and groups data together



# ---- demo goals ----
# 1) file input old school vs pandas
# 2) make a list without duplicates (list vs pandas)
# 3) make a list of just United States items (list vs pandas)
# 4) plot the data for the US (year versus access)



# 1) read the data from the file
f = open("u32SOLNS/u322SOLNS/elec_access_data.csv")
my_list = []
for line in f:
    temp = line.strip()
    my_list.append(temp.split(','))   # append each row as a list
f.close()
print("\nlook at a slice:", my_list[0:5])
# ^^ comment out when ready to move on



# 2) make a list of countries, remove duplicates with 'set'
countries = []
# TODO


# print("\nno duplicates using 'set':", countries)
# print("length of countries, no duplicates:", len(countries))



# 3) make a list of items in 'United States'
us_list = []
for row in my_list[1:]:
    if row[0] == 'United States':
        us_list.append(row)
print("\nlist of US items:", us_list)



# ---------------------------------------
print("\n\n---- pandas ----")
# 1) read the data
df = pd.read_csv("u322/elec_access_data.csv", header=0)

# 2) no duplicates
# TODO

# print("\npandas no duplicates:", countries)



# 3) data frame of entities == 'United States'
# this is still a bit of magic to me...
# TODO

# NOTE: When using [], the result is a Pandas DataFrame.
# print("\npandas data frame of US:\n", us_list)




# 4) plotting data for us: years and access
# create a DataFrame of all the rows where the country is equal to United States, get just the years
# TODO

# print("\n maybe look at this pandas data frame:\n", us_access)

# plt.plot(us_years, us_access)
# plt.show()
# ^^ obviously uncomment those to see the graph



