name = input("Enter your name : ")
weight = float(input('Enter the weight :'))
height = float(input('Enter the height :'))
BMI = weight/(height* height)
print(BMI)
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