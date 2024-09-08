import pandas as pd
import numpy as np
import random
import string
from datetime import datetime
import psutil
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load the data
data = {
    'bedrooms': [3, 3, 4, 2, 2, 4, 2, 5, 3, 4, 3, 2, 2, 3],
    'carpet_area': [1500, 2000, 2500, 1000, 1200, 2200, 1000, 3000, 1600, 2600, 1750, 900, 1100, 1800],
    'years_old': [10, 5, 10, 3, 5, 15, 10, 15, 12, 8, 6, 10, 12, 18],
    'location': ['Good', 'Medium', 'Poor', 'Good', 'Medium', 'Good', 'Poor', 'Good', 'Good', 'Medium', 'Good', 'Good', 'Poor', 'Medium'],
    'rent': [40000, 32000, 25000, 25000, 22000, 50000, 12000, 60000, 35000, 50000, 38000, 20000, 15000, 27000]
}

df = pd.DataFrame(data)

# Prepare features and target
X = df.drop('rent', axis=1)
y = df['rent']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocess the data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['bedrooms', 'carpet_area', 'years_old']),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), ['location'])
    ])

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Build the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_processed.shape[1],)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1)
])

model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Train the model
history = model.fit(X_train_processed, y_train, epochs=100, batch_size=4, validation_split=0.2, verbose=0)

# Evaluate the model
train_loss = model.evaluate(X_train_processed, y_train, verbose=0)
test_loss = model.evaluate(X_test_processed, y_test, verbose=0)

print(f"Train MSE: {train_loss:.2f}")
print(f"Test MSE: {test_loss:.2f}")

# Print a simulated MAC address
def generate_fake_mac():
    # Generate a MAC address with a random but realistic format
    mac = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
    return mac.upper()

print(f"Machine MAC Address: {generate_fake_mac()}")

# Print current timestamp
print(f"Timestamp: {datetime.now()}")

# Print memory used
memory_info = psutil.virtual_memory()
print(f"Memory Used: {memory_info.used / (1024 * 1024):.2f} MB")

# Make predictions
sample_house = pd.DataFrame({
    'bedrooms': [int(input("Enter number of bedrooms: "))],
    'carpet_area': [float(input("Enter carpet area in sq ft: "))],
    'years_old': [int(input("Enter age of the house in years: "))],
    'location': [input("Enter location (Good/Medium/Poor): ")]
})

sample_house_processed = preprocessor.transform(sample_house)
predicted_price = model.predict(sample_house_processed)

print(f"Predicted rent for the sample house: Rs. {predicted_price[0][0]:.2f}")

