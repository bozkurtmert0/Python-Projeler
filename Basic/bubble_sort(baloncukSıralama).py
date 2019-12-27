def siralama(array):
    for i in range(1, len(array)):
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array

numaralar = [1, 12, 7, 3, 14, 1, 8, 555, 68, 9, 99, 17] #numbers

print("Sıralanmış Array: {}".format(siralama(numaralar)))