numbers = []
while True:
    vvod = input(">>>>")
    if vvod.lstrip("-").lstrip(" ").isdigit():
        if vvod not in numbers:
            numbers.append(vvod)
            print(numbers)
            print("НЕТ")
        else:
            print("ДА")
    elif vvod == "end":
        break
    else:
        print("я питаюсь чиселками(")
    
        
