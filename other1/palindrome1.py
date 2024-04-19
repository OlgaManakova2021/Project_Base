def get_word():
    return input("Введите слово:  ")

def is_palindrome(send):
    return "палиндром" if send == send[::-1] else "не палиндром"

def create_message(word, what_is):
    if what_is:
        return "Слово %s - %s" % (word, what_is)
    else:
        return "Слово %s - %s" % (word, what_is)

def check_palindrome():
    print("Поиск палиндромов")
    word = get_word()
    what_is = is_palindrome(word)
    print(create_message(word, what_is))

check_palindrome()