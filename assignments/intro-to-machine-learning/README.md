# 📘 Assignment: Introduction to Machine Learning with scikit-learn

## 🎯 Objective

Use the scikit-learn library to build and evaluate a machine learning model that can classify or predict outcomes from a real dataset, learning the core ML workflow: loading data, training a model, and measuring its performance.

## 📝 Tasks

### 🛠️ Load and Explore the Dataset

#### Description
Load the built-in Iris dataset from scikit-learn and explore its structure before building any model. Understanding your data is the first step in every machine learning project.

#### Requirements
Completed program should:

- Import the Iris dataset using `from sklearn.datasets import load_iris`
- Print the number of samples and features in the dataset
- Print the feature names and the class (target) names
- Print the first 5 rows of the feature data alongside their labels

#### Example

```
Samples: 150, Features: 4
Feature names: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Classes: ['setosa', 'versicolor', 'virginica']
```


### 🛠️ Train a Classification Model

#### Description
Split the dataset into training and test sets, then train a K-Nearest Neighbors (KNN) classifier on the training data.

#### Requirements
Completed program should:

- Split the data into 80% training and 20% test sets using `train_test_split` with `random_state=42`
- Create a `KNeighborsClassifier` with `n_neighbors=3`
- Train (fit) the classifier on the training set
- Print the number of training samples and test samples after the split

#### Example

```
Training samples: 120
Test samples: 30
Model trained successfully.
```


### 🛠️ Evaluate and Make Predictions

#### Description
Use the trained model to make predictions on the test set, then measure how well the model performed.

#### Requirements
Completed program should:

- Predict the class labels for all samples in the test set
- Calculate and print the accuracy score as a percentage (e.g. `Accuracy: 96.67%`)
- Print the full classification report using `classification_report` from `sklearn.metrics`, showing precision, recall, and F1-score for each class
- Predict and print the class name for a single new sample, e.g. `[5.1, 3.5, 1.4, 0.2]`

#### Example

```
Accuracy: 96.67%

Classification Report:
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      0.93      0.97        15
   virginica       0.83      1.00      0.91         5

Prediction for [5.1, 3.5, 1.4, 0.2]: setosa
```
