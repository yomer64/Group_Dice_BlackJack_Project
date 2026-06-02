from game import Player 
from dice import *
valid= True
bet_time=True
money=1000
rebuy=0
bet_amount=0
house_busts_player_response_chooser=[1,2,3,4,5,6,7,8,9,0]
house_busts_player_response=["Karl the dealer: \n Sorry bud better luck next time","Karl the dealer:\nThe house wins! bud sorry but there are consequences","Karl the dealer:\nI hope you had fun bud I'm going to miss you","Karl the dealer:\nYou can't tell me you expected this to be easy right?","Karl the dealer: \nSorry bud that you lost so much money but life is rough","Karl the dealer:\n: I won, I will get a raise.\n player:\n You're serious? \nKarl the dealer: \n I just make 14 an hour of course I'm not serious.","player:\nI wish I had more money.\n Karl the dealer: \n Yeah that is really too bad, nothing I can do about it.","Karl the dealer: \n but You lost, the house wins, drinks on me.","Karl the dealer:\nCheer up bud you're money will be well kept with the house, maybe","Karl the dealer:\n It's 12am just like that, I have kids at home, thank you for ending my shift bud"]
house_reponds_to_cash_out=[]
house_reponds_to_cash_out_chooser=[1,2,3,4,5,6,7,8,9,0]
Trash_talk=["exGood luck","Have Fun","The dealer will beat you","Haha time to win","You won't win","Ye Haw","Hmmm large bet","Think you can beat me", "Big mistake","The house will win"]
Trash_chooser=[1,2,3,4,5,6,7,8,9,0]

# Ask for the player's name

print("Game structure:\n You start with $1000, The player plays against the dealer whom is Karl Vouri. \nThe gameplay for the player:\n They get to see their first roll before they bet, \n after they bet they get to decide whether they hit or stand. \n The player has to roll 2 dice at a time. Once they stand the dealer starts to roll their di they have to stand on 18 and hit if lower than 18. \n Game rules:\n Player gets 2x their initial bet if they have a higher score than the dealer or dealer bust, \nPlayer Gets 4x their initial bet automatically if they get the score 21 , Player rolls 2 dice at a time,\n Dealer wins ties, Dealer rolls One Di at a time, You can always buy back in for $1000 no more and no less, Min bet $1, no max bet as long as it isn't above your own balance")
name = input(" Welcome to Diced Blackjack! What's your name? ").title()

# Create a Player object
player = Player(name)

# Greet the player

