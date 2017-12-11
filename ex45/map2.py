def getmap_module(inp_room):		
	mapeg_kitch = """
	________________________________
	|      | Din-| |U|D| |          |
	| Kit- | ing | | | | / Living   |
	| chen / Room| | | | | Room II  |
	|      |     /       |__________|
	|  x   |     |                  |
	|______|__/__|        _____/____|
	|            |       |   |      |
	|  Living    /       /WC | Off- |
	|  Room  I   |       |   | ice  |
	|____________|___/\__|___|______|
	"""

	mapeg_liv1 = """
	________________________________
	|      | Din-| |U|D| |          |
	| Kit- | ing | | | | / Living   |
	| chen / Room| | | | | Room II  |
	|      |     /       |__________|
	|      |     |                  |
	|______|__/__|        _____/____|
	|            |       |   |      |
	|  Living    /       /WC | Off- |
	|  Room  I   |       |   | ice  |
	|_____x______|___/\__|___|______|
	"""
	mapeg_liv2= """
	________________________________
	|      | Din-| |U|D| |          |
	| Kit- | ing | | | | / Living   |
	| chen / Room| | | | | Room II  |
	|      |     /       |____x_____|
	|      |     |                  |
	|______|__/__|        _____/____|
	|            |       |   |      |
	|  Living    /       /WC | Off- |
	|  Room  I   |       |   | ice  |
	|____________|___/\__|___|______|
	"""
	mapeg_din= """
	________________________________
	|      | Din-| |U|D| |          |
	| Kit- | ing | | | | / Living   |
	| chen / Room| | | | | Room II  |
	|      |     /       |__________|
	|      |  x  |                  |
	|______|__/__|        _____/____|
	|            |       |   |      |
	|  Living    /       /WC | Off- |
	|  Room  I   |       |   | ice  |
	|____________|___/\__|___|______|
	"""
	mapeg_off= """
	________________________________
	|      | Din-| |U|D| |          |
	| Kit- | ing | | | | / Living   |
	| chen / Room| | | | | Room II  |
	|      |     /       |__________|
	|      |     |                  |
	|______|__/__|        _____/____|
	|            |       |   |      |
	|  Living    /       /WC | Off- |
	|  Room  I   |       |   | ice  |
	|____________|___/\__|___|__x___|
	"""
	mapb_laun= """
	________________________________
	|            |  |U|  |          |
	| Laundry    |  | |  | Storage  |
	| Room       |  | |  | Room     |
	|    x       |       |____/_____|
	|_________/__|                  |
	|Sauna /              __________|
	|______|_____________|
	"""
	mapb_saun= """
	________________________________
	|            |  |U|  |          |
	| Laundry    |  | |  | Storage  |
	| Room       |  | |  | Room     |
	|            |       |____/_____|
	|_________/__|                  |
	|Sauna /              __________|
	|__x___|_____________|
	"""
	mapb_stor1= """
	________________________________
	|            |  |U|  |          |
	| Laundry    |  | |  | Storage  |
	| Room       |  | |  | Room  x  |
	|            |       |____/_____|
	|_________/__|                  |
	|Sauna /              __________|
	|______|_____________|
	"""

	map1_bed = """
	_______________________________
	|            |  |D|  |          |
	| Bedroom    |  | |  | Bathroom |
	|     x      |  | |  |          |
	|__/________/|       |__/_______|
	|Small Bath|              / WC  |
	|__________|______/_______|_____|
				  | Kids    | Guest |
				  | Bedroom | Room  |
				  |         |       |
				  |_________|_______|
	"""
	map1_kid = """
	_______________________________
	|            |  |D|  |          |
	| Bedroom    |  | |  | Bathroom |
	|            |  | |  |          |
	|__/________/|       |__/_______|
	|Small Bath|              / WC  |
	|__________|______/_______|_____|
				  | Kids    | Guest |
				  | Bedroom | Room  |
				  |   x     |       |
				  |_________|_______|
	"""
	map1_bath = """
	_______________________________
	|            |  |D|  |          |
	| Bedroom    |  | |  | Bathroom |
	|            |  | |  |    x     |
	|__/________/|       |__/_______|
	|Small Bath|              / WC  |
	|__________|______/_______|_____|
				  | Kids    | Guest |
				  | Bedroom | Room  |
				  |         |       |
				  |_________|_______|
	"""
	map1_wc = """
	_______________________________
	|            |  |D|  |          |
	| Bedroom    |  | |  | Bathroom |
	|            |  | |  |          |
	|__/________/|       |__/_______|
	|Small Bath|              / WC  |
	|__________|______/_______|__x__|
				  | Kids    | Guest |
				  | Bedroom | Room  |
				  |         |       |
				  |_________|_______|
	"""
	mapeg_wc= """
	________________________________
	|      | Din-| |U|D| |          |
	| Kit- | ing | | | | / Living   |
	| chen / Room| | | | | Room II  |
	|      |     /       |__________|
	|      |     |                  |
	|______|__/__|        _____/____|
	|            |       |   |      |
	|  Living    /       /WC | Off- |
	|  Room  I   |       | x | ice  |
	|____________|___/\__|___|______|
	"""
	map1_entrance = """
	_______________________________
	|            |  |D|  |          |
	| Bedroom    |  | |  | Bathroom |
	|            |  | |  |          |
	|__/________/|   x   |__/_______|
	|Small Bath|              / WC  |
	|__________|______/_______|_____|
				  | Kids    | Guest |
				  | Bedroom | Room  |
				  |         |       |
				  |_________|_______|
	"""
	mapb_entrance= """
	________________________________
	|            |  |U|  |          |
	| Laundry    |  | |  | Storage  |
	| Room       |  | |  | Room     |
	|            |       |____/_____|
	|_________/__|   x              |
	|Sauna /              __________|
	|______|_____________|
	"""
	map1_guest = """
	_______________________________
	|            |  |D|  |          |
	| Bedroom    |  | |  | Bathroom |
	|            |  | |  |          |
	|__/________/|       |__/_______|
	|Small Bath|              / WC  |
	|__________|______/_______|_____|
				  | Kids    | Guest |
				  | Bedroom | Room  |
				  |         |   x   |
				  |_________|_______|
	"""
	mapeg_entrance = """
	________________________________
	|      | Din-| |U|D| |          |
	| Kit- | ing | | | | / Living   |
	| chen / Room| | | | | Room II  |
	|      |     /       |__________|
	|      |     |                  |
	|______|__/__|        _____/____|
	|            |       |   |      |
	|  Living    /   x   /WC | Off- |
	|  Room  I   |       |   | ice  |
	|____________|___/\__|___|______|
	"""
	maplist = {
		'entrance_corridor': mapeg_entrance,
		'entrance_corridor2': map1_entrance,
		'wc_eg': mapeg_wc,
		'livingrm1_eg': mapeg_liv1,
		'diningrm_eg': mapeg_din,
		'kitchen_eg': mapeg_kitch,
		'livingrm2_eg': mapeg_liv2,
		'office_eg': mapeg_off,
		'corridor_bs': mapb_entrance,
		'laundry_bs': mapb_laun,
		'sauna_bs': mapb_saun,
		'storage1_bs': mapb_stor1,
		'bedroom_f1': map1_bed,
		'bathroom_f1': map1_bath,
		'wc_f1': map1_wc,
		'bedroomkids1_f1': map1_kid,
		'guestroom1_f1': map1_guest,
		}
	print maplist[inp_room]