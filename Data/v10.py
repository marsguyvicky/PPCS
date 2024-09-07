import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Load and prepare datasets
def prepare_data():
    # Load Pima Indians Diabetes Dataset
    pima_data = pd.read_csv('Data/diabetes.csv')
    
    # Prepare Pima dataset
    pima_data = pima_data.dropna()
    features_pima = pima_data.drop('Outcome', axis=1)  # Assuming 'Outcome' is the target variable
    target_pima = pima_data['Outcome']
    
    # Normalize data
    scaler = StandardScaler()
    features_scaled_pima = scaler.fit_transform(features_pima)
    
    return features_scaled_pima, target_pima, scaler

# Train models
def train_models():
    features_scaled_pima, target_pima, scaler = prepare_data()
    
    # Split the Pima data
    X_train, X_test, y_train, y_test = train_test_split(features_scaled_pima, target_pima, test_size=0.2, random_state=42)
    
    # Train a model (e.g., Logistic Regression)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Predict and evaluate
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))
    
    return model, scaler

# Initialize models and scaler
model, scaler = train_models()

# Function to assess disease risk based on patient input
def assess_risk():
    try:
        # Get values from the input fields
        age = int(entry_age.get())
        cholesterol = float(entry_cholesterol.get())
        blood_pressure_sys = float(entry_blood_pressure_sys.get())
        blood_pressure_dia = float(entry_blood_pressure_dia.get())
        bmi = float(entry_bmi.get())
        waist_circumference = float(entry_waist.get())
        exercise_level = int(entry_exercise.get())
        smoking = 1 if entry_smoking.get().lower() == "yes" else 0
        family_history = 1 if entry_family_history.get().lower() == "yes" else 0
        diet = 1 if entry_diet.get().lower() == "poor" else 0

        # Prepare input for the model
        input_data = np.array([[age, cholesterol, blood_pressure_sys, blood_pressure_dia, bmi, waist_circumference, exercise_level, smoking, family_history, diet]])
        input_data_scaled = scaler.transform(input_data)

        # Predict risk
        risk_prediction = model.predict(input_data_scaled)[0]

        # Display results in table
        results_tree.delete(*results_tree.get_children())  # Clear previous results
        disease = "Diabetes"  # Assuming you want to predict diabetes
        risk_level = "High Risk" if risk_prediction == 1 else "No Risk"
        results_tree.insert("", tk.END, values=(disease, risk_level), tags=('red' if risk_prediction == 1 else 'green',))

        # Update risk bars (example for diabetes only)
        diabetes_risk_bar['value'] = 75 if risk_prediction == 1 else 25
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid values.")

# Function to generate an email for the doctor
def generate_email():
    patient_name = entry_name.get()
    email_content = f"Dear Doctor,\n\nI have conducted a health risk assessment for {patient_name}. Here are the results:\n"
    
    # Loop through the disease results
    for child in results_tree.get_children():
        disease, status = results_tree.item(child, 'values')
        email_content += f"- {disease}: {status}\n"

    email_content += "\nPlease advise on the next steps for diagnosis and treatment."
    
    email_box.delete(1.0, tk.END)
    email_box.insert(tk.END, email_content)

# Function to regenerate a new email
def regenerate_email():
    generate_email()

# UI Design Code
root = tk.Tk()
root.title("Predictive Patient Care System")
root.configure(bg="white")
root.geometry("900x600")

# Left side survey
frame_left = tk.Frame(root, bg="white", padx=20, pady=20)
frame_left.pack(side=tk.LEFT, fill=tk.Y)

# Right side results
frame_right = tk.Frame(root, bg="white", padx=20, pady=20)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Bottom risk bars
frame_bottom = tk.Frame(root, bg="white", padx=20, pady=10)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)

# Input Labels and Fields (Survey Area)
tk.Label(frame_left, text="Patient Name:", bg="white", fg="red", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_left)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame_left, text="Age:", bg="white", fg="red", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
entry_age = tk.Entry(frame_left)
entry_age.grid(row=1, column=1, pady=5)

tk.Label(frame_left, text="Cholesterol (mg/dL):", bg="white", fg="red", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
entry_cholesterol = tk.Entry(frame_left)
entry_cholesterol.grid(row=2, column=1, pady=5)

tk.Label(frame_left, text="Blood Pressure (Sys):", bg="white", fg="red", font=("Arial", 12)).grid(row=3, column=0, sticky="w")
entry_blood_pressure_sys = tk.Entry(frame_left)
entry_blood_pressure_sys.grid(row=3, column=1, pady=5)

tk.Label(frame_left, text="Blood Pressure (Dia):", bg="white", fg="red", font=("Arial", 12)).grid(row=4, column=0, sticky="w")
entry_blood_pressure_dia = tk.Entry(frame_left)
entry_blood_pressure_dia.grid(row=4, column=1, pady=5)

tk.Label(frame_left, text="BMI:", bg="white", fg="red", font=("Arial", 12)).grid(row=5, column=0, sticky="w")
entry_bmi = tk.Entry(frame_left)
entry_bmi.grid(row=5, column=1, pady=5)

tk.Label(frame_left, text="Waist Circumference (cm):", bg="white", fg="red", font=("Arial", 12)).grid(row=6, column=0, sticky="w")
entry_waist = tk.Entry(frame_left)
entry_waist.grid(row=6, column=1, pady=5)

tk.Label(frame_left, text="Exercise Level (0-10):", bg="white", fg="red", font=("Arial", 12)).grid(row=7, column=0, sticky="w")
entry_exercise = tk.Entry(frame_left)
entry_exercise.grid(row=7, column=1, pady=5)

tk.Label(frame_left, text="Do you smoke? (Yes/No):", bg="white", fg="red", font=("Arial", 12)).grid(row=8, column=0, sticky="w")
entry_smoking = tk.Entry(frame_left)
entry_smoking.grid(row=8, column=1, pady=5)

tk.Label(frame_left, text="Family History of Diseases? (Yes/No):", bg="white", fg="red", font=("Arial", 12)).grid(row=9, column=0, sticky="w")
entry_family_history = tk.Entry(frame_left)
entry_family_history.grid(row=9, column=1, pady=5)

tk.Label(frame_left, text="Diet Quality (Good/Poor):", bg="white", fg="red", font=("Arial", 12)).grid(row=10, column=0, sticky="w")
entry_diet = tk.Entry(frame_left)
entry_diet.grid(row=10, column=1, pady=5)

# Assess Risk Button
assess_button = tk.Button(frame_left, text="Assess Risk", bg="red", fg="white", font=("Arial", 12), command=assess_risk)
assess_button.grid(row=11, column=0, columnspan=2, pady=10)

# Results Table (Right Side)
results_tree = ttk.Treeview(frame_right, columns=("Disease", "Risk"), show="headings")
results_tree.heading("Disease", text="Disease")
results_tree.heading
