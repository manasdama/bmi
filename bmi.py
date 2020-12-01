import pandas as pd
def BMI(height, weight): 
	bmi = weight/(height**2) 
	return bmi 


height = float(input("enter your height in meter:"))

weight = int(input("enter your weight in kg:"))


bmi = BMI(height, weight) 
print("The BMI is", format(bmi), "so ", end='') 


if (bmi <= 18.4):
        data=[bmi,"18.4 and below","Malnutrition risk"]
        df = pd.DataFrame(data,columns=['BMI Category','BMI Range (kg/m2)','Health risk'])
        print(df)
        print("underweight health is Malnutrition risk") 

elif ( bmi >= 18.5 and bmi < 24.9): 
	print("Normal weight Health is low risk") 

elif ( bmi >= 24.9 and bmi < 30): 
	print("overweight Health is Enhanced risk") 

elif ( bmi >= 30 and bmi < 35): 
	print("Moderately obese and health is Medium risk")

elif ( bmi >= 35 and bmi < 40): 
	print("Severely obese and health is High risk")


elif ( bmi >= 40 ): 
	print("Very severely obese and health is very High risk")


"""import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df"""



	
