import random

javab = random.randint(1,9)
hads = input("Welcom to bazi hads add: ")

hads = int(hads)

while hads != javab:
    if hads > javab:
        print("add man bozorg tar ast")       
    else:
        print("add man kohectar ast")
        hads = input("hads badi to chieh! ")
        hads = int(hads)
        if javab == 99:
            break

print("Hoooraaaaaa")
