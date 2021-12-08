s='*'
e=' '
print(s*76)
print(s,e*30,'WELCOME TO',e*30,s)
print(s,e*20,'Online Healthcare Information System ',e*13,s)
print(s,e*72,s)
print(s*76)

def weight_analysis():
    print(age)
    if age<1:
        print("Consult your doctor")
    elif 1<=age<=3:
        if weight<10:
            print("Baby is underweight")
            print("SUGGESTION : Drinking of milk can help in gaining weight")
        elif 10<=weight<=13:
            print("BABY is healthy")
            print("SUGGESTION :  Keep it up")
        elif weight>=14:
            print("Baby is overweight")
            print("SUGGESTION : consult your doctor")
    elif 4<=age<=6:
        if weight<=16:
            print("child is underweight")
            print("SUGGESTION : Drinking of milk can help in gaining weight")
        elif 17<=weight<=19:
            print("child is healthy")
            print("SUGGESTION :  Keep it up")
        elif weight>=20:
            print("child is overweight")
            print("SUGGESTION 1 : Avoid eating chocolate and cakes")
            print("SUGGESTION 2 : Child should play outdoor games")

    elif 7 <= age <= 10:
        if weight <=17:
            print("child is underweight")
            print("SUGGESTION : Drinking of milk can help in gaining weight")
        elif 17 < weight <= 24:
            print("child is healthy")
            print("SUGGESTION :  Keep it up")
        elif weight > 24:
            print("child is overweighted")
            print("SUGGESTION 1: Avoid eating chocolate and cakes")
            print("SUGGESTION 2 : Child should play outdoor games")

    elif 11 <= age <=13:
        if weight < 28:
            print("child is underweight")
            print("SUGGESTION : Drinking of milk can help in gaining weight")
            print(" 2 : Eat Avocadoes")
            print(" 3 : Eat banana")
        elif 28 <= weight <=35:
            print("weight is balanced")
            print("SUGGESTION :  Keep it up")
        elif weight > 35:
            print("child is overweighted")
            print("SUGGESTION 1: Avoid eating chocolate and cakes")
            print("SUGGESTION 2 : Child should play outdoor games")

    elif 13 < age <= 15:
        if weight < 40:
            print("child is underweight")
            print("SUGGESTION : Drinking of milk can help in gaining weight")
            print(" 2 : Eat Avocadoes")
            print(" 3 : Eat banana")
        elif 40 <= weight <= 50:
            print("weight is balanced")
            print("SUGGESTION :  Keep it up")
        elif weight > 50:
            print("child is overweighted")
            print("SUGGESTION 1: Avoid eating chocolate and cakes")
            print("SUGGESTION 2 : Child should play outdoor games")

    elif 15 < age <= 17:
        if weight < 45:
            print("child is underweight")
            print("SUGGESTION : Drinking of milk can help in gaining weight")
            print(" 2 : Eat Avocadoes")
            print(" 3 : Eat banana")
        elif 45 <= weight <= 60:
            print("weight is balanced")
            print("SUGGESTION :  Keep it up")
        elif weight > 60:
            print("child is overweighted")
            print("SUGGESTION 1: Avoid eating chocolate and cakes")
            print("SUGGESTION 2 : Child should play outdoor games")
            print(" 3 : Do exercises daily")
            print(" 4 : Drink water before meals.\n 5 : Eat soluble fiber.")

    elif 17 < age <= 20:
        if weight < 50:
            print("You are  underweight")
            print("SUGGESTION 1 : Drinking of milk can help in gaining weight")
            print(" 2 : Eat Avocadoes")
            print(" 3 : Eat banana")
        elif 61 <= weight <= 68:
            print("weight is balanced")
            print("SUGGESTION :  Keep it up")
        elif weight > 68:
            print("You are overweighted")
            print("SUGGESTION 1: Avoid eating chocolate and cakes")
            print(" 2 : You should play outdoor games")
            print(" 3 : Do exercises daily")
            print(" 4 : Drink water before meals.\n 5 : Eat soluble fiber.")

    elif 20 < age <= 25:
        if weight < 60:
            print("You are  underweight")
            print("SUGGESTION 1 : Drinking of milk can help in gaining weight")
            print(" 2 : Eat Avocadoes")
            print(" 3 : Eat banana")
        elif 68 <= weight <= 78:
            print("weight is balanced")
            print("SUGGESTION :  Keep it up")
        elif weight > 78:
            print("You are overweighted")
            print("SUGGESTION 1: Avoid eating chocolate and cakes")
            print(" 2 : You should play outdoor games")
            print(" 3 : Do exercises daily")
            print(" 4 : Drink water before meals.\n 5 : Eat soluble fiber.")

    elif age>25:
        if weight < 70:
            print("You are  underweight")
            print("SUGGESTION 1 : Drinking of milk can help in gaining weight")
            print(" 2 : Eat Avocadoes")
            print(" 3 : Eat banana")
        elif 70 <= weight <= 85:
            print("weight is balanced")
            print("SUGGESTION :  Keep it up")
        elif weight > 85:
            print("You are overweighted")
            print("SUGGESTION 1: Avoid eating chocolate and cakes")
            print(" 2 : You should play outdoor games")
            print(" 3 : Do exercises daily")
            print(" 4 : Drink water before meals.\n 5 : Eat soluble fiber.")


