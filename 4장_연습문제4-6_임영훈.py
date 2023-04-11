'''
파일 저장 명 :  4장_연습문제4-6_자기이름.py

작성일 : 2023년 4월 11일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 사용자로부터 3과목의 점수를 입력 받아 평균이 95점 이상이면 
"당신의 평균은 00.0점입니다.",축하합니다. A+ 입니다."를 출력하고,
마지막에는 평균과 상관없이 "감사합니다"를 출력하는 프로그램을 작성하시오.
'''
# 1. 국어점수의 데이터 값을 실수로 변환하여 변수 kor에 입력받는다.
kor = float(input("국어점수를 입력하시오 : " ))

# 2. 수학점수의 데이터 값을 실수로 변환하여 변수 math에 입력받는다.
math = float(input("수학점수를 입력하시오 : " ))

# 3. 영어점수의 데이터 값을 실수로 변환하여 변수 eng에 입력받는다.
eng = float(input("영어점수를 입력하시오 : " ))

# 4. 입력받은 3과목의 평균을 계산한다
avg = (kor + math + eng) / 3

# 5. 조건문 if를 사용하여 평균이 95.0점 이상인지 비교한다.
        # 3-1. 조건을 달성할 경우, "당신의 평균은 00.0 점 입니다."를 출력한다.
if avg >= 95 :
        print("당신의 평균은" , avg,"점 입니다.")
        print("당신의 평균은 {:.if}점 입니다." .format(avg))
        # 3-2. 조건을 달성할 경우, "축하합니다. A+ 입니다."를 출력한다
if avg >= 95 :
        print("축하합니다 A+ 입니다.")
        
# 6. 조건과 상관없이 마지막에는 "감사합니다"를 출력한다.
print("감사합니다.")
