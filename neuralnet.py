import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from datetime import datetime
import psutil
import random
import string

# Define the model
model = keras.Sequential([
    layers.Input(shape=(2,)),  # Input layer with 2 features (x1, x2)
    layers.Dense(8, activation='relu'),  # Hidden layer with 8 neurons and ReLU activation
    layers.Dense(4, activation='relu'),  # Another hidden layer with 4 neurons and ReLU activation
    layers.Dense(1, activation='sigmoid')  # Output layer with 1 neuron and sigmoid activation
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate some sample data
num_samples = 1000
x1 = np.random.rand(num_samples)
x2 = np.random.rand(num_samples)
X = np.column_stack((x1, x2))
y = np.where(x1 > x2, 1, 0)

# Train the model
model.fit(X, y, epochs=100)

# Evaluate the model
loss, accuracy = model.evaluate(X, y, verbose=0)
print('Accuracy:', accuracy)

# Test the model with some examples
test_data = np.array([[0.2, 0.5], [0.8, 0.3], [0.6, 0.6]])
predictions = model.predict(test_data)
print("Predictions:", predictions)

# Print a simulated MAC address
def generate_fake_mac():
    return ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)]).upper()

print(f"Machine MAC Address: {generate_fake_mac()}")

# Print current timestamp
print(f"Timestamp: {datetime.now()}")

# Print memory used
memory_info = psutil.virtual_memory()
print(f"Memory Used: {memory_info.used / (1024 * 1024):.2f} MB")
