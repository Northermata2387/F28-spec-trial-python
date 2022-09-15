# 1. Create a new file called data_presenter.py.

# 2. Open the CupcakeInvoices.csv.

# 3.Loop through all the data and print each row.
# import pandas as pd

# filename = 'CupcakeInvoices.csv'
# df = pd.read_csv(filename)

# for index, row in df.iterrows():
#     print(row)

# 4. Loop through all the data and print the type of cupcakes purchased.

# importing the module
# import pandas as pd

# # read specific columns of csv file using Pandas
# df = pd.read_csv("CupcakeInvoices.csv", usecols=['cupcake'])
# print(df)

# 5. Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.

# # importing the module
# import pandas as pd

# # # read specific columns of csv file using Pandas
# df = pd.read_csv("CupcakeInvoices.csv")
# df['Total'] = df['quantity'] * df['cost']
# print(df)

# 6. Loop through all the data, and print out the total for all invoices combined.

# Importing the module
# import pandas as pd

# # # read specific columns of csv file using Pandas
# df = pd.read_csv("CupcakeInvoices.csv")
# df['Total'] = df['quantity'] * df['cost']
# print(df.sum())
