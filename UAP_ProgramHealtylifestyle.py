import os
os.system('cls')
from termcolor import colored, cprint
import time
from datetime import datetime
from playsound import playsound
print("Welcome to HealthyLifestyle")
time.sleep(1)
print("Make your future better")
time.sleep(3)
os.system('cls')
print("\nTo continue the program, we need your data")
time.sleep(3)
os.system('cls')

#Dictionary untuk menyimpan data pengguna
user_data = {
    'gender': None,
    'weight': None,
    'height': None,
    'age': None,
    'activity_level': None
}   

#Input Data Diri
user_data['gender'] = input("Input your gender (men/women) : ").lower()
while user_data['gender'] not in ['men', 'women']:
    print("Your input is invalid. Please input only the words 'men' or 'women'")
    user_data['gender'] = input("Input your gender (men/women) : ").lower()

user_data['weight'] = float(input("Input your weight (kg)        : "))
while user_data['weight'] <= 0:
    print("Your input is invalid. Please input a positive number")
    user_data['weight'] = float(input("Input your weight (kg)        : "))

user_data['height'] = float(input("Input your height (cm)        : "))
while user_data['height'] <= 0:
    print("Your input is invalid. Please input a positive number")
    user_data['height'] = float(input("Input your height (cm)        : "))

user_data['age'] = float(input("Input your age (year)         : "))
while user_data['age'] <= 0:
    print("Your input is invalid. Please input a positive number")
    user_data['age'] = float(input("Input your age (year)        : "))

user_data['activity_level'] = input("Input your activity level (sedentary/mild/moderate/active/very active): ").lower()
while user_data['activity_level'] not in ['sedentary', 'mild', 'moderate', 'active', 'very active']:
    print("Your input is invalid. Please input as requested")
    user_data['activity_level'] = input("Input your activity level (sedentary/mild/moderate/active/very active): ").lower()
    
time.sleep(2)
os.system('cls')
print("\nProcessing data...\n")
time.sleep(2)
os.system('cls')

#Rumus hitung BMI (Body Mass Index) dengan memakai data yang ada di dictionary user_data
bmi = user_data['weight'] / (user_data['height'] / 100) ** 2

#Rumus hitung BMR (Basal Metabolic Rate/kebutuhan kalori) dengan memakai data yang ada di dictionary user_data
if user_data['gender'] == 'men':
    bmr = 66.5 + (13.7 * user_data['weight']) + (5 * user_data['height']) - (6.8 * user_data['age'])
else:
    bmr = 65.5 + (9.6 * user_data['weight']) + (1.8 * user_data['height']) - (4.7 * user_data['age'])

#Rumus menghitung kalori dan Dictionary untuk menyimpan activity level user
activity_multipliers = {
    'sedentary': 1.2,
    'mild': 1.375,
    'moderate': 1.55,
    'active': 1.725,
    'very active': 1.9
}
cal = bmr * activity_multipliers[user_data['activity_level']]

#Fungsi untuk membaca menu diet dari file teks
def read_diet_menu(filename):
    with open(filename, 'r') as file:
        return file.readlines()

#Menentukan file yang akan dibaca berdasarkan BMI Calculation
def get_diet_menu_filename(bmi):
    if bmi < 18.5:
        return 'MenuUnder.txt'
    elif 18.5 <= bmi <= 24.9:
        return 'MenuNormal.txt'
    elif 25 <= bmi <= 29.9:
        return 'MenuOver.txt'
    elif 30 <= bmi <= 34.9:
        return 'MenuObesity1.txt'
    elif 35 <= bmi <= 39.9:
        return 'MenuObesity2.txt'
    else:
        return 'MenuObesity3.txt'

#Array untuk food suggestions
food_suggestions_under_1800 = [
    "Breakfast : Green smoothies.\n"
    "Lunch     : Chicken salad with quinoa.\n"
    "Dinner    : Stir-fry tofu with broccoli.\n"
    "Snack     : Low fat yogurt with granola."
]
food_suggestions_1800_to_2200 = [
    "Breakfast : Oatmeal with fruit and nuts.\n"
    "Lunch     : Wrap vegetables with hummus.\n"
    "Dinner    : Grilled salmon with asparagus.\n"
    "Snack     : Fruit smoothies."
]
food_suggestions_above_2200 = [
    "Breakfast : Scrambled eggs with vegetables.\n"
    "Lunch     : Lentil and vegetable soup.\n"
    "Dinner    : Grilled chicken with roasted sweet potatoes.\n"
    "Snack     : Fresh vegetables with yogurt sauce."
]

