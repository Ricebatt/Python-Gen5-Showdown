import socket
from _thread import *
from pokemon import *

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server = input("Enter your IPv4 (Can be found in your command prompt, type ipconfig): ")

    s.bind((server, port))
except socket.error as e:
    str(e)

print("Waiting for a connection, Server started")

s.listen(2)

pokemon1 = Pokemon()

              #nrm fir wtr ele grs ice fig psn grd fly psy bug  roc gst drg drk stl none
typeMatrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],              #normal      0
              [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],          #fire        1
              [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],            #water       2
              [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],            #electric    3
              [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1],    #grass       4
              [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],          #ice         5
              [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 1],          #fighting    6
              [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 1],          #poison      7
              [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1],              #ground      8
              [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1],            #flying      9
              [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],              #psychic     10
              [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 1],      #bug         11
              [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],            #rock        12
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5, 1],              #ghost       13
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 1],                #dragon      14
              [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5, 1],            #dark        15
              [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 1]]          #steel       16

def getWeaknessMulti(type, enemy):
    attacking = -1
    defending1 = -1
    defending2 = -1
    if type == "NORMAL":
        attacking = 0
    if type == "FIRE":
        attacking = 1
    if type == "WATER":
        attacking = 2
    if type == "ELECTRIC":
        attacking = 3
    if type == "GRASS":
        attacking = 4
    if type == "ICE":
        attacking = 5
    if type == "FIGHTING":
        attacking = 6
    if type == "POISON":
        attacking = 7
    if type == "GROUND":
        attacking = 8
    if type == "FLYING":
        attacking = 9
    if type == "PSYCHIC":
        attacking = 10
    if type == "BUG":
        attacking = 11
    if type == "ROCK":
        attacking = 12
    if type == "GHOST":
        attacking = 13
    if type == "DRAGON":
        attacking = 14
    if type == "DARK":
        attacking = 15
    if type == "STEEL":
        attacking = 16

    if enemy.type1 == "NORMAL":
        defending1 = 0
    if enemy.type1 == "FIRE":
        defending1 = 1
    if enemy.type1 == "WATER":
        defending1 = 2
    if enemy.type1 == "ELECTRIC":
        defending1 = 3
    if enemy.type1 == "GRASS":
        defending1 = 4
    if enemy.type1 == "ICE":
        defending1 = 5
    if enemy.type1 == "FIGHTING":
        defending1 = 6
    if enemy.type1 == "POISON":
        defending1 = 7
    if enemy.type1 == "GROUND":
        defending1 = 8
    if enemy.type1 == "FLYING":
        defending1 = 9
    if enemy.type1 == "PSYCHIC":
        defending1 = 10
    if enemy.type1 == "BUG":
        defending1 = 11
    if enemy.type1 == "ROCK":
        defending1 = 12
    if enemy.type1 == "GHOST":
        defending1 = 13
    if enemy.type1 == "DRAGON":
        defending1 = 14
    if enemy.type1 == "DARK":
        defending1 = 15
    if enemy.type1 == "STEEL":
        defending1 = 16
    if enemy.type1 == "NONE":
        defending1 = 17

    if enemy.type2 == "NORMAL":
        defending2 = 0
    if enemy.type2 == "FIRE":
        defending2 = 1
    if enemy.type2 == "WATER":
        defending2 = 2
    if enemy.type2 == "ELECTRIC":
        defending2 = 3
    if enemy.type2 == "GRASS":
        defending2 = 4
    if enemy.type2 == "ICE":
        defending2 = 5
    if enemy.type2 == "FIGHTING":
        defending2 = 6
    if enemy.type2 == "POISON":
        defending2 = 7
    if enemy.type2 == "GROUND":
        defending2 = 8
    if enemy.type2 == "FLYING":
        defending2 = 9
    if enemy.type2 == "PSYCHIC":
        defending2 = 10
    if enemy.type2 == "BUG":
        defending2 = 11
    if enemy.type2 == "ROCK":
        defending2 = 12
    if enemy.type2 == "GHOST":
        defending2 = 13
    if enemy.type2 == "DRAGON":
        defending2 = 14
    if enemy.type2 == "DARK":
        defending2 = 15
    if enemy.type2 == "STEEL":
        defending2 = 16
    if enemy.type2 == "NONE":
        defending2 = 17

    return typeMatrix[attacking][defending1] * typeMatrix[attacking][defending2]

