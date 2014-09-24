# Kodutoo 1
# 05.09.2014
# Andres Liiver

for i in range(1, 101):
    print( str(i) + ": " + str(i), end = "" )
    sum = pudeleid_alles = i

    while pudeleid_alles >= 3:
        sum += pudeleid_alles // 3
        print( " + " + str(pudeleid_alles // 3), end = "" )
        pudeleid_alles = (pudeleid_alles % 3) + (pudeleid_alles // 3)

    print( " = " + str(sum) )