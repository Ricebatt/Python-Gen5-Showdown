import socket
#import pygame
from _thread import *
from pokemon import *
#import sys

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

    print(typeMatrix[attacking][defending1])
    print(typeMatrix[attacking][defending2])

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
    if stage == -6:
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
    elif stage == 6:
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

def mon1Move(teamOneActive, movesList, teamTwoActive):

    if movesList[0] > 4:
        messageList[0] += teamLists[0][0].nick + " switched out for " + teamLists[0][movesList[0] - 4].nick + "!\n"
        print(messageList[0])
        tempPokemon[0] = teamLists[0][movesList[0] - 4]
        teamLists[0][movesList[0] - 4] = teamLists[0][0]
        teamLists[0][0] = tempPokemon[0]

        return
    teamOneMove = teamOneActive.getMove(movesList[0])
    move1Temp = teamOneMove.replace(" ", "")
    move1Temp.replace("-", "")
    move1func = getattr(Pokemon, move1Temp)
    move1String = move1func(teamOneActive).split("/")
    # "Prio/Type/statusPhysicalSpecial/pp/power/Acc/atkChange/defChange/spaChange/spdChange/speChange/accChange/evaChange/atkChangeOpp/defChangeOpp/spaChangeOpp/spdChangeOpp/speChangeOpp/accChangeOpp/evaChangeOpp/StatusSelf/StatusOpp/extraEffect/Contact/Charging/Recharge/protected/reflectable/snatchable/mirrorMove/punch/sound/noGrav/Defrosts/Heals/ignSub/powder/Jaw/pulse/ballistic/mental/Dance"
    power1 = float(move1String[4])

    moveType1 = move1String[1]
    level1 = teamOneActive.level
    # stab1 = 1.0
    attack1 = teamOneActive.startAtk * regStageMulti(teamOneActive.atkStage) * choiceBandMulti(teamOneActive)
    defense2 = teamTwoActive.startDef * regStageMulti(teamTwoActive.defStage)
    spattack1 = teamOneActive.startSpA * regStageMulti(teamOneActive.spaStage) * choiceSpecsMulti(teamOneActive)
    spdefense2 = teamTwoActive.startSpD * regStageMulti(teamTwoActive.spdStage)
    critical1 = 1
    superEffective = 1
    if random.randint(1, int(critStageMulti(teamOneActive.critStage))) == 1:
        critical1 = 2
        attack1 *= unlowerAtkStage(teamOneActive.atkStage)
        defense2 *= unlowerDefStage(teamTwoActive.defStage)
        spattack1 *= unlowerAtkStage(teamOneActive.spaStage)
        spdefense2 *= unlowerDefStage(teamTwoActive.spdStage)

    weather1 = 1
    # fix weather multi

    # miss checks needed

    # damage calc pokemon1
    if move1String[2] == "Physical":
        #print("physical attack")
        '''
        print(str(level1))
        print(str(power1))
        print(str(attack1))
        print(str(defense2))
        print(str(weather1))
        print(str(critical1))
        print(str(stab(moveType1, teamOneActive)))

        print(str(getWeaknessMulti(moveType1, teamTwoActive)))
        print(str(burnMulti(teamOneActive)))
        '''
        superEffective = getWeaknessMulti(moveType1, teamTwoActive)
        damage1 = ((((((2 * level1) / 5) + 2) * power1 + (attack1 / defense2)) / 50) + 2) * weather1 * critical1 * \
                  (float(random.randint(85, 100)) / 100.0) * stab(moveType1, teamOneActive) * superEffective * \
                  burnMulti(teamOneActive)
        damage1 = int(damage1)

        # print(str(damage1))
        # print(str(teamTwoActive.currentHP))
        newHP1 = teamTwoActive.currentHP - damage1
        messageList[0] += teamOneActive.nick + " used " + teamOneActive.getMove(movesList[0]) + "! (-" + str(int(100 * damage1 / teamTwoActive.startHP)) + "%)"
        if superEffective > 1:
            messageList[0] += "\nIt was super effective!"
        elif superEffective == 0:
            messageList[0] += "\nIt doesnt effect " + teamTwoActive.nick + "..."
        elif superEffective < 1:
            messageList[0] += "\nIt wasn't very effective..."
        if critical1 > 1:
            messageList[0] += "\nCritical Hit!"
        messageList[0] += "\n"
        if newHP1 <= 0:
            newHP1 = 0
            teamTwoActive.setFainted(True)
            messageList[0] += teamTwoActive.nick + " Fainted!\n"
        # print(newHP1)
        teamTwoActive.setCurrentHP(newHP1)
        print("team two takes physical damage")

    if move1String[2] == "Special":
        superEffective = getWeaknessMulti(moveType1, teamTwoActive)
        damage1 = ((((((2 * level1) / 5) + 2) * power1 + (spattack1 / spdefense2)) / 50) + 2) * weather1 * critical1 * \
                  (float(random.randint(85, 100)) / 100.0) * stab(moveType1, teamOneActive) * superEffective
        damage1 = int(damage1)
        newHP1 = teamTwoActive.currentHP - damage1
        messageList[0] += teamOneActive.nick + " used " + teamOneActive.getMove(movesList[0]) + "! (-" + str(int(100 * damage1 / teamTwoActive.startHP)) + "%)"
        if superEffective > 1:
            messageList[0] += "\nIt was super effective!"
        elif superEffective == 0:
            messageList[0] += "\nIt doesnt effect " + teamTwoActive.nick + "..."
        elif superEffective < 1:
            messageList[0] += "\nIt wasn't very effective..."
        if critical1 > 1:
            messageList[0] += "\nCritical Hit!"
        messageList[0] += "\n"
        if newHP1 <= 0:
            newHP1 = 0
            teamTwoActive.setFainted(True)
            messageList[0] += teamTwoActive.nick + " Fainted!\n"
        teamTwoActive.setCurrentHP(newHP1)
        print("team two takes special damage")

    if move1String[2] == "Status":
        pass

    # "Prio/Type/statusPhysicalSpecial/pp/power/Acc/atkChange/defChange/spaChange/spdChange/speChange/accChange/evaChange/critChange/atkChangeOpp/defChangeOpp/spaChangeOpp/spdChangeOpp/speChangeOpp/accChangeOpp/evaChangeOpp/critChangeOpp/StatusSelf/StatusOpp/extraEffect/Contact/Charging/Recharge/protected/reflectable/snatchable/mirrorMove/punch/sound/noGrav/Defrosts/Heals/ignSub/powder/Jaw/pulse/ballistic/mental/Dance"
    '''
    #stat changes
    for i in range(6, 22):
        if i == 6:
            teamOneActive.changeStage(1, move1String[i])
        if i == 7:
            teamOneActive.changeStage(2, move1String[i])
        if i == 8:
            teamOneActive.changeStage(3, move1String[i])
        if i == 9:
            teamOneActive.changeStage(4, move1String[i])
        if i == 10:
            teamOneActive.changeStage(5, move1String[i])
        if i == 11:
            teamOneActive.changeStage(6, move1String[i])
        if i == 12:
            teamOneActive.changeStage(7, move1String[i])
        if i == 13:
            teamOneActive.changeStage(8, move1String[i])
        if i == 14:
            teamTwoActive.changeStage(1, move1String[i])
        if i == 15:
            teamTwoActive.changeStage(2, move1String[i])
        if i == 16:
            teamTwoActive.changeStage(3, move1String[i])
        if i == 17:
            teamTwoActive.changeStage(4, move1String[i])
        if i == 18:
            teamTwoActive.changeStage(5, move1String[i])
        if i == 19:
            teamTwoActive.changeStage(6, move1String[i])
        if i == 20:
            teamTwoActive.changeStage(7, move1String[i])
        if i == 21:
            teamTwoActive.changeStage(8, move1String[i])



    if move1String[22] != "-":
        if move1String[22] == "BURNED" or move1String[22] == "TOXIC" or move1String[22] == "POISIONED" or move1String[22] == "FROZEN" or move1String[22] == "PARALYZED":
            if teamOneActive.status == "BURNED" or teamOneActive.status == "TOXIC" or teamOneActive.status == "POISIONED" or teamOneActive.status == "FROZEN" or teamOneActive.status == "PARALYZED":
                #code for display failure
                pass
            else:
                teamOneActive.setStatus(move1String[22])

    if move1String[23] != "-":
        if move1String[23] == "BURNED" or move1String[23] == "TOXIC" or move1String[23] == "POISIONED" or \
                move1String[23] == "FROZEN" or move1String[23] == "PARALYZED":
            if teamTwoActive.status == "BURNED" or teamTwoActive.status == "TOXIC" or teamTwoActive.status == "POISIONED" or teamTwoActive.status == "FROZEN" or teamTwoActive.status == "PARALYZED":
                # code for display failure (cant status statused target)
                pass
            else:
                teamTwoActive.setStatus(move1String[22])
    '''
    print(messageList[0])
    # CODE A DELAY AND A DISPLAY HERE!
    #pygame.time.delay(2000)

