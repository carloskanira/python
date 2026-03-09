
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_excel("studentperfomance.xlsx")
# Check for missing values
print(data.isnull().sum())
# Encode the Final_result labels
label_encoder = LabelEncoder()
data['final_result'] = label_encoder.fit_transform(data['final_result'])
# Normalize feature values
scaler = MinMaxScaler()
features = data.drop('final_result', axis=1)
normalized_features = scaler.fit_transform(features)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(normalized_features, data['final_result'], test_size=0.2, random_state=42)
# Train a KNN classifier and evaluate for different k values    
k_values = range(1, 6)
accuracy_scores = []
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_scores.append(accuracy)
    print(f"K={k}: Accuracy={accuracy}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
# Plot accuracy versus k
plt.plot(k_values, accuracy_scores, marker='o')
plt.title('KNN Accuracy for Different K Values')
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.xticks(k_values)
plt.grid()
plt.show()

