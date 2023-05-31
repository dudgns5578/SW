'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 8장 파일 입출력
'''
# print() 함수로 파일에 저장.   매개변수 file의 값으로 파일 객체에 저장.
f = open("ptext.txt", "w")

print("컴퓨터공학부", file = f)
print("202395027", file = f)
print("임영훈", file = f)

f.close()

# with open("ptext.txt", "w") as f :