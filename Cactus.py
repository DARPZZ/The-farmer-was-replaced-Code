import Drone
swap_counter = 0
def sort_current_cactus():

	size = measure()
	if size == None:
		return False
	if get_entity_type() == Entities.Cactus:
		
		swapped = False
	
		north = measure(North)
		if north != None and size > north:
			swap(North)
			swapped = True
	
		east = measure(East)
		if east != None and size > east:
			swap(East)
			swapped = True
	
		south = measure(South)
		if south != None and size < south:
			swap(South)
			swapped = True
	
		west = measure(West)
		if west != None and size < west:
			swap(West)
			swapped = True
		if swapped == False:
			global swap_counter
			swap_counter = swap_counter + 1
		else:
			global swap_counter
			swap_counter = 0
		global swap_counter
		if swap_counter >52:
		
			harvest()
		quick_print(swap_counter)
		



	

	
