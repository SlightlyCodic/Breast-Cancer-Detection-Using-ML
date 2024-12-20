import tkinter as tk
from tkinter import ttk
import pandas as pd
import pickle
from tkinter import messagebox
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# LOAD THE DATASET
from sklearn.datasets import load_breast_cancer
data_set_1 = load_breast_cancer()

# CREATE DATAFRAME
data_frame_cancer = pd.DataFrame(
    data_set_1.data,
    columns=data_set_1.feature_names
)
data_frame_cancer['target'] = data_set_1.target

# Splitting data into input and output variables
x = data_frame_cancer.drop(['target'], axis=1)
y = data_frame_cancer['target']

# Splitting the dataset into train and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.19, random_state=10)

# Scaling the features
sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)

# SVC classifier
svc_classifier = SVC()
svc_classifier.fit(x_train_scaled, y_train)

# Load the trained model
model = pickle.dumps(svc_classifier)
svc_pickle = pickle.loads(model)

def predict_cancer():
    data_input = []
    for feature in feature_names:
        try:
            value = float(entries[feature].get())
            data_input.append(value)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input value ")
            return

    input_df = pd.DataFrame([data_input], columns=feature_names)
    scaled_input = sc.transform(input_df)
    output = svc_pickle.predict(scaled_input)[0]

    if output == 0:
        result = 'The case is malignant'
    else:
        result = 'The case is benign'
    messagebox.showinfo("Prediction", result)

def clear_entries():
    for entry in entries.values():
        entry.delete(0, tk.END)

root = tk.Tk()
root.title('Breast Cancer Detection')
root.geometry('900x700')
root.configure(bg='pink')

style = ttk.Style()
style.configure('TLabel', font=('Arial', 14), foreground='black')
style.configure('TButton', font=('Arial', 14))

# Styling for the Predict button
style.configure('Predict.TButton', foreground='black', background='white')

# Styling for the Clear button
style.configure('Clear.TButton', foreground='black', background='white')

feature_names = data_set_1.feature_names
entries = {}

num_cols = 2
for i, feature in enumerate(feature_names):
    row = i // num_cols
    col = i % num_cols
    ttk.Label(root, text=feature).grid(row=row, column=col*4, pady=5, padx=10, sticky="e")
    entry = ttk.Entry(root)
    entry.grid(row=row, column=col*4+1, pady=5, padx=10)
    entries[feature] = entry

predict_button = ttk.Button(root, text="Predict", command=predict_cancer, style='Predict.TButton')
predict_button.grid(row=row+1, column=3, pady=20)

clear_button = ttk.Button(root, text="Clear", command=clear_entries, style='Clear.TButton')
clear_button.grid(row=row+1, column=4, pady=40)

root.mainloop()