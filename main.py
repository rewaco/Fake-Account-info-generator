import random
import time

print("""
Fake Account info generator project
female: 1
male: 2
""")

male_names = ["mike", "jessie", "walter", "Kelvin", "Albert", "Harvey", "Owen", "Lucas", "Gregor", "Honour", "Benjamin",
              "Steve", "Michael", "David", "alexander", "edward", "niamh", ]
female_names = ["Astrid", "Alice", "Alessi", "Addison", "Abbey", "Paige", "Tammy", "Tina", "Tasha", "Serenity", "Quinn",
                "Kathy", "Kaylee", "Lole", "Mila", "Germaine", "Faith", "Emma", "Daphe", "Cara", ]
mails = ["gmail","hotmail","Yandex","Yahoo","Outlook","iCloud","Mail","Inbox","MyWayMail"]
fake_gmail = "{}{}{}@{}.com"
random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 14]
random_mails = random.choice(mails)
ramdom_new = random.choice(random_numbers)

random_male = random.choice(male_names)

random_2female = random.choice(female_names)



select = input("please select gender")
select = int(select)
if select == 1:
    randomPerson = random_2female
elif select == 2:
    randomPerson = random_male
else:
    print("wrong choice")

character = "abcdefghklmnopqrstuvwxyzABCGHKLMNOPQRSTUVWXYZ1234567890!#$&"
password_length = int(input("How many characters should the password be? : "))
password_count = int(input("How many passwords : "))
for x in range(0, password_count):
    password = ""
    for x in range(0, password_length):
        password_char = random.choice(character)
        password = password + password_char

print("Generating information please wait")
a = 3
while (a > 0):
    print (a)
    time.sleep(1)
    a -= 1

print("Name",randomPerson)

print("Your random mail",fake_gmail.format(randomPerson,ramdom_new,ramdom_new,random_mails))

print("Your randomly generated Password : ", password)