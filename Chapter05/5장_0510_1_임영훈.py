'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 사용자로부터 하나의 정수를 입력 받아 다음과 같이 *을 출력하는 프로그램을 작성하시오.
'''

# 1. 정수 입력

# 2. 줄1 부터 입력 받ㅇ느 수까지 반복하면서
    # 2-1. 칸 줄까지 반복하면서
        # *을 출력한다.
    # 2-2. 줄바꿈한다.
    
num = int(input("정수를 입력하시오. : "))
for jul in range(num) :
    for kan in range(jul + 1) :
        print("*",end='')
    print() #줄바꿈.