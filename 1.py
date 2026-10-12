from rich.console import Console # type: ignore
questions: list [tuple[str,list[str],str]]=[
("the best CMS in the Morld",["A: wordpress","B: joomla","C: Drupal","D:squarepace"],"A"),
 ("what is the most popular cms?",["A: wordpress","B: joomla","C: Drupal","D:squarepace"],"B"),
 ("which cms is known for its user-friendly interface?", ["A: wordpress","B: joomla","C: Drupal","D:squarepace"],"D")
 ]
console=Console()
score=0
total_correct=0
CORRECT_BOUNES=10
PENALTY=3
for question,options,correct in questions:
    console.print(question,style="white")
    for option in options:
        console.print(f"{option}\n",style="belue")
    user_answer: str= input("your answer (A,B,C,D): ").strip().upper()
    if user_answer == correct:
        total_correct+=1
        score+=10
        console.print("correct!\n",style="blue")
        score+=CORRECT_BOUNES
    else:
        score -=3
        console.print(f"wrong! the correct answer is {correct}.\n",style="bold yellow")

console.print(f"your score is:{score}",style=" pink")
console.print(f"total correcct answer:{total_correct}",style="bold red")