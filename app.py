#Strings are for representing characters, names, words etc.
name = "Damian"
#integer represents whole numbers
age: 14
#Floats represent decimals
wallet = 100.50
#boolean represents true or false, used in evaluations
graduated = False

def add(x,y):
    print(x + y)
#input asks the user a question and stores their response as a value
bill = float(input("what was the bill?"))
print(type(bill))
add(40, bill)

#lists
students = ["Damian", "Aiden", "Andrew", "Hi"]
#similar to saying for i in range(5): print(students[i])
""" print(students[4])
for student in students:
    print(student) """

moneys = [100, 200, 300, 400]
total = 0
for money in moneys:
    total = total + money
print(total)
