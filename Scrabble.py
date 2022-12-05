letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = dict(zip(letters, points))
print(letter_to_points)

letter_to_points[""] = 0
print(letter_to_points)

total_points = 0
playerName = input('What is your Name?').upper()
usedLetters= []

for letters in playerName:
    if letters in letter_to_points and letters not in usedLetters:
        usedLetters.append(letters)
        total_points += letter_to_points[letters]

print('Your name is worth %d points' % total_points)