#Menentukan array yang akan digunakan berdasarkan kalori
def get_food_suggestions(cal):
    if cal <= 1800:
        return food_suggestions_under_1800
    elif 1800 < cal <= 2200:
        return food_suggestions_1800_to_2200
    else:
        return food_suggestions_above_2200

#Fungsi menentukan berapa kebutuhan air harian
def calculate_water_intake(gender, weight, activity_level):
    base_water_intake = weight * 0.033  # base intake in liters (33 ml per kg)
    if activity_level == 'sedentary':
        return base_water_intake
    elif activity_level == 'mild':
        return base_water_intake + 0.2
    elif activity_level == 'moderate':
        return base_water_intake + 0.4
    elif activity_level == 'active':
        return base_water_intake + 0.6
    elif activity_level == 'very active':
        return base_water_intake + 0.8

# Array 2D untuk jenis olahraga sesuai BMI
exercise_recommendations = [
    ["Underweight", "swimming", "zumba", "weight lifting", "sit-ups", "push ups"],
    ["Normal weight", "Swimming", "Cycling", "Yoga", "Jogging", "Swimming", "Skipping", "Aerobics"],
    ["Overweight", "Going up and down stairs", "swimming", "gymnastics", "walking", "water aerobics", "strength training"],
    ["Obese I", "Tai Chi", "Strength training", "Cycling, Swimming or walking in water", "Walking"],
    ["Obese II", "Water Aerobics", "Interval Training", "Jogging", "Stationary Bike", "Walking"],
    ["Obese III", "Personal training", "Kickboxing", "Walking", "Running"]
]

#Fungsi validasi waktu alarm
def validate_time(alarm_time):
    try:
        time.strptime(alarm_time, '%I:%M:%S %p') #Penjelasannya ada di https://www-geeksforgeeks-org.translate.goog/python-datetime-strptime-function/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc
        return "ok"
    except ValueError:
        return "\nYour input is invalid. Please input the time settings according to the format\n"

#Fungsi untuk mengatur alarm
def set_alarm(alarm_times):
    for alarm_time in alarm_times:
        print(f"Setting alarm for {alarm_time}")
        print()
        alarm_hour = int(alarm_time[0:2])
        alarm_minute = int(alarm_time[3:5])
        alarm_second = int(alarm_time[6:8])
        alarm_period = alarm_time[9:11].upper()
        
        if alarm_period == 'PM' and alarm_hour != 12:
            alarm_hour += 12
        elif alarm_period == 'AM' and alarm_hour == 12:
            alarm_hour = 0

        alarm_time_formatted = datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=alarm_second, microsecond=0)
        time_diff_seconds = (alarm_time_formatted - datetime.now()).total_seconds()
        
        if time_diff_seconds < 0:
            print("\nAlarm time is in the past. Please set a future time.\n")
            continue
        time.sleep(time_diff_seconds)
        print("\n!!  IT'S THE TIME  !!\n")
        playsound('C:\Raisatun.py\positive_energy.mp3') 