teamLists = [[pokemon1, pokemon1, pokemon1, pokemon1, pokemon1, pokemon1], [pokemon1, pokemon1, pokemon1, pokemon1, pokemon1, pokemon1]]

tempPokemon = [pokemon1, pokemon1]

messageList = [""]

moves = [-1, -1]

def regStageMulti(stage):
    if stage == -6:
        return 0.25
    elif stage == -5:
        return 2.0 / 7.0
    elif stage == -4:
        return 2.0 / 6.0
    elif stage == -3:
        return 2.0 / 5.0
    elif stage == -2:
        return 2.0 / 4.0
    elif stage == -1:
        return 2.0 / 3.0
    elif stage == 0:
        return 1.0
    elif stage == 1:
        return 3.0 / 2.0
    elif stage == 2:
        return 4.0 / 2.0
    elif stage == 3:
        return 5.0 / 2.0
    elif stage == 4:
        return 6.0 / 2.0
    elif stage == 5:
        return 7.0 / 2.0
    elif stage == 6:
        return 8.0 / 2.0
    return 0.0

def unlowerAtkStage(stage):
    if stage == -6:
        return 4
    elif stage == -5:
        return 7.0 / 2.0
    elif stage == -4:
        return 6.0 / 2.0
    elif stage == -3:
        return 5.0 / 2.0
    elif stage == -2:
        return 4.0 / 2.0
    elif stage == -1:
        return 3.0 / 2.0
    else:
        return 1.0

def unlowerDefStage(stage):
    if stage == 1:
        return 2.0 / 3.0
    elif stage == 2:
        return 2.0 / 4.0
    elif stage == 3:
        return 2.0 / 5.0
    elif stage == 4:
        return 2.0 / 6.0
    elif stage == 5:
        return 2.0 / 7.0
    elif stage == 6:
        return 2.0 / 8.0
    return 1.0

def stab(type, mon):
    if type == mon.type1 or type == mon.type2:
        return 1.5
    return 1.0

def accEvaStageMulti(stage):
    if stage <= -6:
        return 3.0 / 9.0
    elif stage == -5:
        return 3.0 / 8.0
    elif stage == -4:
        return 3.0 / 7.0
    elif stage == -3:
        return 3.0 / 5.0
    elif stage == -2:
        return 3.0 / 4.0
    elif stage == -1:
        return 3.0 / 3.0
    elif stage == 0:
        return 1.0
    elif stage == 1:
        return 4.0 / 3.0
    elif stage == 2:
        return 5.0 / 3.0
    elif stage == 3:
        return 6.0 / 3.0
    elif stage == 4:
        return 7.0 / 3.0
    elif stage == 5:
        return 8.0 / 3.0
    elif stage >= 6:
        return 9.0 / 3.0
    return 0.0

def critStageMulti(stage):
    if stage == 0:
        return 16.0
    if stage == 1:
        return 8.0
    if stage == 2:
        return 4.0
    if stage == 3:
        return 3.0
    if stage >= 4:
        return 2.0

def faint(mon):
    mon.setFainted(True)

def paralyzeMulti(mon):
    if mon.status == "PARALYZED":
        return 0.25
    else:
        return 1.0

def choiceScarfMulti(mon):
    if mon.item == "Choice Scarf":
        return 1.5
    return 1.0

def choiceBandMulti(mon):
    if mon.item == "Choice Band":
        return 1.5
    return 1.0

def choiceSpecsMulti(mon):
    if mon.item == "Choice Specs":
        return 1.5
    return 1.0

def burnMulti(mon):
    if mon.status == "BURNED" and mon.ability != "Guts":
        return 0.5
    else:
        return 1.0

readyForNextTurn = True

