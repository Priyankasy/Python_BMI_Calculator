import tkinter as tk

def calculate_BMI():
    #Get the User's input names
    #name = str (name_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    #Calculate the BMI 
    BMI =  weight / (height * height)

    #Display the BMI 
    result_label.config(text=f"BMI: {BMI:.2f}")

#Create  the GUI window 
window = tk.Tk()
window.title("BMI Calculator")

#Create the input fields and labels
name_label = tk.Label(text="Name : ")

weight_label=tk.Label(text="Weight (kg): ")
weight_label.pack()
weight_entry =tk.Entry()
weight_entry.pack()

height_label=tk.Label(text="Height (m): ")
height_label.pack()
height_entry=tk.Entry()
height_entry.pack()

#Create the button to calculate the BMI
calculate_button = tk.Button(text="Calculate BMI", command = calculate_BMI)
calculate_button.pack()

#Create the label to display the result 
result_label = tk.Label(text="")
result_label.pack()

#Run the GUI Window
window.mainloop()



#name = input("Enter your name : ")
#weight = int(input('Enter the weight :'))
#height = int(input('Enter the height :'))
##BMI = weight/(height* height)
"""print(BMI)
if BMI >0:
    if(BMI<18.5):
        print(name+", You are under weight")
    elif(BMI<24.9):
        print(name+", You are normal weight")
    elif(BMI<29.9):
        print(name+", You are over weight. You need to exercise more and stop sitting and writing so many pythin tutorials")
    elif(BMI<34.9):
        print(name+", You are obese")
    elif(BMI<39.9):
        print(name+", You are severely obese")   
    else:
        print(name+", You are morbidly obese")
else:
    print("Enter a valid inputs")
    """