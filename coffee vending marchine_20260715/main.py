
#안내문 가져오기

from vending_coffee.사용안내 import guide, explain

print(guide)
print(explain)

# * -------------------------------

#카드랑 현금을 고른다고 했을 때 현금 일 때 넣어주세요. 카드 일 때는 대주세요를 집어 넣고 싶다. 
#이건 조건문을 써야 한다. 반복문이 아니다.

#결제 방법 고르는거 가져오기

from vending_coffee.시작 import choice

print(choice)

# * --------------------------------

#커피 고르기

from vending_coffee.선택 import choice, choicedrink

print(choice)
print(choicedrink)

# * --------------------------------

#위에 결제까지 이어진 함수라서 선택과 결제를 합쳤다. 
#원하던 제품을 고르고 가격 안내와 계산에 거스름돈 까지는 되었다. 



