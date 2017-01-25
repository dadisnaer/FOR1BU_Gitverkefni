#Daði Snær Hálfdánsson
#25.01.17
#Git verkefni

#Liður 1
#Bið notanda um að slá inn tölu eitt
tala1=int(input("Sláðu inn tölu eitt "))
#Bið notanda um að slá inn tölu tvö
tala2=int(input("Sláðu inn tölu tvö "))
#Plúsa tölurnar saman
plus=tala1+tala2
#Margfalda tölurnar saman
marg=tala1*tala2
#Birti tölurnar lagðar saman
print("Tölurnar lagðar saman:",plus)
#Birti tölurnar margfaldaðar saman
print("Tölurnar margfaldaðar saman:",marg)

#Liður 2
#Bið notanda um fornafn
fornafn=input("Sláðu inn fornafn ")
#Bið notanda um eftirnafn
eftirnafn=input("Sláðu inn eftirnafn ")
#Birti nöfnin ásamt "Halló" í byrjun
print("Halló",fornafn,eftirnafn)

#Liður 3
text=input("Sláðu inn texta ")
telhastafir=0
tellagstafir=0
tellagstafireftira=0
for x in range(len(text)):
    if(text[x].isalpha() and text[x].isupper()):
        telhastafir=telhastafir+1
        if(text[x+1].islower()):
            tellagstafireftira=tellagstafireftira+1
    if (text[x].isalpha() and text[x].islower()):
        tellagstafir=tellagstafir+1
print("Í þessum texta eru",telhastafir," hástafir,")
print("                  ",tellagstafir," lágstafir")
print("Og",tellagstafireftira," koma strax á eftir hástaf.")
