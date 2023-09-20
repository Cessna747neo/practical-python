name = input("What is your name")
current_year = int(input("What year is it?"))
current_age = int(input("What is your age?"))
wondering_age = (input("What age do you want to know about?"))
result = current_year + wondering_age - current_age

print(name + ", you will be " + wondering_age + "in" + result + "years")