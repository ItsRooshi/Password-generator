from random import randint

chars = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é~\"#'\{[()]\}-|è`_\\ç^à@)=+°ù%$£¤*µ!§:/;.,?<>")
carryOn = True


while carryOn:
    password = ""


    try:
        nbchar = int(input("How many characters ?"))
    except:
        print("please type a number")
        continue

    for i in range(nbchar):
        char = ""
        random = randint(0,len(chars)-1)
        password += chars[random]
    print(password)
    
    if input("Hit r to regenerate or any other key to exit") == "r":
        continue
    else:
        carryOn = False