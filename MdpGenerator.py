from random import randint

chars = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é~\"#'\{[()]\}-|è`_\\ç^à@)=+°ù%$£¤*µ!§:/;.,?<>")
mdp = ""
nbchar = int(input("combien de charactères ?"))

for i in range(nbchar):
    char = ""
    random = randint(0,len(chars)-1)
    mdp += chars[random]
print(mdp)

input("Tapez sur entrer pour fermer")