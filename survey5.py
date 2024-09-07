import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
import random

# Define risk levels and advice
RISK_LEVELS = {
    "Very Low": {"color": "#98FB98", "message": "No immediate action needed."},
    "Low": {"color": "#00FF7F", "message": "Maintain a healthy lifestyle."},
    "Moderate": {"color": "#FFD700", "message": "Consult a healthcare provider."},
    "High": {"color": "#FF8C00", "message": "Seek medical advice soon."},
    "Critical": {"color": "#FF0000", "message": "Immediate medical attention required."}
}

ADVICE = {
    "Heart Disease": {
        "Very Low": "Maintain a healthy lifestyle.",
        "Low": "Monitor your diet and exercise regularly.",
        "Moderate": "Consult a cardiologist.",
        "High": "Seek medical tests as soon as possible.",
        "Critical": "Immediate medical attention required."
    },
    "Diabetes": {
        "Very Low": "Keep your diet balanced and stay active.",
        "Low": "Monitor blood sugar regularly.",
        "Moderate": "Consult an endocrinologist for further evaluation.",
        "High": "Follow medical advice for treatment.",
        "Critical": "Immediate intervention required."
    },
    # Add more diseases and advice here...
}

# Function to determine risk level
def determine_risk(score):
    if score < 20:
        return "Very Low"
    elif 20 <= score < 40:
        return "Low"
    elif 40 <= score < 60:
        return "Moderate"
    elif 60 <= score < 80:
        return "High"
    else:
        return "Critical"

# Function to predict time until disease
def predict_time(risk_level):
    if risk_level == "Very Low":
        return "N/A"
    elif risk_level == "Low":
        return "10+ years"
    elif risk_level == "Moderate":
        return "5-10 years"
    elif risk_level == "High":
        return "1-5 years"
    elif risk_level == "Critical":
        return "Immediate"

# Function to generate a unique email every time
def generate_email(name, disease_risk):
    return f"Dear Doctor,\n\nI am {name}, and I recently conducted a health assessment. Based on my results, I might be at risk for the following conditions:\n{disease_risk}\n\nI would like to schedule an appointment for further evaluation.\n\nBest regards,\n{name}"

# Function to assess the risk
def assess_risk():
    # Clear previous results
    for item in results_tree.get_children():
        results_tree.delete(item)

    try:
        age = int(entry_age.get())
        cholesterol = int(entry_cholesterol.get())
        bp_systolic = int(entry_bp_systolic.get())
        bp_diastolic = int(entry_bp_diastolic.get())
        smoking = smoking_var.get()
        bmi = float(entry_bmi.get())
        waist = float(entry_waist.get())
        exercise = int(entry_exercise.get())
        
        # Calculate some risk score (example)
        score = (cholesterol + bp_systolic + smoking + (age / 2)) / 10
        risk_level = determine_risk(score)

        # Predict time until risk
        time_until_disease = predict_time(risk_level)

        # Add data to results table
        diseases = ["Heart Disease", "Diabetes", "Stroke", "Hypertension", "Obesity"]  # Add more diseases here
        for disease in diseases:
            disease_risk = determine_risk(random.randint(10, 90))  # Simulating random risk assessment
            color = RISK_LEVELS[disease_risk]["color"]
            results_tree.insert("", "end", values=(disease, disease_risk, time_until_disease), tags=(color,))

        # Generate email
        email = generate_email(entry_name.get(), ", ".join(diseases))
        messagebox.showinfo("Generated Email", email)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid inputs!")

# Function to regenerate email with new content
def regenerate_email():
    name = entry_name.get()
    diseases = ["Heart Disease", "Diabetes", "Stroke", "Hypertension", "Obesity"]  # Add more diseases here
    email = generate_email(name, ", ".join(diseases))
    messagebox.showinfo("Generated Email", email)

# UI setup
root = tk.Tk()
root.title("Predictive Patient Care System")
root.geometry("1200x800")
root.config(bg="#fff0f0")

# Header
header_frame = tk.Frame(root, bg="white")
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Predictive Patient Care", font=("Helvetica", 24, "bold"), bg="#ff4d4d", fg="white")
header_label.pack(pady=10)

# Input fields
input_frame = tk.Frame(root, bg="white")
input_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

# Form labels and fields
tk.Label(input_frame, text="Name:", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
entry_name = tk.Entry(input_frame, font=("Helvetica", 14))
entry_name.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Age:", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
entry_age = tk.Entry(input_frame, font=("Helvetica", 14))
entry_age.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Cholesterol:", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
entry_cholesterol = tk.Entry(input_frame, font=("Helvetica", 14))
entry_cholesterol.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Blood Pressure (Systolic):", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
entry_bp_systolic = tk.Entry(input_frame, font=("Helvetica", 14))
entry_bp_systolic.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Blood Pressure (Diastolic):", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
entry_bp_diastolic = tk.Entry(input_frame, font=("Helvetica", 14))
entry_bp_diastolic.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Smoking (Yes=1, No=0):", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
smoking_var = tk.IntVar()
tk.Radiobutton(input_frame, text="Yes", variable=smoking_var, value=1, bg="white").pack(anchor=tk.W)
tk.Radiobutton(input_frame, text="No", variable=smoking_var, value=0, bg="white").pack(anchor=tk.W)

tk.Label(input_frame, text="BMI:", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
entry_bmi = tk.Entry(input_frame, font=("Helvetica", 14))
entry_bmi.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Waist Circumference:", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
entry_waist = tk.Entry(input_frame, font=("Helvetica", 14))
entry_waist.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Exercise (hours per week):", font=("Helvetica", 14), bg="white").pack(anchor=tk.W)
entry_exercise = tk.Entry(input_frame, font=("Helvetica", 14))
entry_exercise.pack(fill=tk.X, pady=5)

# Submit Button
submit_button = tk.Button(input_frame, text="Submit", command=assess_risk, bg="#ff4d4d", fg="white", font=("Helvetica", 14))
submit_button.pack(pady=20)

# Results frame
results_frame = tk.Frame(root, bg="white")
results_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH)

results_label = tk.Label(results_frame, text="Results", font=("Helvetica", 18, "bold"), bg="#ff4d4d", fg="white")
results_label.pack(anchor=tk.W)

# Treeview for results
columns = ("Disease", "Risk Level", "Time Until Risk")
results_tree = ttk.Treeview(results_frame, columns=columns, show="headings")
for col in columns:
    results_tree.heading(col, text=col)
results_tree.pack(fill=tk.BOTH, expand=True)

# Tags for color-coding the risk levels
for level, data in RISK_LEVELS.items():
    results_tree.tag_configure(level, background=data["color"])

# Regenerate email button
regenerate_button = tk.Button(root, text="Regenerate Email", command=regenerate_email, bg="#ff4d4d", fg="white", font=("Helvetica", 14))
regenerate_button.pack(pady=20)

root.mainloop()
