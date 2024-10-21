'''
to implement higher lower problem
'''

from art import *
from game_data import data
import random
from replit import clear

def format_data(account):
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return (f"{account_name}, a {account_descr},from {account_country}")

def check_answer(guess,a_followers,b_followers):
     if a_followers > b_followers:
         if guess=="a":
             return True
         else:
             return False         
     else:
         return guess == "b"    





score=0
print(logo)
game_should_continue=True
account_b=random.choice(data)



while(game_should_continue):
  account_a=account_b
  account_b=random.choice(data)
  if account_a== account_b:
      account_b=random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Compare B: {format_data(account_b)}.")

  guess=input("Who has more followers?Type A or B").lower()

  a_follower_count=account_a["follower_count"]
  b_follower_count=account_b["follower_count"]

  clear() 

  is_correct=check_answer(guess,a_follower_count,b_follower_count)
  clear() 
  if is_correct:
      score+=1
      print(f"you are correct.Current score={score}")
  else:
    game_should_continue=False
    print("that is wrong.final score= ",score)    


