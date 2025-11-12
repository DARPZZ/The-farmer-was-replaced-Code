
import plant_types
import Dino
import Drone
import Unlock

#Out comment line 9 and 10 to make The dino run( The default dino world size is 6, you can change this in Dino file)
#while True:
	#Dino.dino()

WORLD = get_world_size()
MY_NUMBER_OF_DRONES = 32
ZONE_WIDTH = WORLD / MY_NUMBER_OF_DRONES

def wavefront_drone_0():
	wavefront_drone(0)

def wavefront_drone_1():
	wavefront_drone(1)

def wavefront_drone_2():
	wavefront_drone(2)

def wavefront_drone_3():
	wavefront_drone(3)

def wavefront_drone_4():
	wavefront_drone(4)

def wavefront_drone_5():
	wavefront_drone(5)

def wavefront_drone_6():
	wavefront_drone(6)

def wavefront_drone_7():
	wavefront_drone(7)

def wavefront_drone_8():
	wavefront_drone(8)

def wavefront_drone_9():
	wavefront_drone(9)

def wavefront_drone_10():
	wavefront_drone(10)

def wavefront_drone_11():
	wavefront_drone(11)

def wavefront_drone_12():
	wavefront_drone(12)

def wavefront_drone_13():
	wavefront_drone(13)

def wavefront_drone_14():
	wavefront_drone(14)

def wavefront_drone_15():
	wavefront_drone(15)

def wavefront_drone_16():
	wavefront_drone(16)

def wavefront_drone_17():
	wavefront_drone(17)

def wavefront_drone_18():
	wavefront_drone(18)

def wavefront_drone_19():
	wavefront_drone(19)

def wavefront_drone_20():
	wavefront_drone(20)

def wavefront_drone_21():
	wavefront_drone(21)

def wavefront_drone_22():
	wavefront_drone(22)

def wavefront_drone_23():
	wavefront_drone(23)

def wavefront_drone_24():
	wavefront_drone(24)

def wavefront_drone_25():
	wavefront_drone(25)

def wavefront_drone_26():
	wavefront_drone(26)

def wavefront_drone_27():
	wavefront_drone(27)

def wavefront_drone_28():
	wavefront_drone(28)

def wavefront_drone_29():
	wavefront_drone(29)

def wavefront_drone_30():
	wavefront_drone(30)

def wavefront_drone_31():
	wavefront_drone(31)
	
	
def wavefront_drone(zone_index):
	set_world_size(66)
	start_x = zone_index * ZONE_WIDTH
	end_x = start_x + ZONE_WIDTH - 1

	for _ in range(start_x - get_pos_x()):
		move(East)

	while True:
		number_of_pumpkins = num_items(Items.Pumpkin)

		Unlock.all_unlocks()
		#This farms the default farm can be changed to  "plant_types.plant_cactus_grid()" to farm cactus
		plant_types.decide_where_to_plant()
		y = get_pos_y()
		x = get_pos_x()

		if y % 2 == 0:
			if x < end_x:
				move(East)
			else:
				move(South)
		else:
			if x > start_x:
				move(West)
			else:
				move(South)

	
if num_drones() < max_drones():
	spawn_drone(wavefront_drone_1)
	spawn_drone(wavefront_drone_2)
	spawn_drone(wavefront_drone_3)
	spawn_drone(wavefront_drone_4)
	spawn_drone(wavefront_drone_5)
	spawn_drone(wavefront_drone_6)
	spawn_drone(wavefront_drone_7)
	spawn_drone(wavefront_drone_8)
	spawn_drone(wavefront_drone_9)
	spawn_drone(wavefront_drone_10)
	spawn_drone(wavefront_drone_11)
	spawn_drone(wavefront_drone_12)
	spawn_drone(wavefront_drone_13)
	spawn_drone(wavefront_drone_14)
	spawn_drone(wavefront_drone_15)
	spawn_drone(wavefront_drone_16)
	spawn_drone(wavefront_drone_17)
	spawn_drone(wavefront_drone_18)
	spawn_drone(wavefront_drone_19)
	spawn_drone(wavefront_drone_20)
	spawn_drone(wavefront_drone_21)
	spawn_drone(wavefront_drone_22)
	spawn_drone(wavefront_drone_23)
	spawn_drone(wavefront_drone_24)
	spawn_drone(wavefront_drone_25)
	spawn_drone(wavefront_drone_26)
	spawn_drone(wavefront_drone_27)
	spawn_drone(wavefront_drone_28)
	spawn_drone(wavefront_drone_29)
	spawn_drone(wavefront_drone_30)
	spawn_drone(wavefront_drone_31)
	
	
wavefront_drone_0()


