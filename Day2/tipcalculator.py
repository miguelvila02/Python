print("Welcome to the tip calculator:")
bill_price = int((input("Bill price:")))
number_of_people = int(input("Number of people:"))
tip_value = int(input("What percentage was the tip 10%,12%, or 15%?? "))

a = ((bill_price / number_of_people)* 0.1)

b = ((bill_price / number_of_people)* 0.12)

c = ((bill_price / number_of_people)* 0.15)

if tip_value == 10 : 
    print("The price per person is " + str(a))
elif tip_value ==  12 : 
    print("The price per person is " + str(b))
elif tip_value == 15 : 
    print("The price per person is " + str(c))
else : 
    print("The price per person is " + str(((bill_price / number_of_people)* (tip_value / 100))))