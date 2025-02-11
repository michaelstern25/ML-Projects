from tkinter import *
from tkinter import messagebox
import tkinter as tk
import numpy as np
import pickle
from PIL import ImageTk, Image

# Load model
dt, sc = pickle.load(open("weather_model.pkl", "rb"))

# Function to predict weather type
def predict_weather():
    try:
        # Prepare the input for prediction
        input_data = np.array([[float(precip_entry.get()), float(temp_max_entry.get()),
                                float(temp_min_entry.get()), float(wind_entry.get())
                                ]])
                                # [precipitation, temp_max, temp_min, wind]
        # Transform the input data using the same scaler used in training
        input_data = sc.transform(input_data)
        # Predict the weather type
        prediction = dt.predict(input_data)

        # Show the prediction result on the GUI
        if prediction[0] == 0:
            result_label.config(text="Predicted Weather: Drizzle")
        elif prediction[0] == 1:
            result_label.config(text="Predicted Weather: Fog")
        elif prediction[0] == 2:
            result_label.config(text="Predicted Weather: Rain")
        elif prediction[0] == 3:
            result_label.config(text="Predicted Weather: Snow")
        elif prediction[0] == 4:
            result_label.config(text="Predicted Weather: Sun Rise")
        else:
            result_label.config(text="Invalid Input")
    except ValueError:
        result_label.config(text="Please enter valid numerical values.")


# Create the main Tkinter window
app = Tk()
app.geometry("500x600")
app.title("Weather Prediction App")
app.config(bg="light blue")
# img = Image.open("weather.jpg")
# resized_img = img.resize((20,30))
# img = ImageTk.PhotoImage(resized_img)
# img_label = Label(app,  image=img)
# img_label.pack()

# Title Label
# font = Courier,Helvetica, Times New Roman, Verdana, Georgia, Comic Sans MS, Tahoma, Impact
lab = Label(app, text="Weather Prediction", font=("Comic Sans MS",25,"bold"), fg="black", bg="light blue")
lab.place(x=60,y=20, height=50,width=380)

# Labels and entry widgets for user input
tk.Label(app, text="Precipitation (mm)",font=("Helvetica",15), fg="black", bg="light blue").place(x=160, y=100)
precip_entry = tk.Entry(app,font=("Helvetica",15,"bold"), fg="black", justify="center",bg="aqua")
precip_entry.place(x=170, y=140, width=150, height=30)

tk.Label(app, text="Max Temperature (°C)",font=("Helvetica",15), fg="black", bg="light blue").place(x=140, y=190)
temp_max_entry = tk.Entry(app,font=("Helvetica",15,"bold"), fg="black", justify="center",bg="aqua")
temp_max_entry.place(x=170, y=230, width=150, height=30)

tk.Label(app, text="Min Temperature (°C)",font=("Helvetica",15), fg="black", bg="light blue").place(x=140, y=280)
temp_min_entry = tk.Entry(app,font=("Helvetica",15,"bold"), fg="black", justify="center",bg="aqua")
temp_min_entry.place(x=170, y=320, width=150, height=30)

tk.Label(app, text="Wind Speed (km/h)",font=("Helvetica",15), fg="black",bg="light blue").place(x=160, y=370)
wind_entry = tk.Entry(app,font=("Helvetica",15,"bold"), fg="black", justify="center",bg="aqua")
wind_entry.place(x=170, y=410, width=150, height=30)

# Button
button = Button(app, text="Check Weather", font=("Comic Sans MS",20,"bold"), relief=RAISED,bg="aqua",fg="black",command=predict_weather)
button.place(x=130,y=480, height=35,width=220)

# Label to show the result
result_label = tk.Label(app, text="Predicted Weather: ", font=("Arial", 12, "bold"), bg="light blue")
result_label.place(x=100,y=540, height=35,width=300)

# Run the Tkinter main loop
app.mainloop()

