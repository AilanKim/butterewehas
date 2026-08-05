
#시작부분

intro = input("라면자판기를 사용하시겠습니까?(엔터)")
choice = input("그런다면 네/아니요로 대답해주세요.")

print(intro)
print(choice)

#종류 고르기

from make_ramen.시작 import start

def 시작들() : 
      for 시작들 in start : 
        print(시작들)

시작들()

# * -------------------------------------

def 선택(멘트) :
        ment = input("골라주세요")
        kindment = (ment +"물양을" + 멘트)
        print(kindment)

선택("다음으로 터치해주세요(ml)")

# * -------------------------------------

#물

from make_ramen.물 import water

def 물양() : 
      for 물양들 in water : 
            print(물양들)

물양()

def 선택(멘트) :
    ment = input("골라주세요")
    waterment = (ment + "냄비를" + 멘트)
    
    print(waterment)

선택("다음으로 터치해주세요")

# * -------------------------------------

#냄비

from make_ramen.냄비 import bowl

def 냄비들() : 
      for 추가재료 in bowl : 
            print(추가재료)

냄비들()

def 선택(멘트) :
    ment = input("골라주세요")
    bowlment = (ment + "면을" + 멘트)
    
    print(bowlment)

선택("다음으로 터치해주세요")

# * ----------------------------

#면

from make_ramen.면 import noodle

def 면들() : 
      for 면 in noodle : 
            print(면)

면들()

def 선택(멘트) :
    ment = input("골라주세요")
    noodlesment = (ment + "후레이크" + 멘트)
    
    print(noodlesment)

선택("다음으로 터치해주세요")

# * -------------------------------------

#후레이크

from make_ramen.후레이크 import powder

def 건더기들() : 
      for 건더기 in powder : 
            print(건더기)

건더기들()

def 선택(멘트) :
    ment = input("골라주세요")
    powderment = (ment + "수프" + 멘트)
    
    print(powderment)

선택("다음으로 터치해주세요")

# * -------------------------------------

#스프

from make_ramen.스프 import soup

def 스프들() : 
      for 스프 in soup : 
            print(스프)

스프들()

def 선택(멘트) :
    ment = input("골라주세요")
    soupment = (ment + "조미류를" + 멘트)
    
    print(soupment)

선택("다음으로 터치해주세요")

# * -------------------------------------

#조미

from make_ramen.조미 import side

def 조미들() : 
      for 조미류 in side : 
            print(조미류)

조미들()

def 선택(멘트) :
    ment = input("골라주세요")
    sidement = (ment + "추가" + 멘트)
    
    print(sidement)

선택("다음으로 터치해주세요")


# * -------------------------------------

#추가

from make_ramen.추가 import add

def 추가들() : 
      for 추가재료 in add : 
            print(추가재료)

추가들()

intro = input("잠시만 기다려주세요.")
print(intro)

# * -------------------------------------

#완료
finish = input("주문이 접수 되었습니다. 완료되면 주문 번호로 불러드립니다.")
print(finish)
