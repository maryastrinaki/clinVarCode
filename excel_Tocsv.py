#code to transorm xls file to csv file 

import pandas as pd
data_xls = pd.read_excel('example_analyses.xlsx')
data_xls.to_csv('example_analyses.csv', encoding='utf-8')
