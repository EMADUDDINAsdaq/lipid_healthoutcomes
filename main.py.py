print("*********WELCOME TO CVD RISK ASSESSMENT**************")
print('')
print("The following details is used to calculate ASCVD risk factor")
global ASCVD_risk_score
import math


def compute_ten_year_score(
    isMale,
    isBlack,
    smoker,
    hypertensive,
    diabetic,
    age,
    systolicBloodPressure,
    totalCholesterol,
    hdl
):
    """
    Args:
        isMale (bool)
        isBlack (bool)
        smoker (bool)
        hypertensive (bool)
        diabetic (bool)
        age (int)
        systolicBloodPressure (int)
        totalCholesterol (int)
        hdl (int)
    """
    if age < 40 or age > 79:
        return None
    lnAge = math.log(age)
    lnTotalChol = math.log(totalCholesterol)
    lnHdl = math.log(hdl)
    trlnsbp = math.log(systolicBloodPressure) if hypertensive else 0
    ntlnsbp = 0 if hypertensive else math.log(systolicBloodPressure)
    ageTotalChol = lnAge * lnTotalChol
    ageHdl = lnAge * lnHdl
    agetSbp = lnAge * trlnsbp
    agentSbp = lnAge * ntlnsbp
    ageSmoke = lnAge if smoker else 0
    if isBlack and not isMale:
        s010Ret = 0.95334
        mnxbRet = 86.6081
        predictRet = (
            17.1141 * lnAge
            + 0.9396 * lnTotalChol
            + -18.9196 * lnHdl
            + 4.4748 * ageHdl
            + 29.2907 * trlnsbp
            + -6.4321 * agetSbp
            + 27.8197 * ntlnsbp
            + -6.0873 * agentSbp
            + (0.6908 if smoker else 0)
            + (0.8738 if diabetic else 0)
        )
    elif not isBlack and not isMale:
        s010Ret = 0.96652
        mnxbRet = -29.1817
        predictRet = (
            -29.799 * lnAge
            + 4.884 * lnAge ** 2
            + 13.54 * lnTotalChol
            + -3.114 * ageTotalChol
            + -13.578 * lnHdl
            + 3.149 * ageHdl
            + 2.019 * trlnsbp
            + 1.957 * ntlnsbp
            + (7.574 if smoker else 0)
            + -1.665 * ageSmoke
            + (0.661 if diabetic else 0)
        )
    elif isBlack and isMale:
        s010Ret = 0.89536
        mnxbRet = 19.5425
        predictRet = (
            2.469 * lnAge
            + 0.302 * lnTotalChol
            + -0.307 * lnHdl
            + 1.916 * trlnsbp
            + 1.809 * ntlnsbp
            + (0.549 if smoker else 0)
            + (0.645 if diabetic else 0)
        )
    else:
        s010Ret = 0.91436
        mnxbRet = 61.1816
        predictRet = (
            12.344 * lnAge
            + 11.853 * lnTotalChol
            + -2.664 * ageTotalChol
            + -7.99 * lnHdl
            + 1.769 * ageHdl
            + 1.797 * trlnsbp
            + 1.764 * ntlnsbp
            + (7.837 if smoker else 0)
            + -1.795 * ageSmoke
            + (0.658 if diabetic else 0)
        )

    pct = 1 - s010Ret ** math.exp(predictRet - mnxbRet)
    return round(pct * 100 * 10) / 10


isMale = input("are u male or female:(M/F)")
if isMale =="M":
    True
else:
    False
isBlack = input("race: (black/non-black)")
if isBlack == "black"or"Black"or"BLACK":
    True
else:
    False
smoker = input("Do u smoke:(Y/N)")
if smoker == "Y":
    True
else:
    False
hypertensive = input("are u constantly stressed?(Y/N): ")
if hypertensive =="Y":
    True
else:
    False
diabetic = input("do you have DIABETIES:(Y/N):")
if diabetic == "y":
    True
else:
    False
age=int(input("Enter ur age:"))
systolicBloodPressure = int(input("Enter ur BP level"))
totalCholesterol = int(input("total cholestrol:(150-240)"))
hdl = int(input("enter HDL:(20-100)"))

ASCVD=print(compute_ten_year_score(isMale,
                           isBlack,
                           smoker,
                           hypertensive,
                           diabetic,
                           age,
                           systolicBloodPressure,
                           totalCholesterol,
                           hdl, ),"%")