def mon2Move(teamOneActive, movesList, teamTwoActive):

    if movesList[1] > 4:
        messageList[0] += teamLists[1][0].nick + " switched out for " + teamLists[1][movesList[1] - 4].nick + "!\n"
        print(messageList[0])
        tempPokemon[1] = teamLists[1][movesList[1] - 4]
        teamLists[1][movesList[1] - 4] = teamLists[1][0]
        teamLists[1][0] = tempPokemon[1]
        return

    teamTwoMove = teamTwoActive.getMove(movesList[1])
    #print("here")

    move2temp = teamTwoMove.replace(" ", "")
    move2temp.replace("-", "")
    print(move2temp)
    move2func = getattr(Pokemon, move2temp)
    move2String = move2func(teamTwoActive).split("/")
    # "Prio/Type/statusPhysicalSpecial/pp/power/Acc/atkChange/defChange/spaChange/spdChange/speChange/accChange/evaChange/atkChangeOpp/defChangeOpp/spaChangeOpp/spdChangeOpp/speChangeOpp/accChangeOpp/evaChangeOpp/StatusSelf/StatusOpp/extraEffect/Contact/Charging/Recharge/protected/reflectable/snatchable/mirrorMove/punch/sound/noGrav/Defrosts/Heals/ignSub/powder/Jaw/pulse/ballistic/mental/Dance"
    power2 = float(move2String[4])
    moveType2 = move2String[1]
    level2 = teamTwoActive.level
    # stab2 = 1.0
    attack2 = teamTwoActive.startAtk * regStageMulti(teamTwoActive.atkStage) * choiceBandMulti(teamTwoActive)
    defense1 = teamOneActive.startDef * regStageMulti(teamOneActive.defStage)
    spattack2 = teamTwoActive.startSpA * regStageMulti(teamTwoActive.spaStage) * choiceSpecsMulti(teamTwoActive)
    spdefense1 = teamOneActive.startSpD * regStageMulti(teamOneActive.spdStage)
    critical2 = 1
    superEffective = 1

    if random.randint(1, int(critStageMulti(teamTwoActive.critStage))) == 1:
        critical2 = 2
        attack2 *= unlowerAtkStage(teamTwoActive.atkStage)
        defense1 *= unlowerDefStage(teamOneActive.defStage)
        spattack2 *= unlowerAtkStage(teamTwoActive.spaStage)
        spdefense1 *= unlowerDefStage(teamOneActive.spdStage)

    weather2 = 1
    # fix weather multi

    # miss checks needed

    # damage calc pokemon1
    if move2String[2] == "Physical":
        '''
        print(str(level2))
        print(str(power2))
        print(str(attack2))
        print(str(defense1))
        print(str(weather2))
        print(str(critical2))
        print(str(stab(moveType2, teamTwoActive)))

        print(str(getWeaknessMulti(moveType1, teamTwoActive)))
        print(str(burnMulti(teamOneActive)))
        '''
        superEffective = getWeaknessMulti(moveType2, teamOneActive)
        damage2 = ((((((2 * level2) / 5) + 2) * power2 + (attack2 / defense1)) / 50) + 2) * weather2 * critical2 * \
                  (float(random.randint(85, 100)) / 100.0) * stab(moveType2, teamTwoActive) * superEffective * \
                  burnMulti(teamTwoActive)
        damage2 = int(damage2)
        newHP2 = teamOneActive.currentHP - damage2
        messageList[0] += teamTwoActive.nick + " used " + teamTwoActive.getMove(movesList[1]) + "! (-" + str(int(100 * damage2 / teamOneActive.startHP)) + "%)"
        if superEffective > 1:
            messageList[0] += "\nIt was super effective!"
        elif superEffective == 0:
            messageList[0] += "\nIt doesnt effect " + teamOneActive.nick + "..."
        elif superEffective < 1:
            messageList[0] += "\nIt wasn't very effective..."
        if critical2 > 1:
            messageList[0] += "\nCritical Hit!"
        messageList[0] += "\n"
        if newHP2 <= 0:
            newHP2 = 0
            teamOneActive.setFainted(True)
            messageList[0] += teamOneActive.nick + " Fainted!\n"
        teamOneActive.setCurrentHP(newHP2)
        print("team one takes physical damage")

    if move2String[2] == "Special":
        superEffective = getWeaknessMulti(moveType2, teamOneActive)
        damage2 = ((((((2 * level2) / 5) + 2) * power2 + (
                spattack2 / spdefense1)) / 50) + 2) * weather2 * critical2 * \
                  (float(random.randint(85, 100)) / 100.0) * stab(moveType2, teamTwoActive) * superEffective
        newHP2 = teamOneActive.currentHP - damage2
        messageList[0] += teamTwoActive.nick + " used " + teamTwoActive.getMove(movesList[1]) + "! (-" + str(
            int(100 * damage2 / teamOneActive.startHP)) + "%)"
        if superEffective > 1:
            messageList[0] += "\nIt was super effective!"
        elif superEffective == 0:
            messageList[0] += "\nIt doesnt effect " + teamOneActive.nick + "..."
        elif superEffective < 1:
            messageList[0] += "\nIt wasn't very effective..."
        if critical2 > 1:
            messageList[0] += "\nCritical Hit!"
        messageList[0] += "\n"
        if newHP2 <= 0:
            newHP2 = 0
            teamOneActive.setFainted(True)
            messageList[0] += teamOneActive.nick + " Fainted!\n"
        teamOneActive.setCurrentHP(newHP2)
        print("team one takes special damage")

    if move2String[2] == "Status":
        pass

    # "Prio/Type/statusPhysicalSpecial/pp/power/Acc/atkChange/defChange/spaChange/spdChange/speChange/accChange/evaChange/critChange/atkChangeOpp/defChangeOpp/spaChangeOpp/spdChangeOpp/speChangeOpp/accChangeOpp/evaChangeOpp/critChangeOpp/StatusSelf/StatusOpp/extraEffect/Contact/Charging/Recharge/protected/reflectable/snatchable/mirrorMove/punch/sound/noGrav/Defrosts/Heals/ignSub/powder/Jaw/pulse/ballistic/mental/Dance"

    # stat changes
    '''
    for i in range(6, 22):
        if i == 6:
            teamTwoActive.changeStage(1, move2String[i])
        if i == 7:
            teamTwoActive.changeStage(2, move2String[i])
        if i == 8:
            teamTwoActive.changeStage(3, move2String[i])
        if i == 9:
            teamTwoActive.changeStage(4, move2String[i])
        if i == 10:
            teamTwoActive.changeStage(5, move2String[i])
        if i == 11:
            teamTwoActive.changeStage(6, move2String[i])
        if i == 12:
            teamTwoActive.changeStage(7, move2String[i])
        if i == 13:
            teamTwoActive.changeStage(8, move2String[i])
        if i == 14:
            teamOneActive.changeStage(1, move2String[i])
        if i == 15:
            teamOneActive.changeStage(2, move2String[i])
        if i == 16:
            teamOneActive.changeStage(3, move2String[i])
        if i == 17:
            teamOneActive.changeStage(4, move2String[i])
        if i == 18:
            teamOneActive.changeStage(5, move2String[i])
        if i == 19:
            teamOneActive.changeStage(6, move2String[i])
        if i == 20:
            teamOneActive.changeStage(7, move2String[i])
        if i == 21:
            teamOneActive.changeStage(8, move2String[i])

    if move2String[22] != "-":
        if move2String[22] == "BURNED" or move2String[22] == "TOXIC" or move2String[22] == "POISIONED" or \
                move2String[22] == "FROZEN" or move2String[22] == "PARALYZED":
            if teamTwoActive.status == "BURNED" or teamTwoActive.status == "TOXIC" or teamTwoActive.status == "POISIONED" or teamTwoActive.status == "FROZEN" or teamTwoActive.status == "PARALYZED":
                # code for display failure
                pass
            else:
                teamTwoActive.setStatus(move2String[22])

    if move2String[23] != "-":
        if move2String[23] == "BURNED" or move2String[23] == "TOXIC" or move2String[23] == "POISIONED" or \
                move2String[23] == "FROZEN" or move2String[23] == "PARALYZED":
            if teamOneActive.status == "BURNED" or teamOneActive.status == "TOXIC" or teamOneActive.status == "POISIONED" or teamOneActive.status == "FROZEN" or teamOneActive.status == "PARALYZED":
                # code for display failure
                pass
            else:
                teamOneActive.setStatus(move2String[22])

    '''
    # CODE A DELAY AND A DISPLAY HERE!
    #pygame.time.delay(2000)
    print(messageList[0])

