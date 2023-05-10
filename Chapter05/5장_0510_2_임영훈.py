'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 2단부터 9단까지 구구단을 출력하시오.
단, 구구단의 결과가 짝수인 경우만 출력하시오.
while문과 for문으로 작성하고, 비교하시오.
'''

print("for 반복문으로 구구단을 출력하세요.")

for dan in range(2,10) :
    print("{} 단".format(dan))
    for num in range(1, 10) :
        if (dan*num) %2 == 0 :
            print("{} X {} = {}" .format(dan,num,dan*num))
            
    
    
dan = 2

while dan <= 9 :
    print("{} 단".format(dan))
    num = 1
    while num <= 9 :
        if (dan*num) %2 == 0 :
            print("{} X {} = {}" .format(dan,num,dan*num))
        num = num + 1      
    dan = dan + 1