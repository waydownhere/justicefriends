import os
import random

class Mission:
    def __init__(self, gameType='Tempest'):
        self.gameType = gameType
        self.deployment = {}
        self.gameRules = self.getRules()

    def getRules(self):
        rulesPath = f'{os.getcwd()}\\Tempest_Images\\Tempest_Rules.txt'
        ruleSets = {"Tempest":self.readRules(rulesPath)}
        return ruleSets[self.gameType]
    
    def readRules(self, path):
        contents = ""
        with open(path, 'r') as txtFile:
            contents = txtFile.read()
        return contents

class TempestGame(Mission):
    def __init__(self, gameType='Tempest', mission_rule=random.randrange(0, 11, 1)):
        super().__init__(gameType)
        self.gameRules = self.gameRules
        self.missionRule = self.checkMaelstrom(self.getMissionRule())
        self.primary = self.getPrimary()
        self.playerSecondarys = {
            "CurrentSecondary":{

            },
            "CurrentRound":1,
        }
        self.secondaryDeck = self.buildSecDeck()

    def showRules(self):
        return self.gameRules
    
    def getMissionRule(self, missionRule):
        directory = f'{os.getcwd()}\\Tempest_Images\\Mission_Rules'
        files = os.listdir(directory)
        if missionRule.isnumeric() == True or type(missionRule) == int:
            if missionRule > 0 and missionRule < len(files):
                return {files[missionRule]:self.readRules(f'{directory}\\{files[missionRule]}')}
            else:
                pass #Raise Exception
        elif missionRule.isalpha():
            return self.readRules(f'{directory}\\{missionRule}')
        else:
            pass # Raise Exception
    
    def checkMaelstrom(self, missionRule):
        if missionRule.keys()[0] == "MAELSTROM OF BATTLE.txt":
            missionCards = os.listdir(f'{os.getcwd()}\\Tempest_Images\\Mission_Rules')
            missionCards.pop("MAELSTROM OF BATTLE.txt")
            return self.getMissionRule(random.randrange(0, 10, 1))
        else:
            return missionRule
        
    def getPrimary(self):
        files = os.listdir(f'{os.getcwd()}\\Tempest_Images\\Mission_Primarys')
        file = files[f'{random.randrange(0, 5, 1)}']
        return {files:self.readRules(f'{os.getcwd()}\\Tempest_Images\\Mission_Primarys\\{files}')}
    
    def buildSecDeck(self):
        files = os.listdir(f'{os.getcwd()}\\Tempest_Images\\Mission_Secondarys')
        return {file: files[file] for file in files}
    
    ## TODO Handle Secondary draw 
    def handleSecondarys(self, currentSecondaryCt, roundNum):
        if roundNum == 1:
            for i in range 2:
                card = draw()
                # TODO Check card if possible -- maybe user input, maybe internal check
                ## Check for 1st round discard
                 
        def draw():
            key = self.secondaryDeck.keys()[(random.randrange(0, len(self.secondaryDeck.keys(), 1)))]
            return {key:self.secondaryDeck[key]}

if __name__ == "__main__":
    test = TempestGame("Tempest")
    print(test.showRules())