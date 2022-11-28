#8 Nov 2022

#sum
def sum(*ang):
    total = 0
    for number in ang:
        total += number
    return total
    return sum

#average
def average(*ang):
    total = 0
    jumlah = len(ang)
    for number in ang:
        total += number
    hasil = total/jumlah
    return hasil
    return average

#max
def max(*ang):
    max = ang[0]
    for item in ang:
        if(item > max):
            max = item
    return max

#min
def min(*ang):
    min = ang[0]
    for item in ang:
        if(item < min):
            min = item
    return min
