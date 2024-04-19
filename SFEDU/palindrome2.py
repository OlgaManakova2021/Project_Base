def get_word():
    return input("Введите слово:  ")

def is_palindrome():
    return "палиндром" if word == word[::-1] else "не палиндром"

def create_message():
    if what_is:
        return "Слово %s - %s" % (word, what_is)
    else:
        return "Слово %s - %s" % (word, what_is)

def check_palindrome():
    global word, what_is # так делать ПЛОХО!!!
    print("Поиск палиндромов")
    word = get_word()
    what_is = is_palindrome()
    print(create_message())

check_palindrome()


# print("Поиск палиндромов")
# word = get_word()
# what_is = is_palindrome()
# print(create_message())
