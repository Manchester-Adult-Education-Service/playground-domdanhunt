#PythonExperiment
# I would like to create a program asking for your date of birth, it then generating it in the format dd/mm/yyyy.
#I would also like it to then use the current date to calculate how old you are in days, weeks, months, years. 
while True:
    try:
        dob = int(input("What day of the month were you born? i.e: 8 fof 8th: "))
    except ValueError:
        print("Please enter your day of birth, for instance 8 for the 8th of the month")

print(f"You were born on the {dob}th of the month")
while True:
    try:
        mob = int(input("And what month of the year? i.e: 6 for June: "))
    except ValueError:
        print("Please enter your month of birth, for instance 6 for June")
        
while True:
    try:
        yob = int(input("And what year were you born? i.e: 1992: "))
    except ValueError:
        print("Please enter your year of birth in a yyyy format, for instance 1992: ")
dateofbirth = (f"{dob}/{mob}+{yob}")
print(f"{dateofbirth}")
