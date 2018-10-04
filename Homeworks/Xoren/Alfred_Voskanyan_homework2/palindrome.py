def is_palindrome(word: str):
    l = len(word)
    for i in range(l//2):
        if word[i] != word[l-i-1]:
            return False
    return True

while True:
    word = input("Enter the word or type 'exit' to exit")
    if word == 'exit':
        print("Thanks")
        break
    print("The word", word, "is a palindrome" if is_palindrome(word) else "is not a palindrome")