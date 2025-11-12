def get_drone_y():
	return get_pos_y()
def get_drone_x():
	return get_pos_x()
def drop_water():
	if num_items(Items.water) >0 and get_water() <0.3:
		use_item(Items.Water)
