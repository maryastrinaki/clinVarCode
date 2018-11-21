#geting and store the columns that we need in a csv file

import pandas as pd 

data = pd.read_csv("example_analyses.csv") 
newdf1 = data[["# locus","type","clinvar","length"]]
newdf1.to_csv('example_analyses_modified.csv')
