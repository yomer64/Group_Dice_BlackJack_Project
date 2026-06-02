import random
#This might be done I gave some docunent code to show how it can work, a hard coded model of course. 
# BUT this is a practical set up....
six_side_di=[1,2,3,4,5,6]
dealer_score=[]#will be tracked with int variable called n for example dealer[round]
player_score=[]#will be tracked with int variable called n for example player[round]
n = 0
sub_total_score = 0  # the starting score
all_loses= 0
all_wins = 0



def player_hit():    
    return random.choice(six_side_di) + random.choice(six_side_di) 

def dealer_hit():
    return random.choice(six_side_di)

def stand_dealer(sub_score):
    return dealer_score.append(sub_score)

def stand_player(sub_score):
    return player_score.append(sub_score)


    
# This is to both test the code and get an idea on how the input will go.
"""di = player_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"The 1st hit for the player \n")
di = player_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"The 2nd hit for the player \n")
stand_player()
print(sub_total_score,"player 1st total\n")
print(f" Player scored {player_score[n]} (score{n+1})\n")
sub_total_score=0

di = dealer_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"The 1st hit for the dealer \n")
di = dealer_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"The 2nd hit for the dealer \n")
di = dealer_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"The 3rd hit for the dealer \n")
di = dealer_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"The 4th hit for the dealer \n")
print(sub_total_score,"dealer 1st total\n")

stand_dealer()

print(f" Dealer scored {dealer_score[n]} (score{n+1})\n")

print("First Round:\n")
if dealer_score[n] >= player_score[n]:
    print(f"Dealer wins {dealer_score[n]} to {player_score[n]}\n")
else:
    print(f"Player wins {player_score[n]} to {dealer_score[n]}\n")
n=n+1
sub_total_score=0
#round 2



di = player_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"[1]The 1st hit for the player \n")
di = player_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"[1]The 2nd hit for the player \n")
stand_player()
print(sub_total_score,"[1]player 1st total\n")
print(f" [1]Player scored {player_score[n]} (score{n+1})\n")
sub_total_score=0

di = dealer_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"[1]The 1st hit for the dealer \n")
di = dealer_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"[1]]The 2nd hit for the dealer \n")
di = dealer_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"[1]The 3rd hit for the dealer \n")
di = dealer_hit()
sub_total_score = sub_total_score+di
print("rolled:",di,"[1]The 4th hit for the dealer \n")
print(sub_total_score,"[1]dealer 1st total\n")


stand_dealer()


print(f" Dealer scored {dealer_score[n]} (score{n+1})\n")

sub_total_score=0
print("Second Round:\n")

if dealer_score[n] >= player_score[n]:
    print(f"Dealer wins {dealer_score[n]} to {player_score[n]}\n")
else:
    print(f"Player wins {player_score[n]} to {dealer_score[n]}\n")
n=n+1
"""