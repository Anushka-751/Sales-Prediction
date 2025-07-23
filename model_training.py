# model_training.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# Step 1: Load Dataset
print(" Reading dataset.csv...")
df = pd.read_csv("dataset.csv", index_col=0)
print(" Dataset loaded.")

# Step 2: Basic EDA
print("\n Dataset Info:")
print(df.info())
print("\n Dataset Description:")
print(df.describe())
print("\n Missing Values:")
print(df.isnull().sum())

# Optional: Visualization
print("\n Generating pairplot...")
sns.pairplot(df)
plt.suptitle("Feature Relationships", y=1.02)
plt.show()

# Step 3: Prepare Data
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# Step 4: Train-Test Split
print("\n Splitting train/test...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train Model
print(" Training Linear Regression Model...")
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate Model
print("\n Model Trained.")
y_pred = model.predict(X_test)
print(" R2 Score:", r2_score(y_test, y_pred))
print(" Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Visualization: Actual vs Predicted
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.grid(True)
plt.show()

# Step 7: Save Model
print(" Saving model to 'sales_model.pkl'...")
with open("sales_model.pkl", "wb") as file:
    pickle.dump(model, file)
print(" Model saved successfully.")
