import random


Player = 100
Monster = 50
Monster_List = [50]
level = 0
exp = 0


def playerAction():
    print("1. Attack")
    print("2. Heal")


def levelUp():
    print("****************************")
    print("You level up to level :", level)
    print("Hp reset and expanded")
    print("Attack Damage Increase")
    print("****************************")


Monster = random.randint(1,4)
print(Monster,"Monster has appeared")


if Monster >= 2:
    Monster_List.append(50)
if Monster >= 3:
    Monster_List.append(50)
if Monster >= 4:
    Monster_List.append(50)    


while(True):
    if Player <= 0:
        print("Yep you are death")
        break
    elif Monster_List[-1] <= 0:
        print("You Win!!!")
        break
    else:
        playerAction()
        for i in range(0,len(Monster_List)):
           
                while Monster_List[i] > 0:
                    if exp == 50:
                        levelUp()
                        exp = 0
                        level += 1
                        Player = 100 + (10 * level)


                    critical = int(random.randint(1,3))
                    action = int(input("Enter action : "))
                    impact = random.randint(5+level,15+level)


                    while action != 1 and action != 2:
                        print("Please input 1 or 2")
                        action = int(input("Enter action : "))  


                    if action == 1:
                        print("Attack")
                        if critical == 1:
                            impact = impact * 2
                            print("Critical Attack!!")
                        Monster_List[i] = Monster_List[i] - impact
                        print("Monster", i+1, "Health =", Monster_List[i])


                    elif action == 2:
                        Player += impact
                        print("Healing")
                        print("Current Health :", Player)


                    mon_attack = random.randint(5,15)
                    Player -= mon_attack
                    print()
                    print("Monster Attack You")
                    print("Current Health =", Player)
                    print("____________________________")
        print("Monster Killed")
        print("EXP + by 25")
        exp += 25      
