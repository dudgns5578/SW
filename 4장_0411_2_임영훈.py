'''
파일 저장 명 :  4장_0411_2_자기이름.py

작성일 : 2023년 4월 11일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 점수를 입력 받아 80점 이상이면 "합격"
        아니면 "불합격"을 출력하시오.
        점수와 상관없이 프로그램 마지막에는 "감사합니다"를 출력
'''
# 1. 점수를 입력받는다
score = int(input("점수를 입력하시오 : " ))

# 2. 만약에 점수가 80점 이상이라면 :
#   1) "합격입니다."를 출력한다.
if score >= 80 :
        print("합격입니다.")
        
# 3. 아니면
#   1) "불합격입니다."를 출력한다.
else :
        print("불합격입니다.")
        
# 6. 조건과 상관없이 마지막에는 "감사합니다"를 출력한다.
print("감사합니다.")
