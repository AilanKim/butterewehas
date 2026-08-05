
#새로 짜보는 선택 작업.
#우선 커피 이름 가격을 각 키, 값 해서 다시 짰다. 

coffee_nameprice = [
    {'name' : '조지아', 'price' : 2400},
    {'name' : '티오피', 'price' : 2200},
    {'name' : '바리스타', 'price' : 2900},
    {'name' : '칸타타', 'price' : 2800},
    {'name' : '레쓰비', 'price' : 1000},
    {'name' : '프렌치카페', 'price' : 2700},
    {'name' : '스타벅스', 'price' : 3200},
    {'name' : '맥스웰하우스', 'price' : 1500},
    {'name' : '일리', 'price' : 1300},
    {'name' : 'ucc', 'price' : 2500},
]

# * --------------------------------------

#자동으로 나오게끔 설정 해보기

def choice(coffee_nameprice) : 
    print(['List'])
    for coffeechoice in coffee_nameprice : 
        print(coffeechoice['name'] + '' + str(coffeechoice['price']) + '원')
        print('\n')

# * -------------------------------------

#선택 할 수 있게 입력

def choicedrink(coffee_nameprice) :
    choosee = input("커피를 골라주세요.")
    chooseinfo = {}

    for i, iscoffee in enumerate(coffee_nameprice) : 
        if choosee in iscoffee['name'] :
            chooseinfo['name'] = choosee
            chooseinfo['price'] = coffee_nameprice[i]['price']
            print('{}를 선택하셨습니다.'. format(chooseinfo['name']))
            print('가격은 {}원 입니다.\n'. format(chooseinfo['price']))
            break


    inputprice = input("금액을 투입해 주세요 : ")
    if int(inputprice) >= chooseinfo['price'] :
        print('구입 후 잔액은 {} 입니다.'. format(int(inputprice) - chooseinfo['price']))
    else : 
        print('돈이 부족합니다.')

choicedrink(coffee_nameprice)

# * -------------------------------------

# 이 부분은 결제 부분이므로 결제로 끌어가서 해봐야 한다.

