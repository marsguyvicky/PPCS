import tkinter as tk
from tkinter import messagebox, scrolledtext

# Function to assess disease risk based on patient input
def assess_risk():
    # Collect patient data from the UI fields
    age = entry_age.get()
    cholesterol = entry_cholesterol.get()
    blood_pressure = entry_blood_pressure.get()
    smoking = entry_smoking.get()
    bmi = entry_bmi.get()
    exercise = entry_exercise.get()
    family_history = entry_family_history.get()
    
    try:
        # Convert inputs to the right data types
        age = int(age)
        cholesterol = int(cholesterol)
        blood_pressure = int(blood_pressure)
        smoking = int(smoking)
        bmi = float(bmi)
        exercise = int(exercise)
        family_history = int(family_history)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid values for all fields.")
        return

    # Risk assessment logic
    risks = []

    # Heart Disease
    if age >= 45 or cholesterol >= 240 or blood_pressure >= 140 or smoking == 1:
        risks.append("Heart Disease")

    # Diabetes
    if bmi >= 30 or family_history == 1 or age >= 45:
        risks.append("Diabetes")

    # Hypertension
    if blood_pressure >= 140 or age >= 40 or family_history == 1:
        risks.append("Hypertension")

    # Chronic Obstructive Pulmonary Disease (COPD)
    if smoking == 1 or family_history == 1:
        risks.append("COPD")

    # Stroke
    if blood_pressure >= 140 or smoking == 1 or cholesterol >= 240:
        risks.append("Stroke")

    # Display the results in a scrollable text box
    risk_result.delete(1.0, tk.END)
    if risks:
        risk_result.insert(tk.END, f"Patient is at risk for: {', '.join(risks)}")
    else:
        risk_result.insert(tk.END, "No significant risk factors identified.")
    
# Function to generate email to the doctor
def generate_email():
    patient_info = f"Patient Data:\nAge: {entry_age.get()}\nCholesterol: {entry_cholesterol.get()}\nBlood Pressure: {entry_blood_pressure.get()}\nSmoking: {entry_smoking.get()}\nBMI: {entry_bmi.get()}\nExercise Level: {entry_exercise.get()}\nFamily History of Disease: {entry_family_history.get()}\n\n"
    risk_info = risk_result.get(1.0, tk.END).strip()

    # Email template
    email_text = f"Dear Doctor,\n\nI recently completed a self-assessment of my health risk factors. Here is my information:\n\n{patient_info}Based on my self-assessment, here are the potential health risks identified:\n\n{risk_info}\n\nI would like to schedule an appointment to discuss these results and get a proper diagnosis.\n\nBest regards,\n[Your Name]"
    
    # Display the email in a new window
    email_window = tk.Toplevel(root)
    email_window.title("Generated Email")
    email_textbox = scrolledtext.ScrolledText(email_window, width=60, height=20)
    email_textbox.insert(tk.END, email_text)
    email_textbox.pack()

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Comprehensive Disease Risk Assessment")
root.geometry("500x600")

# Title Label
label_title = tk.Label(root, text="Patient Health Risk Assessment", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Age Label and Entry
label_age = tk.Label(root, text="Age")
label_age.pack()
entry_age = tk.Entry(root)
entry_age.pack()

# Cholesterol Label and Entry
label_cholesterol = tk.Label(root, text="Cholesterol (mg/dL)")
label_cholesterol.pack()
entry_cholesterol = tk.Entry(root)
entry_cholesterol.pack()

# Blood Pressure Label and Entry
label_blood_pressure = tk.Label(root, text="Blood Pressure (mm Hg)")
label_blood_pressure.pack()
entry_blood_pressure = tk.Entry(root)
entry_blood_pressure.pack()

# Smoking Status Label and Entry
label_smoking = tk.Label(root, text="Smoking (0 for No, 1 for Yes)")
label_smoking.pack()
entry_smoking = tk.Entry(root)
entry_smoking.pack()

# BMI Label and Entry
label_bmi = tk.Label(root, text="Body Mass Index (BMI)")
label_bmi.pack()
entry_bmi = tk.Entry(root)
entry_bmi.pack()

# Exercise Frequency Label and Entry
label_exercise = tk.Label(root, text="Exercise Frequency (days per week)")
label_exercise.pack()
entry_exercise = tk.Entry(root)
entry_exercise.pack()

# Family History Label and Entry
label_family_history = tk.Label(root, text="Family History of Disease (0 for No, 1 for Yes)")
label_family_history.pack()
entry_family_history = tk.Entry(root)
entry_family_history.pack()

# Submit Button
button_submit = tk.Button(root, text="Assess Risk", command=assess_risk)
button_submit.pack(pady=10)

# Textbox for displaying the assessment result
risk_result = scrolledtext.ScrolledText(root, height=5, width=50)
risk_result.pack(pady=10)

# Email Button
button_email = tk.Button(root, text="Generate Email for Doctor", command=generate_email)
button_email.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
