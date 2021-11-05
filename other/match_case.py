def get_mood(day):
    match day:
        case 'Monday':
            return 'Oh...'
        case 'Thursday':
            return 'Getting close!'
        case 'Friday':
            return 'Almost there!'
        case 'Saturday' | 'Sunday':
            return 'Weekend!!!'
        case _:
            return 'Meh...'


print(get_mood(day='Monday'))
# Oh...
print(get_mood(day='Wednesday'))
# Meh...
print(get_mood(day='Friday'))
# Almost there!
print(get_mood(day='Sunday'))
# Weekend!!!