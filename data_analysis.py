import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load Heart Disease Dataset from UCIMLRepo
from ucimlrepo import fetch_ucirepo
heart_disease = fetch_ucirepo(id=45)
print(heart_disease.metadata) 
  
# variable information 
print(heart_disease.variables) 
X = heart_disease.data.features
y = heart_disease.data.targets

# Load Pima Indians Diabetes Dataset
pima_data = pd.read_csv('Data/diabetes.csv')

# Prepare Pima dataset
pima_data = pima_data.dropna()
features_pima = pima_data.drop('Outcome', axis=1)  # Assuming 'Outcome' is the target variable
target_pima = pima_data['Outcome']

# Normalize data
scaler = StandardScaler()
features_scaled_pima = scaler.fit_transform(features_pima)

# Split the Pima data
X_train, X_test, y_train, y_test = train_test_split(features_scaled_pima, target_pima, test_size=0.2, random_state=42)

# Train a model (e.g., Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
