'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터 공학부
학번 : 202395027
이름 : 임영훈
설명 : 8장 파일 입출력
'''
# 문장을 입력 받아 파일에 저장
sentence = []   # 빈 리스트 생성

# enter 키를 입력 할 때까지 반복하여 문자 입력 받기
while True :
    text = input("저장할 문장 입력(종료:엔터키) : ")
      
    sentence.append(text + "\n")   # 입력 받은 내용 리스트가 추가
    print("입력될 리스트 : ", sentence)

# sentence.txt 파일에 내용 출력(쓰기)
with open("sentence.txt", "w") as f : # 파일 오픈(쓰기)
    f.writelines(sentence)
    
print("sentence.txt 파일이 생성되었습니다.")