# Import libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd

df=pd.read_csv('D:\ML model deplyment\myenv\dataset\BankNote_Authentication.csv')

# Features and target
X = df[['variance', 'skewness', 'curtosis', 'entropy']]
y = df['class']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Optional: check accuracy
accuracy = model.score(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")

# Save the model to a pickle file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
