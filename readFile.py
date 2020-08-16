import pandas as pd
import numpy as np
import tablesInformation
import plotInfo
#### STEP 1 ####

# Reading the document from CSV file in the directory
print('# Reading the document from CSV file in the directory')
df = tablesInformation.dfTable()
print(df)

#### STEP 2 ####

# Getting the columns that will used in this development
print('# Getting the columns that will used in this development')
data_frame = tablesInformation.tblDataFrame()
print(data_frame)

#### STEP 3 ####

# Getting all the data from column 'Estado'
# Getting the unique result from column 'Estado'
# Getting the total states in their column
data_states = pd.DataFrame(df, columns = ['Estado'])
data_states_unique = df['Estado'].unique()
data_states_qty = len(data_states_unique)

# Getting months with unique results from their column
# Getting the quantity of months
data_months = df['Mes'].unique()
data_months_qty = len(data_months)

# Getting years with unique results from their column
# Getting the quantity of years
data_years = df['Año'].unique()
data_years_qty = len(data_years)

# Getting visitors with unique results from their column
# Getting the quantity of visitors
data_visitors = df['Tipo de visitantes'].unique()
data_visitors_qty = len(data_visitors)

# Converting the data types
df = df.convert_dtypes()

# Total per state per month and per year
print('# Total per state per month and per year')
total_state_by_month = tablesInformation.total_state_by_month()
total_state_by_year = tablesInformation.total_state_by_year()
print(total_state_by_month)
print(total_state_by_year)

#### STEP 3 ####

# Total per kind of visitor
print('# Total per kind of visitor')
total_state_by_kind_visitor = tablesInformation.total_state_by_kind_visitor()
print(total_state_by_kind_visitor)

# Total per kind of visitor and time (year and month)
print('# Total per kind of visitor and time (year and month)')
total_state_by_kind_visitor_year = tablesInformation.total_state_by_kind_visitor_year()
total_state_by_kind_visitor_month = tablesInformation.total_state_by_kind_visitor_month()
print(total_state_by_kind_visitor_year)
print(total_state_by_kind_visitor_month)

# Total per kind of work type and time (year and month)
print('# Total per kind of work type and time (year and month)')
total_state_by_kind_work_year = tablesInformation.total_state_by_kind_work_year()
total_state_by_kind_work_month = tablesInformation.total_state_by_kind_work_month()
print(total_state_by_kind_work_year)
print(total_state_by_kind_work_month)

# Total per kind of work type and kind of visitor
print('# Total per kind of work type and kind of visitor')
total_state_by_kind_work_visitor_year = tablesInformation.total_state_by_kind_work_visitor_year()
print(total_state_by_kind_work_visitor_year)

# Average per state
print('# Average per state')
average_state_month = tablesInformation.average_state_month()
average_state_year = tablesInformation.average_state_year()
print(average_state_month)
print(average_state_year)

# Average per state and kind of visitors
print('# Average per state and kind of visitors')
average_state_visitors_month = tablesInformation.average_state_visitors_month()
average_state_visitors_year = tablesInformation.average_state_visitors_year()
print(average_state_visitors_month)
print(average_state_visitors_year)

# percentage per kind of visitor by month per state
print('# percentage per kind of visitor by month per state')
percentage_visitors = total_state_by_kind_work_month / len(df)
print(percentage_visitors)

# percentage per kind of work type and time (year and month)
print('# percentage per kind of work type and time (year and month)')
percentage_visitors_month = tablesInformation.percentage_visitors_month()
percentage_visitors_year = tablesInformation.percentage_visitors_year()
print(percentage_visitors_month)
print(percentage_visitors_year)

# percentage visitor per kind of work
print('# percentage visitor per kind of work')
percentage_visitors_work_month = tablesInformation.percentage_visitors_work_month()
percentage_visitors_work_year = tablesInformation.percentage_visitors_work_year()
print(percentage_visitors_work_month)
print(percentage_visitors_work_year)


#### STEP 4 ####
print('#### STEP 4 ####')
plotInfo.plotInfo(total_state_by_month,'Total per state per month','State', 'Total of visitors')
plotInfo.plotInfo(total_state_by_year,'Total per state per year', 'State', 'Total of visitors')
plotInfo.plotInfo(total_state_by_kind_visitor,'Total per kind of visitor', 'Kind of visitors', 'Total of visitors')
plotInfo.plotInfo(total_state_by_kind_visitor_month,'Total per kind of visitor and time (month)', 'Kind of visitors (monthly)', 'Total of visitors')
plotInfo.plotInfo(total_state_by_kind_visitor_year,'Total per kind of visitor and time (month)', 'Kind of visitors yearly)', 'Total of visitors')
plotInfo.plotInfo(total_state_by_kind_work_month,'Total per kind of work type and time (month)', 'Kind of visitors & work (monthly)', 'Total of visitors')
plotInfo.plotInfo(total_state_by_kind_work_year,'Total per kind of work type and time (year)', 'Kind of visitors & work (yearly)', 'Total of visitors')
plotInfo.plotInfo(total_state_by_kind_work_visitor_year,'Total per kind of work type and kind of visitor', 'Kind of visitors & work', 'Total of visitors')
plotInfo.plotInfo(average_state_month,'Average per state (month)', 'States (monthly)', 'Avg of visitors')
plotInfo.plotInfo(average_state_year,'Average per state (year)', 'States (yearly)', 'Avg of visitors')
plotInfo.plotInfo(average_state_visitors_month,'Average per state and kind of visitors (month)', 'Kind of visitors per state (yearly)', 'Avg of visitors')
plotInfo.plotInfo(average_state_visitors_year,'Average per state and kind of visitors(year)', 'Kind of visitors per state (yearly)', 'Avg of visitors')
plotInfo.plotInfo(percentage_visitors,'percentage per kind of visitor by month per state', 'Kind of visitors per state', 'Percent of visitors')
plotInfo.plotInfo(percentage_visitors_month,'percentage per kind of work type and time (month)', 'Work (monthly)', 'Percent of visitors')
plotInfo.plotInfo(percentage_visitors_year,'percentage per kind of work type and time (year)', 'Work (yearly)', 'Percent of visitors')
plotInfo.plotInfo(percentage_visitors_work_month,'percentage per state per month', 'States (monthly)', 'Percent of visitors')
plotInfo.plotInfo(percentage_visitors_work_year,'percentage per state per year', 'States (yearly)', 'Percent of visitors')
