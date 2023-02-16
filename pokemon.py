import random

class Pokemon():
    def __init__(self):
        self.startHP = -1
        self.startDef = -1
        self.startAtk = -1
        self.startSpA = -1
        self.startSpD = -1
        self.startSpe = -1
        self.item = "NOPOKEMON"
        self.nick = "NOPOKEMON"
        self.dexName = "NOPOKEMON"
        self.dex = -1
        self.move1 = "NOPOKEMON"
        self.move2 = "NOPOKEMON"
        self.move3 = "NOPOKEMON"
        self.move4 = "NOPOKEMON"
        self.ability = "NOPOKEMON"
        self.shiny = False
        self.gender = "None"
        self.level = 100
        self.happiness = 255
        self.nature = "Jolly"
        #self.position = 1
        self.status = "None"
        self.currentHP = 0
        self.atkStage = 0
        self.defStage = 0
        self.spaStage = 0
        self.spdStage = 0
        self.speStage = 0
        self.accStage = 0
        self.evaStage = 0
        self.critStage = 0
        self.fainted = True
        self.type1 = "NONE"
        self.type2 = "NONE"
        self.curse = False
        self.perishCount = -1
        self.taunt = False
        self.encore = False
        self.move1maxPP = -1
        self.move2maxPP = -1
        self.move3maxPP = -1
        self.move4maxPP = -1
        self.move1currentPP = -1
        self.move2currentPP = -1
        self.move3currentPP = -1
        self.move4currentPP = -1

    def determineAndSetMovesPP(self):
        move1Temp = self.move1.replace(" ", "")
        move1Temp.replace("-", "")
        #print(move1Temp)
        move2Temp = self.move2.replace(" ", "")
        move2Temp.replace("-", "")
        #print(move2Temp)
        move3Temp = self.move3.replace(" ", "")
        move3Temp.replace("-", "")
        #print(move3Temp)
        move4Temp = self.move4.replace(" ", "")
        move4Temp.replace("-", "")
        #print(move4Temp)

        move1func = getattr(Pokemon, move1Temp)
        move2func = getattr(Pokemon, move2Temp)
        move3func = getattr(Pokemon, move3Temp)
        move4func = getattr(Pokemon, move4Temp)

        move1PP = int(move1func(self).split("/")[3])
        #print(str(move1PP))
        self.setMaxPP1(move1PP)
        self.move1currentPP = move1PP

        move2PP = int(move2func(self).split("/")[3])
        #print(move2PP)
        self.setMaxPP2(move2PP)
        self.move2currentPP = move2PP

        move3PP = int(move3func(self).split("/")[3])
        #print(move3PP)
        self.setMaxPP3(move3PP)
        self.move3currentPP = move3PP

        move4PP = int(move4func(self).split("/")[3])
        #print(move4PP)
        self.setMaxPP4(move4PP)
        self.move4currentPP = move4PP

        self.setFainted(False)

    def getMove(self, moveNum):
        if moveNum == 1:
            return self.move1
        if moveNum == 2:
            return self.move2
        if moveNum == 3:
            return self.move3
        if moveNum == 4:
            return self.move4
        return "NULL"

    def getMovePrio(self, moveNum):
        if moveNum == 1:
            self.move1Prio()
        if moveNum == 2:
            self.move2Prio()
        if moveNum == 3:
            self.move3Prio()
        if moveNum == 4:
            self.move4Prio()
        return 0

    def move1Prio(self):
        moveTemp = self.move1.replace(" ", "")
        moveTemp.replace("-", "")
        move1func = getattr(Pokemon, moveTemp)
        return move1func(self).split("/")[0]
    def move2Prio(self):
        moveTemp = self.move2.replace(" ", "")
        moveTemp.replace("-", "")
        move1func = getattr(Pokemon, moveTemp)
        return move1func(self).split("/")[0]
    def move3Prio(self):
        moveTemp = self.move3.replace(" ", "")
        moveTemp.replace("-", "")
        move1func = getattr(Pokemon, moveTemp)
        return move1func(self).split("/")[0]
    def move4Prio(self):
        moveTemp = self.move4.replace(" ", "")
        moveTemp.replace("-", "")
        move1func = getattr(Pokemon, moveTemp)
        return move1func(self).split("/")[0]

    def move1Type(self):
        moveTemp = self.move1.replace(" ", "")
        moveTemp.replace("-", "")
        move1func = getattr(Pokemon, moveTemp)
        return move1func(self).split("/")[1]

    def move2Type(self):
        moveTemp = self.move2.replace(" ", "")
        moveTemp.replace("-", "")
        move1func = getattr(Pokemon, moveTemp)
        return move1func(self).split("/")[1]

    def move3Type(self):
        moveTemp = self.move3.replace(" ", "")
        moveTemp = moveTemp.replace("-", "")
        move1func = getattr(Pokemon, moveTemp)
        return move1func(self).split("/")[1]

    def move4Type(self):
        #print(self.move4)
        moveTemp = self.move4.replace(" ", "")
        #print(moveTemp)
        moveTemp.replace("-", "")
        #print(moveTemp)
        movefunc = getattr(Pokemon, moveTemp)
        return movefunc(self).split("/")[1]

    def setMaxPP1(self, amt):
        self.move1maxPP = amt
    def setMaxPP2(self, amt):
        self.move2maxPP = amt
    def setMaxPP3(self, amt):
        self.move3maxPP = amt
    def setMaxPP4(self, amt):
        self.move4maxPP = amt

    def setCurrentPP1(self, amt):
        self.move1currentPP = amt
    def setCurrentPP2(self, amt):
        self.move2currentPP = amt
    def setCurrentPP3(self, amt):
        self.move3currentPP = amt
    def setCurrentPP4(self, amt):
        self.move4currentPP = amt
    def setType1(self, newType):
        self.type1 = newType
    def setType2(self, newType):
        self.type2 = newType
    def setFainted(self, newVal):
        self.fainted = newVal
    def getFainted(self):
        return self.fainted
    def setNick(self, newNick):
        self.nick = newNick
    def setAtkStage(self, stage):
        self.atkStage = stage
    def setDefStage(self, stage):
        self.defStage = stage
    def setSpaStage(self, stage):
        self.spaStage = stage
    def setSpdStage(self, stage):
        self.spdStage = stage
    def setSpeStage(self, stage):
        self.speStage = stage
    def setAccStage(self, stage):
        self.accStage = stage
    def setEvaStage(self, stage):
        self.evaStage = stage
    def setCritStage(self, stage):
        self.critStage = stage
    def changeStage(self, stat, stage):
        if stat == 1:
            self.atkStage += stage
            if self.atkStage >= 6:
                self.atkStage = 6
            if self.atkStage <= -6:
                self.atkStage = -6
        if stat == 2:
            self.defStage += stage
            if self.defStage >= 6:
                self.defStage = 6
            if self.defStage <= -6:
                self.defStage = -6
        if stat == 3:
            self.spaStage += stage
            if self.spaStage >= 6:
                self.spaStage = 6
            if self.spaStage <= -6:
                self.spaStage = -6
        if stat == 4:
            self.spdStage += stage
            if self.spdStage >= 6:
                self.spdStage = 6
            if self.spdStage <= -6:
                self.spdStage = -6
        if stat == 5:
            self.speStage += stage
            if self.speStage >= 6:
                self.speStage = 6
            if self.speStage <= -6:
                self.speStage = -6
        if stat == 6:
            self.accStage += stage
            if self.accStage >= 6:
                self.accStage = 6
            if self.accStage <= -6:
                self.accStage = -6
        if stat == 7:
            self.evaStage += stage
            if self.evaStage >= 6:
                self.evaStage = 6
            if self.evaStage <= -6:
                self.evaStage = -6
        if stat == 8:
            self.critStage += stage
            if self.critStage >= 4:
                self.critStage = 4
            if self.critStage <= 0:
                self.critStage = 0

    def setDex(self, newDex):
        self.dex = newDex
    def setStatus(self, newStat):
        self.status = newStat
    def setPosition(self, pos):
        self.position = pos
    def getDex(self):
        return self.dex
    def setCurrentHP(self, hp):
        self.currentHP = hp
    def setName(self, newName):
        self.dexName = newName
    def setItem(self, newItem):
        self.item = newItem
    def setAbility(self, newAbil):
        self.ability = newAbil
    def setGender(self, newGender):
        self.gender = newGender
    def getGender(self):
        return self.gender
    def setLevel(self, newLevel):
        self.level = newLevel
    def setShiny(self, shinyness):
        self.shiny = shinyness
    def getShiny(self):
        return self.shiny
    def setHappiness(self, newHappiness):
        self.happiness = newHappiness
    def setHP(self, base, iv, ev):
        self.startHP = int(0.01 * (2 * base + iv + int(0.25 * ev)) * self.level) + self.level + 10
    def setHPStat(self, hp):
        self.startHP = hp
    def setNature(self, newNature):
        self.nature = newNature
    def getName(self):
        return self.dexName
    def setStats(self, base, ivSpread, evSpread):
        self.startAtk = (int(0.01 * (2 * int(base[0]) + ivSpread[1] + int(0.25 * evSpread[1])) * self.level) + 5)
        self.startDef = (int(0.01 * (2 * int(base[1]) + ivSpread[2] + int(0.25 * evSpread[2])) * self.level) + 5)
        self.startSpA = (int(0.01 * (2 * int(base[2]) + ivSpread[3] + int(0.25 * evSpread[3])) * self.level) + 5)
        self.startSpD = (int(0.01 * (2 * int(base[3]) + ivSpread[4] + int(0.25 * evSpread[4])) * self.level) + 5)
        self.startSpe = (int(0.01 * (2 * int(base[4]) + ivSpread[5] + int(0.25 * evSpread[5])) * self.level) + 5)
        #nature increases
        if self.nature == "Lonely" or self.nature == "Brave" or self.nature == "Adamant" or self.nature == "Naughty":
            self.startAtk = int(self.startAtk * 1.1)
        if self.nature == "Bold" or self.nature == "Impish" or self.nature == "Lax" or self.nature == "Relaxed":
            self.startDef = int(self.startDef * 1.1)
        if self.nature == "Timid" or self.nature == "Hasty" or self.nature == "Jolly" or self.nature == "Naive":
            self.startSpe = int(self.startSpe * 1.1)
        if self.nature == "Modest" or self.nature == "Mild" or self.nature == "Quiet" or self.nature == "Rash":
            self.startSpA = int(self.startSpA * 1.1)
        if self.nature == "Calm" or self.nature == "Gentle" or self.nature == "Sassy" or self.nature == "Careful":
            self.startSpD = int(self.startSpD * 1.1)
        #nature decreases
        if self.nature == "Bold" or self.nature == "Modest" or self.nature == "Calm" or self.nature == "Timid":
            self.startAtk = int(self.startAtk * 0.9)
        if self.nature == "Lonely" or self.nature == "Gentle" or self.nature == "Mild" or self.nature == "Hasty":
            self.startDef = int(self.startDef * 0.9)
        if self.nature == "Brave" or self.nature == "Relaxed" or self.nature == "Quiet" or self.nature == "Sassy":
            self.startSpe = int(self.startSpe * 0.9)
        if self.nature == "Adamant" or self.nature == "Impish" or self.nature == "Careful" or self.nature == "Jolly":
            self.startSpA = int(self.startSpA * 0.9)
        if self.nature == "Naughty" or self.nature == "Lax" or self.nature == "Rash" or self.nature == "Naive":
            self.startSpD = int(self.startSpD * 0.9)

    def setAttack(self, attack):
        self.startAtk = attack

    def setDefense(self, defense):
        self.startDef = defense

    def setSPA(self, spa):
        self.startSpA = spa

    def setSPD(self, spd):
        self.startSpD = spd

    def setSpe(self, spe):
        self.startSpe = spe

    def setMove(self, moveNum, moveName):
        if moveNum == 1:
            self.move1 = moveName
        elif moveNum == 2:
            self.move2 = moveName
        elif moveNum == 3:
            self.move3 = moveName
        elif moveNum == 4:
            self.move4 = moveName
        else:
            print("invalid move number")


    def curseEffect(self, val):
        self.curse = val

    #"Prio/Type/statusPhysicalSpecial/pp/power/Acc/atkChange/defChange/spaChange/spdChange/speChange/accChange/evaChange/atkChangeOpp/defChangeOpp/spaChangeOpp/spdChangeOpp/speChangeOpp/accChangeOpp/evaChangeOpp/StatusSelf/StatusOpp/extraEffect/Contact/Charging/Recharge/protected/reflectable/snatchable/mirrorMove/punch/sound/noGrav/Defrosts/Heals/ignSub/powder/Jaw/pulse/ballistic/mental/Dance"

    # def Absorb():

    '''
    Acid
    Acid Armor
    Acid Spray
    Acrobatics
    Acupressure
    Aerial Ace
    Aeroblast
    After You
    Agility
    Air Cutter
    Air Slash
    Ally Switch
    Amnesia
    '''
    def AncientPower(self):
        if random.randint(0,9) == 0:
            return "0/ROCK/Special/8/60/100/1/1/1/1/1/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
        else:
            return "0/ROCK/Special/8/60/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    Aqua Jet
    Aqua Ring
    Aqua Tail
    Arm Thrust
    Aromatherapy
    Assist
    Assurance
    Astonish
    Attack Order
    Attract
    Aura Sphere
    Aurora Beam
    Autotomize
    Avalanche
    Barrage
    Barrier
    '''
    def BatonPass(self):
        return "0/NORMAL/Status/64/-/-/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/BatonPass/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    Beat Up
    Belly Drum
    Bestow
    Bide
    Bind
    Bite
    Blast Burn
    Blaze Kick
    Blizzard
    Block
    Blue Flare
    '''
    def BodySlam(self):
        if random.randint(0,9) <= 2:
            return "0/NORMAL/Physical/24/85/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/PARALYZED/-/1/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
        else:
            return "0/NORMAL/Physical/24/85/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/-/1/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    Bolt Strike
    Bone Club
    Bone Rush
    Bonemerang
    Bounce
    Brave Bird
    Brick Break
    Brine
    Bubble
    BubbleBeam
    Bug Bite
    Bug Buzz
    '''
    def BulkUp(self):
        return "0/FIGHTING/Status/32/-/-/1/1/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    Bulldoze
    Bullet Punch
    Bullet Seed
    Calm Mind
    Camouflage
    Captivate
    Charge
    Charge Beam
    Charm
    Chatter
    Chip Away
    Circle Throw
    Clamp
    Clear Smog
    Close Combat
    Coil
    Comet Punch
    Confuse Ray
    Confusion
    Constrict
    Conversion
    Conversion 2
    Copycat
    Cosmic Power
    Cotton Guard
    Cotton Spore
    Counter
    Covet
    Crabhammer
    Cross Chop
    Cross Poison
    '''
    def Crunch(self):
        if random.randint(0,4) == 0:
            return "0/DARK/Physical/24/80/100/0/0/0/0/0/0/0/0/0/-1/0/0/0/0/0/0/-/-/-/1/0/0/1/0/0/1/0/0/0/0/0/0/0/1/0/0/0/0"
        else:
            return "0/DARK/Physical/24/80/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/-/1/0/0/1/0/0/1/0/0/0/0/0/0/0/1/0/0/0/0"
    '''
    Crush Claw
    Crush Grip'''

    def Curse(self):
        if self.type1 == "GHOST" or self.type2 == "GHOST":
            return "0/GHOST/Status/16/-/-/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/Curse/selfCurseDmg/0/0/0/0/0/0/0/0/0/0/0/0/1/0/0/0/0/0/0"
        else:
            return "0/GHOST/Status/16/-/-/1/1/0/0/-1/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/0/0/0/0/0/0/0/0/0/1/0/0/0/0/0/0"

    '''
    Cut
    '''
    def DarkPulse(self):
        if random.randint(0,4) == 0:
            return "0/DARK/Special/24/80/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/Flinch/0/0/0/1/0/0/1/0/0/0/0/0/0/0/0/1/0/0/0"
        else:
            return "0/DARK/Special/24/80/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/1/0/0/1/0/0/0/0/0/0/0/0/1/0/0/0"
    '''
    Dark Void
    Defend Order
    Defense Curl
    Defog
    Destiny Bond
    Detect
    Dig
    Disable
    Discharge
    Dive
    Dizzy Punch
    Doom Desire
    Double Hit
    Double Kick
    Double Team
    '''
    def DoubleEdge(self):
        return "0/NORMAL/Pysical/24/120/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/ThirdRecoil/1/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    DoubleSlap
    Draco Meteor
    Dragon Claw
    '''
    def DragonDance(self):
        return "0/DRAGON/Status/32/-/-/1/0/0/0/1/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    Dragon Pulse
    Dragon Rage
    Dragon Rush
    Dragon Tail
    DragonBreath
    Drain Punch
    Dream Eater
    Drill Peck
    Drill Run
    Dual Chop
    DynamicPunch
    Earth Power
    Earthquake
    Echoed Voice
    Egg Bomb
    Electro Ball
    Electroweb
    Embargo
    Ember
    Encore
    Endeavor
    Endure
    Energy Ball
    Entrainment
    Eruption
    Explosion
    Extrasensory
    ExtremeSpeed
    Facade
    Faint Attack
    Fake Out
    Fake Tears
    False Swipe
    FeatherDance
    Feint
    Fiery Dance
    Final Gambit
    Fire Blast
    Fire Fang
    Fire Pledge
    Fire Punch
    Fire Spin
    Fissure
    Flail
    Flame Burst
    Flame Charge
    Flame Wheel
    Flamethrower
    Flare Blitz
    Flash
    Flash Cannon
    Flatter
    Fling
    Fly
    Focus Blast
    Focus Energy
    Focus Punch
    Follow Me
    Force Palm
    Foresight
    Foul Play
    Freeze Shock
    Frenzy Plant
    Frost Breath
    Frustration
    Fury Attack
    Fury Cutter
    Fury Swipes
    Fusion Bolt
    Fusion Flare
    Future Sight
    Gastro Acid
    Gear Grind'''
    def GigaDrain(self):
        return "0/GRASS/Special/16/75/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/GigaDrain/0/0/0/1/0/0/1/0/0/0/0/1/0/0/0/0/0/0/0"

    '''
    Giga Impact
    Glaciate
    Glare
    Grass Knot
    Grass Pledge
    GrassWhistle
    Gravity
    Growl
    Growth
    Grudge
    Guard Split
    Guard Swap
    Guillotine
    Gunk Shot
    Gust
    Gyro Ball
    Hail
    Hammer Arm
    Harden
    Haze
    Head Charge
    Head Smash
    Headbutt
    Heal Bell
    Heal Block
    Heal Order
    Heal Pulse
    Healing Wish
    Heart Stamp
    Heart Swap
    Heat Crash
    Heat Wave
    Heavy Slam
    Helping Hand
    Hex
    Hi Jump Kick
    Hidden Power
    Hone Claws
    Horn Attack
    Horn Drill
    Horn Leech
    Howl
    Hurricane
    Hydro Cannon
    Hydro Pump
    Hyper Beam
    Hyper Fang
    Hyper Voice
    Hypnosis
    Ice Ball
    Ice Beam
    Ice Burn
    Ice Fang
    Ice Punch
    Ice Shard
    Icicle Crash
    Icicle Spear
    Icy Wind
    Imprison
    Incinerate
    Inferno
    Ingrain
    Iron Defense
    Iron Head
    Iron Tail
    Judgement
    Jump Kick
    Karate Chop
    Kinesis
    Knock Off
    Last Resort
    Lava Plume
    Leaf Blade
    Leaf Storm
    Leaf Tornado
    Leech Life'''
    def LeechSeed(self):
        return "0/GRASS/Status/16/-/90/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/Seeded/-/0/0/0/1/1/0/1/0/0/0/0/0/0/0/0/0/0/0/0"

    '''
    Leer
    Lick
    Light Screen
    Lock-On
    Lovely Kiss
    Low Kick
    Low Sweep
    Lucky Chant
    Lunar Dance
    Luster Purge
    Mach Punch
    Magic Coat
    Magic Room
    Magical Leaf
    Magma Storm
    Magnet Bomb
    Magnet Rise
    Magnitude
    Me First
    Mean Look
    Meditate
    Mega Drain
    Mega Kick
    Mega Punch
    Megahorn
    Memento
    Metal Burst
    Metal Claw
    Metal Sound
    Meteor Mash
    Metronome
    Milk Drink
    Mimic
    Mind Reader
    Minimize
    Miracle Eye
    Mirror Coat
    Mirror Move
    Mirror Shot
    Mist
    Mist Ball
    Moonlight
    Morning Sun
    Mud Bomb
    Mud Shot
    Mud Sport
    Mud-Slap
    Muddy Water
    Nasty Plot
    Natural Gift
    Nature Power
    Needle Arm
    Night Daze
    Night Shade
    Night Slash
    Nightmare
    Octazooka
    Odor Sleuth
    '''
    def OminousWind(self):
        if random.randint(0,9) == 0:
            return "0/GHOST/Special/8/60/100/1/1/1/1/1/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
        else:
            return "0/GHOST/Special/8/60/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    Outrage
    Overheat
    Pain Split
    Pay Day
    Payback
    Peck
    Perish Song
    Petal Dance
    Pin Missile
    Pluck
    Poison Fang
    Poison Gas
    Poison Jab
    Poison Sting
    Poison Tail
    PoisonPowder
    Pound
    Powder Snow
    Power Gem
    Power Split
    Power Swap
    Power Trick'''
    def PowerWhip(self):
        return "0/GRASS/Physical/16/120/85/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/-/1/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"

    '''
    Present
    Protect
    Psybeam
    Psych Up
    Psychic
    Psycho Boost
    Psycho Cut
    Psycho Shift
    Psyshock
    Psystrike
    Psywave
    Punishment
    Pursuit
    Quash
    Quick Attack
    Quick Guard
    Quiver Dance
    Rage
    Rage Powder
    Rain Dance
    Rapid Spin
    Razor Leaf
    Razor Shell
    Razor Wind
    Recover
    Recycle
    Reflect
    Reflect Type
    Refresh
    Relic Song
    Rest
    Retaliate
    Return
    Revenge
    Reversal
    Roar
    Roar of Time
    Rock Blast
    Rock Climb
    Rock Polish
    Rock Slide
    Rock Smash
    Rock Throw
    Rock Tomb
    Rock Wrecker
    Role Play
    Rolling Kick
    Rollout
    Roost
    Round
    Sacred Fire
    Sacred Sword
    Safeguard
    Sand Tomb
    Sand-Attack
    Sandstorm
    Scald
    Scary Face
    Scratch
    Screech
    Searing Shot
    Secret Power
    Secret Sword
    Seed Bomb
    Seed Flare
    Seismic Toss
    Selfdestruct
    Shadow Ball
    Shadow Claw
    Shadow Force
    Shadow Punch
    Shadow Sneak
    Sharpen
    Sheer Cold
    Shell Smash
    Shift Gear
    Shock Wave
    Signal Beam
    '''
    def SilverWind(self):
        if random.randint(0,9) == 0:
            return "0/BUG/Special/8/60/100/1/1/1/1/1/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
        else:
            return "0/BUG/Special/8/60/100/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/-/-/0/0/0/1/0/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    Simple Beam
    Sing
    Sketch
    Skill Swap
    Skull Bash
    Sky Attack
    Sky Drop
    Sky Uppercut
    Slack Off
    Slam
    Slash
    Sleep Powder
    Sleep Talk
    Sludge
    Sludge Bomb
    Sludge Wave
    Smack Down
    SmellingSalt
    Smog
    SmokeScreen
    Snarl
    Snatch
    Snore
    Soak
    Softboiled
    SolarBeam
    SonicBoom
    Spacial Rend
    Spark
    Spider Web
    Spike Cannon
    Spikes
    Spit Up
    Spite
    Splash
    Spore
    Stealth Rock
    Steamroller
    Steel Wing
    Stockpile
    Stomp
    Stone Edge
    Stored Power
    Storm Throw
    Strength
    String Shot
    Struggle
    Struggle Bug
    Stun Spore
    Submission
    Substitute
    Sucker Punch
    Sunny Day
    Super Fang
    Superpower
    Supersonic
    Surf
    Swagger
    Swallow
    Sweet Kiss
    Sweet Scent
    Swift
    Switcheroo
    Swords Dance
    Synchronoise
    Synthesis
    Tackle
    Tail Glow
    Tail Slap
    Tail Whip
    Tailwind
    Take Down
    Taunt
    Techno Blast
    Teeter Dance
    Telekinesis
    Teleport
    Thief
    Thrash
    Thunder
    Thunder Fang
    '''
    def ThunderWave(self):
        return "0/ELECTRIC/Status/32/-/90/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/-/PARALYZED/-/0/0/0/1/1/0/1/0/0/0/0/0/0/0/0/0/0/0/0"
    '''
    ThunderPunch
    ThunderShock
    Thunderbolt
    Tickle
    Torment
    Toxic
    Toxic Spikes
    Transform
    Tri Attack
    Trick
    Trick Room
    Triple Kick
    Trump Card
    Twineedle
    Twister
    U-turn
    Uproar
    V-create
    Vacuum Wave
    Venoshock
    ViceGrip
    Vine Whip
    Vital Throw
    Volt Switch
    Volt Tackle
    Wake-Up Slap
    Water Gun
    Water Pledge
    Water Pulse
    Water Sport
    Water Spout
    Waterfall
    Weather Ball
    Whirlpool
    Whirlwind
    Wide Guard
    Wild Charge
    Will-O-Wisp
    Wing Attack
    Wish
    Withdraw
    Wonder Room
    Wood Hammer
    Work Up
    Worry Seed
    Wrap
    Wring Out
    X-Scissor
    Yawn
    Zap Cannon
    Zen Headbutt '''

