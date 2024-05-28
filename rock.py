rock =''' 
      ___ 
  ---'  _)
       (__)
       (__)
       (_)
  ---.(_)
     
'''   
paper ='''
       __
  ----'  _)_
           __)
           ___)
          ___)
  ----.____)

'''
scissor= '''
     __
 ---' _)_
      __)
      ___)
      (_)
 ---.(_)
'''
#print("Rock:"+rock)
#print("Paper:"+paper)
#print("Scissor:"+scissor)
import random
image=[rock,paper,scissor]
user_choice=int(input("Enter your choice ?Type 0 for rock or 1 for paper or 2 for scissor.\n"))
print(image[user_choice])
computer_choice=random.randint(0,2)
print("computer choice:",computer_choice)
print(image[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid number,you lose")
elif user_choice==0 and computer_choice==2:
    print("you win!")
elif computer_choice > user_choice:
    print("you loss")
elif user_choice== computer_choice:
    print("its draw")
