import os
import random

# TODO 7/1/23
    # Fix .txt reading - special chars formatting as plain text instead of \n as linebreaks etc.
    # Implement secondary hand drawing and managamenet 
        # Draw 3 cards on round 1 
        # read each card, if card must be redrawn, reinsert drawn card into deck and draw new
        # check hand size, check phase, allow redraw - allow exception if card impossible 
    # Implement returning deployment zome image - may move down to SubClass 

# Mission class - sets gametype, game rules and deployment 
# Main class of specific missions - instantiate a mission type
class Mission:
    def __init__(self, gameType='Tempest'):
        self.gameType = gameType
        self.deployment = {}
        self.gameRules = self.getRules()

    # getRules() sets the gameRules attribute - callable from subMissionClass below 
    def getRules(self):
        rulesPath = f'{os.getcwd()}\\Tempest_Images\\Tempest_Rules.txt'
        ruleSets = {"Tempest":self.readRules(rulesPath)}
        return ruleSets[self.gameType]
    
    # readRules() method used to read rules files from filesystem - convenience method for populating game rules
    def readRules(self, path):
        contents = ""
        with open(path, 'r') as txtFile:
            contents = txtFile.read()
        return contents

# First of the "GameType" classes - Tempest of War 
# Inherits helpers from Mission - with callable attribute "gameRules" and "Deployment"
# helper function readRules() used below to populate attributes from rule.txt docs in filesystem
class TempestGame(Mission):
    def __init__(self, gameType='Tempest', mission_rule=random.randrange(0, 11, 1)):
        super().__init__(gameType)
        self.gameRules = self.gameRules
        self.missionRule = self.checkMaelstrom(self.getMissionRule(random.randrange(0, 12, 1)))
        self.primary = self.getPrimary()
        self.playerSecondarys = {
            "CurrentSecondary":{

            },
            "CurrentRound":1,
        }
        self.secondaryDeck = self.buildSecDeck()

    # Function for returning attribute "gameRules" of parent Class
    def showRules(self):
        return self.gameRules
    
    # getMissionRule reads a specified or random mission rule from the file system and returns its txt value 
    # if random, pass a # between 1-12 for random rule, else pass specific rule name 
        # method accepts missionRule as ambiguous argument (either int or str)
        # need to add error handling to commented Exception blocks (7/1/23)
    def getMissionRule(self, missionRule):
        directory = f'{os.getcwd()}\\Tempest_Images\\Mission_Rules'
        files = os.listdir(directory)
        if type(missionRule) == int:
            if missionRule > 0 and missionRule < len(files):
                return {files[missionRule].rstrip(".txt"):self.readRules(f'{directory}\\{files[missionRule]}')}
            else:
                pass #Raise Exception
        # Need to add handling for selected (may remove feature, sort of defeats purpose of Tempest games)
        elif missionRule.isalpha():
            return self.readRules(f'{directory}\\{missionRule}')
        else:
            pass # Raise Exception
    
    # checkMaelstrom() called above getMissionRule() on instantiation of tempest mission 
        # Maelstrom rule requires players to discard the Maelstrom care and draw 2 mission rules instead
        # If getMissionRule returns MAELSTROM then draw 2 new cards and set as mission rule 
    def checkMaelstrom(self, missionRule):
        if list(missionRule.keys())[0] == "MAELSTROM OF BATTLE":
            missionCards = os.listdir(f'{os.getcwd()}\\Tempest_Images\\Mission_Rules')
            missionCards.pop("MAELSTROM OF BATTLE.txt")
            return (self.getMissionRule(random.randrange(0, 10, 1)), self.getMissionRule(random.randrange(0, 10, 1)))
        else:
            return missionRule

    # Draw primary card randomly from file system (removed option to select - can add back later)    
    def getPrimary(self):
        files = os.listdir(f'{os.getcwd()}\\Tempest_Images\\Mission_Primarys')
        file = files[random.randrange(0, 5, 1)]
        return {file.rstrip(".txt"):self.readRules(f'{os.getcwd()}\\Tempest_Images\\Mission_Primarys\\{file}')}
    
    # Populates a dictionary of secondary missions - secondary cards should only be drawn once 
        # on draw, remove from deck and add to actives 
    def buildSecDeck(self):
        files = os.listdir(f'{os.getcwd()}\\Tempest_Images\\Mission_Secondarys')
        return {files[file].rstrip(".txt"): self.readRules(f'{os.getcwd()}\\Tempest_Images\\Mission_Secondarys\\{files[file]}') for file in range(len(files))}
    
    ## TODO Handle Secondary draw 
    def handleSecondarys(self, currentSecondaryCt, roundNum):
        if roundNum == 1:
            for i in range(2):
                card = draw()
                # TODO Check card if possible -- maybe user input, maybe internal check
                ## Check for 1st round discard
                 
        def draw():
            key = list(self.secondaryDeck.keys())[(random.randrange(0, len(self.secondaryDeck.keys(), 1)))]
            return {key.rstrip(".txt"):self.secondaryDeck[key]}

# Tester code 
if __name__ == "__main__":
    test = TempestGame("Tempest")
    print(test.missionRule)