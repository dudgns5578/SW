'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 10개의 정수를 입력 받아 합을 구하는 프로그램을 작성하시오.
단, 짝수 번째에 이력되는 숫자는 양수를 음수로, 음수를 양수로 바꾸어 합을 구하시오.
'''

# 1. 반복하면서
# 1)정수 입력
# 2) 만약 짝수번째 라면
# 양수 → 음수 , 음수 → 양수로 변환
# # 합계 계산
count = 1
sum = 0

for count in range(10) :
    num = int(input(str(count) + "번째 정수를 입력하세요. : "))
    if count % 2 == 0 :
        num = num * -1
    sum = sum + num
    count = count + 1 
print("10개 정수의 합 :" , sum)

print("---------------------------------------------------------------")

count = 1
sum = 0
while True :
    num = int(input("{} 번째 정수 입럭 : " .format(count)))
    if count % 2 == 0:
        num = -num
    sum += num
    count += 1
    
    if count > 10 :
        break
print("10개 정수의 합 : {}".format(sum))