#Program Utama
while True :
    print("\nMain Course : ")
    time.sleep(0.5)
    print()
    print("1. BMI (Body Mass Index) Calculation")
    time.sleep(0.2)
    print("2. Healthy Diet Menu")
    time.sleep(0.2)
    print("3. Recommended Daily Calorie Intake")
    time.sleep(0.2)
    print("4. Healthy Food Suggestions")
    time.sleep(0.2)
    print("5. Sport Recommendation")
    time.sleep(0.2)
    print("6. Water Drinking Alarm")
    time.sleep(0.2)
    print("7. Rest Alarm")
    time.sleep(1)
    c = int(input("\nWhat do you want to know? Type in Your Choice (1-7) : "))
    while c not in [1,2,3,4,5,6,7] :
        print("Your input is invalid. Please enter numbers in the interval 1 to 7 only")
        c = int(input("\nWhat do you want to know? Type in Your Choice (1-7) : "))
    os.system('cls')
    time.sleep(0.5)
    print("Please wait...")
    time.sleep(2)
    os.system('cls')

    #Program 1 : BMI Calculation
    if c == 1 : 
        def hbmi(gender, bmi, bb, tb): 
            if bmi < 18.5 :
                cprint("\nYou are underweight", 'light_red', 'on_yellow')
            elif 18.5 <= bmi <= 24.9 : 
                cprint("You are ideal", 'blue', 'on_light_blue')
            elif 25 <= bmi <= 29.9 :
                cprint("You are overweight", 'light_red', 'on_light_magenta')
            elif 30 <= bmi <= 34.9 :
                cprint("You are level 1 obese", 'black', 'on_light_red')
            elif 35 <= bmi <= 39.9 :
                cprint("You are level 2 obese", 'black', 'on_light_red')
            else :
                cprint("You are level 3 obese", 'black', 'on_light_red')
                
            #mencari berat badan seharusnya
            if gender == 'men' :
                bbs = (tb-100) - ((tb-100)*(10/100))
                if bb == bbs :
                    print("\nYou have the ideal body weight")
                else :
                    print('\nYour weight should be : ', bbs, 'kg')
            else :
                bbs = (tb-100) - ((tb-100)*(15/100))
                if bb == bbs :
                    print("\nYou have the ideal body weight")
                else :
                    print('\nYour weight should be : ', bbs, 'kg')
        print("Your BMI Calculation : ", bmi)
        print()
        hbmi(user_data['gender'], bmi, user_data['weight'], user_data['height'])

    #Program 2 : Healthy Diet Menu Based on BMI
    elif c == 2:
        print("This is your personalized healthy diet menu based on your BMI")
        print()
        diet_menu_file = get_diet_menu_filename(bmi)
        diet_menu = read_diet_menu(diet_menu_file)
        for item in diet_menu:
            print(item.strip())

    #Program 3 : Calorie needs
    elif c == 3 :
        print("You need ",cal," kcal of calories for today") 

    #Program 4 : Healthy Food Suggestion Based on Calorie needs
    elif c == 4 :
        print("This is your personalized healthy food suggestions based on your calorie needs")
        print()
        food_suggestions = get_food_suggestions(cal)
        for item in food_suggestions:
            print(item)

    #Program 5 : Sport Suggestion
    elif c == 5:
        def print_exercise_recommendations(bmi_category):
            if 0 <= bmi_category < len(exercise_recommendations):
                print(f"\nRecommended Exercises for {exercise_recommendations[bmi_category][0]} : ")
                print()
                for i in range(1, len(exercise_recommendations[bmi_category])):
                    print(exercise_recommendations[bmi_category][i])
            else:
                print("Invalid BMI category.")

        bmi_category = 0
        if 18.5 <= bmi <= 24.9:
            bmi_category = 1
        elif 25 <= bmi <= 29.9:
            bmi_category = 2
        elif 30 <= bmi <= 34.9:
            bmi_category = 3
        elif 35 <= bmi <= 39.9:
            bmi_category = 4
        elif bmi >= 40:
            bmi_category = 5

        print_exercise_recommendations(bmi_category)

    #Program 6 dan 7 : Water Drinking and Rest Alarm
    elif c == 6 or c == 7:
        def alarm_program(alarm_type):
            alarm_count = int(input("Input how many alarms you want to set: "))
            print()
            alarm_times = []
            for _ in range(alarm_count):
                alarm_time = input("Input the alarm time (format HH:MM:SS AM/PM): ")
                while validate_time(alarm_time) != "ok":
                    print("Invalid time format! Please try again...")
                    alarm_time = input("Input the alarm time (format HH:MM:SS AM/PM): ")
                alarm_times.append(alarm_time)
            print(f"{alarm_type} alarm set successfully!")
            set_alarm(alarm_times)
            
        if c == 6:
            water_intake = calculate_water_intake(user_data['gender'], user_data['weight'], user_data['activity_level'])
            print(f"Based on your activity level, you should drink approximately {water_intake:.2f} liters of water per day.\n")
            time.sleep(3)
            alarm_program("Water drinking")
            
        elif c == 7:
            alarm_program("Rest")

    print()
    opsi = str(input("Do you want to try other menus in this program? (y/n) : ")).lower()
    while opsi != 'y' and opsi != 'n' :
        print("\nYour input is invalid. Please input only the letters 'y' or 'n'")
        opsi = str(input("Do you want to try other menus in this program? (y/n) : ")).lower()
    if opsi == 'n' :
        os.system('cls')
        print("\n^-^ Thank you for using this program ^-^\n") 
        break
    elif opsi == 'y' :
        True
        os.system('cls')
        print("Please Wait...")
        time.sleep(2)
        os.system('cls')