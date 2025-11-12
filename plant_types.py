import Drone
import maze_stuff
import Cactus
def harvest_each():
	if num_items(Items.Fertilizer)>=0 and get_entity_type() == Entities.Bush:
			use_item(Items.Fertilizer)
			
	if can_harvest():
		harvest()
	
def check_ground_type():
	if get_ground_type() !=  Grounds.Soil:
		till()
		
def plant_tree_bush():
	harvest_each()
	if  Drone.get_drone_x() % 2 ==0 and  Drone.get_drone_y()  %2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		#use_item(Items.Weird_Substance, substance)
		if get_entity_type() == Entities.Hedge:
			maze_stuff.treasure_hunt()

		
	
		
def plant_sunflower():
	check_ground_type()
	harvest_each()
	Drone.drop_water()
	plant(Entities.Sunflower)
	
def plant_carrot():
	check_ground_type()
	harvest_each()
	plant(Entities.Carrot)
	
def plantpumpkins():
	check_ground_type()
	harvest_each()
	plant(Entities.Pumpkin)
	
def plant_cactus_grid():
	y = get_pos_y()
	check_ground_type()
	if Drone.get_drone_y() ==30 or Drone.get_drone_y() == 31:
		if can_harvest():
			harvest()
		plant(Entities.Sunflower)
		Drone.drop_water()
	if get_entity_type() == Entities.Cactus:
		Cactus.sort_current_cactus()
	
		
	else:
		plant(Entities.Cactus)
	

	
def decide_where_to_plant():

	Drone.drop_water()
	y = Drone.get_drone_y()

	if y <= 8:
		plant_carrot()
	elif y <= 20:
		plantpumpkins()
	elif y <= 27:
		plant_tree_bush()
		
	elif y <= 2:
		harvest()
		plant(Entities.Grass)
		
	elif y == 30 or y ==31:
		plant_sunflower()


		
		
	
			
		
		
	
		
	
	
	
	

	
	
	
