# Breast Cancer Detection Application

Welcome to the **Breast Cancer Detection Application** project! This project implements a machine learning-based tool to predict breast cancer cases as malignant or benign using Support Vector Classifier (SVC). The application provides a user-friendly graphical interface built with Tkinter.

---

## Features
- **Breast Cancer Prediction**: Predicts if a case is malignant or benign based on user inputs.
- **Machine Learning Model**: Utilizes an SVM (Support Vector Machine) classifier trained on the Breast Cancer dataset.
- **Data Preprocessing**: Includes data scaling for improved model performance.
- **Interactive GUI**: Easy-to-use interface built with Tkinter for entering input data and viewing predictions.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Technologies Used](#technologies-used)
4. [Dataset](#dataset)
5. [Model Details](#model-details)
6. [Contributing](#contributing)
7. [License](#license)

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/breast-cancer-detection.git
    cd breast-cancer-detection
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

---

## Usage

1. Launch the application by running the provided Python script.
2. Enter the feature values in the input fields based on the dataset attributes.
3. Click on the **Predict** button to get the result (malignant or benign).
4. Use the **Clear** button to reset all input fields.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - pandas
  - numpy
  - scikit-learn
  - tkinter
  - pickle

---

## Dataset
- The application uses the **Breast Cancer Wisconsin Dataset** from `sklearn.datasets`.
- The dataset contains 30 numeric features and a target variable indicating malignancy (0: malignant, 1: benign).

---

## Model Details
- The model is a **Support Vector Classifier (SVC)**.
- Preprocessing includes:
  - Splitting data into training and test sets.
  - Scaling features using `StandardScaler` for better performance.
- Model evaluation:
  - Accuracy Score
  - Confusion Matrix
  - Classification Report

---

## Acknowledgements
- The Breast Cancer Wisconsin Dataset: [scikit-learn Datasets](https://scikit-learn.org/stable/datasets.html)
- Open-source libraries and contributors.

---

Feel free to explore, contribute, and build on this project to make predictions more accessible and effective!
