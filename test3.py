from datetime import datetime
name=input("enter your name")
lists='''
Rice  Rs 20/kg
sugar Rs 30/kg
salt  Rs 20/kg
oil   Rs 80/liter
paneer Rs 110/kg
maggie Rrs 50/kg
Boost Rs 90/each
colgate Rs 70/each
'''
print(lists)
price=0
pricelist=[]
Totalprice=0
finalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggie':50,'Boost':90,'colgate':70}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to but press 1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items")
        quantity=int(input("enter your quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            Totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(Totalprice*5)/100
            finalprice=gst+Totalprice
        else:
            print("sorry you entered item is available")
    else:
        print("you entered wrong number")
    inp=input('can i bill the items yes or no:')
    if inp=='yes':
        pass
        if finalprice!=0:
            print(25*"=","kiran supermarket",25*"=")
            print(28*" ","wanaparthy")
            print("name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')



            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
                print(75*"-")
                print(50*" ",'finalprice:','rs',finalprice)
                print(75*"-")
                print(20*" ","thanks for visiting")
                print(75*"-")