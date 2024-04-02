
#NOT USING CODE
#First ever OOP code practice

# class Ghost:
#     def __init__(self):
#         self.position = 0 
#     def move_left(self):
#         self.position  -=1
#     def move_right(self):
#         self.position +=1
#     def report_position(self):
#         print(f"the ghost is at position {self.position}")

# my_ghost = Ghost()#creating a specific object from the ghost class
# my_ghost.move_left()
# my_ghost.move_left()
# my_ghost.move_left()
# my_ghost.report_position()


class SpaceShip1:
    def __init__(self):
        self.position = 0
        self.stars_collected = 0
    def move_left(self):
        self.position -= 1
        print (f"The spaceship moved to {self.position}.")
    def move_right(self):
        self.position += 1
        print(f"The spaceship move to {self.position}.")
    def collect_stars(self,star):
        if self.position == star.position:
            self.stars_collected +=1
            print("You collected a star!")
        else:
            print("There is no star here :)")

class Star:
    def __init__(self,position):
        self.position = position

class Game:
    def __init__(self):
        self.SpaceShip1 = SpaceShip1()
        self.Star = Star(3)
    def status(self):
        print("-"*50)
        print(f"SpaceShip1 is at {self.SpaceShip1.position}.")
        print("-"*50)
        print(f"Stars collected_{self.SpaceShip1.stars_collected}.")
        print("-"*50)
    def move_spaceship(self,direction):
        if direction == "left":
            self.SpaceShip1.move_left()
        elif direction == "right":
            self.SpaceShip1.move_right()
        self.check_for_star()
    def check_for_star(self):
        self.SpaceShip1.collect_stars(self.Star)

game = Game()
game.move_spaceship("right")
game.move_spaceship("right")
game.move_spaceship("right")
game.move_spaceship("right")
game.move_spaceship("right")
game.status()