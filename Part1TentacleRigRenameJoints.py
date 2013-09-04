import pymel.core as pm

jointArray = pm.ls (sl=True)

#description strings
assetName = "Tentacle"
assetType = "Character"
description = "Arm"
objType = "skinBone"
divider = "_"

for i in range (0,len(jointArray), 1):
    pm.rename ("joint" + str(i+1), assetName + divider + assetType + divider + description + str(i+1) + divider + objType )

