'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 8장 파일 입출력
'''
# writelines() 메소드
list1 = ['월요일\n', '화요일\n', '수요일\n', '목요일\n', '금요일\n', '토요일\n', '일요일\n']

# readline() 메소드 사용하여 무한 반복분으로 읽기
print("== 무한 반복문으로 이용하여 읽기 ==")
with open("Linetext.txt," "r")as f :
    while True :
        line = f.readline()
        print(line, end='')