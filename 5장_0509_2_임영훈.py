'''
작성일 : 2023년 5월 9일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 5과목의 성적을 입력 받아 각 과목의 점수, 총점, 평균을 출력하는 프로그램을 작성하시오.
입력한 성적이 0~100점 사이가 아닌 경우 "유효한 성적이 아닙니다."를 출력하고, 다음 과목을 입력받으시오
'''

# 1. 첫번째 성적 입력
i = 1
while i <= 5 :
    sc = int(input(str(i) + "번째 성적을 입력하시오. : "))
    print("첫번째 성적은 {}점 입니다.".format(sc))
    i = i + 1
if sc >= 0 and sc <= 100 :
    total = total + score
    print("{}번째 성적은 {}점 입니다.".format(i,sc))
    i = i + 1
else :
    print("유효한 성적이 아닙니다.")

print("총점 : {}".format(total))

print("평균 : ".format(total / 5))

# total = sc1 + sc2 + sc3 + sc4 + sc5
# 평균 - avg
# avg = total / 5