filesnames = ["CHILLING RAIN",
              "SECRET INTEL",
              "DELAYED RESERVES",
              "SUPPLY LINES",
              "HIDDEN SUPPLIES",
              "SWEEP AND CLEAR",
              "MAELSTROM OF BATTLE",
              "TACTICAL RESERVES",
              "PALL OF DREAD",
              "VOX STATIC",
              "SCRAMBLER FIELDS"]

missionPrimary = [
    "BURN AND RAZE",
    "PRIORITY TARGETS",
    "CLAIM THE BATTLEFIELD",
    "TAKE AND HOLD",
    "VITAL GROUNDS",
    "DIRECT ASSAULT"
]

missionSecondary = [
    "A TEMPTING TARGET",
    "EXTEND BATTLE LINES",
    "AREA DENIAL",
    "GRIND THEM DOWN",
    "ASSASSINATION",
    "HOLD THE LINE",
    "BATTLEFIELD SUPREMACY",
    "INVESTIGATE SITE",
    "BEHIND ENEMY LINES",
    "NO PRISONERS",
    "BLOOD AND GUTS",
    "NO RETREAT, NO SURRENDER",
    "BRING IT DOWN",
    "OVERWHELMING FIREPOWER",
    "CAPTURE ENEMY OUTPOST",
    "DEFEND STRONGHOLD",
    "RAISE BANNER",
    "DEPLOY TELEPORT HOMER",
    "SECURE NO MAN’S LAND",
    "STORM HOSTILE OBJECTIVE"
]

filePath = "C:/Users/Michael Rufo/Documents/GitHub_Projects/justicefriends/Tempest_Images/Mission_Secondarys/"

for i in missionSecondary:
    with open(filePath + i + ".txt", "w") as file:
        pass
