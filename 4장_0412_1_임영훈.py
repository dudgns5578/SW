'''
파일 저장 명 :  4장_0412_1_자기이름.py

작성일 : 2023년 4월 12일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 입력 받은 정수가 양수인지 음수인지 0인지 판단하는 프로그램을 작성하시오.
'''

# 1. 숫자를 입력받아 정수로 변환하고 저장한다.
num = int(input("숫자를 입력하시오 : "))

# 2. 만약 입력받은 정수가 0보다 크다면
if num > 0 :
# 2-1. "00은 양수입니다." 출력
    print("{}은 양수입니다.".format())

# 3. 그게 아니라 정수가 0보다 작다면
elif num < 0 :
# 3-1. "00은 음수입니다." 출력
    print("{}은 음수입니다.".format())

# 4. 그것도 아니라면
else :
# 4-1. "00은 0입니다." 출력
    print("{}은 0입니다.".format())