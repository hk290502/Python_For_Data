

brutus_speech = "There is a tide in the affairs of men \nWhich, taken at the flood, leads on to fortune; \nOmitted, all the voyage of their life \nIs bound in shallows and in miseries. \nOn such a full sea are we now afloat, \nAnd we must take the current when it serves, \nOr lose our ventures."


number_of_words = print(f"\nNumber of Words = {len(brutus_speech.split())}\n")


two_letter_count = 0
three_letter_count = 0
four_letter_count = 0
five_letter_count = 0
six_letter_count = 0
seven_letter_count = 0
eight_letter_count = 0
nine_letter_count = 0


print("Word Lengths:")

for word in brutus_speech.split():
   
    length = len(word)
    print(f"'{word}': {length}")
    
    # 4. Count 2 or 3 letter words
    if length == 2:
        two_letter_count += 1
    elif length == 3:
        three_letter_count += 1
    elif length == 4:
        four_letter_count += 1
    elif length == 5:
        five_letter_count += 1
    elif length == 6:
        six_letter_count += 1
    elif length == 7:
        seven_letter_count += 1
    elif length == 8:
        eight_letter_count += 1
    elif length == 9:
        nine_letter_count += 1

print("-" * 20)
print(f"Total 2-letter words: {two_letter_count}")
print(f"Total 3-letter words: {three_letter_count}")
print(f"Total 4-letter words: {four_letter_count}")
print(f"Total 5-letter words: {five_letter_count}")
print(f"Total 6-letter words: {six_letter_count}")
print(f"Total 7-letter words: {seven_letter_count}")
print(f"Total 8-letter words: {eight_letter_count}")
print(f"Total 9-letter words: {nine_letter_count}")

