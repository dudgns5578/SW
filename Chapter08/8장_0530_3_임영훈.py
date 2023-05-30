'''
작성일 : 2023년 5월 30일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 8장 파일 입출력
'''
# open() 함수로 파일 쓰기 - write() 메소드
f = open("text.txt", "r") # 파일 오픈

text = f.read()
print(text)

f.close() # 파일 종료