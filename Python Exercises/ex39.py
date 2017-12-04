laender = {
	'Hessen': 'HE',
	'Bavaria': 'BY',
	'Bremen': 'HB',
	'Hamburg': 'HH',
	'Mecklenburg-Vorpommern':'MV',
	'Nieder-Sachsen':'NI'
	}
	 
capitals = {
	'HE': 'Wiesbaden',
	'BY': 'Munich',
	'MV': 'Schwerin',
	'HH': 'Hamburg',
	'HB': 'Bremen',
	'NI': 'Hannover'
	}
	
capitals['HB'] = 'Bremen'
capitals['HH'] = 'Hamburg'

print '-' * 10
print "Capital of HE is: ", capitals['HE']
print "Capital of BY is: ", capitals['BY']

print '-' * 10
print "Hessen's abbreviation is: ", laender['Hessen']
print "Bavaria's abbreviation is: ", laender['Bavaria']

print '-' * 10 
print "Capital of Hessen is: ", capitals[laender['Hessen']]
print "Capital of Bavaria is: ", capitals[laender['Bavaria']]

print '-' * 10
for land, abbrev in laender.items():
	print "%s is abbreviated %s" % (land, abbrev)
	
print "-" * 10
for abbrev, capital in capitals.items():
	print "Bundesland %s capital is %s "  %(abbrev, capital)

	print '-' * 10
for land, abbrev in laender.items():
	print "%s Bundesland is abbreviated %s and its capital is %s" % (
		land, abbrev, capitals[abbrev])
	
print '-' * 10
land = laender.get('Berlin')
if not land: 
	print "Sorry, no Berlin."
		
capital = capitals.get ("BE", 'Does not Exist')
print "The capital of Bundesland 'BE' is: %s" % capital