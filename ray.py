print ('Choose an operation:')

def reverse(text): #1
    return text[::-1]
def countVowels(text): #2
    vowel = 'aeiouAEIOU'
    return str(sum(1 for char in text if char in vowel))
def palindrome(text): #3
    words = text.split()
    result = {}
    for word in words:
        result[word] = (word.lower() == word.lower()[::-1])
    return result
def replace(text): #4
    while True:
        oldWord = input('Enter word to find: ')
        replaceWord = input('Enter replacement word: ')
        if oldWord not in text:
            print(f"{oldWord} not in the sentence! Please choose the right word.")
        else:
            return text.replace(oldWord, replaceWord)
def format(text): #5
    result = ""
    words = text.split()
    for word in words:
        result += word[0].upper() + word[1:].lower() + " "
    return result.strip()
def split(text): #6
    return text.split()
def frequency(text): #7
    words = text.split()
    freq = {}
    for eachword in words:
        wordlow = eachword.lower()
        freq[wordlow] = freq.get(wordlow, 0) + 1
    return freq
def swap_case(text): #8
    result = ""
    for char in text: 
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

sentence = input('Enter a sentence: ')

while True:
    choices = int(input("\n[1] Reverse the Sentence \n[2] Count Vowels \n[3] Check if Palindrome \n[4] Find and replace a Word" \
    "\n[5] Format (Title Case) \n[6] Split into Words \n[7] Word frequency Counter \n[8] Swap Case \n[9] Exit \nAnswer: " ))
    print("")
    match choices:
        case 0: sentence = input("Enter a new sentence: ")
        case 1: print("Reverse: " + reverse(sentence))
        case 2: print("Vowels: " + countVowels(sentence))
        case 3: print("Palindrome: ", palindrome(sentence))
        case 4: print("New Sentence: " + replace(sentence))
        case 5: print("Format in Title Case: " + format(sentence))
        case 6: print("Split Words: ", split(sentence))
        case 7: print("Word Frequency: ", frequency(sentence))
        case 8: print("Swap Case: " + swap_case(sentence))
        case 9: break
        case _: print("Invalid input, Pls choose from 1-9")