def monMove(monNum):
    oppMonNum = -1
    if monNum == 0:
        oppMonNum = 1
    elif monNum == 1:
        oppMonNum = 0

    if moves[monNum] > 4:
        messageList[0] += teamLists[monNum][0].nick + " switched out for " + teamLists[monNum][moves[monNum] - 4].nick + "!\n"
        tempPokemon[monNum] = teamLists[monNum][moves[monNum] - 4]
        teamLists[monNum][moves[monNum] - 4] = teamLists[monNum][0]
        teamLists[monNum][0] = tempPokemon[monNum]
        return

    teamOneMove = teamLists[monNum][0].getMove(moves[monNum])
    moveTemp = teamOneMove.replace(" ", "")
    moveTemp.replace("-", "")
    print(moveTemp)
    move1func = getattr(Pokemon, moveTemp)
    move1String = move1func(teamLists[monNum][0]).split("/")
    # "Prio/Type/statusPhysicalSpecial/pp/power/Acc/atkChange/defChange/spaChange/spdChange/speChange/accChange/evaChange/atkChangeOpp/defChangeOpp/spaChangeOpp/spdChangeOpp/speChangeOpp/accChangeOpp/evaChangeOpp/StatusSelf/StatusOpp/extraEffect/Contact/Charging/Recharge/protected/reflectable/snatchable/mirrorMove/punch/sound/noGrav/Defrosts/Heals/ignSub/powder/Jaw/pulse/ballistic/mental/Dance"
    try:
        power1 = float(move1String[4])
    except:
        power1 = 0

    if teamLists[monNum][0].fainted:
        return

    pp = 0
    if moves[monNum] == 1:
        pp = teamLists[monNum][0].move1currentPP
    if moves[monNum] == 2:
        pp = teamLists[monNum][0].move2currentPP
    if moves[monNum] == 3:
        pp = teamLists[monNum][0].move3currentPP
    if moves[monNum] == 4:
        pp = teamLists[monNum][0].move4currentPP

    moveType1 = move1String[1]
    level1 = teamLists[monNum][0].level
    attack1 = teamLists[monNum][0].startAtk * regStageMulti(teamLists[monNum][0].atkStage) * choiceBandMulti(teamLists[monNum][0])
    defense2 = teamLists[oppMonNum][0].startDef * regStageMulti(teamLists[oppMonNum][0].defStage)
    spattack1 = teamLists[monNum][0].startSpA * regStageMulti(teamLists[monNum][0].spaStage) * choiceSpecsMulti(teamLists[monNum][0])
    spdefense2 = teamLists[oppMonNum][0].startSpD * regStageMulti(teamLists[oppMonNum][0].spdStage)
    critical1 = 1
    superEffective = 1
    if random.randint(1, int(critStageMulti(teamLists[monNum][0].critStage))) == 1:
        critical1 = 2
        attack1 *= unlowerAtkStage(teamLists[monNum][0].atkStage)
        defense2 *= unlowerDefStage(teamLists[oppMonNum][0].defStage)
        spattack1 *= unlowerAtkStage(teamLists[monNum][0].spaStage)
        spdefense2 *= unlowerDefStage(teamLists[oppMonNum][0].spdStage)

    weather1 = 1
    # fix weather multi

    #paralyze check
    if teamLists[monNum][0].status == "PARALYZED":
        messageList[0] += teamLists[monNum][0].nick + " is paralyzed...\n"
        if random.randint(0,3) == 0:
            messageList[0] += teamLists[monNum][0].nick + " is unable to move!\n"
            return

    #miss check
    gravity = 1.0
    tangledFeet = 1.0
    hustle = 1.0
    sandVeil = 1.0
    snowCloak = 1.0
    victoryStar = 1.0
    compoundEyes = 1.0
    brightPowder = 1.0
    laxIncence = 1.0
    wideLens = 1.0
    zoomLens = 1.0

    miracleBerry = 1.0

    accModifier = gravity * tangledFeet * hustle * sandVeil * snowCloak * victoryStar * compoundEyes * brightPowder * laxIncence * wideLens * zoomLens

    moveAcc = -1
    try:
        moveAcc = int(move1String[5])
    except:
        pass

    totalAccEvaStage = teamLists[monNum][0].accStage - teamLists[oppMonNum][0].evaStage

    if moveAcc != -1:
        moddedAcc = moveAcc * accModifier * accEvaStageMulti(totalAccEvaStage) * miracleBerry
        if random.randint(1,100) > moddedAcc:
            messageList[0] += teamLists[monNum][0].nick + " used " + teamLists[monNum][0].getMove(moves[monNum]) + "!\n"
            messageList[0] += teamLists[monNum][0].nick + " missed!\n"
            return


    # damage calc pokemon1
    if move1String[2] == "Physical":
        #print(attack1)
        superEffective = getWeaknessMulti(moveType1, teamLists[oppMonNum][0])
        damage1 = ((((((2 * level1) / 5) + 2) * power1 * (attack1 / defense2)) / 50) + 2) * weather1 * critical1 * (float(random.randint(85, 100)) / 100.0) * stab(moveType1, teamLists[monNum][0]) * superEffective * burnMulti(teamLists[monNum][0])
        print(damage1)
        damage1 = int(damage1)

        newHP1 = teamLists[oppMonNum][0].currentHP - damage1
        messageList[0] += teamLists[monNum][0].nick + " used " + teamLists[monNum][0].getMove(moves[monNum]) + "! (-" + str(int(100 * damage1 / teamLists[oppMonNum][0].startHP)) + "%)"
        if superEffective > 1:
            messageList[0] += "\nIt was super effective!"
        elif superEffective == 0:
            messageList[0] += "\nIt doesnt effect " + teamLists[oppMonNum][0].nick + "..."
        elif superEffective < 1:
            messageList[0] += "\nIt wasn't very effective..."
        if critical1 > 1:
            messageList[0] += "\nCritical Hit!"
        messageList[0] += "\n"
        if newHP1 <= 0:
            newHP1 = 0
            teamLists[oppMonNum][0].setFainted(True)
            messageList[0] += teamLists[oppMonNum][0].nick + " Fainted!\n"

        teamLists[oppMonNum][0].setCurrentHP(newHP1)

    if move1String[2] == "Special":
        superEffective = getWeaknessMulti(moveType1, teamLists[oppMonNum][0])
        damage1 = ((((((2 * level1) / 5) + 2) * power1 * (spattack1 / spdefense2)) / 50) + 2) * weather1 * critical1 * \
                  (float(random.randint(85, 100)) / 100.0) * stab(moveType1, teamLists[monNum][0]) * superEffective
        damage1 = int(damage1)
        newHP1 = teamLists[oppMonNum][0].currentHP - damage1
        messageList[0] += teamLists[monNum][0].nick + " used " + teamLists[monNum][0].getMove(moves[monNum]) + "! (-" + str(int(100 * damage1 / teamLists[oppMonNum][0].startHP)) + "%)"
        if superEffective > 1:
            messageList[0] += "\nIt was super effective!"
        elif superEffective == 0:
            messageList[0] += "\nIt doesnt effect " + teamLists[oppMonNum][0].nick + "..."
        elif superEffective < 1:
            messageList[0] += "\nIt wasn't very effective..."
        if critical1 > 1:
            messageList[0] += "\nCritical Hit!"
        messageList[0] += "\n"
        if newHP1 <= 0:
            newHP1 = 0
            teamLists[oppMonNum][0].setFainted(True)
            messageList[0] += teamLists[oppMonNum][0].nick + " Fainted!\n"
        teamLists[oppMonNum][0].setCurrentHP(newHP1)

    if move1String[2] == "Status":
        messageList[0] += teamLists[monNum][0].nick + " used " + teamLists[monNum][0].getMove(moves[monNum]) + "!\n"

    # "Prio/Type/statusPhysicalSpecial/pp/power/Acc/atkChange/defChange/spaChange/spdChange/speChange/accChange/evaChange/critChange/atkChangeOpp/defChangeOpp/spaChangeOpp/spdChangeOpp/speChangeOpp/accChangeOpp/evaChangeOpp/critChangeOpp/StatusSelf/StatusOpp/extraEffect/Contact/Charging/Recharge/protected/reflectable/snatchable/mirrorMove/punch/sound/noGrav/Defrosts/Heals/ignSub/powder/Jaw/pulse/ballistic/mental/Dance"

    statString = ""

    #stat changes
    for i in range (6, 14):
        if i == 6:
            statString = "Attack"
        if i == 7:
            statString = "Defense"
        if i == 8:
            statString = "Special Attack"
        if i == 9:
            statString = "Special Defense"
        if i == 10:
            statString = "Speed"
        if i == 11:
            statString = "Accuracy"
        if i == 12:
            statString = "Evasiveness"
        if i == 13:
            statString = "Crit Rate"

        if int(move1String[i]) <= -3:
            messageList[0] += teamLists[monNum][0].nick + "'s " + statString + " severely fell!\n"
        elif int(move1String[i]) == -2:
            messageList[0] += teamLists[monNum][0].nick + "'s " + statString + " harshly fell!\n"
        elif int(move1String[i]) == -1:
            messageList[0] += teamLists[monNum][0].nick + "'s " + statString + " fell!\n"
        elif int(move1String[i]) == 1:
            messageList[0] += teamLists[monNum][0].nick + "'s " + statString + " rose!\n"
        elif int(move1String[i]) == 2:
            messageList[0] += teamLists[monNum][0].nick + "'s " + statString + " sharply rose!\n"
        elif int(move1String[i]) == 3:
            messageList[0] += teamLists[monNum][0].nick + "'s " + statString + " rose drastically!\n"

        teamLists[monNum][0].changeStage(i - 5, int(move1String[i]))

    for i in range (14, 22):
        if i == 14:
            statString = "Attack"
        if i == 15:
            statString = "Defense"
        if i == 16:
            statString = "Special Attack"
        if i == 17:
            statString = "Special Defense"
        if i == 18:
            statString = "Speed"
        if i == 19:
            statString = "Accuracy"
        if i == 20:
            statString = "Evasiveness"
        if i == 21:
            statString = "Crit Rate"

        if int(move1String[i]) <= -3:
            messageList[0] += teamLists[oppMonNum][0].nick + "'s " + statString + " severely fell!\n"
        elif int(move1String[i]) == -2:
            messageList[0] += teamLists[oppMonNum][0].nick + "'s " + statString + " harshly fell!\n"
        elif int(move1String[i]) == -1:
            messageList[0] += teamLists[oppMonNum][0].nick + "'s " + statString + " fell!\n"
        elif int(move1String[i]) == 1:
            messageList[0] += teamLists[oppMonNum][0].nick + "'s " + statString + " rose!\n"
        elif int(move1String[i]) == 2:
            messageList[0] += teamLists[oppMonNum][0].nick + "'s " + statString + " sharply rose!\n"
        elif int(move1String[i]) == 3:
            messageList[0] += teamLists[oppMonNum][0].nick + "'s " + statString + " rose drastically!\n"

        teamLists[oppMonNum][0].changeStage(i - 13, int(move1String[i]))

    if move1String[22] != "-":
        if move1String[22] == "BURNED" or move1String[22] == "TOXIC" or move1String[22] == "POISONED" or move1String[22] == "FROZEN" or move1String[22] == "PARALYZED" or move1String[22] == "ASLEEP":
            if teamLists[monNum][0].status == "BURNED" or teamLists[monNum][0].status == "TOXIC" or teamLists[monNum][0].status == "POISONED" or teamLists[monNum][0].status == "FROZEN" or teamLists[monNum][0].status == "PARALYZED" or teamLists[monNum][0].status == "ASLEEP":
                #code for display failure
                messageList[0] += teamLists[monNum][0].nick + " is already affected by a status condition! (" + teamLists[monNum][0].status + ")\n"
            else:
                teamLists[monNum][0].setStatus(move1String[22])
                messageList[0] += teamLists[monNum][0].nick + " has been " + teamLists[monNum][0].status + "!\n"

    if move1String[23] != "-":
        if move1String[23] == "BURNED" or move1String[23] == "TOXIC" or move1String[23] == "POISONED" or move1String[23] == "FROZEN" or move1String[23] == "PARALYZED" or move1String[23] == "ASLEEP":
            if teamLists[oppMonNum][0].status == "BURNED" or teamLists[oppMonNum][0].status == "TOXIC" or teamLists[oppMonNum][0].status == "POISONED" or teamLists[oppMonNum][0].status == "FROZEN" or teamLists[oppMonNum][0].status == "PARALYZED" or teamLists[oppMonNum][0].status == "ASLEEP":
                # code for display failure
                messageList[0] += teamLists[oppMonNum][0].nick + " is already affected by a status condition! (" + teamLists[oppMonNum][0].status + ")\n"
            else:
                teamLists[oppMonNum][0].setStatus(move1String[23])
                messageList[0] += teamLists[oppMonNum][0].nick + " has been " + teamLists[oppMonNum][0].status + "!\n"
    '''
    if moves[monNum] == 1:
        teamLists[monNum][0].setCurrentPP1(pp - 1)
    if moves[monNum] == 2:
        teamLists[monNum][0].setCurrentPP2(pp - 1)
    if moves[monNum] == 3:
        teamLists[monNum][0].setCurrentPP3(pp - 1)
    if moves[monNum] == 4:
        teamLists[monNum][0].setCurrentPP4(pp - 1)
    '''

    print(messageList[0])
    # CODE A DELAY AND A DISPLAY HERE!
    #pygame.time.delay(2000)

