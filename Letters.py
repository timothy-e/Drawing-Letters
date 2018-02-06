alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def print_art(msg, filename):
    ind = []
    msg = msg.upper()
    for i in msg:
        if i == " ":
            ind = ind + [" "]
        else:
            ind = ind + [alphabet.index(i)]

    # convert file to list
    letters = [[],[],[],[],[],[]]
    with open(filename) as file:
        i = 0
        for line in file:
            letters[i % 6].append(line.rstrip("$\n"))
            i += 1
    
    for r in range(0, 5):
        s = ""
        for i in ind:
            if i == " ":
                s += "    "
            else:
                s += letters[r][i]
        print(s)

while (True):
    msg = input("What would you like to print? (*exit to quit) ")
    print("\n")
    if (msg == "*exit"):
        break
    print_art(msg, "letters.txt")
    print("\n")
print("Goodbye!")
