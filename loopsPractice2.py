# listOfNumbers = range(1,101)
# print(listOfNumbers)
# #for loop - number is gonna be the following number
# for number in listOfNumbers:
#     # print(number)
#     if number % 2 == 0:
#         #type conversion - a number is an inter but str for it to make it work
#         print(str(number) + "is even")
#     else:
#         print(str(number) + "is odd")

#create a list of numbers from 1 to 10000
numberlist = range(1,10001)
#print out the sum of all numbers in the list
total = 0
for number in numberlist:
    if number % 2 == 0:
        sumOfList = total + number
        print(sumOfList)
else:
    print("This numbeer is not")
#if the number is even. add it to the sum

