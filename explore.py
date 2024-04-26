import pandas as pd

# TODO uncomment the print statements, one at a time
# run the code each time


# the main difference between this activity and the last one:
# 3.2.1 graphs all data
# 3.2.2 chooses a portion of the data



# ---- demo goals ----
# 1) file input old school vs pandas
# 2) make a list without duplicates (list vs pandas)
# 3) make a list of just United States items (list vs pandas)



# 1) read the data from the file
f = open("u322/elec_access_data.csv")
my_list = []
for line in f:
    temp = line.strip()
    my_list.append(temp.split(','))   # append each row as a list
f.close()
# print("\na slice:", my_list[0:5])



# 2) make a list of countries, remove duplicates with 'set'
countries = []
for row in my_list[1:]:
    countries.append(row[0])

countries = list(set(countries))
# print("\nno duplicates using 'set':", countries)
# print("length of countries, no duplicates:", len(countries))



# 3) make a list of items in 'United States'
us_list = []
for row in my_list[1:]:
    if row[0] == 'United States':
        us_list.append(row)
# print("\nlist of US items:", us_list)



# ---------------------------------------
print("\n\n---- pandas ----")
# 1) read the data
df = pd.read_csv("u32SOLNS/u322SOLNS/elec_access_data.csv", header=0)


# 2) no duplicates
countries = df['Entity'].unique()
# print("\npandas no duplicates:", countries)



# 3) data frame of entities == 'United States'
us_list = df[df['Entity'] == 'United States']
# NOTE: When using [], the result is a Pandas DataFrame.
# print("\npandas data frame of US:\n", us_list)
# print(type(us_list))


# further experiments
# create a DataFrame of all the rows where the country is equal to United States, get just the years
us_list = df[df['Entity'] == 'United States']['Year']
# print("\npandas data frame of US years only:\n", us_list)
# print(type(us_list))




