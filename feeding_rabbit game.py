# Feeding the Rabbit Game

map = input("Please enter feeding map as a list:\n")
# input should be like this
# [[’W’, ’X’, ’W’, ’C’, ’X’], [’A’, ’X’, ’X’, ’A’, ’W’], [’C’, ’X’, ’X’,’X’, ’P’], [’X’, ’X’, ’X’, ’X’, ’X’], [’X’, ’*’, ’X’, ’X’, ’X’]]

liste = [i for i in map if i == "X" or i == "A" or i == "C" or i == "W" or i == "*" or i == "P" or i == "M"]
a = len(liste)//(map.count("]")-1)

movements = input("Please enter direction of movements as a list:\n")
# input should be like this
# [’U’,’U’,’L’,’U’,’L’]

movementsliste = [i for i in movements if i == "R" or i == "L" or i == "U" or i == "D"]

mapliste = []
c = 0
b = 1
while b*a <= len(liste):            #creating board to list
    liste1 = liste[c*a:b*a]
    mapliste.append(liste1)
    c += 1
    b += 1

print("Your board is:")         #print first board
for i in mapliste:
    for j in i:
        print(j, end=" ")
        if j == "*":                 #location of rabbit
            n = mapliste.index(i)
            m = i.index(j)
    print()

score=0
#rabbit's movement and score
for x in movementsliste:
    if x == "R" and m+1 <= a-1:
        m += 1
        if mapliste[n][m] == "X":
            mapliste[n][m-1] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "W":
            m -= 1
            continue
        elif mapliste[n][m] == "M":
            score -= 5
            mapliste[n][m-1] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "A":
            score += 5
            mapliste[n][m-1] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "C":
            mapliste[n][m-1] = "X"
            mapliste[n][m] = "*"
            score += 10
        elif mapliste[n][m] == "P":
            mapliste[n][m-1] = "X"
            mapliste[n][m] = "*"
            break

    elif x == "L" and m-1 >= 0:
        m += -1
        if mapliste[n][m] == "X":
            mapliste[n][m+1] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "W":
            m += 1
            continue
        elif mapliste[n][m] == "M":
            score = score-5
            mapliste[n][m+1] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "A":
            score += 5
            mapliste[n][m+1] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "C":
            score += 10
            mapliste[n][m+1] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "P":
            mapliste[n][m+1] = "X"
            mapliste[n][m] = "*"
            break

    elif x == "U" and n-1 >= 0:
        n += -1
        if mapliste[n][m] == "X":
            mapliste[n+1][m] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "W":
            n += 1
            continue
        elif mapliste[n][m] == "M":
            score=score-5
            mapliste[n+1][m] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "A":
            score += 5
            mapliste[n+1][m] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "C":
            score += 10
            mapliste[n+1][m] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "P":
            mapliste[n+1][m] = "X"
            mapliste[n][m] = "*"
            break

    elif x == "D" and n+1 <= len(liste)//a-1:
        n += 1
        if mapliste[n][m] == "X":
            mapliste[n-1][m] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "W":
            n += -1
            continue
        elif mapliste[n][m] == "M":
            score = score-5
            mapliste[n-1][m] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "A":
            score += 5
            mapliste[n-1][m] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "C":
            score += 10
            mapliste[n-1][m] = "X"
            mapliste[n][m] = "*"
        elif mapliste[n][m] == "P":
            mapliste[n-1][m] = "X"
            mapliste[n][m] = "*"
            break

print("Your output should be like this:")        #print last board
for i in mapliste:
    for j in i:
        print(j,end=" ")
    print()
print("Your score is:", score)       #print score
