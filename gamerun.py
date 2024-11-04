import CarRacing.project as carrace #cargame
import flappy.main as flappy #flap
import Tetris.code.main as tt
# This will run games
print("Enter the game you wanna play\n1 for flappy\n2 for car racing\n3for space invader")

x= int(input("Enter your choice = "))

if x == 1:
	flappy.flap()

if x==2:
	carrace.cargame()

if x ==3:
	import SpaceInvader.main as rocket #spacerunpass

if x ==4:
	tt

print("Finished")