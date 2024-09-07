import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import random

# Function to assess disease risk based on patient input
def assess_risk():
    # Collect patient data from the UI fields
    age = entry_age.get()
    cholesterol = entry_cholesterol.get()
    blood_pressure_systolic = entry_blood_pressure_systolic.get()
    blood_pressure_diastolic = entry_blood_pressure_diastolic.get()
    smoking = entry_smoking.get()
    bmi = entry_bmi.get()
    waist = entry_waist.get()
    exercise = entry_exercise.get()
    family_history = entry_family_history.get()
    diet = entry_diet.get()
    sleep = entry_sleep.get()
    mental_health = entry_mental_health.get()

    try:
        # Convert inputs to the right data types
        age = int(age)
        cholesterol = int(cholesterol)
        blood_pressure_systolic = int(blood_pressure_systolic)
        blood_pressure_diastolic = int(blood_pressure_diastolic)
        smoking = int(smoking)
        bmi = float(bmi)
        waist = float(waist)
        exercise = int(exercise)
        family_history = int(family_history)
        diet = int(diet)
        sleep = int(sleep)
        mental_health = int(mental_health)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid values for all fields.")
        return

    # Expanded disease evaluation logic
    risks = []

    # Heart Disease
    if age >= 45 or cholesterol >= 240 or blood_pressure_systolic >= 140 or smoking == 1:
        risks.append("Heart Disease")

    # Diabetes
    if bmi >= 30 or waist >= 40 or family_history == 1 or age >= 45:
        risks.append("Diabetes")

    # Hypertension
    if blood_pressure_systolic >= 140 or blood_pressure_diastolic >= 90 or family_history == 1:
        risks.append("Hypertension")

    # Additional disease evaluations...
    # Add more diseases here with custom logic
    
    # Display the results in a scrollable text box
    risk_result.delete(1.0, tk.END)
    if risks:
        risk_result.insert(tk.END, f"Patient is at risk for: {', '.join(risks)}")
    else:
        risk_result.insert(tk.END, "No significant risk factors identified.")
    
# Function to generate email to the doctor
def generate_email():
    emails = [
        "Dear Doctor,\n\nI recently completed a health risk assessment. Based on the results, I would like to discuss my risks for the following conditions...\n",
        "Hello Doctor,\n\nAfter evaluating my health data, I discovered potential risks for heart disease and hypertension. I would like to schedule a follow-up...\n",
        # More variations
    ]
    email_content = random.choice(emails)
    email_textbox.delete(1.0, tk.END)
    email_textbox.insert(tk.END, email_content)

# Function to regenerate email
def regenerate_email():
    generate_email()

# Create UI with Tkinter
root = tk.Tk()
root.title("Advanced Health Risk Assessment")
root.geometry("1200x800")  # Full-screen

# Title
title_label = tk.Label(root, text="Advanced Health Risk Assessment", font=("Arial", 24))
title_label.pack(pady=10)

# Data collection fields
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Age:").grid(row=0, column=0)
entry_age = tk.Entry(frame)
entry_age.grid(row=0, column=1)

tk.Label(frame, text="Cholesterol:").grid(row=1, column=0)
entry_cholesterol = tk.Entry(frame)
entry_cholesterol.grid(row=1, column=1)

tk.Label(frame, text="Blood Pressure (Systolic):").grid(row=2, column=0)
entry_blood_pressure_systolic = tk.Entry(frame)
entry_blood_pressure_systolic.grid(row=2, column=1)

tk.Label(frame, text="Blood Pressure (Diastolic):").grid(row=3, column=0)
entry_blood_pressure_diastolic = tk.Entry(frame)
entry_blood_pressure_diastolic.grid(row=3, column=1)

tk.Label(frame, text="Smoking (1 = Yes, 0 = No):").grid(row=4, column=0)
entry_smoking = tk.Entry(frame)
entry_smoking.grid(row=4, column=1)

tk.Label(frame, text="BMI:").grid(row=5, column=0)
entry_bmi = tk.Entry(frame)
entry_bmi.grid(row=5, column=1)

tk.Label(frame, text="Waist Circumference (inches):").grid(row=6, column=0)
entry_waist = tk.Entry(frame)
entry_waist.grid(row=6, column=1)

tk.Label(frame, text="Exercise (hours per week):").grid(row=7, column=0)
entry_exercise = tk.Entry(frame)
entry_exercise.grid(row=7, column=1)

tk.Label(frame, text="Family History (1 = Yes, 0 = No):").grid(row=8, column=0)
entry_family_history = tk.Entry(frame)
entry_family_history.grid(row=8, column=1)

tk.Label(frame, text="Diet (1 = Poor, 2 = Average, 3 = Good):").grid(row=9, column=0)
entry_diet = tk.Entry(frame)
entry_diet.grid(row=9, column=1)

tk.Label(frame, text="Sleep (hours per night):").grid(row=10, column=0)
entry_sleep = tk.Entry(frame)
entry_sleep.grid(row=10, column=1)

tk.Label(frame, text="Mental Health (1 = Poor, 2 = Average, 3 = Good):").grid(row=11, column=0)
entry_mental_health = tk.Entry(frame)
entry_mental_health.grid(row=11, column=1)

# Result display
risk_result = scrolledtext.ScrolledText(root, width=80, height=10)
risk_result.pack(pady=20)

# Submit Button
submit_btn = tk.Button(root, text="Assess Risk", command=assess_risk)
submit_btn.pack(pady=10)

# Email generation
email_textbox = scrolledtext.ScrolledText(root, width=80, height=10)
email_textbox.pack(pady=20)

generate_email_btn = tk.Button(root, text="Generate Email to Doctor", command=generate_email)
generate_email_btn.pack(pady=5)

regenerate_email_btn = tk.Button(root, text="Regenerate Email", command=regenerate_email)
regenerate_email_btn.pack(pady=5)

root.mainloop()
