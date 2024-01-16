import pandas 

nato_word = pandas.read_csv("nato_word.csv")

nato_word_dict = {row.letter:row.code for (index,row) in nato_word.iterrows()}
is_not_correct = True
while is_not_correct:
    try:
        user_input = input("Enter the word: ").upper()
        word_list= [nato_word_dict[letter] for letter in user_input]
    except KeyError :
        print("Sorry, only letters in alphabet please.")
    else:
        is_not_correct = False
    
print(word_list)