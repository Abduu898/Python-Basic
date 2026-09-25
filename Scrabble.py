def scrabble_score(word):
    values = {
        1:  "AEIOULNSTR",
        2:  "DG",
        3:  "BCMP",
        4:  "FHVWY",
        5:  "K",
        8:  "JX",
        10: "QZ",
    }
    points = {}
    for score, letters in values.items():
        for letter in letters:
            points[letter] = score

    total = 0
    for c in word:
        total += points.get(c.upper(), 0) ## look uo for th eletter in the point dic 
    return total

print(scrabble_score("Test"))
