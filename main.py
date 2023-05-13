from tkinter.filedialog import askopenfile
from tkinter import *
import AttPred

def clearall():
    for widgets in window.winfo_children():
        widgets.place(x=-100, y=-100)

def uploadFile():
    clearall()
    global file_path
    file_path = askopenfile(mode='r', filetypes=[('CSV Files', '*csv')])
    predictor.train_data(file_path.name)
    predict()

def predict():
    # predictor.train_data(file_path)
    Label(window, text="Enter the name of student :",
          font=('arial', 10, 'bold',)).place(x=20, y=50)
    nameField.place(x=250, y=50)
    predictBtn = Button(window, text="Predict", bg='light yellow',
                        width=20, command=predictAttendance).place(x=250, y=100)
    
def predictAttendance():
    result = predictor.predict(name=str(nameField.get()))

    if (result is not None):
        outputData = "\tName of Student\t\t\t\tPredicted Attendance\n\n" + \
            result[0] + "\t\t\t\t" + str(result[1])

        outputField.config(text=outputData)
        outputField.place(x=20, y=200)
    else:
        outputField.config(text="Enter the Name in the proper format")
        outputField.place(x=200, y=200)

    backButton = Button(window, text="Exit", bg='light yellow',
                        width=20, command=destroy).place(x=250, y=300)


def destroy():
    window.destroy()

# =========Main Program============#

predictor = AttPred.attPred()

window = Tk()
window.title("Attendance Predictor")

# Initialization of global variables
file_path = ""
nameField = Entry(window, width=50)
outputField = Label(window, font=('arial', 10, 'bold',))

window_height, window_width = 500, 650
screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width,
                window_height, x_cordinate, y_cordinate))

# Upload Button
uploadBtn = Button(window, text="Upload CSV File",
                   bg='light yellow', width=20, command=uploadFile).place(x=250, y=200)

window.mainloop()