def teamString(team):
    ans = ""
    for mon in team:
        ans += str(mon.startHP) + "/"
        ans += str(mon.startAtk) + "/"
        ans += str(mon.startDef) + "/"
        ans += str(mon.startSpA) + "/"
        ans += str(mon.startSpD) + "/"
        ans += str(mon.startSpe) + "/"
        ans += mon.item + "/"
        ans += mon.nick + "/"
        ans += mon.dexName + "/"
        ans += str(mon.dex) + "/"
        ans += mon.move1 + "/"
        ans += mon.move2 + "/"
        ans += mon.move3 + "/"
        ans += mon.move4 + "/"
        ans += mon.ability + "/"
        if (mon.shiny):
            ans += "True" + "/"
        else:
            ans += "False" + "/"
        ans += mon.gender + "/"
        ans += str(mon.level) + "/"
        ans += str(mon.happiness) + "/"
        ans += mon.nature + "/"
        ans += mon.status + "/"
        ans += str(mon.currentHP) + "/"
        ans += str(mon.atkStage) + "/"
        ans += str(mon.defStage) + "/"
        ans += str(mon.spaStage) + "/"
        ans += str(mon.spdStage) + "/"
        ans += str(mon.speStage) + "/"
        ans += str(mon.accStage) + "/"
        ans += str(mon.evaStage) + "/"
        #print(mon.fainted)
        if (mon.fainted):
            ans += "True" + "/"
        else:
            ans += "False" + "/"
        ans += mon.type1 + "/"
        ans += mon.type2 + "/"
        ans += str(mon.curse) + "/"
        ans += str(mon.move1maxPP) + "/"
        ans += str(mon.move2maxPP) + "/"
        ans += str(mon.move3maxPP) + "/"
        ans += str(mon.move4maxPP) + "/"
        ans += str(mon.move1currentPP) + "/"
        ans += str(mon.move2currentPP) + "/"
        ans += str(mon.move3currentPP) + "/"
        ans += str(mon.move4currentPP) + "/"
        ans += str(mon.critStage) + "\n"
    return ans

