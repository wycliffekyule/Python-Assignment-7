import pandas as pd
#read file from source
file_path = r"C:\Users\Window\Downloads\cities_by_gdp.csv"
#Load the CSV file into a DataFrame
df = pd.read_csv(file_path)
#inspect dataset
print("Dataset loaded successfully! Here are the first 5 rows:")
print(df.head())
import matplotlib.pyplot as plt
#bar chart
plt.bar(df['Metropolitian_Area/City'], df['Metropolitian_Population'])
plt.xlabel('Metropolitan Area / City')
plt.ylabel('Metropolitan Population')
plt.title('Population of Metropolitan Areas')