def RBC_analysis():
    if 6<age<12:
        if rbc<4:
            print("RBC is low")
        elif rbc>4:
            print("RBC count is normal")
    elif age>11:
        if rbc<4.5:
            print("RBC is low")
        else:
            print("RBC count is normal")


def WBC_analysis():
    if wbc<4500:
        print("WBC count low")
    else:
        print("WBC is normal")


def Platelets_analysis():
    if plt<150000:
        print("your platelets are are down")
        print("Suggestions : \nEat papaya")
        print("Drink goat milk")
    else:
        print("your platelets are normal")


def BP_analysis():
    if bp<90:
        print("your blood pressure is low")
        print("Suggestions : \ntake Energy drinks")
    elif bp>120:
        print("Your blood pressure is high")
        print("Suggestions : \nEat Cashew nuts")
        print("Eat  Berries")
        print("Eat Bananas")
    else:
        print("Your blood pressure is normal")


def Sugar_level_analysis():
    if sug<54:
        print("You Blood sugar level is low")
        print("Suggestions : \nEat Pistachios")
        print("Eat Apples")
    elif sug>140:
        print("your Blood sugar level is high")
        print("Suggestions : \nEat Apples")
        print("Eat Pears")
        print("Eat Swiss Chards")
        print("Eat Pistachios")
    else:
        print("Your Blood sugar level is normal")


def Hemoglobin_analysis():
    if hmg<12.5:
        print("Your hemoglobin is low")
        print("Suggestions : \nEat Almonds")
        print("Eat pomegranates, watermelons, apples, apricots")
    else:
        print("Your hemoglobin is normal")


k='y'
while k=='y':
    name = input("Enter name of patient : ")
    age = float(input("Enter age of patient : "))
    address = input("Enter address of patient : ")
    weight = float(input("Enter weight of patient : "))
    if age < 14:
        a2 = weight_analysis()
        print()
        k=input("If you want to check health of another person the press y else n")
        print()
    else:
        bp = float(input("Enter blood pressue of patient : "))
        hmg = float(input("Enter Haemoglobin of patient : "))
        wbc = float(input("Enter WBC count of patient : "))
        rbc = float(input("Enter RBC (in million) count of patient : "))
        plt = float(input("Enter platelet count of patient : "))
        sug = float(input("Enter sugar level of patient : "))
        print("\n1 : Result of weight:\n")
        a2 = weight_analysis()
        print("\n2 : Result of RBC:\n")
        a3 = RBC_analysis()
        print("\n3 : Result of WBC:\n")
        a4 = WBC_analysis()
        print("\n4 : Result of Platelets:\n")
        a5 = Platelets_analysis()
        print("\n5 : Result of Blood pressure:\n")
        a6 = BP_analysis()
        print("\n6 : Result of Sugar level:\n")
        a7 = Sugar_level_analysis()
        print("\n7 : Result of  Hemoglobin:\n")
        a8 = Hemoglobin_analysis()
        k = input("\nIf you want to check health of another person the press y else n")



















