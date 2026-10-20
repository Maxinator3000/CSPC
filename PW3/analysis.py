import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")
print("Dataset shape :",df.shape)
print("\nFirts five rows :")
print(df.head())
columns = ["age", "chol", "trestbps", "thalach"]
continuous = df[columns]
print("\nSummary statistics:")
print(continuous.describe())
print("\nMissing values:")
print(continuous.isnull().sum())
fig, axes = plt.subplots(2,2, figsize=(10,8)) 
for column, ax in zip(columns,axes.flat):
    values = continuous[column].dropna()
    ax.hist(values, bins = 20,density = True, edgecolor = "black", alpha = 0.7)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Density")
    ax.grid(alpha=0.2)
plt.savefig("distributions.png", dpi = 150)
plt.tight_layout()    
plt.show()
fig,axes = plt.subplots(2,2, figsize=(10,8)) 
print("\nShapiro-Wilk normality tests :")
for column, ax in zip(columns,axes.flat):
    values = continuous[column].dropna()
    W,p = stats.shapiro(values)
    print(f"\nVariable : {column}")
    print(f"W statistic : {W:4f}")
    print(f"p-value : {p:.6g}")
    if p < 0.05 :
        print("Verdict: evidence against normality.")
    else:
        print("Verdict: insufficient evidence to reject normality.")    
    stats.probplot(values, dist="norm", plot=ax)
    ax.set_title(f"Q-Q Plot : {column}")        
    ax.grid(alpha = 0.2)
plt.savefig("normality_qq.png", dpi=150)    
plt.tight_layout()
plt.show()    

