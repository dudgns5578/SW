using System;

class Program
{
    static void Main()
    {
        string[] dialogues = {
            "리안, 너의 힘은 그 누구보다 특별해. 스스로를 믿어야 해.",
            "네가 잃어버린 기억 속에 중요한 단서가 숨어있어. 내가 도와줄게."
        };
        
        int dialogueIndex = 0;

        Console.WriteLine("아리엘과의 대화 시작!");
        while (dialogueIndex < dialogues.Length)
        {
            Console.WriteLine(dialogues[dialogueIndex]);
            Console.WriteLine("다음 대화로 넘어가려면 Enter 키를 누르세요.");
            Console.ReadLine();  // 사용자가 Enter 키를 누를 때까지 대기
            dialogueIndex++;
        }
        
        Console.WriteLine("대화 종료.");
    }
}