def teamStringSplit(teams):
    return teams.split("//split//")

def teamsStringCombine(team1, team2):
    return team1 + "//split//" + team2

def teamUnstring(teamStringForm):

    pokemon1 = Pokemon()
    pokemon2 = Pokemon()
    pokemon3 = Pokemon()
    pokemon4 = Pokemon()
    pokemon5 = Pokemon()
    pokemon6 = Pokemon()
    ans = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
    #print(teamStringForm)
    splitByMon = teamStringForm.split("\n")
    #print(splitByMon)
    i = 0
    for mon in ans:
        slashed = splitByMon[i].split("/")
        mon.setHPStat(int(slashed[0]))
        mon.setAttack(int(slashed[1]))
        mon.setDefense(int(slashed[2]))
        mon.setSPA(int(slashed[3]))
        mon.setSPD(int(slashed[4]))
        mon.setSpe(int(slashed[5]))
        mon.setItem(slashed[6])
        mon.setNick(slashed[7])
        mon.setName(slashed[8])
        mon.setDex(int(slashed[9]))
        mon.setMove(1, slashed[10])
        mon.setMove(2, slashed[11])
        mon.setMove(3, slashed[12])
        mon.setMove(4, slashed[13])
        mon.setAbility(slashed[14])
        mon.setShiny("True" == (slashed[15]))
        mon.setGender(slashed[16])
        mon.setLevel(int(slashed[17]))
        mon.setHappiness(int(slashed[18]))
        mon.setNature(slashed[19])
        mon.setStatus(slashed[20])
        mon.setCurrentHP(int(slashed[21]))
        mon.setAtkStage(int(slashed[22]))
        mon.setDefStage(int(slashed[23]))
        mon.setSpaStage(int(slashed[24]))
        mon.setSpdStage(int(slashed[25]))
        mon.setSpeStage(int(slashed[26]))
        mon.setAccStage(int(slashed[27]))
        mon.setEvaStage(int(slashed[28]))
        if slashed[29] == "True":
            mon.setFainted(True)
        else:
            mon.setFainted(False)
        mon.setType1(slashed[30])
        mon.setType2(slashed[31])
        mon.curseEffect(slashed[32])
        mon.setMaxPP1(slashed[33])
        mon.setMaxPP2(slashed[34])
        mon.setMaxPP3(slashed[35])
        mon.setMaxPP4(slashed[36])
        mon.setCurrentPP1(slashed[37])
        mon.setCurrentPP2(slashed[38])
        mon.setCurrentPP3(slashed[39])
        mon.setCurrentPP4(slashed[40])
        mon.setCritStage(int(slashed[41]))

        i += 1
    return ans