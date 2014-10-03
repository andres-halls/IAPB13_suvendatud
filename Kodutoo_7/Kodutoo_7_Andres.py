'''
Kodutoo 7
03.10.2014
Andres Liiver
'''

import simulator
from robot import *

def main():
    world = simulator.World(width = 30, height = 30, sleep_time = 0)
    robots = []
    for i in range (world.width):
        robots.append(Robot(world, i, world.height-1, 0))
        
    world.print_state()

    while True:
        world.tick()
        world.print_state()
    
if __name__ == "__main__":
    main()
