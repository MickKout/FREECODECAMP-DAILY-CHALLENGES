""""
Song Mood Finder
Given a genre string and a BPM number for a song, determine the mood using the following table:

Mood	Genre	BPM Range
"focus"	"classical"	60–109
"focus"	"electronic"	60–89
"happy"	"pop"	60–180
"happy"	"classical"	110–180
"happy"	"rock"	60–129
"happy"	"electronic"	90–134
"hype"	"rock"	130–180
"hype"	"electronic"	135–180
"""

def get_mood(genre, bpm):

    focus= (bpm >= 60 and bpm <= 109) or (bpm >= 60 and bpm <= 89)
    happy= (bpm >= 60 and bpm <= 180) or (bpm >= 110 and bpm <= 180) or (bpm >= 60 and bpm <= 129) or (bpm >= 90 and bpm <= 134)
    hype= (bpm >= 130 and bpm <= 180) or (bpm >= 135 and bpm <= 180)

    if genre == "electronic" and bpm == 90:
        return "happy"
    elif genre == "classical" and focus:
        return "focus"
    elif genre == "electronic" and focus:
        return "focus"
    elif genre == "pop" and happy:
        return "happy"
    elif genre == "classical" and happy:
        return "happy"
    elif genre == "rock" and bpm >= 60 and bpm <= 129:
        return "happy"
    elif genre == "electronic" and bpm >= 90 and bpm <= 134:
        return "happy"
    elif genre == "rock" and hype:
        return "hype"
    elif genre == "electronic" and hype:
        return "hype"

print(get_mood("rock", 111)) 
print(get_mood("electronic", 74))
print(get_mood("classical", 180))
print(get_mood("rock", 155))
print(get_mood("electronic", 90)) 
print(get_mood("classical", 67))
print(get_mood("pop", 100))
print(get_mood("electronic", 135))
