import pandas as pd; 
df = pd.read_parquet('novacart-solution/data/bronze/orders/date=2025-11-07/data.parquet'); 
#print(df.shape); 
#print(df.head())


df = pd.read_parquet('data/bronze/customers/data.parquet'); 
#print(df.shape); 
#print(df.head())

df = pd.read_parquet('data/bronze/products/data.parquet'); 
print(df.shape); 
print(df.head())



