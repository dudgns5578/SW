'''
파일 저장 명 :  4장_0411_3_자기이름.py

작성일 : 2023년 4월 11일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 입력 받은 정수가 짝수인지 홀수인지 판단하는 프로그램을 작성하시오.
'''
# 1. 정수를 입력받는다
num = int(input("숫자를 입력하시오 : " ))

# 2. 만약에 입력 받은 정수가 2로 나누었을때 나머지가 0이라면 :
#   1) "00은 짝수입니다."를 출력한다.
if num % 2 == 0 :
        print("{} 은 짝수입니다.".format(num))
        
# 3. 그게 아니면
#   1) "00은 홀수입니다."를 출력한다.
else :
        print("{} 은 홀수입니다.".format(num))
