import pandas as pd
link="https://en.wikipedia.org/wiki/Periodic_table"
table=pd.read_html(link)
print(len(table))
required_table=table[1]
print(required_table)
print(required_table.head())
print(required_table.tail())

required_table.to_csv("Periodic Data.csv",index=False, encoding='utf-8')