def turn(playerNum):
    if playerNum == 1:
        return

    messageList[0] = ""

    if teamLists[0][0].fainted and moves[0] < 5:
        return
    if teamLists[1][0].fainted and moves[1] < 5:
        return

    teamOneMovePrio = 0
    teamTwoMovePrio = 0
    teamOneGoFirst = False
    teamTwoGoFirst = False
    #set priority for order of moves
    if moves[0] > 4:
        teamOneMovePrio = 6
    else:
        teamOneMovePrio = teamLists[0][0].getMovePrio(moves[0])
    if moves[1] > 4:
        teamTwoMovePrio = 6
    else:
        teamTwoMovePrio = teamLists[1][0].getMovePrio(moves[1])
    #pursuit
    #code will go here

    if teamOneMovePrio > teamTwoMovePrio:
        teamOneGoFirst = True
    elif teamTwoMovePrio > teamOneMovePrio:
        teamTwoGoFirst = True
    else:
        #same priority, go to speed check
        teamOneCurrentSpe = teamLists[0][0].startSpe * regStageMulti(teamLists[0][0].speStage) * paralyzeMulti(teamLists[0][0]) * choiceScarfMulti(teamLists[0][0])
        teamTwoCurrentSpe = teamLists[1][0].startSpe * regStageMulti(teamLists[1][0].speStage) * paralyzeMulti(teamLists[1][0]) * choiceScarfMulti(teamLists[1][0])
        if teamTwoCurrentSpe > teamOneCurrentSpe:
            teamTwoGoFirst = True
        elif teamOneCurrentSpe > teamTwoCurrentSpe:
            teamOneGoFirst = True

    if teamTwoGoFirst == False and teamOneGoFirst == False:
        if random.randint(0,1) == 0:
            teamOneGoFirst = True
        else:
            teamTwoGoFirst = True

    readyForNextTurn = False

    #if a pokemon is fainted
    if teamLists[0][0].fainted and teamLists[1][0].fainted:
        monMove(0)
        monMove(1)
        return
    elif teamLists[0][0].fainted:
        monMove(0)
        return
    elif teamLists[1][0].fainted:
        monMove(1)
        return

    if teamOneGoFirst:
        print("team one will go first")
    elif teamTwoGoFirst:
        print("team two will go first")

    damage1 = 0
    damage2 = 0

    if teamOneGoFirst:
        monMove(0)
        monMove(1)

    elif teamTwoGoFirst:
        monMove(1)
        monMove(0)

    #if team
    #print(teamsStringCombine(teamString(teamLists[0]), teamString(teamLists[1])))

    #add all end of turn effects here

