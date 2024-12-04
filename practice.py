# task 3
name1=input('enter ur name :')
email=input('enter mail_id :')
ph_number=input('enter ph no :')
print (name1,email,ph_number)email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if not re.match(email_pattern, email):
    print("Invalid email address. Please enter a valid email.")
else:
    print(name1, email, ph_number)
# task 2 height
height = float(input('enter height :'))
height_inches="{:.2f}".format(height/2.54)
# .2f is for taking 2 numbers in decimal
print (height_inches)
print("hi")5
# add number
num1 = 3
num2 = 4
print(num1+num2)
print(8+2)
# Check if a Numbe bnr is Even or Odd

num =int(input("enter a number:"))
print(num+4)

#reverse
a = input("enter string :")
b = a[::-1]
print(f"Reversed string is: {b}")
# formatted string literal.

# task 1
name ='Anand'
days ='15'
year=2024
print(f"dear {name} \n u have {str(days)+'1'} days of leave \n year({year})")

