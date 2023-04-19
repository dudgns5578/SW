'''
파일 저장 명 :  4장_0419_2_자기이름.py

작성일 : 2023년 4월 19일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 숫자 → 연산자 → 숫자 순으로 입력 받아 
사칙연산의 결과를 출력하는 계산기 프로그램을 작성하시오.
'''

# 1. 첫번째 숫자를 입력하시오.
score1 = int(input("첫번째 숫자를 입력하시오. : "))

# 2. 연산자를 입력하시오.
cal = (input("연산자를 입력하시오. : "))

# 3. 두번째 숫자를 입력하시오.
score2 = int(input("두번째 숫자를 입력하시오. : "))

# 4. 만약 cal이 + 라면
if cal == '+' :
    print("{} + {} = {}" .format(score1, score2, score1 + score2))
    
# 4-1. 만약 cal이 - 라면
elif cal == '-' :
    print("{} - {} = {}" .format(score1, score2, score1 - score2))
    
# 4-2. 만약 cal이 * 라면
elif cal == '*' :
    print("{} * {} = {}" .format(score1, score2, score1 * score2))
    
# 4-3. 만약 cal이 / 라면
elif cal == '/' :
    print("{} / {} = {}" .format(score1, score2, score1 / score2))
    
# 5. 그게 아니라면
else :
    print("해당 연산자가 없습니다.")