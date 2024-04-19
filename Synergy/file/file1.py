# f2 = open('123.txt', 'w')
# f2.write('This is ...')
# f2.close()
#
# f2 = open('123.txt')
# print(f2.read())
# f2.close()


l = ['2, 4, 6, 8']
f3 = open('data_3.txt', 'w')
f3.writelines(l)
f3.close()
