import string, random, os

with open('Buscador aleatorio.bat', 'w') as f:
    f.writelines("start msedge\n")
    for k in range(35):
        randome = ""
        for x in range(16):
            y = random.randrange(1, 3, 1)
            if y % 2 == 0:
                rstr = random.choice(string.ascii_letters)
            else:
                rstr = str(random.randrange(1, 10, 1))

            randome = randome + rstr

        f.writelines("start msedge " + "https://www.bing.com/search?q=" + randome +"\n")
        f.writelines("timeout /T 1 > nul\n")
    f.writelines("exit")

f.close()

os.startfile("Buscador aleatorio.bat")
exit()
