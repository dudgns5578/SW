'''
작성일 : 2023년 5월 30일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 8장 파일 입출력
'''
# open() 함수로 파일 쓰기 - write() 메소드
f = open("text.txt", "w") # 파일 오픈

#파일에 쓸 내용.
for i in range(1,11):
    f.write("{}번쨰 메시지 입니다. \n".format(i))

f.close() # 파일 종료