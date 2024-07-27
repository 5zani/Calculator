print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child ticket is $5.")
  elif age <= 18:
    bill = 7
    print("Youth ticket is $7. ")
  elif age >= 45 and age <=55:
    print("Everything is going to be ok. Have a free ride on us! ")
  else:
    bill = 12
    print("Adult ticket is $12. ")
  want_photo = input("Do you want to take a photo? Y or N. ")
  if want_photo == "Y":
    bill += 3
  print(f"Your final bill is ${bill}. ")
else:
  print("Sorry, you have to grow taller before you can ride")