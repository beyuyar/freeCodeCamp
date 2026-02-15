"""2026 Winter Games Day 9: Skeleton
Given a string representing the curves on a skeleton track, determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment
Each direction change adds 15 points (an "L" followed by an "R" or vice versa).
All other curves add 5 points each (all other "L" or "R" characters).
Straight segments add 0 points.
The difficulty of the track is based on the total score. Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200


Passed: 1. get_difficulty("SLSLLSRRLSRLRL") should return "Easy".
Passed: 2. get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS") should return "Hard".
Passed: 3. get_difficulty("SRRRRLSLLRLRSSRLSRL") should return "Medium".
Passed: 4. get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL") should return "Hard".
Passed: 5. get_difficulty("SLLSSLRLSLSLRSLSSLRL") should return "Medium".
Passed: 6. get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR") should return "Easy"."""
#** start of main.py **

"""def get_difficulty(track):
    moves = list(track)
    points = 0
    for n,m in enumerate(moves):
        if m == "L":
            if moves[n-1] == "R":
                points += 15
            else:
                points += 5
        if m == "R":
            if moves[n-1] == "L":
                points += 15
            else:
                points += 5
    if points >= 0 and points <= 100:
        return "Easy"
    elif points >= 101 and points <= 200:
        return "Medium"
    else:
        return "Hard"
    return track

print(get_difficulty("SLSLLSRRLSRLRL"))
print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))
print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))
print(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"))
print(get_difficulty("SLLSSLRLSLSLRSLSSLRL"))
print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))"""

#** end of main.py **

#VER 2.0

def get_difficulty(track):
    moves = list(track)
    points = 0
    for n,m in enumerate(moves):
        if not m == "S":
            if n == 0:
                points +=5
            else:
                if moves[n-1] != m and moves[n-1] != "S":
                    points += 15
                else:
                    points += 5
    if  points <= 100:
        return "Easy"
    elif points <= 200:
        return "Medium"
    else:
        return "Hard"
    return track

print(get_difficulty("SLSLLSRRLSRLRL"))
print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))
print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))
print(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"))
print(get_difficulty("SLLSSLRLSLSLRSLSSLRL"))
print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))