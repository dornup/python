try:
    g = open("23-02.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Файлик не найден, покусик!")
    quit()
content = g.readlines()
g.close()

for i, student in enumerate(content):
    content[i] = student.split()

maxi = -1
for student in content:
    try:
        if int(student[3]) > maxi:
            maxi = int(student[3])
    except ValueError:
        print("неверно указаны баллы", student)
    except IndexError:
        print("баллы отсутствуют", student)

if maxi == -1:
    print("записи об участниках не найдены")
else:
    print("максимальный балл: ", maxi)
    
devyatiy = 0
colvo_9 = 0
desyatiy = 0
colvo_10 = 0
odinnatsatiy = 0
colvo_11 = 0

for student in content:
    try:
        if student[2] == "9":
            devyatiy += int(student[3])
    except ValueError:
        print("неверно указаны баллы", student)
    except IndexError:
        print("баллы отсутствуют", student)
    else:
        if student[2] == "9":
            colvo_9 += 1
            
    try:
        if student[2] == "10":
            desyatiy += int(student[3])
    except ValueError:
        print("неверно указаны баллы", student)
    except IndexError:
        print("баллы отсутствуют", student)
    else:
        if student[2] == "10":
            colvo_10 += 1
            
    try:
       if student[2] == "11":
            odinnatsatiy += int(student[3])
    except ValueError:
        print("неверно указаны баллы", student)
    except IndexError:
            print("баллы отсутствуют", student)
    else:
        if student[2] == "11":
            colvo_11 += 1

print(f"среднее арифметическое в\n9 классе: {devyatiy/colvo_9}\n"
      f"10 классе: {desyatiy/colvo_10}\n"
      f"11 классе: {odinnatsatiy/colvo_11}")
        
