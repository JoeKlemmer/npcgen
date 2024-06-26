import random

# NPC Generator Tables
weakness = {
    0: "Weakness -> ",
    1: "Blunt, speaks in short, direct sentences",
    2: "Fearful, seems paranoid and afraid",
    3: "Talkative, talks too much, overshares",
    4: "Jealous, jealous of other players",
    5: "Depressed, sad, speaks softly",
    6: "Angry, shouts, dislikes players",
    7: "Quiet, speaks softly, only when spoken to",
    8: "Suspicious, doesn't trust others",
    9: "Impatient, rushes players",
    10: "Manic, overly joyfull, nearly crazy",
}

strength = {
    0: "Strength -> ",
    1: "Honest, always tells the truth",
    2: "Brave, doesn't back down, even when threatened",
    3: "Good Humored, can take jokes/teasings",
    4: "Friendly, befriends all, happy to see others",
    5: "Helpful, will assist player in any way",
    6: "Smart, can assist players with Knowledge checks",
    7: "Generous, gives freely and abundently",
    8: "Charitable, gives what thw can to the less fortunate",
    9: "Pioius, uses religion to better themselves",
    10: "Defender, will fight to defent others",
}

fear = {
    0: "Fear -> ",
    1: "Dark Secret Revieled",
    2: "Losing Loved Ones",
    3: "Being Alone",
    4: "Rejection",
    5: "Death",
    6: "Losing Material Wealth",
    7: "Failing",
    8: "Change",
}

desire = {
    0: "Desire -> ",
    1: "Political Power",
    2: "Physical Power",
    3: "Wealth",
    4: "Health",
    5: "Love",
    6: "Friendship",
    7: "See The World",
    8: "Revenge",
}

print(len(weakness))
print(len(strength))
print(len(fear))
print(len(desire))

random.seed()

for i in [weakness, strength, fear, desire]:
    choice = random.randint(1, len(i))
    print(i[0], i[choice])

# for i in [weakness, strength]:
    # choice1 = random.randint(1, 10)
    # print(i[0], i[choice1])

# for i in [fear, desire]:
    # choice2 = random.randint(1, 8)
    # print(i[0], i[choice2])
