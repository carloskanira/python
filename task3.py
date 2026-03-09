"""write python code which prompt the user to input hours studied attendance percentage number of assignments completed
 and past exam score. the system should the predict if student will pass or fail
 1.validate that all inputs are numeric and within expected ranges
 2.
 apply the same scaling method used during model training
 3.use the trained KNN model to predict PASSor FAIL
 4.display a claer mesaage such as:based on the entered data the student is likely to pass exams"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
data = pd.read_excel("studentperfomance.xlsx")

# Remove missing values
data = data.dropna()

# Encode final_result
label_encoder = LabelEncoder()
data['final_result'] = label_encoder.fit_transform(data['final_result'])

# Separate features and target
features = data.drop('final_result', axis=1)
target = data['final_result']

# Normalize features
scaler = MinMaxScaler()
normalized_features = scaler.fit_transform(features)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    normalized_features, target, test_size=0.2, random_state=42
)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)


# Function to get user input automatically for all features
def get_user_input():
    user_values = []

    try:
        print("\nEnter student details:")

        for column in features.columns:
            value = float(input(f"Enter {column}: "))
            user_values.append(value)

        return user_values

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None


# Prediction function
def predict_student_performance(user_input):

    if user_input is not None:

        scaled_input = scaler.transform([user_input])

        prediction = knn.predict(scaled_input)

        result = label_encoder.inverse_transform(prediction)[0]

        print(f"\nPrediction: The student will likely {result}")

    else:
        print("Prediction failed due to invalid input.")


# Run program
if __name__ == "__main__":
    user_input = get_user_input()
    predict_student_performance(user_input)