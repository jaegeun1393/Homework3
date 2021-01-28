# Open the shell
# Type “python jaegeun_oh_hw1.py”
# Enter a positive number only if not it will print out “Number is below 0.”

year = int(input("Input-"))

if year > 0:
  if year % 400 == 0:
    print('Output-', year ,'is a leap year')
  elif year % 4 == 0 and year % 100 != 0:
    print('Output-', year ,'is a leap year')
  else:
    print("It is not a leap year")
else:
  print("Number is below 0")