def threaded_client(conn, playerNum):
    conn.send(str.encode("player " + str(playerNum) + " connected"))
    '''
    try:
        if playerNum == 0:
            print(teamString(teamLists[0]))
            conn.send(str.encode(teamsStringCombine(teamString(teamLists[0]), teamString(teamLists[1]))))

        else:
            conn.send(str.encode(teamsStringCombine(teamString(teamLists[1]), teamString(teamLists[0]))))
    except:
        pass
    '''
    reply = ""

    while True:
        try:
            #print("hello world")
            data = conn.recv(4096).decode()
            #print(playerNum)
            #print(data)
            if data == "1" or data == "2" or data == "3" or data == "4" or data == "5" or data == "6" or data == "7" or data == "8" or data == "9" or data == "-1":
                moves[playerNum] = int(data)
                #print(moves)
            elif playerNum == 0:
                teamLists[0] = teamUnstring(data)
            elif playerNum == 1:
                teamLists[1] = teamUnstring(data)
            #print(data)

            '''
            
            if teamLists[0][0].fainted == True:
                readyForNextTurn = False
                if moves[0] > 4:
                    readyForNextTurn = True
            if teamLists[1][0].fainted == True:
                readyForNextTurn = False
                if moves[1] > 4:
                    readyForNextTurn = True
            
            '''

            if moves[0] != -1 and moves[1] != -1 and readyForNextTurn:
                turn(playerNum)

            if teamLists[0][0].status == "BURNED":
                messageList[0] += teamLists[0][0].nick + "was hurt by its burn!\n"
                teamLists[0][0].currentHP = teamLists[0][0].currentHP - (teamLists[0][0].startHP / 8)
                if teamLists[0][0].currentHP <= 0:
                    teamLists[0][0].currentHP = 0
                    messageList[0] += teamLists[0][0].nick + " fainted!\n"
                    teamLists[0][0].fainted = True

            if teamLists[1][0].status == "BURNED":
                messageList[0] += teamLists[1][0].nick + "was hurt by its burn!\n"
                teamLists[1][0].currentHP = teamLists[1][0].currentHP - (teamLists[1][0].startHP / 8)
                if teamLists[1][0].currentHP <= 0:
                    teamLists[1][0].currentHP = 0
                    messageList[0] += teamLists[1][0].nick + " fainted!\n"
                    teamLists[1][0].fainted = True

            if teamLists[0][0].status == "POISONED":
                messageList[0] += teamLists[0][0].nick + "was hurt by its poison!\n"

            if teamLists[1][0].status == "POISONED":
                messageList[0] += teamLists[1][0].nick + "was hurt by its poison!\n"

            if teamLists[0][0].status == "TOXIC":
                messageList[0] += teamLists[0][0].nick + "was hurt by its poison!\n"

            if teamLists[1][0].status == "TOXIC":
                messageList[0] += teamLists[1][0].nick + "was hurt by its poison!\n"

            #if no info received from client, disconnect
            '''
            if not data:
                print("Disconnected")
                break
            else:
                if playerNum == 0:
                    reply = teamsStringCombine(teamString(teamLists[0]), teamString(teamLists[1]))
                else:
                    reply = teamsStringCombine(teamString(teamLists2[0]), teamString(teamLists2[1]))
            '''

            if playerNum == 0:
                reply = teamsStringCombine(teamsStringCombine(teamString(teamLists[0]), teamString(teamLists[1])), messageList[0])
            elif playerNum == 1:
                reply = teamsStringCombine(teamsStringCombine(teamString(teamLists[1]), teamString(teamLists[0])), messageList[0])

            conn.sendall(str.encode(reply))

        except:
            print("error?")
            break

    print("Lost Connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    print(currentPlayer)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1