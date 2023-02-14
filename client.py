import pygame
import os
import sys
from network import Network
from pokemon import *


pygame.font.init()

width = 1000
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("ShowDown!")

clientNumber = 0

#print(sys.path[0])

class textBox:
    def __init__(self):
        self.text = []
        self.x = 500
        self.y = 0
        self.width = 500
        self.height = 700

    def setText(self, newText):
        self.text = newText.split('\n')

    def draw(self, win):
        pygame.draw.rect(win, pygame.Color(0,0,0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, pygame.Color(255,255,255), (self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        font = pygame.font.SysFont("calibri", 20)
        i = 0
        for line in self.text:

            text = font.render(line, True, (0,0,0))
            win.blit(text, (self.x + 5, self.y + i + 5))
            i += 20

class Button:
    def __init__(self):
        self.text = ""
        self.x = 0
        self.y = 0
        self.color = 0
        self.width = 220
        self.height = 70
        self.selected = False

    def setX(self, newX):
        self.x = newX

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def setY(self, newY):
        self.y = newY

    def setColor(self, newColor):
        self.color = newColor

    def setText(self, newText):
        self.text = newText

    def draw(self, win):
        pygame.draw.rect(win, pygame.Color(0,0,0), (self.x, self.y, self.width, self.height))
        if self.selected:
            pygame.draw.rect(win, pygame.Color(150, 150, 150), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.color, (self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        font = pygame.font.SysFont("calibri", 20)
        text = font.render(self.text, True, (0,0,0))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

class SwitchButton:
    def __init__(self):
        self.mon = Pokemon()
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.selected = False

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def setColor(self, newColor):
        self.color = newColor

    def setPokemon(self, mon):
        self.mon = mon

    def draw(self, win):
        pygame.draw.rect(win, pygame.Color(0,0,0), (self.x, self.y, self.width, self.height))
        if self.selected:
            pygame.draw.rect(win, pygame.Color(150, 150, 150), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, pygame.Color(255, 255, 255), (self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        if self.mon.getDex == -1:
            return
        dexNo = str(self.mon.getDex())
        if self.mon.getShiny():
            if self.mon.getGender() == "F":
                try:
                    activePokemon = pygame.image.load(
                        sys.path[0] + r"\\black-white\\shiny\\female\\" + dexNo + ".png")
                except:
                    activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\shiny\\" + dexNo + ".png")
            else:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\shiny\\" + dexNo + ".png")
        else:
            if self.mon.getGender() == "F":
                try:
                    activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\female\\" + dexNo + ".png")
                except:
                    activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\" + dexNo + ".png")
            else:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\" + dexNo + ".png")
        activePokemon = pygame.transform.scale(activePokemon, (75, 75))

        pygame.draw.rect(win, pygame.Color(255, 0, 0), (100, 200, 200, 10))
        pygame.draw.rect(win, pygame.Color(0, 255, 0), (100, 200, (float(self.mon.currentHP) / float(self.mon.startHP)) * 200, 10))

        if self.mon.fainted == True:
            activePokemon = pygame.transform.rotate(activePokemon, 90)

        win.blit(activePokemon, (self.x - 13, self.y - 13))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height and not self.mon.fainted and self.mon.dexName != "NOPOKEMON":
            return True
        else:
            return False

class JustText:
    def __init__(self):
        self.text = ""
        self.x = 0
        self.y = 0
        self.color = 0
        self.width = 220
        self.height = 70

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def setColor(self, newColor):
        self.color = newColor

    def setText(self, newText):
        self.text = newText

    def draw(self, win):
        #pygame.draw.rect(win, pygame.Color(0,0,0), (self.x, self.y, self.width, self.height))
        #pygame.draw.rect(win, self.color, (self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        font = pygame.font.SysFont("calibri", 20)
        text = font.render(self.text, True, (0,0,0))
        win.blit(text, (self.x, self.y))

def loadTeam(fileName):
    team = open(os.path.join(sys.path[0], fileName), "r")
    data = team.readlines()
    readFile = open(os.path.join(sys.path[0], "gen1dex.txt"), "r")
    dex = readFile.readlines()
    lists = [[]]
    pokemon1 = Pokemon()
    pokemon2 = Pokemon()
    pokemon3 = Pokemon()
    pokemon4 = Pokemon()
    pokemon5 = Pokemon()
    pokemon6 = Pokemon()
    #print(data)
    numMons = 0
    for x in data:
        if x == '\n':
            numMons += 1
            lists.append([])
        else:
            lists[-1].append(x)

    #lists = lists[:numMons]
    pokemonList = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
    print(lists)
    # pokemon number
    i = 0
    #y represents each pokemon
    for y in lists:

        setMoveCounter = 1
        lineNum = 1
        for lineReading in y:
            EVSpread = [0, 0, 0, 0, 0, 0]
            IVSpread = [31, 31, 31, 31, 31, 31]
            #Nick, Name, Gender, Item
            #print(lineReading[:5])
            if lineNum == 1:
                #print(lineReading.split(" ("))

                # pokemon has Nickname AND Gender
                if len(lineReading.split(" (")) == 3:

                    pokemonList[i].setNick(lineReading.split(" (")[0])
                    #print(lineReading.split(" (")[0])


                    pokemonList[i].setName(lineReading.split(" (")[1].split(") ")[0])
                    #print(lineReading.split(" (")[1].split(") ")[0])


                    pokemonList[i].setGender(lineReading.split(" (")[2].split(")")[0])
                    #print(lineReading.split(" (")[2].split(")")[0])

                # pokemon has Gender xor Nick
                elif len(lineReading.split(" (")) == 2:
                    # Pokemon has Gender but no Nick
                    if lineReading.split(" (")[1][:2] == "M)" or lineReading.split(" (")[1][:2] == "F)":
                        pokemonList[i].setName(lineReading.split(" (")[0])

                        pokemonList[i].setGender(lineReading.split(" (")[1][:1])
                        #print(lineReading.split(" (")[1][:1])
                    # pokemon has Nick but no Gender
                    else:
                        pokemonList[i].setNick(lineReading.split(" (")[0])
                        pokemonList[i].setName(lineReading.split(" (")[1].split(") ")[0])
                #pokemon has no gender or nick
                else:
                    #print(lineReading.split(" @ ")[0])
                    pokemonList[i].setName(lineReading.split(" @ ")[0])

                # pokemon has item
                if len(lineReading.split(" @ ")) == 2:
                    pokemonList[i].setItem(lineReading.split(" @ ")[1][:-1])
                    #print(lineReading.split(" @ ")[1][:-1])

            # Ability
            elif lineNum == 2:
                # set ability
                pokemonList[i].setFainted(False)
                pokemonList[i].setAbility(lineReading.split(": ")[1][:-1])
                #print(lineReading.split(": ")[1][:-1])

            #set level
            elif lineReading[:5] == "Level":
                pokemonList[i].setLevel(int(lineReading.split(": ")[1][:-1]))
                #print("level")
            #set shiny
            elif lineReading[:5] == "Shiny":
                pokemonList[i].setShiny(True)
                print("shiny")
            #set happiness
            elif lineReading[:9] == "Happiness":
                pokemonList[i].setHappiness(int(lineReading.split(": ")[1][:-1]))
            #set ev spread
            elif lineReading[:3] == "EVs":
                for stat in lineReading[5:].split(" / "):
                    if stat[-3:] == " HP":
                        EVSpread[0] = int(stat.split()[0])
                    elif stat[-3:] == "Atk":
                        EVSpread[1] = int(stat.split()[0])
                    elif stat[-3:] == "Def":
                        EVSpread[2] = int(stat.split()[0])
                    elif stat[-3:] == "SpA":
                        EVSpread[3] = int(stat.split()[0])
                    elif stat[-3:] == "SpD":
                        EVSpread[4] = int(stat.split()[0])
                    else:
                        EVSpread[5] = int(stat.split()[0])
            #set nature
            elif lineReading[-7:] == "Nature\n":
                pokemonList[i].setNature(lineReading.split()[0])
            #set iv spread
            elif lineReading[:3] == "IVs":
                for stat in lineReading[5:].split(" / "):
                    if stat[-3:] == " HP":
                        IVSpread[0] = int(stat.split()[0])
                    elif stat[-3:] == "Atk":
                        IVSpread[1] = int(stat.split()[0])
                    elif stat[-3:] == "Def":
                        IVSpread[2] = int(stat.split()[0])
                    elif stat[-3:] == "SpA":
                        IVSpread[3] = int(stat.split()[0])
                    elif stat[-3:] == "SpD":
                        IVSpread[4] = int(stat.split()[0])
                    else:
                        IVSpread[5] = int(stat.split()[0])
            #set moves
            elif lineReading[:2] == "- ":
                pokemonList[i].setMove(setMoveCounter, lineReading[2:-1])
                setMoveCounter += 1
            #file is wrong
            else:
                print(lineNum)
                print("Team file is broken!")
                break

            monData = []
            #print(pokemonList[0].getName())
            for dexEntry in dex:
                #print(dexEntry.split()[1])
                #print(pokemonList[i].getName())

                if dexEntry.split()[1] == pokemonList[i].getName():
                    monData = dexEntry.split()
                    #print(monData)
            pokemonList[i].setDex(int(monData[0]))
            if pokemonList[i].nick == "NOPOKEMON":
                pokemonList[i].setNick(pokemonList[i].getName())
            pokemonList[i].setType1(monData[len(monData) - 9])
            pokemonList[i].setType2(monData[len(monData) - 8])
            pokemonList[i].setHP(int(monData[len(monData) - 6]), IVSpread[0], EVSpread[0])
            pokemonList[i].setCurrentHP(pokemonList[i].startHP)
            pokemonList[i].setStats(monData[-5:], IVSpread, EVSpread)

            lineNum += 1

        #print(y[1].split(": ")[1].split('\n')[0])
        pokemonList[i].setAbility(y[1].split(": ")[1].split('\n')[0])
        print(pokemonList[i].shiny)
        i += 1

        for mon in pokemonList:
            try:
                mon.determineAndSetMovesPP()
                #if mon.getName() != "NOPOKEMON":

            except:
                break

    return pokemonList

#loadTeam("test.txt")


def makeTeam():
    f = open(os.path.join(sys.path[0], input("Choose a team/file name: ") + ".txt"), "w")

    readFile = open(os.path.join(sys.path[0], "gen1dex.txt"), "r")
    numMons = int(input("Enter the number of pokemon in your team: "))

    dex = readFile.readlines()
    #print(dex)

    for x in range(numMons):

        pokemon1DexNum = input("Enter your pokemon's dex#: ")
        pokemon1Nick = input("Enter that pokemon's nickname: ")
        pokemon1Item = input("Enter that pokemon's item: ")
        pokemon1Ability = input("Enter that pokemon's ability: ")
        pokemon1Nature = input("Enter that pokemon's Nature: ")
        pokemon1EVs = input("Enter that pokemon's EVs (enter the values in the following format: HP/ATK/DEF/SPA/SPD/SPE): ")
        pokemon1IVs = input("Enter that pokemon's IVs (enter the values in the following format: HP/ATK/DEF/SPA/SPD/SPE): ")
        pokemon1Move1 = input("Enter that pokemon's first move: ")
        pokemon1Move2 = input("Enter that pokemon's second move: ")
        pokemon1Move3 = input("Enter that pokemon's third move: ")
        pokemon1Move4 = input("Enter that pokemon's fourth move: ")

        pokemon1EVs = pokemon1EVs.split("/")
        pokemon1IVs = pokemon1IVs.split("/")
        pokemonData = "001 Bulbasaur GRASS   POISON 318 45 49 49 65 65 45".split()
        newPokemon1EVs = ""
        newPokemon1IVs = ""

        for y in dex:

            pokemonData = y.split()


            if int(pokemonData[0]) == int(pokemon1DexNum):

                newPokemon1EVs = "EVs: "
                newPokemon1IVs = "IVs: "
                #EVs text
                eVStatCounter = 0
                for z in pokemon1EVs:
                    if int(z) != 0:
                        if eVStatCounter == 0:
                            newPokemon1EVs += (str(z) + "HP")
                            if int(pokemon1EVs[1]) != 0 or int(pokemon1EVs[2]) != 0 or int(pokemon1EVs[3]) != 0 or int(pokemon1EVs[4]) != 0 or int(pokemon1EVs[5]) != 0:
                                newPokemon1EVs += " / "
                            else: break
                        elif eVStatCounter == 1:
                            newPokemon1EVs += (str(z) + "Atk")
                            if int(pokemon1EVs[2]) != 0 or int(pokemon1EVs[3]) != 0 or int(pokemon1EVs[4]) != 0 or int(pokemon1EVs[5]) != 0:
                                newPokemon1EVs += " / "
                            else: break
                        elif eVStatCounter == 2:
                            newPokemon1EVs += (str(z) + "Def")
                            if int(pokemon1EVs[3]) != 0 or int(pokemon1EVs[4]) != 0 or int(pokemon1EVs[5]) != 0:
                                newPokemon1EVs += " / "
                            else: break
                        elif eVStatCounter == 3:
                            newPokemon1EVs += (str(z) + "SpA")
                            if int(pokemon1EVs[4]) != 0 or int(pokemon1EVs[5]) != 0:
                                newPokemon1EVs += " / "
                            else:
                                break
                        elif eVStatCounter == 4:
                            newPokemon1EVs += (str(z) + "SpD")
                            if int(pokemon1EVs[5]) != 0:
                                newPokemon1EVs += " / "
                            else: break
                        else:
                            newPokemon1EVs += (str(z) + "Spe")
                    eVStatCounter += 1


                #IVs text
                iVStatCounter = 0
                for z in pokemon1IVs:

                    if int(z) != 31:
                        if iVStatCounter == 0:
                            newPokemon1IVs += (str(z) + "HP")
                            if int(pokemon1IVs[1]) != 31 or int(pokemon1IVs[2]) != 31 or int(pokemon1IVs[3]) != 31 or int(pokemon1IVs[4]) != 31 or int(pokemon1IVs[5]) != 31:
                                newPokemon1IVs += " / "
                            else: break
                        elif iVStatCounter == 1:
                            newPokemon1IVs += (str(z) + "Atk")
                            if int(pokemon1IVs[2]) != 31 or int(pokemon1IVs[3]) != 31 or int(pokemon1IVs[4]) != 31 or int(pokemon1IVs[5]) != 31:
                                newPokemon1IVs += " / "
                            else: break
                        elif iVStatCounter == 2:
                            newPokemon1IVs += (str(z) + "Def")
                            if int(pokemon1IVs[3]) != 31 or int(pokemon1IVs[4]) != 31 or int(pokemon1IVs[5]) != 31:
                                newPokemon1IVs += " / "
                            else: break
                        elif iVStatCounter == 3:
                            newPokemon1IVs += (str(z) + "SpA")
                            if int(pokemon1IVs[4]) != 31 or int(pokemon1IVs[5]) != 31:
                                newPokemon1IVs += " / "
                            else:
                                break
                        elif iVStatCounter == 4:
                            newPokemon1IVs += (str(z) + "SpD")
                            if int(pokemon1IVs[5]) != 31:
                                newPokemon1IVs += " / "
                            else: break
                        else:
                            newPokemon1IVs += (str(z) + "Spe")
                    iVStatCounter += 1


                newPokemon1EVs += "\n"
                newPokemon1IVs += "\n"

                #print(pokemon1EVs)

                standardEVs = True
                standardIVs = True

                for z in pokemon1EVs:
                    if int(z) != 0:
                        standardEVs = False
                if standardEVs:
                    newPokemon1EVs = ""

                for z in pokemon1IVs:
                    if int(z) != 31:
                        standardIVs = False
                if standardIVs:
                    newPokemon1IVs = ""

                f.write(pokemon1Nick + " (" + pokemonData[1] + ") @ " + pokemon1Item + "\nAbility: " + pokemon1Ability + "\n" + newPokemon1EVs + pokemon1Nature + " Nature\n" + newPokemon1IVs + "- " + pokemon1Move1 + "\n- " + pokemon1Move2 + "\n- " + pokemon1Move3 + "\n- " + pokemon1Move4 + "\n\n")


    f.close()
    readFile.close()



def redrawWindow(win, myTeam, oppTeam, button1, button2, button3, button4):
    win.fill((255,255,255))

    if oppTeam[0].dexName == "NOPOKEMON":
        font = pygame.font.SysFont("calibri", 30)
        text = font.render("Waiting for opponent to connect!", True, (0, 0, 0))
        win.blit(text, (0, 350))
        pygame.display.update()
        return

    winning = True
    losing = True

    for i in oppTeam:
        if not i.fainted:
            winning = False

    for j in myTeam:
        if not j.fainted:
            losing = False

    if winning:
        font = pygame.font.SysFont("calibri", 30)
        text = font.render("You won!", True, (0, 0, 0))
        win.blit(text, (0, 350))
        pygame.display.update()
        return

    if losing:
        font = pygame.font.SysFont("calibri", 30)
        text = font.render("You lost!", True, (0, 0, 0))
        win.blit(text, (0, 350))
        pygame.display.update()
        return


    backDrop = pygame.image.load(sys.path[0] + r"\\black-white\\backDrop.png")
    backDrop = pygame.transform.scale(backDrop, (500, 500))
    win.blit(backDrop, (0, 0))

    activeMon = myTeam[0]
    oppActiveMon = oppTeam[0]

    myName = activeMon.nick
    oppName = oppActiveMon.nick

    #for i in range(5):
        #monSwitchList[i].setPokemon(myTeam[i])
        #monSwitchList[i].draw(win)

    for i in range(5):
        if myTeam[i+1].dexName != "NOPOKEMON":
            monSwitchList[i].setPokemon(myTeam[i + 1])
            monSwitchList[i].draw(win)

    button1.setText(activeMon.move1 + " " + activeMon.move1currentPP + "/" + activeMon.move1maxPP)
    button2.setText(activeMon.move2 + " " + activeMon.move2currentPP + "/" + activeMon.move2maxPP)
    button3.setText(activeMon.move3 + " " + activeMon.move3currentPP + "/" + activeMon.move3maxPP)
    button4.setText(activeMon.move4 + " " + activeMon.move4currentPP + "/" + activeMon.move4maxPP)

    myTeamName.setText(myName + " (" + str(int(activeMon.currentHP * 100 / activeMon.startHP)) + "%)")
    myTeamName.draw(win)

    oppTeamName.setText(oppName+ " (" + str(int(oppActiveMon.currentHP * 100 / oppActiveMon.startHP)) + "%)")
    oppTeamName.draw(win)

    button1.setColor(getColor(activeMon.move1Type()))
    button2.setColor(getColor(activeMon.move2Type()))
    button3.setColor(getColor(activeMon.move3Type()))
    button4.setColor(getColor(activeMon.move4Type()))

    myActive(activeMon)
    oppActive(oppActiveMon)

    if not activeMon.fainted:
        button1.draw(win)
        button2.draw(win)
        button3.draw(win)
        button4.draw(win)

    if mainBox.text != "":
        mainBox.draw(win)

    pygame.display.update()

def getColor(type):
    if type == "NORMAL":
        return pygame.Color("#A8A77A")
    if type == "FIRE":
        return pygame.Color("#EE8130")
    if type == "WATER":
        return pygame.Color("#6390F0")
    if type == "ELECTRIC":
        return pygame.Color("#F7D02C")
    if type == "GRASS":
        return pygame.Color("#7AC74C")
    if type == "ICE":
        return pygame.Color("#96D9D6")
    if type == "FIGHTING":
        return pygame.Color("#C22E28")
    if type == "POISON":
        return pygame.Color("#A33EA1")
    if type == "GROUND":
        return pygame.Color("#E2BF65")
    if type == "FLYING":
        return pygame.Color("#A98FF3")
    if type == "PSYCHIC":
        return pygame.Color("#F95587")
    if type == "BUG":
        return pygame.Color("#A6B91A")
    if type == "ROCK":
        return pygame.Color("#B6A136")
    if type == "GHOST":
        return pygame.Color("#735797")
    if type == "DRAGON":
        return pygame.Color("#6F35FC")
    if type == "DARK":
        return pygame.Color("#705746")
    if type == "STEEL":
        return pygame.Color("#B7B7CE")
    return pygame.Color("#D685AD")

def myActive(mon):
    dexNo = str(mon.getDex())
    if mon.getShiny():
        if mon.getGender() == "F":
            try:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\back\\shiny\\female\\" + dexNo + ".png")
            except:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\back\\shiny\\" + dexNo + ".png")
        else:
            activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\back\\shiny\\" + dexNo + ".png")
    else:
        if mon.getGender() == "F":
            try:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\back\\female\\" + dexNo + ".png")
            except:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\back\\" + dexNo + ".png")
        else:
            activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\back\\" + dexNo + ".png")
    activePokemon = pygame.transform.scale(activePokemon, (300, 300))

    pygame.draw.rect(win, pygame.Color(255, 0, 0), (100, 200, 200, 10))
    pygame.draw.rect(win, pygame.Color(0, 255, 0), (100, 200, (float(mon.currentHP)/float(mon.startHP)) * 200, 10))

    if mon.fainted == True:
        activePokemon = pygame.transform.rotate(activePokemon, -90)
    win.blit(activePokemon, (55,190))

def oppActive(mon):

    dexNo = str(mon.getDex())
    if dexNo == "-1":
        dexNo = "0"
    if mon.getShiny():
        if mon.getGender() == "F":
            try:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\shiny\\female\\" + dexNo + ".png")
            except:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\shiny\\" + dexNo + ".png")
        else:
            activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\shiny\\" + dexNo + ".png")
    else:
        if mon.getGender() == "F":
            try:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\female\\" + dexNo + ".png")
            except:
                activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\" + dexNo + ".png")
        else:
            activePokemon = pygame.image.load(sys.path[0] + r"\\black-white\\" + dexNo + ".png")
    activePokemon = pygame.transform.scale(activePokemon, (150, 150))

    pygame.draw.rect(win, pygame.Color(255, 0, 0), (285, 80, 200, 10))
    pygame.draw.rect(win, pygame.Color(0, 255, 0), (285, 80, (float(mon.currentHP)/float(mon.startHP)) * 200, 10))

    if mon.fainted == True:
        activePokemon = pygame.transform.rotate(activePokemon, 90)

    win.blit(activePokemon, (320,80))

def main():
    run = True
    myTeam = loadTeam(input("select a team name to load: ") + ".txt")

    n = Network()
    print(n.send(teamString(myTeam)))

    teamsDisplay = n.send(teamString(myTeam))
    print(teamsDisplay)


    #clock = pygame.time.Clock()
    #print(n.getFirstTeamString())
    #active = myTeam[0]

    moveSelected = -1

    while run:
        teamsDisplayOld = teamsDisplay

        if moveSelected == -1:
            monmove1.deselect()
            monmove2.deselect()
            monmove3.deselect()
            monmove4.deselect()
            monSwitchButton1.deselect()
            monSwitchButton2.deselect()
            monSwitchButton3.deselect()
            monSwitchButton4.deselect()
            monSwitchButton5.deselect()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if monmove1.click(pos):
                    moveSelected = 1
                    monmove1.select()
                    monmove2.deselect()
                    monmove3.deselect()
                    monmove4.deselect()
                    monSwitchButton1.deselect()
                    monSwitchButton2.deselect()
                    monSwitchButton3.deselect()
                    monSwitchButton4.deselect()
                    monSwitchButton5.deselect()
                if monmove2.click(pos):
                    moveSelected = 2
                    monmove1.deselect()
                    monmove2.select()
                    monmove3.deselect()
                    monmove4.deselect()
                    monSwitchButton1.deselect()
                    monSwitchButton2.deselect()
                    monSwitchButton3.deselect()
                    monSwitchButton4.deselect()
                    monSwitchButton5.deselect()
                if monmove3.click(pos):
                    moveSelected = 3
                    monmove1.deselect()
                    monmove2.deselect()
                    monmove3.select()
                    monmove4.deselect()
                    monSwitchButton1.deselect()
                    monSwitchButton2.deselect()
                    monSwitchButton3.deselect()
                    monSwitchButton4.deselect()
                    monSwitchButton5.deselect()
                if monmove4.click(pos):
                    moveSelected = 4
                    monmove1.deselect()
                    monmove2.deselect()
                    monmove3.deselect()
                    monmove4.select()
                    monSwitchButton1.deselect()
                    monSwitchButton2.deselect()
                    monSwitchButton3.deselect()
                    monSwitchButton4.deselect()
                    monSwitchButton5.deselect()

                if monSwitchButton1.click(pos) and monSwitchButton1.mon.dexName != "NOPOKEMON" and not monSwitchButton1.mon.fainted:
                    moveSelected = 5
                    monmove1.deselect()
                    monmove2.deselect()
                    monmove3.deselect()
                    monmove4.deselect()
                    monSwitchButton1.select()
                    monSwitchButton2.deselect()
                    monSwitchButton3.deselect()
                    monSwitchButton4.deselect()
                    monSwitchButton5.deselect()
                if monSwitchButton2.click(pos) and monSwitchButton2.mon.dexName != "NOPOKEMON" and not monSwitchButton2.mon.fainted:
                    moveSelected = 6
                    monmove1.deselect()
                    monmove2.deselect()
                    monmove3.deselect()
                    monmove4.deselect()
                    monSwitchButton1.deselect()
                    monSwitchButton2.select()
                    monSwitchButton3.deselect()
                    monSwitchButton4.deselect()
                    monSwitchButton5.deselect()
                if monSwitchButton3.click(pos) and monSwitchButton3.mon.dexName != "NOPOKEMON" and not monSwitchButton3.mon.fainted:
                    moveSelected = 7
                    monmove1.deselect()
                    monmove2.deselect()
                    monmove3.deselect()
                    monmove4.deselect()
                    monSwitchButton1.deselect()
                    monSwitchButton2.deselect()
                    monSwitchButton3.select()
                    monSwitchButton4.deselect()
                    monSwitchButton5.deselect()
                if monSwitchButton4.click(pos) and monSwitchButton4.mon.dexName != "NOPOKEMON" and not monSwitchButton4.mon.fainted:
                    moveSelected = 8
                    monmove1.deselect()
                    monmove2.deselect()
                    monmove3.deselect()
                    monmove4.deselect()
                    monSwitchButton1.deselect()
                    monSwitchButton2.deselect()
                    monSwitchButton3.deselect()
                    monSwitchButton4.select()
                    monSwitchButton5.deselect()
                if monSwitchButton5.click(pos) and monSwitchButton5.mon.dexName != "NOPOKEMON" and not monSwitchButton5.mon.fainted:
                    moveSelected = 9
                    monmove1.deselect()
                    monmove2.deselect()
                    monmove3.deselect()
                    monmove4.deselect()
                    monSwitchButton1.deselect()
                    monSwitchButton2.deselect()
                    monSwitchButton3.deselect()
                    monSwitchButton4.deselect()
                    monSwitchButton5.select()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        #print(str(moveSelected))
        try:
            teamsDisplay = n.send(str(moveSelected))
        except:
            pass

        if teamsDisplayOld != teamsDisplay:
            print("Next Turn")
            moveSelected = -1


        #pygame.time.delay(2000)

        try:
            boxMessage = teamStringSplit(teamsDisplay)[2]
            mainBox.setText(boxMessage)
            redrawWindow(win, teamUnstring(teamStringSplit(teamsDisplay)[0]), teamUnstring(teamStringSplit(teamsDisplay)[1]), monmove1, monmove2, monmove3, monmove4)
        except:
            pass


monmove1 = Button()
monmove2 = Button()
monmove3 = Button()
monmove4 = Button()

monSwitchButton1 = SwitchButton()
monSwitchButton2 = SwitchButton()
monSwitchButton3 = SwitchButton()
monSwitchButton4 = SwitchButton()
monSwitchButton5 = SwitchButton()

monSwitchList = [monSwitchButton1, monSwitchButton2, monSwitchButton3, monSwitchButton4, monSwitchButton5]

myTeamName = JustText()
oppTeamName = JustText()

boxMessage = ""

moveButtonsList = [monmove1, monmove2, monmove3, monmove4]

monSwitchButton1.setX(25)
monSwitchButton2.setX(125)
monSwitchButton3.setX(225)
monSwitchButton4.setX(325)
monSwitchButton5.setX(425)

monmove1.setX(20)
monmove2.setX(260)
monmove3.setX(20)
monmove4.setX(260)
myTeamName.setX(100)
oppTeamName.setX(285)

monSwitchButton1.setY(650)
monSwitchButton2.setY(650)
monSwitchButton3.setY(650)
monSwitchButton4.setY(650)
monSwitchButton5.setY(650)

monmove1.setY(505)
monmove2.setY(505)
monmove3.setY(580)
monmove4.setY(580)
myTeamName.setY(180)
oppTeamName.setY(60)

mainBox = textBox()

main()

#makeTeam()

