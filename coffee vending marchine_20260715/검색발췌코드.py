drinkMenu = [{'name': '사이다', 'price': 1700}, 
             {'name': '콜라', 'price': 1900}, 
             {'name': '식혜', 'price': 2500}, 
             {'name': '솔의눈', 'price': 3000}]

def menuList(drinkMenu):
    print('[ Menu ]')
    for drink in drinkMenu:
        print(drink['name'] + '' + str(drink['price']) + '원')
    print('\n')

def choiceDrink(drinkMenu):
    choiceDrink = input("음료를 선택해주세요 : ")
    choiceDrinkInfo = {}

    for i, drink in enumerate(drinkMenu):
        if choiceDrink in drink['name']:
            choiceDrinkInfo['name'] = choiceDrink
            choiceDrinkInfo['price'] = drinkMenu[i]['price']
            print('{}를 선택하셨습니다.'.format(choiceDrinkInfo['name']))
            print('가격은 {}원 입니다.\n'.format(choiceDrinkInfo['price']))   
            break

    if choiceDrinkInfo == {}:
        print('입력한 음료는 없습니다.')   

    inputPrice = input("금액을 투입해주세요 : ")
    if int(inputPrice) >= choiceDrinkInfo['price']:
        print('구입 후 잔액은 {}원 입니다'.format(int(inputPrice)-choiceDrinkInfo['price']))
    else:
        print('돈이 부족합니다.')


menuList(drinkMenu)
choiceDrink(drinkMenu)