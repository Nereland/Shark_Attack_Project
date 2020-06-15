def InjuryType(x):
    if "fatal" in x:
        return "Fatal"
    elif "no harm" in x:
        return "No harm"
    elif "clothing" in x:
        return "No harm"
    elif "dinghy" in x:
        return "No harm"
    elif "tried to" in x:
        return "No harm"
    elif "no injury" in x:
        return "No harm"
    elif "no inury" in x:
        return "No harm"
    elif "shark leapt" in x:
        return "No harm"
    elif "leg"in x:
        return "Lower limbs"
    elif "knee"in x:
        return "Lower limbs"
    elif "shin"in x:
        return "Lower limbs"
    elif "thigh"in x:
        return "Lower limbs"
    elif "foot" in x:
        return "Lower limbs"
    elif "feet" in x:
        return "Lower limbs"
    elif "ankle" in x:
        return "Lower limbs"
    elif "calf" in x:
        return "Lower limbs"
    elif "wrist" in x:
        return "Upper limbs"
    elif "radious" in x:
        return "Upper limbs"
    elif "arm" in x:
        return "Upper limbs"
    elif "hand" in x:
        return "Upper limbs"
    elif "arms" in x:
        return "Upper limbs"
    elif "shoulder" in x:
        return "Upper limbs"
    elif "minor" in x:
        return "Minor"
    elif "heel" in x:
        return "Minor"
    elif "fingers" in x:
        return "Minor"
    elif "finger" in x:
        return "Minor"
    elif "toe" in x:
        return "Minor"
    elif "fingernails"in x:
        return "Minor"
    elif "fingernail" in x:
        return "Minor"
    elif "severe" in x:
        return "Severe"
    elif "'serious" in x:
        return "Severe"
    elif "'fearful'" in x:
        return "Severe"
    elif "ribs" in x:
        return "Severe"
    elif "seriously" in x:
        return "Severe"
    elif "injured" in x:
        return "Severe"
    elif "ribs" in x:
        return "Severe"
    elif "face" in x:
        return "Severe"
    elif "neck" in x:
        return "Severe"
    elif "head" in x:
        return "Severe"
    elif "hip" in x:
        return "Severe"
    elif "chest" in x:
        return "Severe"
    elif "torso" in x:
        return "Severe"
    elif "abdomen" in x:
        return "Severe"
    elif "bite to face" in x:
        return "Severe"
    elif "major"in x:
        return "Severe"
    elif "multiple injuries" in x:
        return "Severe"
    elif "lacerations" in x:
        return "Lacerations"
    elif "laceration" in x:
        return "Lacerations"
    elif "lacerated" in x:
        return "Lacerations"
    elif "bitten" in x:
        return "Bitten"
    elif "abrasions" in x:
        return "Abrasions"
    elif "abrasion" in x:
        return "Abrasions"
    elif "perished" in x:
        return "Deads related with sharks but not due to attacks"
    elif "survived" in x:
        return "No information about type of injury"
    elif "survivor" in x:
        return "No information about type of injury"
    else: 
        return "Doubtful data"





def Activity(x):
    
    if "surf" in x:
        return "Surfing"
    elif "surfing" in x:
        return "Surfing"
    elif "boogie" in x:
        return "Surfing"
    elif "body-boarding" in x:
        return "Surfing"
    elif "body boarding" in x:
        return "Surfing"
    elif "bathing" in x:
        return "Swimming"
    elif "floating" in x:
        return "Swimming"
    elif "swimming" in x:
        return "Swimming"
    elif "swim" in x:
        return "Swimming"
    elif "spearfishing" in x:
        return "Swimming"
    elif "treading" in x:
        return "Swimming"
    elif "snorkeling" in x:
        return "Diving"
    elif "diving" in x:
        return "Diving"
    elif "dive" in x:
        return "Diving"
    elif "diving" in x:
        return "Diving"
    elif "free diving" in x:
        return "Diving"
    elif "kayak"in x:
        return "In kayak or canoe"
    elif "canoeing"in x:
        return "In kayak or canoe"
    elif "paddle"in x:
        return "In kayak or canoe"
    elif "paddling"in x:
        return "In kayak or canoe"
    elif "rowing"in x:
        return "In kayak or canoe"
    elif "boating" in x:
        return "Boating"
    elif "boat" in x:
        return "Boating"
    elif "scuba" in x:
        return "Diving"
    elif "shark" in x:
        return "Shark fishing"
    elif "fishing" in x:
        return "Fishing"
    elif "fish" in x:
        return "Fishing"
    elif "sail" in x:
        return "Sailing"
    elif "splashing" in x:
        return "Playing"
    elif "jumping" in x:
        return "Playing"
    elif "splashing" in x:
        return "Playing"
    elif "ski" in x:
        return "Skiing"
    else: 
        return "Sole cases or undescribed activities"
    


def Fatal_injury(x, y):
    if x == "0" and y == "fatal":
        return "Y"
    elif x== "0" and y != "fatal":
        return "N"
    else:
        return x


def Activity_injury(x, y):
    if x == "Swimming" and y == "Lower limbs":
        return "Swim_Lower"
    elif x == "Swimming" and y == "Fatal":
        return "Swim_Death"
    elif x == "Swimming" and y == "No harm":
        return "Swim_Noharm"
    elif x == "Swimming" and y == "Upper limbs":
        return "Swim_Upper"
    elif x == "Surfing" and y == "Lower limbs":
        return "Surf_Lower"
    elif x == "Surfing" and y == "Fatal":
        return "Surf_Death"
    elif x == "Surfing" and y == "No harm":
        return "Surf_Noharm"
    elif x == "Surfing" and y == "Upper limbs":
        return "SurfUpper"
    elif x == "Diving" and y == "Lower limbs":
        return "Divi_Lower"
    elif x == "Diving" and y == "Fatal":
        return "Divi_Death"
    elif x == "Diving" and y == "No harm":
        return "Divi_Noharm"
    elif x == "Diving" and y == "Upper limbs":
        return "Divi_Upper"
    elif x == "Fishing" and y == "Lower limbs":
        return "Fish_Lower"
    elif x == "Fishing"  and y == "Fatal":
        return "Fish_Death"
    elif x == "Fishing"  and y == "No harm":
        return "Fish_Noharm"
    elif x == "Fishing"  and y == "Upper limbs":
        return "Fish_Upper"
    else:
        return "mix"
    