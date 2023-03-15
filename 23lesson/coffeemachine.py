voda = 500
cofe = 500
moloko = 500
dengi = 0

class Coffee:
    def __init__(self, water, coffee, milk, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        
def resurses(water, coffee, milk):
    global voda 
    global cofe 
    global moloko
    if voda >= water and cofe >= coffee and moloko >= milk:
        voda -= water
        cofe -= coffee
        moloko -= milk
        print(voda, cofe, moloko)
        return True
    else:
        return False

def galya(water, coffee, milk):
    global voda 
    global cofe 
    global moloko
    voda += water
    cofe += coffee
    moloko += milk
    
    
capuchino = Coffee(200, 100, 100, 100)
espresso = Coffee(50, 20, 0, 50)
latte = Coffee(225, 50, 125, 120)

while True:
    while True:
        command = input("Выбери одно из: латте/эспрессо/капучино: ").lower()
        if command == "отчет":
            print(f"Вода:{voda} мл\nКофе:{cofe} г\nМолоко:{moloko} мл\nДеньги:{dengi} руб")
        elif command == "капучино":
            if resurses(capuchino.water, capuchino.coffee, capuchino.milk) == True:
                oplata = input(f"С вас {capuchino.money} рублей: ")
                while True:
                    if oplata == "отмена":
                        galya(capuchino.water, capuchino.coffee, capuchino.milk)
                        break
                    oplatai = int(oplata)
                    if oplatai == capuchino.money:
                        dengi += oplatai
                        print("Оплата прошла успешно, вот ваш кофе ☕")
                        break
                    elif oplatai < capuchino.money:
                        ostatok = input(f"С вас еще {capuchino.money - oplatai} "
                                            "рублей или отмена:")
                        if ostatok == "отмена":
                            galya(capuchino.water, capuchino.coffee, capuchino.milk)
                            break
                        ostatoki = int(ostatok)
                        if ostatoki == capuchino.money - oplatai:
                            dengi += oplatai + ostatoki
                            print("Оплата прошла успешно, вот ваш кофе ☕")
                        elif ostatoki > capuchino.money - oplatai:
                            oplata_dlya_tupih = ostatoki + oplatai
                            if dengi >= oplata_dlya_tupih:
                                print(f"А вот это уже многовато. Ваша сдача {oplata_dlya_tupih - capuchino.money} рублей")
                                dengi += capuchino.money
                            else:
                                print("У меня нет сдачи... Прости, заказ отменен")
                                galya(capuchino.water, capuchino.coffee, capuchino.milk)
                                break
                        elif ostatoki < capuchino.money - oplatai:
                            oplata_dlya_tupih = ostatoki + oplatai
                            ostatokа = input(f"С вас еще {capuchino.money - oplata_dlya_tupih} "
                                            "рублей или отмена:")
                            if ostatokа == "отмена":
                                galya(capuchino.water, capuchino.coffee, capuchino.milk)
                                break
                            ostatoki = int(ostatokа)
                            if ostatoki == capuchino.money - oplatai:
                                dengi += oplatai + ostatoki
                                print("Оплата прошла успешно, вот ваш кофе ☕")
                            elif ostatoki > capuchino.money - oplatai:
                                oplata_dlya_tupih = ostatoki + oplatai
                                if dengi >= oplata_dlya_tupih:
                                    print(f"А вот это уже многовато. Ваша сдача {oplata_dlya_tupih - capuchino.money} рублей")
                                    dengi += capuchino.money
                                else:
                                    print("У меня нет сдачи... Прости, заказ отменен")
                                    galya(capuchino.water, capuchino.coffee, capuchino.milk)
                                    break
                            elif ostatoki < capuchino.money - oplatai:
                                print("я устала это писать, поэтому никакого кофе ты не получишь!")
                                galya(capuchino.water, capuchino.coffee, capuchino.milk)
                    elif oplatai > capuchino.money:
                        if dengi >= oplatai-capuchino.money:
                            print(f"А вот это уже многовато. Ваша сдача {oplatai - capuchino.money} рублей")
                            dengi += capuchino.money
                        else:
                            print("У меня нет сдачи... Прости, заказ отменен")
                            galya(capuchino.water, capuchino.coffee, capuchino.milk)
                        break
            else:
                print("Прости, не хватает ингредиентов")
                galya(capuchino.water, capuchino.coffee, capuchino.milk)
            break
                
        elif command == "латте":
            if resurses(latte.water, latte.coffee, latte.milk) == True:
                oplata = input(f"С вас {latte.money} рублей: ")
                while True:
                    if oplata == "отмена":
                        galya(latte.water, latte.coffee, latte.milk)
                        break
                    oplatai = int(oplata)
                    if oplatai == latte.money:
                        dengi += oplatai
                        print("Оплата прошла успешно, вот ваш кофе ☕")
                        break
                    elif oplatai < latte.money:
                        ostatok = input(f"С вас еще {latte.money - oplatai} "
                                            "рублей или отмена:")
                        if ostatok == "отмена":
                            galya(latte.water, latte.coffee, latte.milk)
                            break
                        ostatoki = int(ostatok)
                        if ostatoki == latte.money - oplatai:
                            dengi += oplatai + ostatoki
                            print("Оплата прошла успешно, вот ваш кофе ☕")
                        elif ostatoki > latte.money - oplatai:
                            oplata_dlya_tupih = ostatoki + oplatai
                            if dengi >= oplata_dlya_tupih:
                                print(f"А вот это уже многовато. Ваша сдача {oplata_dlya_tupih - latte.money} рублей")
                                dengi += latte.money
                            else:
                                print("У меня нет сдачи... Прости, заказ отменен")
                                galya(latte.water, latte.coffee, latte.milk)
                                break
                        elif ostatoki < latte.money - oplatai:
                            oplata_dlya_tupih = ostatoki + oplatai
                            ostatokа = input(f"С вас еще {latte.money - oplata_dlya_tupih} "
                                            "рублей или отмена:")
                            if ostatokа == "отмена":
                                galya(latte.water, latte.coffee, latte.milk)
                                break
                            ostatoki = int(ostatokа)
                            if ostatoki == latte.money - oplatai:
                                dengi += oplatai + ostatoki
                                print("Оплата прошла успешно, вот ваш кофе ☕")
                            elif ostatoki > latte.money - oplatai:
                                oplata_dlya_tupih = ostatoki + oplatai
                                if dengi >= oplata_dlya_tupih:
                                    print(f"А вот это уже многовато. Ваша сдача {oplata_dlya_tupih - latte.money} рублей")
                                    dengi += latte.money
                                else:
                                    print("У меня нет сдачи... Прости, заказ отменен")
                                    galya(latte.water, latte.coffee, latte.milk)
                                    break
                            elif ostatoki < latte.money - oplatai:
                                print("я устала это писать, поэтому никакого кофе ты не получишь!")
                                galya(latte.water, latte.coffee, latte.milk)
                        break
                    elif oplatai > latte.money:
                        if dengi >= oplata - latte.money:
                            print(f"А вот это уже многовато. Ваша сдача {oplatai - latte.money} рублей")
                            dengi += latte.money
                        else:
                            print("У меня нет сдачи... Прости, заказ отменен")
                            galya(latte.water, latte.coffee, latte.milk)
                        break
            else:
                print("Прости, не хватает ингредиентов")
                galya(latte.water, latte.coffee, latte.milk)
            break
        elif command == "эспрессо":
            if resurses(espresso.water, espresso.coffee, espresso.milk) == True:
                oplata = input(f"С вас {espresso.money} рублей: ")
                while True:
                    if oplata == "отмена":
                        galya(espresso.water, espresso.coffee, espresso.milk)
                        break
                    oplatai = int(oplata)
                    if oplatai == espresso.money:
                        dengi += oplatai
                        print("Оплата прошла успешно, вот ваш кофе ☕")
                        break
                    elif oplatai < espresso.money:
                        ostatok = input(f"С вас еще {espresso.money - oplatai} "
                                            "рублей или отмена:")
                        if ostatok == "отмена":
                            galya(espresso.water, espresso.coffee, espresso.milk)
                            break
                        ostatoki = int(ostatok)
                        if ostatoki == espresso.money - oplatai:
                            dengi += oplatai + ostatoki
                            print("Оплата прошла успешно, вот ваш кофе ☕")
                        elif ostatoki > espresso.money - oplatai:
                            oplata_dlya_tupih = ostatoki + oplatai
                            if dengi >= oplata_dlya_tupih:
                                print(f"А вот это уже многовато. Ваша сдача {oplata_dlya_tupih - espresso.money} рублей")
                                dengi += espresso.money
                            else:
                                print("У меня нет сдачи... Прости, заказ отменен")
                                galya(espresso.water, espresso.coffee, espresso.milk)
                                break
                        elif ostatoki < espresso.money - oplatai:
                            oplata_dlya_tupih = ostatoki + oplatai
                            ostatokа = input(f"С вас еще {espresso.money - oplata_dlya_tupih} "
                                            "рублей или отмена:")
                            if ostatokа == "отмена":
                                galya(espresso.water, espresso.coffee, espresso.milk)
                                break
                            ostatoki = int(ostatokа)
                            if ostatoki == espresso.money - oplatai:
                                dengi += oplatai + ostatoki
                                print("Оплата прошла успешно, вот ваш кофе ☕")
                            elif ostatoki > espresso.money - oplatai:
                                oplata_dlya_tupih = ostatoki + oplatai
                                if dengi >= oplata_dlya_tupih:
                                    print(f"А вот это уже многовато. Ваша сдача {oplata_dlya_tupih - espresso.money} рублей")
                                    dengi += espresso.money
                                else:
                                    print("У меня нет сдачи... Прости, заказ отменен")
                                    galya(espresso.water, espresso.coffee, espresso.milk)
                                    break
                            elif ostatoki < espresso.money - oplatai:
                                print("я устала это писать, поэтому никакого кофе ты не получишь!")
                                galya(espresso.water, espresso.coffee, espresso.milk)
                        break
                    elif oplatai > espresso.money:
                        if dengi >= oplatai - espresso.money:
                            print(f"А вот это уже многовато. Ваша сдача {oplatai - espresso.money} рублей")
                            dengi += espresso.money
                        else:
                            print("У меня нет сдачи... Прости, заказ отменен")
                            galya(espresso.water, espresso.coffee, espresso.milk)
                        break
            else:
                print("Прости, не хватает ингредиентов")
                galya(espresso.water, espresso.coffee, espresso.milk)
            break
        else:
            print("Вы что-то ввели неправильно, попробуйте еще раз")
            
        
            
                        
                        
                    
        
    
