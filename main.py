import random

words = ['backlog', 'beacon', 'bike', 'bone', 'broke']
word = random.choice(words)
good_guesses = [None for good_guess in word]
guesses = []
x = True

while x:
    letter = input("Please enter your letter:")

    # check if variable letter contains only letters and if there is only one letter
    if not letter.isalpha() and len(letter) == 1:
        print("Sorry, you must enter only a single letter.")
        continue

    # check if the letter was already guessed
    if letter in guesses:
        print("You have already guessed this letter.")
        continue

    # if you guessed the letter, add it to already guessed ones
    guesses.append(letter)

    # check if the letter is in a word
    good_indexes = []
    for i in range(len(word)):
        if word[i] == letter:
            good_indexes.append(i)

    # check if there was actually a good guess
    if len(good_indexes) == 0:
        print("Wrong guess.")
        continue

    print("Good guess!")
    print(f"Those are letter(s) of index(es) {good_indexes}")

    for letter_index in good_indexes:
        # add the correctly guessed letters to a list
        good_guesses[letter_index] = letter

    # print only correctly guessed letters
    print([l for l in good_guesses if l is not None])

    # Finishing the process when player guessed all letters
    if None not in good_guesses:
        print("Nice job! You won!")
        x = False
