import random
life=6
word_list= ["flabergastic", "idiot", "chips","embbookreviews"]
chosen = random.choice(word_list)
print(chosen)
emp_list = []
for i in chosen:
    emp_list +='_'
print(emp_list)
game_over=False
while not game_over:
    guess= input("dear user guess any letter").lower()
    for pos in range(len(chosen)):
        i= chosen[pos]
        if(i==guess):
            emp_list[pos]=guess
            print(emp_list)
    if guess not in  chosen:
        life -= 1
        if(life==0):
            game_over = True
            print("loser")
    if '_' not in emp_list:
        game_over=True

        print("You win!")


