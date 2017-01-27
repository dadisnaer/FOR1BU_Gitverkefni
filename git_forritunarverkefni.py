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
#Byð notanda um texta
text=input("Sláðu inn texta ")
#Bý til teljara fyrir hástafi
telhastafi=0
#Bý til teljara fyrir lágstafi
tellagstafi=0
#Bý til teljara fyrir lágstafi sem eru eftir hástafi
tellagstafieftir=0

#Bý til for lykkju sem keyrir í gegnum textann
for x in range(len(text)):
    #Ef stafurinn í texta er bókstafur og er í hástaf
    if (text[x].isalpha() and text[x].isupper()):
        #Bæti 1 við teljara fyrir hágstafi
        telhastafi=telhastafi+1
        #Ef næsti stafur er lágstafur
        if (text[x+1].islower()):
            #Bæti 1 við teljara fyrir lágstafi á eftir hástafi
            tellagstafieftir=tellagstafieftir+1
    #Ef stafurinn í texta er bókstafur og er í lágstaf
    elif(text[x].isalpha() and text[x].islower()):
        #Bæti 1 við teljara fyrir lágstafi
        tellagstafi=tellagstafi+1
#Birti fjölda hástafi
print("Það komu",telhastafi,"hástafir")
#Birti fjölda lágstafi
print("Það komu",tellagstafi,"lágstafir")
#Birti fjölda lágstafi á eftir hástafi
print("Það komu",tellagstafieftir,"lágstafir koma strax á eftir hástaf")
