import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
import math

# Load dataset
df = pd.read_csv("hour.csv")

# Renaming columns names to more readable names
df.rename(columns={
    'instant':'record_id',
    'dteday':'datetime',
    'holiday':'is_holiday',
    'workingday':'is_workingday',
    'weathersit':'weather_condition',
    'hum':'humidity',
    'mnth':'month',
    'cnt':'total_count',
    'hr':'hour',
    'yr':'year'
}, inplace=True)

# Drop unnecessary columns
df.drop(['record_id','casual', 'registered','datetime','temp'], axis=1, inplace=True)

# Separate features and target variable
X = df.drop(['total_count'], axis=1)
y = df['total_count']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define preprocessing steps for numerical features
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),  # Impute missing values with median
    ('scaler', StandardScaler())  # Standardize features
])

# Combine preprocessing steps for numerical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features)
    ])

# Define the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor())
])

# Fit the pipeline on training data
pipeline.fit(X_train, y_train)

# Predict on testing data
predictions = pipeline.predict(X_test)

# Evaluate the model and return prediction value:
rmse = math.sqrt(mean_squared_error(y_test, predictions))
print("Root Mean Squared Error:", rmse)
