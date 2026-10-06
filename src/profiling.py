import pandas as pd

def profile_dataframe(df : pd.DataFrame , name :str)-> None:
   print ("\n"+"="*50)
   print(f"TABLE:{name}")
   print("="*50)

   print("\nShape")
   print(df.shape)

   print("\nColumns")
   print(df.columns.tolist())


   print("\nData")
   print (df.dtypes)


   print("\nMissing Values")
   print(df.isna().sum())

   print("\nMissing pourcentage")
   print((df.isna().mean()*100).round(2)) 

   print("\nDuplicate rows")   
   print(df.duplicated().sum())

   print("\nUnique rows")
   print (df.nunique())
   print("\nStatistics")
   print(df.describe(include="all"))