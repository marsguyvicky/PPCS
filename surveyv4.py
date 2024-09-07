import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
import random

# Function to assess disease risk based on patient input
def assess_risk():
    # Get values from the input fields
    age = int(entry_age.get())
    cholesterol = float(entry_cholesterol.get())
    blood_pressure_sys = float(entry_blood_pressure_sys.get())
    blood_pressure_dia = float(entry_blood_pressure_dia.get())
    bmi = float(entry_bmi.get())
    waist_circumference = float(entry_waist.get())
    exercise_level = int(entry_exercise.get())
    smoking = entry_smoking.get()
    family_history = entry_family_history.get()
    diet = entry_diet.get()

    # Simple logic for disease risk (replace with a real model)
    risk = {
        "Heart Disease": (age > 50 or cholesterol > 200 or smoking == "Yes"),
        "Diabetes": (bmi > 30 or family_history == "Yes"),
        "Hypertension": (blood_pressure_sys > 140 or blood_pressure_dia > 90),
        "Stroke": (age > 55 and family_history == "Yes"),
        "Obesity": (bmi > 30),
        "Kidney Disease": (blood_pressure_sys > 160 or family_history == "Yes"),
        "Liver Disease": (diet == "Poor"),
        "Arthritis": (age > 60 or smoking == "Yes"),
        "Cancer": (family_history == "Yes"),
        "Asthma": (smoking == "Yes" or family_history == "Yes"),
        "COPD": (smoking == "Yes"),
        "Osteoporosis": (age > 65),
        "Depression": (exercise_level == 0),
        "Chronic Fatigue": (exercise_level == 0 and diet == "Poor"),
        "Sleep Apnea": (bmi > 35)
    }

    # Display results in table
    for disease, at_risk in risk.items():
        if at_risk:
            results_tree.insert("", tk.END, values=(disease, "High Risk"), tags=('red',))
        else:
            results_tree.insert("", tk.END, values=(disease, "No Risk"), tags=('green',))

    # Update risk bars
    heart_risk_bar['value'] = 80 if risk["Heart Disease"] else 20
    diabetes_risk_bar['value'] = 75 if risk["Diabetes"] else 25

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
results_tree.heading("Risk", text="Risk Level")
results_tree.tag_configure('red', background='red')
results_tree.tag_configure('green', background='green')
results_tree.tag_configure('orange', background='orange')
results_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Email Box and Generate Email Button
email_box = scrolledtext.ScrolledText(frame_right, height=10, bg="white", font=("Arial", 12))
email_box.pack(fill=tk.BOTH, padx=20, pady=10)

generate_email_button = tk.Button(frame_right, text="Generate Email", bg="red", fg="white", font=("Arial", 12), command=generate_email)
generate_email_button.pack(pady=5)

regenerate_email_button = tk.Button(frame_right, text="Regenerate Email", bg="red", fg="white", font=("Arial", 12), command=regenerate_email)
regenerate_email_button.pack(pady=5)

# Bottom Risk Bars
tk.Label(frame_bottom, text="Heart Disease Risk:", bg="white", fg="red", font=("Arial", 12)).pack(side=tk.LEFT, padx=20)
heart_risk_bar = ttk.Progressbar(frame_bottom, length=200, mode='determinate')
heart_risk_bar.pack(side=tk.LEFT, padx=10)

tk.Label(frame_bottom, text="Diabetes Risk:", bg="white", fg="red", font=("Arial", 12)).pack(side=tk.LEFT, padx=20)
diabetes_risk_bar = ttk.Progressbar(frame_bottom, length=200, mode='determinate')
diabetes_risk_bar.pack(side=tk.LEFT, padx=10)

root.mainloop()
