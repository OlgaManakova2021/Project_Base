def max2(max,min):
    if max > min:
        return max
    return min

def max3(a,b,c):
    return max2(a, max2(b,c))

a,b,c = int(input('Введи первое число:   ')), int(input('Введи второе число:   ')), int(input('Введи третье число:   '))

print('Максимальное число:   ',max3(a,b,c))