total_money_lost=0
total_money_won=0
try_again=True
print(f"Hello, {player.name}! Let's play Blackjack!")
while try_again==True:
    try:
        age= int(input("How old are you?"))
        
        if age<0:
            print("Your age can't be negative you were born at least sometime today.")     
            continue
        else:
            try_again=False
    except:
        print("Your age has to be a whole number")
        tried_again= True
        continue
    
    if age >= 18:
        while True:
            if valid==True:
                if money==0 and bet_time == True:
                    que=input("would you like to rebuy in? \n(yes/y/1 for yes other keys for no)")
                    if que== "yes" or que=="y" or que=="1":
                        print("Okay Good Luck")
                        money=1000
                        rebuy+=1
                        
                    else:
                        #Ramdom dialogue from house
                        print(f"you lost ${(rebuy*1000)+1000}!")
                        print(f"{house_busts_player_response[random.choice(house_busts_player_response_chooser)]}")
                        quit()
                print("round:",n+1)
                di = player_hit()  
                sub_total_score += di
                print(f"{player.name}, you rolled: {di}. Your total is now {sub_total_score}.")
                while bet_time==True:
                    try:
                        bet_amount=int(input(f"{player.name} you have ${money}.00  \nHow much would you like to bet, no max, minimun is $1:"))
                        if bet_amount<=0:
                            print("The bet must be positive")
                            continue
                        if bet_amount>money:
                            print(f"Sorry {player.name}. You can't bet more money than you have, you have {money}. {bet_amount} is an invalid bet")
                            continue
                        else:
                            money=money-bet_amount
                            print(f"{player.name}'s money: {money}")
                            bet_time=False
                            print(f"{player.name} bet: {bet_amount}\n {Trash_talk[random.choice(house_reponds_to_cash_out_chooser)]}\n")
                            
                    except:
                        print("Type whole numbers")

            else:
                print("still round:",n+1,"still roll",sub_total_score)
                print("Invalid choice. Please type 'hit' or 'stand'.")
                choice = input("Hit or stand?").strip().lower()
                if choice=="hit":
                    valid=True
                    di = player_hit()  
                    sub_total_score += di
                    print(f"{player.name}, you rolled: {di}. Your total is now {sub_total_score}.")
                elif choice == "stand" and sub_total_score == 21:
                    stand_player(sub_total_score)
                    sub_total_score=0
                    stand_dealer(sub_total_score)
                    all_wins=all_wins+1
                    total_money_won= total_money_won+(bet_amount*3)
                    print(f"{player.name} wins {player_score[n]} to {dealer_score[n]} by Black Jack\n")
                    money=money+(4*bet_amount)
                    print(f"{player.name} you won ${(4*bet_amount)}!!!")
                    bet_amount=0
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        valid=True
                        bet_time=True
                        continue
                        
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                        if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                            print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                            break
                        else:
                            print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                            break
                        
                        
                        
                        
                
                elif choice =="stand":
                    print("round:",n+1)
                    stand_player(sub_total_score)
                    print(f"You chose to stand with a total of {player_score[n]}.")
                    sub_total_score=0
                    while sub_total_score<18:
                        di = dealer_hit()
                        sub_total_score += di
                        print(f"dealer rolled a {di} his current score:{sub_total_score}")
                    if sub_total_score >21:
                        all_wins=all_wins+1
                        total_money_won= total_money_won+bet_amount
                        stand_dealer(sub_total_score)
                        print(f"The dealer has busted!! with a score of {dealer_score[n]}.")
                        print(f"{player.name}, your score is {player_score[n]} you won!")
                        money=money+(2*bet_amount)
                        print(f"{player.name} you won ${(2*bet_amount)}!!!")
                        bet_amount=0
                        play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()
                        
                        if play_again=="yes" or play_again=="y" or play_again=="1":
                            n=n+1
                            sub_total_score=0
                            valid=True
                            bet_time=True
                            continue
                        else:
                            print(f"{player.name} you've played {n+1} rounds")
                            print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                            print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                            if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                                print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                                break
                            else:
                                print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                                break
                    stand_dealer(sub_total_score)
                    if dealer_score[n] >= player_score[n]:
                        all_loses=all_loses+1
                        total_money_lost+=bet_amount
                        
                        bet_amount=0
                        print(f"Dealer wins {dealer_score[n]} to {player_score[n]}\n")
                        bet_amount=0
                        play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()
                        if play_again=="yes" or play_again=="y" or play_again=="1":
                            n=n+1
                            sub_total_score=0
                            valid=True
                            bet_time=True
                            continue
                        else:
                            print(f"{player.name} you've played {n+1} rounds")
                            print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                            print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                            if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                                print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                                break
                            else:
                                print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                                break
                    else:
                        all_wins=all_wins+1
                        total_money_won= total_money_won+bet_amount
                        print(f"{player.name} wins {player_score[n]} to {dealer_score[n]}\n")
                        money=money+(2*bet_amount)
                        print(f"{player.name} you won ${(2*bet_amount)}!!!")
                        bet_amount=0
                        play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()
                        if play_again=="yes" or play_again=="y" or play_again=="1":
                            n=n+1
                            sub_total_score=0
                            valid=True
                            bet_time=True
                            continue
                        else:
                            print(f"{player.name} you've played {n+1} rounds")
                            print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                            print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                            if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                                print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                                break
                            else:
                                print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                                break
                        

                else:
                    continue    

                # 🃏 Check for bust 
            if sub_total_score > 21:
                print("round:",n+1)
                all_loses=all_loses+1
                total_money_lost+=bet_amount
                bet_amount=0
                stand_player(sub_total_score)
                stand_dealer(0)
                print(f" {player.name}, you busted with a total of {player_score[n]}! Dealer has score of {dealer_score[n]}")
                play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()
                if play_again=="yes" or play_again=="y" or play_again=="1":
                    n=n+1
                    sub_total_score=0
                    bet_time=True
                    continue
                    
                else:
                    print(f"{player.name} you've played {n+1} rounds")
                    print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                    print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                    if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                        print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                        break
                    else:
                        print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                        break


            # ask player if they want to hit or stand
            choice = input("Hit or stand? ").strip().lower()
            
            if choice == "stand" and sub_total_score == 21:
                    stand_player(sub_total_score)
                    sub_total_score=0
                    stand_dealer(sub_total_score)
                    all_wins=all_wins+1
                    total_money_won= total_money_won+(3*bet_amount)
                    print(f"{player.name} wins {player_score[n]} to {dealer_score[n]} by Black Jack\n")
                    money=money+(4*bet_amount)
                    print(f"{player.name} you won ${(4*bet_amount)}!!!")
                    bet_amount=0
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        valid=True
                        bet_time=True
                        continue
                    
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                        if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                            print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                            break
                        else:
                            print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                            break
            elif choice == "stand":
                stand_player(sub_total_score)
                print(f"You chose to stand with a total of {player_score[n]}.")
                sub_total_score=0
                while sub_total_score<18:
                    di = dealer_hit()
                    sub_total_score += di
                    print(f"dealer rolled a {di} his current score:{sub_total_score}")
                if sub_total_score >21:
                    total_money_won= total_money_won+bet_amount
                    all_wins=all_wins+1
                    stand_dealer(sub_total_score)
                    print(f"The dealer has busted!! with a score of {dealer_score[n]}.")
                    print(f"{player.name}, your score is {player_score[n]} you won!")
                    money=money+(2*bet_amount)
                    print(f"{player.name} you won ${(2*bet_amount)}!!!")
                    bet_amount=0
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()

                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        bet_time=True
                        continue
                    
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                        if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                            print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                            break
                        else:
                            print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                            break
                stand_dealer(sub_total_score)
                if dealer_score[n] >= player_score[n]:
                    all_loses=all_loses+1
                    total_money_lost+=bet_amount
                    bet_amount=0
                    print(f"Dealer wins {dealer_score[n]} to {player_score[n]}\n")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        valid=True
                        bet_time=True
                        continue
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                        if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                            print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                            break
                        else:
                            print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                            break

                else:
                    all_wins=all_wins+1
                    total_money_won= total_money_won+bet_amount
                    
                    print(f"{player.name} wins {player_score[n]} to {dealer_score[n]}\n")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, press any other key to cashout: ").strip().lower()
                    money=money+(2*bet_amount)
                    
                    bet_amount=0
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        valid=True
                        bet_time=True
                        continue
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        print(f"{player.name} you have cashed out with ${money}\n That is {(money/10)}% of the starting starting stack")
                        if money-(total_money_lost-total_money_won)<=1000+(1000*rebuy):
                            print(f"{player.name} remember you lost ${total_money_lost-(total_money_won)}.00 so not much of a winning")
                            break
                        else:
                            print(f"{player.name} you profit ${money-(1000+(1000*rebuy))}.00 nice win!")
                            break
                            
                
            elif choice != "hit":
                valid=False

    else:
        print("You're too young to gamble, sorry.")
    
