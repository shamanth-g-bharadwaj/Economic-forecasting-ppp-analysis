import pandas as pd
import numpy as np


df = pd.read_csv("2. CPI_Combined_Data_with_EDA(Monthly Data).csv")  


df["Year/Month"] = pd.to_datetime(df["Year/Month"], errors='coerce').dt.to_period("M").astype(str)


# Applying natural log 
columns_to_log = ["CPI_Singapore", "CPI_Switzerland", "Nominal", "Real"]
for col in columns_to_log:
    df[f"log_{col}"] = np.log(df[col])



# Display DAta
print(df.head())  

# Saving the transfomred data
df.to_csv("3. log_transformed_data.csv", index=False)  