ASCVD_risk_score=compute_ten_year_score(isMale,
                           isBlack,
                           smoker,
                           hypertensive,
                           diabetic,
                           age,
                           systolicBloodPressure,
                           totalCholesterol,
                           hdl,)
print('')


print("The following details calculates statin intensity level")
#Statin Benefit group
def statin():
    age=int(input("enter your age:"))
    a=''
    LDC=int(input("Enter LDC colestrol level:(100-220)"))
    DIABETES=input("Do u have Diabetes:(yes/no)")
    if DIABETES == "yes":
        Diabetes=True
    else:
        Diabetes=False
    if age>=21:
        if age<=75:
            a="high-intensity statin"
        else:
            a="moderate-intensity statin"
        if LDC>=190:
            a="high-intensity statin"
        else:
            a="moderate-intensity statin"
        if (ASCVD_risk_score>7.5) and (age>40 and age<70):
            a="moderate-intensity statin"
        if Diabetes and (age>40 and age<75):
            if ASCVD_risk_score>7.5:
                a="high-intensity statin"
            else:
                a="moderate-intensity statin"
    else:
        print("invalid")
    print(a)

statin()


print("Please refer the below details for consultation")
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Ilovechess23",database="doctor")
if mycon.is_connected():
    print("successfully connected")
cursor=mycon.cursor()
cursor.execute("select * from doctor_recom")
data=cursor.fetchall()
print("(City) | (no of doctors)")
for row in data:
    print(row)
city=input("select the city u are from List--(mumbai,bangalore,chennai,delhi):-")

if city=="mumbai":
    cursor.execute("select * from doctor_mumbai")
    data=cursor.fetchall()
    print("(Doctor name) | (Work place)")
    for row in data:
        print(row)
    print("for further details please visit the website")

elif city=="chennai":
    cursor.execute("select * from doctor_chennai")
    data=cursor.fetchall()
    print("(Doctor name) | (Work place)")
    for row in data:
        print(row)
    print("for further details please visit the website")

elif city=="delhi":
    cursor.execute("select * from doctor_chennai")
    data=cursor.fetchall()
    print("(Doctor name) | (Work place)")
    for row in data:
        print(row)
    print("for further details please visit the website")

elif city=="bangalore":
    cursor.execute("select * from doctor_details")
    data=cursor.fetchall()
    print("(Doctor name) | (Work place)")
    for row in data:
        print(row)
    print("for further details please visit the website")    

print("RECOMMENDED DIET FOR THE FOLLOWING DISEASE")
def diet():
    ch=input("Choose any of the following:(Dyslipidemia/IHD/CVD)")
    if ch=="Dyslipidemia":
        print("FOODS TO AVOID")
        print("(1)Dairy products made from milk fat")
        print("(2)Coconut oil/palm oil")
        print("(3)Fried Food")
        print("(4)Sausages")
        print("(5)Bakery goods")
        print('')
        print("FOOD TO CONSUME")
        print("(1)Oranges")
        print("(2)Eggplant")
        print("(3)Fish")
        print("(4)Nuts")
        print("(5)Lentis")

    elif ch=="IHD":
        print("FOOD TO AVOID")
        print("(1)Whole milk")
        print("(2)Bacon")
        print("(3)Processed Foods")
        print("(4)Egg Yokes/Whole Eggs")
        print("(5)Organ meats")
        print('')
        print("FOOD TO CONSUME")
        print("(1)Tender cooked vegetables")
        print("(2)Whole wheat noodles")
        print("(3)cereals")
        print("(4)Fruits")
        print("(5)Tortillas")

    elif ch=="CVD":
        print("FOOD TO CONSUME")
        print("(1)Non dairy cream")
        print("(2)Pasteries")
        print("(3)Junk Food")
        print("(4)Processed Meat")
        print("(5)Gravy")
        print('')
        print("FOOD TO CONSUME")
        print("(1)Fresh Fruits and vegetables")
        print("(2)Whole Grain")
        print("(3)Healthy Fats")
        print("(4)Lean ground meat")
        print("(5)Soyabeans")

    else:
        print("Invalid choice")
        
diet()
print("THANK YOU")
print("Hopefully it was useful")
        
        

        
        
        
    
    
        






        
        
