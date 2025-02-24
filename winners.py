# Scenario: A popular game company, GameMasters Inc., has decided to show 
# appreciation to its loyal user base by giving out some exciting goodies. 
# They have announced a special giveaway where they will randomly select 
# 10 users out of their 10,000 registered users to receive a gift card and 
# another 10 users to receive a tumbler.  
# To ensure fairness, no user can win more than one prize. 
# UserIDs are numbers from 1 to 10000.

from random import *
users = range(1,10001) #create numbers from 1-10000
print(type(users))
users = list(users)
shuffle(users)
winners = sample(users, 20) #select 20 winners

print ("---- Winners ----")
print("Gift Cards : {0}" .format(winners[0:10]))
print("Tumbers : {0}" .format(winners[10:]))
print("--- Congratulations! ---")