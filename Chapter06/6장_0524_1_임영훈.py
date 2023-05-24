'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학부
학번 : 202395027
이름 : 임영훈
설명 : 6장 시퀀스 자료형
        04. 튜플
'''

# 튜플 생성
tuple1 = ()  # 빈 튜플 생성.
tuple2 = ('a',) # 원소가 하나여도 쉼표는 필수!!!
tuple3 = ('a','b','c')

color = ('red','blue','white','white','white','red','black')
print("color 내용 : ", color)
print("color 의 길이 : ", len(color))
print("white 의 개수 : ", color.count('white'))
print("blue의 위치 : ", color.index('blue'))

# 실습 예제 6-7
#  2개의 튜플을 하나의 리스트로 만들기
fruit = ('딸기','배','포도','사과','망고')
price = ('200','4500',',8000','12000','5500')

# 결과 : [사과, 2000, 배, 4500, .....]
fp_list = []    # 2개의 튜플 내용이 저장 될 리스트 생성.

for i in range(len(fruit)) :
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    
print("과일 목록 : ", fruit)
print("가격 목록 : ", price)
print("과일의 가격 리스트 : ", fp_list)
