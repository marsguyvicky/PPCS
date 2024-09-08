import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

# Example datasets and training models (using synthetic data)
def create_sample_data():
    # Example data for heart disease
    heart_disease_data = {
        'age': np.random.randint(20, 80, 100),
        'blood_pressure': np.random.randint(80, 180, 100),
        'diabetes': np.random.randint(0, 2, 100),
        'heart_disease': np.random.randint(0, 2, 100)
    }
    df_heart_disease = pd.DataFrame(heart_disease_data)
    
    # Example data for chronic kidney disease
    kidney_disease_data = {
        'age': np.random.randint(20, 80, 100),
        'blood_pressure': np.random.randint(80, 180, 100),
        'diabetes': np.random.randint(0, 2, 100),
        'kidney_disease': np.random.randint(0, 2, 100)
    }
    df_kidney_disease = pd.DataFrame(kidney_disease_data)
    
    return df_heart_disease, df_kidney_disease

def train_models():
    df_heart_disease, df_kidney_disease = create_sample_data()
    
    # Prepare data for heart disease model
    X_heart = df_heart_disease[['age', 'blood_pressure', 'diabetes']]
    y_heart = df_heart_disease['heart_disease']
    X_train_heart, X_test_heart, y_train_heart, y_test_heart = train_test_split(X_heart, y_heart, test_size=0.2, random_state=42)
    
    # Train heart disease model
    heart_disease_model = make_pipeline(StandardScaler(), LogisticRegression())
    heart_disease_model.fit(X_train_heart, y_train_heart)
    
    # Prepare data for chronic kidney disease model
    X_kidney = df_kidney_disease[['age', 'blood_pressure', 'diabetes']]
    y_kidney = df_kidney_disease['kidney_disease']
    X_train_kidney, X_test_kidney, y_train_kidney, y_test_kidney = train_test_split(X_kidney, y_kidney, test_size=0.2, random_state=42)
    
    # Train chronic kidney disease model
    kidney_disease_model = make_pipeline(StandardScaler(), RandomForestClassifier())
    kidney_disease_model.fit(X_train_kidney, y_train_kidney)
    
    return heart_disease_model, kidney_disease_model

heart_disease_model, kidney_disease_model = train_models()

def assess_risk():
    # Get values from the input fields
    features = {
        'age': int(entry_age.get()),
        'blood_pressure': float(entry_blood_pressure.get()),
        'diabetes': 1 if entry_diabetes.get().lower() == "yes" else 0,
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame([features])
    
    # Predict using the models
    heart_disease_prediction = heart_disease_model.predict(input_df)[0]
    kidney_disease_prediction = kidney_disease_model.predict(input_df)[0]
    
    # Display results in table
    risk = {
        "Heart Disease": heart_disease_prediction,
        "Chronic Kidney Disease": kidney_disease_prediction,
    }
    
    results_tree.delete(*results_tree.get_children())  # Clear previous results
    
    for disease, at_risk in risk.items():
        risk_level = f"Risk Level {at_risk}"
        results_tree.insert("", tk.END, values=(disease, risk_level))

    # Update risk bars
    heart_risk_bar['value'] = heart_disease_prediction * 100  # Assuming prediction is between 0 and 1
    kidney_risk_bar['value'] = kidney_disease_prediction * 100  # Assuming prediction is between 0 and 1

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

# UI Design Code
root = tk.Tk()
root.title("Predictive Patient Care System")
root.configure(bg="white")
root.geometry("900x600")

# Define styles
style = ttk.Style()
style.configure('TButton', background='red', foreground='white')
style.configure('TButton.Hidden', background='lightgray', foreground='gray')

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
tk.Label(frame_left, text="Patient Name:", bg="white", fg="black", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_left)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame_left, text="Age:", bg="white", fg="black", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
entry_age = tk.Entry(frame_left)
entry_age.grid(row=1, column=1, pady=5)

tk.Label(frame_left, text="Blood Pressure (mmHg):", bg="white", fg="black", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
entry_blood_pressure = tk.Entry(frame_left)
entry_blood_pressure.grid(row=2, column=1, pady=5)

tk.Label(frame_left, text="Diabetes Mellitus (Yes/No):", bg="white", fg="black", font=("Arial", 12)).grid(row=3, column=0, sticky="w")
entry_diabetes = tk.Entry(frame_left)
entry_diabetes.grid(row=3, column=1, pady=5)

# Assess Risk Button
assess_button = ttk.Button(frame_left, text="Assess Risk", command=assess_risk)
assess_button.grid(row=4, column=0, columnspan=2, pady=10)

# Results Table (Right Side)
results_tree = ttk.Treeview(frame_right, columns=("Disease", "Risk"), show="headings")
results_tree.heading("Disease", text="Disease")
results_tree.heading("Risk", text="Risk Level")
results_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Email Box and Generate Email Button
email_box = scrolledtext.ScrolledText(frame_right, height=10, bg="white", font=("Arial", 12))
email_box.pack(fill=tk.BOTH, padx=20, pady=10)

generate_email_button = ttk.Button(frame_right, text="Generate Email", command=generate_email)
generate_email_button.pack(pady=5)

# Bottom Risk Bars
tk.Label(frame_bottom, text="Heart Disease Risk:", bg="white", fg="black", font=("Arial", 12)).pack(side=tk.LEFT, padx=20)
heart_risk_bar = ttk.Progressbar(frame_bottom, length=200, mode='determinate')
heart_risk_bar.pack(side=tk.LEFT, padx=10)

tk.Label(frame_bottom, text="Chronic Kidney Disease Risk:", bg="white", fg="black", font=("Arial", 12)).pack(side=tk.LEFT, padx=20)
kidney_risk_bar = ttk.Progressbar(frame_bottom, length=200, mode='determinate')
kidney_risk_bar.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()
