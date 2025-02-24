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
