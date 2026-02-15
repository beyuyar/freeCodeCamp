"""2026 Winter Games Day 10: Alpine Skiing
Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill by taking the drop divided by the distance.
Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2
"Slalom": multiply steepness by 0.9
"Giant Slalom": multiply steepness by 1.0
Return:

"Green" if the adjusted steepness is less than or equal to 0.1
"Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
"Black" if the adjusted steepness is greater than 0.25

Passed: 1. get_hill_rating(95, 900, "Slalom") should return "Green".
Passed: 2. get_hill_rating(620, 2800, "Downhill") should return "Black".
Passed: 3. get_hill_rating(420, 1680, "Giant Slalom") should return "Blue".
Passed: 4. get_hill_rating(250, 3000, "Downhill") should return "Green".
Passed: 5. get_hill_rating(110, 900, "Slalom") should return "Blue".
Passed: 6. get_hill_rating(380, 1500, "Giant Slalom") should return "Black"."""

def get_hill_rating(drop, distance, hill_type):
    steep = drop/distance
    hill_type_multiplier = 0
    if hill_type == "Downhill":
        hill_type_multiplier = 1.2
    elif hill_type == "Slalom":
        hill_type_multiplier = 0.9
    elif hill_type == "Giant Slalom":
        hill_type_multiplier = 1.0    
    adjusted_steepness = steep*hill_type_multiplier

    if adjusted_steepness <= 0.1:
        return "Green"
    elif adjusted_steepness <= 0.25:
        return "Blue"
    elif adjusted_steepness > 0.25:
        return "Black"
    return drop