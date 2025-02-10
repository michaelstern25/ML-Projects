import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import pickle

from jupyterlab.extensions import entry
from webencodings import LABELS

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
root = Tk()
root.title("Diabetes Prediction")
root.geometry("500x600")
root.config(bg="aqua")

custom_font = ("Arial",12,"bold")

# Title Label
lab = Label(root, text="Diabetes Prediction App", font=("Time New Roman",25,"bold"),bg="aqua", fg="brown")
lab.place(x=60,y=40, height=50,width=380)

# Pregnancies label and entry field
tk.Label(root, text="Pregnancies : ", font=custom_font, bg="aqua").place(x=70, y=130)
entry_pregnancies = Entry(root, font=custom_font, bg="white")
entry_pregnancies.place(x=210, y=130, width=200)

# Glucose level label and entry field
tk.Label(root, text="Glucose Level : ", font=custom_font, bg="aqua").place(x=70, y=170)
entry_glucose = Entry(root, font=custom_font, bg="white")
entry_glucose.place(x=210, y=170, width=200)

# Blood Pressure label and entry field
tk.Label(root, text="Blood Pressure : ", font=custom_font, bg="aqua").place(x=70, y=210)
entry_bp = Entry(root, font=custom_font, bg="white")
entry_bp.place(x=210, y=210, width=200)

# Skin Thickness label and entry field
tk.Label(root, text="Skin Thickness : ", font=custom_font, bg="aqua").place(x=70, y=250)
entry_skin_thickness = Entry(root, font=custom_font, bg="white")
entry_skin_thickness.place(x=210, y=250, width=200)

# Insulin Level label and entry field
tk.Label(root, text="Insulin Level : ", font=custom_font, bg="aqua").place(x=70, y=290)
entry_insulin = Entry(root, font=custom_font, bg="white")
entry_insulin.place(x=210, y=290, width=200)

# BMI label and entry field
tk.Label(root, text="BMI : ", font=custom_font, bg="aqua").place(x=70, y=330)
entry_bmi = Entry(root, font=custom_font, bg="white")
entry_bmi.place(x=210, y=330, width=200)

# Diabetes Pedigree Function label and entry field
tk.Label(root, text="DPF : ", font=custom_font, bg="aqua").place(x=70, y=370)
entry_dpf = Entry(root, font=custom_font, bg="white")
entry_dpf.place(x=210, y=370, width=200)

# Age label and entry field
tk.Label(root, text="Age : ", font=custom_font, bg="aqua").place(x=70, y=410)
entry_age = Entry(root, font=custom_font, bg="white")
entry_age.place(x=210, y=410, width=200)


# Button
button = Button(root, text="Predict", font=("Time New Roman",15,"bold"), relief=RAISED,bg="light blue",command=predict)
button.place(x=170,y=470, height=40,width=150)

root.mainloop()