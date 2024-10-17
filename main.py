#Project will allow for people to write a word, project will show an image of that word in ASL

def word_list(word:str)->list[str]:
    '''Takes the word input and then converts it into a list of each letter'''
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    print(letter_list)

#def letter_to_image(letters:list[str]):


word = input("Your Word!")
word_list(word.lower())