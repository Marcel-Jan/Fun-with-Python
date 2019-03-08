import pandas as pd
__author__ = 'Marcel-Jan Krijgsman'

# Show wider tables. I've got the screen for it.
pd.set_option('display.width', 300)

fuel_file = "Pandas moon fueling.xlsx"
xl = pd.ExcelFile(fuel_file)
print(xl.sheet_names)
fuel_df = xl.parse("Moon", header=[1], index_col=[0,1,2])

# Dimension of the data frame
sheet_width = fuel_df.shape[1]
sheet_depth = fuel_df.shape[0]
print("sheet_width: " + str(sheet_width))
print("sheet_depth: " + str(sheet_depth))


# print(fuel_df.columns)

weeknumbers = fuel_df.columns
weeknumbers_list = list(fuel_df.columns)
spacecustomers = fuel_df.iloc[1]


# Make list of all cells with "Week" in the name.
positions_weeknumbers = [pos for pos,field in enumerate(weeknumbers_list) if "Week" in field]
print("Weeknumbers cel positions: " + str(positions_weeknumbers))

# Adjust the columns so they show weeknumbers for every column in that week
# -------------------------------------------------------------------------
start_position = 0
# Loop through values with "Week" in the name
for weeknr_pos in positions_weeknumbers:
    # Go from the start position of that week and name everything with that weeknumber
    # until the end of that week.
    for pos in range(start_position, weeknr_pos):
        # Cell gets weeknumber in the
        weeknumbers_list[pos] = weeknumbers_list[weeknr_pos]
    # Determine the first column position of the next weeknumber.
    start_position = weeknr_pos + 1
    # The last column of weeknr has the totals. We'll remove that one.
    weeknumbers_list[weeknr_pos] = "Remove"


print(fuel_df.iloc[1])

# print(weeknumbers_list)
fuel_df.columns = weeknumbers_list

# Remove columns with totals.
fuel_df.drop("Remove", axis=1, inplace=True)

# Remove the first two rows
fuel_df = fuel_df.iloc[2:]


print(fuel_df.head())

spacecustomers_cleanlist = [x for x in spacecustomers if str(x) != 'nan']
print("spacecustomers_cleanlist: " + str(spacecustomers_cleanlist))

# Make names spacecustomers part of the header.
column_array = []
column_array.append(fuel_df.columns)
column_array.append(spacecustomers_cleanlist)
fuel_df.columns = column_array

# print(fuel_df.columns)
# print(fuel_df)

# Add a column to define what row is the amount of fuel and what is the price
row_definer_column = []
for rowdef in range(2, sheet_depth):
    # print(rowdef)
    if rowdef % 2 == 0:
        # Even
        row_definer_column.append("Amount")
    elif rowdef % 2 == 1 and rowdef != 1:
        # Uneven
        row_definer_column.append("Price")

fuel_df.insert(loc=3, column='amount_or_price', value=row_definer_column)
fuel_df.set_index('amount_or_price', append=True, inplace=True)

fuel_df.index.names = ['Location', 'Description', 'Fueling_port', 'amount_or_price']

fuel_df = fuel_df.iloc[:-6]
print(fuel_df)
fuel_df = fuel_df.stack(1)
print(fuel_df)
fuel_df = fuel_df.unstack(3)
print(fuel_df)
fuel_df = fuel_df.stack(0)

fuel_df.index.names = ['Location', 'Description', 'Fueling_port', 'Space_customer', 'Weeknumber']
print(fuel_df)
# print(fuel_df.to_csv())
print(fuel_df.to_csv('pandas_moon_fueling.csv'))
