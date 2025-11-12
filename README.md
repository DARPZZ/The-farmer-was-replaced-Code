# The-farmer-was-replaced-Code

This project contains custom code and automation routines for the game The Farmer Was Replaced. It focuses on building, refactoring, and orchestrating farming automation patterns — including multi-drone choreography, crop planting logic, and zone-based routines — to maximize efficiency and visual impact.

**Features**
  - Multi-drone coordination: Supports up to 32 drones working in parallel.

  - Choreographed planting patterns: Symmetric, staggered, checkerboard, and dynamic switching.

  - Zone-based logic: Assigns drones to specific grid zones for safe, efficient coverage.

# Maze Code Explained

use_weird_substance_on_bush()
Logic:

  - Checks if the player has at least one Weird_Substance in inventory.

  - If the current entity is a Bush, it uses the item on it.


**treasure_hunt()** 

Purpose: Automates exploration of the maze to find and harvest treasures.

Logic flow:
  - Starts moving West from the current position.

  - Tracks the player’s coordinates (x, y).

  - If movement fails (position doesn’t change), it rotates direction clockwise (West → North → East → South → West).

  - If movement succeeds, it rotates direction counter-clockwise (West → South → East → North → West).

While moving:

  - If the entity is Treasure, it calls harvest().

  - If the entity is Grass, it calls clear() and breaks the loop (ending the hunt).
    
## 🌵 Cactus Code Explained

### `sort_current_cactus()`

**Purpose**  
Automates sorting and harvesting of cactus entities based on their measured size compared to neighbors.  
It ensures cactus plants are swapped into optimal positions and harvested when no further swaps are possible.

---

###  Step-by-step logic

1. **Measure current cactus size**  
   - Calls `measure()` to get the size of the cactus at the current position.  
   - If no size is returned (`None`), the function exits.  

2. **Check entity type**  
   - Only runs if the current entity is a `Cactus`.  

3. **Compare with neighbors**  
   - Looks at cactus sizes in all four directions (`North`, `East`, `South`, `West`).  
   - Swaps if certain conditions are met:  
     - **North/East** → swap if current cactus is *larger* than neighbor.  
     - **South/West** → swap if current cactus is *smaller* than neighbor.  
   - This creates a sorting effect across the grid.  

4. **Track swap attempts**  
   - If no swap occurred, increment a global `swap_counter`.  
   - If a swap occurred, reset `swap_counter` to 0.  

5. **Harvest condition**  
   - If `swap_counter` exceeds **52** (meaning repeated attempts without successful swaps), the cactus is harvested.  
   - This prevents infinite loops and ensures progress.
**Current farm**
<img width="986" height="1002" alt="billede" src="https://github.com/user-attachments/assets/11b01ad2-e010-4a8e-bca0-63fe921f906e" />
