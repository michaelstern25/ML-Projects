import tkinter as tk
from tkinter import messagebox
import numpy as np
import pickle

# Load model
model, scaler = pickle.load(open("diabetes_model.pkl", "rb"))

# Function to predict
def predict():
    try:
        input_data = np.array([
            float(entry_pregnancies.get()), float(entry_glucose.get()), float(entry_bp.get()),
            float(entry_skin_thickness.get()), float(entry_insulin.get()), float(entry_bmi.get()),
            float(entry_dpf.get()), float(entry_age.get())
        ]).reshape(1, -1)

        input_data = scaler.transform(input_data)
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            messagebox.showerror("Result", "The person is likely to have diabetes.")
        else:
            messagebox.showinfo("Result", "The person is unlikely to have diabetes.")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input!")


# GUI setup
root = tk.Tk()
root.title("Diabetes Prediction")

labels = ["Pregnancies", "Glucose Level", "Blood Pressure", "Skin Thickness",
          "Insulin Level", "BMI", "Diabetes Pedigree Function", "Age"]

entries = []
for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

entry_pregnancies, entry_glucose, entry_bp, entry_skin_thickness, entry_insulin, entry_bmi, entry_dpf, entry_age = entries

tk.Button(root, text="Predict", command=predict).grid(row=len(labels), columnspan=2)

root.mainloop()