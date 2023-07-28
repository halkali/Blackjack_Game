import random
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
kasa = []
dealer=[]
a=True
for i in range(2):
    kasa.append(deck[random.randint(0, len(deck)-1)])
    dealer.append(deck[random.randint(0, len(deck)-1)])

def deal(dealer):
    toplam = 0
    for i in dealer:
        toplam +=i
    return toplam

def kas(kasa):
    toplam = 0
    for i in kasa:
        toplam += i
    return toplam

while a:
    print(dealer)
    print(kasa)

    if deal(dealer) <21:
        if(input("another card? y or n:")) == "y":
            dealer.append(deck[random.randint(0, len(deck)-1)])
            if kas(kasa) < 17:
                kasa.append(deck[random.randint(0, len(deck) - 1)])

        id(deal(dealer) == kas(kasa))
        if(deal(dealer)<kas(kasa)):
            if(kas(kasa)>21):
                print("you win!")
            else:
                print("you lose")
            a=False
        elif(deal(dealer)>kas(kasa)) and deal(dealer)<21:
            print("you win")
            a=False


    if deal(dealer) ==21:
        if(kas(kasa)==21):
            print("deal")
            a=False
        print("winner!")
        a = False

    if deal(dealer) >21:
        print("you lose!")
        a =False

print(dealer)
print(kasa)



