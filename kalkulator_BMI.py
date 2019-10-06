
masa=float(input("proszę podaj swoją masę w kg"))
wzrost=float(input("proszę podaj swój wzrost w centymetrach"))
wzrost=wzrost/100
BMI=masa/((wzrost)**2)
if BMI<18.5:
    print("BMI=", BMI,"masz niedowagę")
if 18.5<=BMI<=25:
    print("BMI=", BMI,"waga prawidłowa")
else:
    print("BMI=", BMI,"żryj mniej")
