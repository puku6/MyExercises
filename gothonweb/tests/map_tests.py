from nose.tools import *
from map import *
def test_room():
	gold = Scene("GoldScene", "goldroom", """
				This room has gold in it you can grab. There's a
				door to the north.
				""")
	assert_equal(gold.title, "GoldScene")
	assert_equal(gold.urlname, "goldroom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Scene("Center", "center", "Test room in the center.")
	north = Scene("North", "north", "Test room in the north.")
	south = Scene("South", "south", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)
	
def test_map():
	start = Scene("Start", "start", "You can go west and down a hole.")
	west = Scene("Trees", "trees", "There are trees here, you can go east.")
	down = Scene("Dungeon", "dungeon", "It's dark down here, you can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
	
def test_gothon_game_map():
	assert_equal(START, welcome_screen)
	assert_equal(START.go('abc').go('joke').go('lwa'), laser_weapon_armory)
	assert_equal(START.go('*').go('punch').go('*'), generic_death)
	assert_equal(START.go('*').go('joke').go('lwa').go('3-1-2').go('*').go('lwa'), laser_weapon_armory_alt)
	assert_equal(START.go('*').go('joke').go('bridge').go('sing').go('*').go('leave').go('bridge'), the_bridge_alt)
def test_gothon_game_flags():
	item = START.go('*').go('joke').go('lwa').go('3-1-2').go('*')
	assert_equal(inventory, ['bomb'])
	
	item2 = START.go('*').go('joke').go('bridge').go('sing').go('*').go('place bomb')
	assert_equal(inventory, [])
	assert_equal(item2, the_bridge_no_bomb )
	
	item3 = START.go('*').go('joke').go('lwa').go('3-1-2').go('*').go('bridge').go('sing').go('*').go('place bomb')
	assert_equal(inventory, []) 
	assert_equal(item3, the_bridge_bomb)
	
	item4 = START.go('*').go('joke').go('lwa').go('3-1-2').go('*').go('bridge').go('sing').go('*').go('place bomb').go('*').go('lwa')
	assert_equal(item4, laser_weapon_armory_alt)
	assert_equal(inventory, [])
	
	item5 = START.go('*').go('joke').go('lwa').go('3-1-2').go('*').go('bridge').go('sing').go('*').go('place bomb').go('*').go('pods').go('2')
	assert_equal(item5, the_end_winner)
	