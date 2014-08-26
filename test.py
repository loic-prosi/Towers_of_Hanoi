nb_disc = [1, 8, 12]

def input_n():
    global n
    n = int(input('Number of discs : '))
    return n
    nb_disc.append(n)

input_n()

print(nb_disc)
