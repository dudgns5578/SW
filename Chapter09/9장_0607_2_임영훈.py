'''
작성일 : 2023년 6월 7일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 랜덤으로 문제를 출력하고 그에 맞는 답을 입력하였을때
정답과 오답이 몇개인지 출력하고 오답이 0개였을때는 '당신은 천재 입니다.'를 출력하시오.
'''
import random
# make_question 변수를 만든다.
def make_question() :
    # num1 의 값은 1 ~ 40 의 수 중 랜덤으로 저장한다.
    num1 = random.randint(1, 40)
    # num2 의 값은 1 ~ 20 의 수 중 랜덤으로 저장한다.
    num2 = random.randint(1, 20)
    # op 의 값은 1 ~ 3 의 수 중 랜덤으로 저장한다.
    op = random.randint(1, 3)
    # 문제 변수의 첫번째 수를 문자열로 변환하고 저장
    que = str(num1)
    # 만약 연산자 변수가 1일때
    if op == 1:
        # 문제 변수에 '+' 입력
        que = que + '+'
    # 만약 연산자 변수가 2일때
    if op == 2:
        # 문제 변수에 '-' 입력
        que = que + '-'
    # 만약 연산자 변수가 3일때
    if op == 3:
        # 문제 변수에 '*' 입력
        que = que + '*'
    # 문제 변수에 두번째 수를 문자열로 변환하고 저장
    que = que + str(num2)
    # 문제 변수를 변환한다.
    return que
# 정답, 오답의 개수를 0 으로 초기화
R_ans = 0
W_ans = 0
# 질문을 5번 반복하여 생성한다.
for i in range(5) :
    que = make_question()
    # 줄 바꿈 없이 문제를 출력한다.
    print(que, end='')
    # 문제 뒤에 = 을 출력하고 정수형으로 값을 입력받는다.
    result = int(input('='))
    # 문제의 값과 입력받는 값이 같다면
    if eval(que) == result :
        # 정답입니다. 출력
        print('정답입니다.')
        # 정답 개수를 1개 추가
        R_ans += 1
    # 그게 아니면
    else :
        # 오답입니다. 출력
        print('오답입니다!')
        # 오답 개수를 1개 추가
        W_ans += 1
# 정답과 오답의 개수를 출력한다.
print('정답 : ', R_ans, '오답 : ', W_ans)
# 오답이 0개라면
if W_ans == 0 :
    # 당신은 천재 입니다. 출력
    print('당신은 천재 입니다.')