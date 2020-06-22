#Calculator

Firstnumber = input("Enter First Number: ")
Secondnumber = input("Enter Second Number: ")
menu_option = int(input("Enter option: "))

#print("Menu")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

Answer1 = float(Firstnumber) 
Answer2 = int(Secondnumber)

if menu_option == 1:
    print(Answer1 + Answer2)
elif menu_option == 2:
    print(Answer1 - Answer2)
elif menu_option == 3:
    print(Answer1 * Answer2)
elif menu_option == 4:
    print(Answer1 / Answer2)
#else:
    #print("Error: invalid option")

