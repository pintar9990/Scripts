import string, random,time, webbrowser

for k in range(25):
    randome = ""
    for x in range(16):
        y = random.randrange(1, 3, 1)
        if y % 2 == 0:
            rstr = random.choice(string.ascii_letters)
        else:
            rstr = str(random.randrange(1, 10, 1))

        randome = randome + rstr

    webbrowser.open('https://www.bing.com/search?q=' + randome)
    time.sleep(1)

exit()

