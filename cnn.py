import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, Flatten, Dense, Dropout

# Assuming input_data is your feature matrix (n_samples, 20, 1)
# and target_data is your price values (n_samples, 1)

# Parameters
input_shape = (20, 1)  # Each sample has 20 digits, each treated as a feature
n_filters = 64         # Number of filters for Conv1D
kernel_size = 3        # Size of the convolutional filter
dropout_rate = 0.3     # Dropout rate to prevent overfitting

# Model Architecture
model = Sequential([
    Conv1D(filters=n_filters, kernel_size=kernel_size, activation='relu', input_shape=input_shape),
    Dropout(dropout_rate),
    Conv1D(filters=n_filters, kernel_size=kernel_size, activation='relu'),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(dropout_rate),
    Dense(64, activation='relu'),
    Dense(1, activation='linear')  # Output layer for regression
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

# Print model summary
model.summary()

# Assuming input_data is your input feature array and target_data is your target prices
# Train the model
input_data =[
66503475508126408822,
12462141253706297494,
17925271694289747107,
02042753238122342320,
72272151125920663581,
34010046000023825554,
24598817958517830425,
59067010553545546969,
49755157220540286110,
20489070523093950944,
35692715252657807006,
24898034983381851259,
70819051604419847017,
]

input_data_preprocessing =[]



target_data=[
284.6,
41.8,
259.8,
77.8,
64.2,
301.2,
145.7,
166.7,
152.8,
310.1,
94.9,
256.7,
258.5,
]

history = model.fit(input_data, target_data, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the model
loss, mae = model.evaluate(input_data, target_data)
print(f"Mean Absolute Error: {mae}")

# You can now use this model to predict prices on new data
# predicted_prices = model.predict(new_input_data)