def turn(movesList, playerNum):
    if playerNum == 1:
        return

    messageList[0] = ""
    teamOneActive = teamLists[0][0]
    teamTwoActive = teamLists[1][0]

    if teamOneActive.fainted and movesList[0] < 5:
        return
    if teamTwoActive.fainted and movesList[1] < 5:
        return

    teamOneMovePrio = 0
    teamTwoMovePrio = 0
    teamOneGoFirst = False
    teamTwoGoFirst = False
    #set priority for order of moves
    if movesList[0] > 4:
        teamOneMovePrio = 6
    else:
        teamOneMovePrio = teamOneActive.getMovePrio(movesList[0])
    if movesList[1] > 4:
        teamTwoMovePrio = 6
    else:
        teamTwoMovePrio = teamTwoActive.getMovePrio(movesList[1])
    #pursuit
    #code will go here

    if teamOneMovePrio > teamTwoMovePrio:
        teamOneGoFirst = True
    elif teamTwoMovePrio > teamOneMovePrio:
        teamTwoGoFirst = True
    else:
        #same priority, go to speed check
        teamOneCurrentSpe = teamOneActive.startSpe * regStageMulti(teamOneActive.speStage) * paralyzeMulti(teamOneActive) * choiceScarfMulti(teamOneActive)
        teamTwoCurrentSpe = teamTwoActive.startSpe * regStageMulti(teamTwoActive.speStage) * paralyzeMulti(teamTwoActive) * choiceScarfMulti(teamTwoActive)
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

    if teamOneGoFirst:
        print("team one will go first")
    elif teamTwoGoFirst:
        print("team two will go first")

    damage1 = 0
    damage2 = 0

    if teamOneGoFirst:
        #first mon move
        '''if movesList[0] < 5:
            displayText += teamOneActive.nick + " used " + teamOneActive.getMove(movesList[0]) + "!\n"
        else:
            displayText += teamOneActive.nick + " switched out to " + teamLists[0][movesList[movesList[0] - 4]].nick + "!\n"'''
        mon1Move(teamOneActive, movesList, teamTwoActive)

        teamOneActive = teamLists[0][0]
        teamTwoActive = teamLists[1][0]

        #second mon move
        #displayText += teamTwoActive.nick + " used " + teamTwoActive.getMove(movesList[1]) + "!\n"
        mon2Move(teamOneActive, movesList, teamTwoActive)

    elif teamTwoGoFirst:
        # second mon move
        '''if movesList[0] < 5:
            displayText += teamTwoActive.nick + " used " + teamTwoActive.getMove(movesList[1]) + "!\n"
        else:
            displayText += teamTwoActive.nick + " switched out to " + teamLists[1][movesList[movesList[1] - 4]].nick + "!\n"'''

        mon2Move(teamOneActive, movesList, teamTwoActive)

        teamOneActive = teamLists[0][0]
        teamTwoActive = teamLists[1][0]

        #first mon move
        #displayText += teamOneActive.nick + " used " + teamOneActive.getMove(movesList[0]) + "!\n"
        mon1Move(teamOneActive, movesList, teamTwoActive)


    #if team
    #print(teamsStringCombine(teamString(teamLists[0]), teamString(teamLists[1])))

    #add all end of turn effects here
    '''
    if playerNum == 0:
        teamLists[0][0] = teamOneActive
        teamLists[1][0] = teamTwoActive
    else:
        teamLists2[0][0] = teamOneActive
        teamLists2[1][0] = teamTwoActive
    '''

    #print(teamsStringCombine(teamString(teamLists[0]), teamString(teamLists[1])))

    # CODE A DELAY AND A DISPLAY HERE!
    #pygame.time.delay(2000)


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
    #print("hello world")
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

                turn(moves, playerNum)
                #print("ready for turn")


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

                #print("Received: ", data)
                #print("Sending : ", reply)

            conn.sendall(str.encode(reply))

            #print("error before here?")
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