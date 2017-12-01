def pizza_party(slices_of_pizza, bottles_of_beer, glasses_of_wine, bags_of_chips, bars_of_chocolate):
	print "You have %d slices of pizza!" % slices_of_pizza
	print "You have %d bottles of beer!" % bottles_of_beer
	print "You have %d glasses of wine!" % glasses_of_wine
	print "You have %d bags of chips!" % bags_of_chips
	print "You have %d bars of chocolate!" % bars_of_chocolate 
	print "Boy, thats gonna be a nice party!"
	print "Get a plate.\n"
	
pizza_party(10, 10, 20, 30, 50)
	

peperoni_pizza_slices=4
heineken_beer = 8
merlot_glasses = 15
lays_chips = 16
milka_chocolate = 23
pizza_party(peperoni_pizza_slices, heineken_beer, merlot_glasses, lays_chips, milka_chocolate)

pizza_hawaii = int(raw_input("How many slices Pizza Hawaii do you have?"))
becks_beer = int(raw_input("How many bottles of Becks beer do you have?"))
chardonnay_glasses = int(raw_input("How many glasses Chardonnay do you have?"))
salt_vinegar = int(raw_input("How many Bags Salt and Vinegar chips do you have?"))
oreo_chocolate = int(raw_input("How many bars of Oreo chocolate do you have?"))
pizza_party(pizza_hawaii, becks_beer, chardonnay_glasses, salt_vinegar, oreo_chocolate)

pizza_party(peperoni_pizza_slices*5,heineken_beer*2, merlot_glasses-3, lays_chips+37.5, milka_chocolate/2)

pizza_margherita=int(raw_input("How many slices of Margherita Pizza do you have?"))
pizza_party(pizza_margherita, pizza_margherita +5, 42,(pizza_margherita+lays_chips)/2, milka_chocolate)

pizza_funghi = peperoni_pizza_slices/2
flensburger = heineken_beer/2
shiraz_wine = merlot_glasses/2
paprika_chips = lays_chips/2
caramel_choclate = milka_chocolate/2
pizza_party(pizza_funghi,flensburger,shiraz_wine,paprika_chips,caramel_choclate)

pizza_salami = pizza_funghi
oettinger = pizza_salami
pinot_noir = oettinger
sea_salt = pinot_noir
white_chocolate = sea_salt
pizza_party(pizza_salami,oettinger,pinot_noir,sea_salt,white_chocolate)

plus_all = int(raw_input ("How many Slices of Pizza, glasses of wine, Bars of Choclate, Bags of Chips plus glasses of wine do you have?"))
pizza_party(plus_all/5, plus_all/5, plus_all/5, plus_all/5, plus_all/5)

var11=11
pizza_formaggi=var11^0
tyskie=pizza_formaggi*var11
Dornfelder=tyskie*var11
nachos=Dornfelder*var11
rittersport=nachos*var11
pizza_party(pizza_formaggi,tyskie,Dornfelder,nachos,rittersport)

pizza_party(10+peperoni_pizza_slices+pizza_hawaii+peperoni_pizza_slices*5+peperoni_pizza_slices/2+pizza_funghi+plus_all/5+pizza_formaggi,
10+heineken_beer+becks_beer+heineken_beer*2+pizza_margherita+5+flensburger+oettinger+plus_all/5+tyskie,
20+merlot_glasses+chardonnay_glasses+merlot_glasses-3+42+shiraz_wine+pinot_noir+plus_all/5+Dornfelder,
30+lays_chips+salt_vinegar+lays_chips+37.5+(pizza_margherita+lays_chips)/2+paprika_chips+sea_salt+plus_all/5+nachos,
50+milka_chocolate+oreo_chocolate+milka_chocolate/2+milka_chocolate+milka_chocolate/2+white_chocolate+plus_all/5+rittersport

)
