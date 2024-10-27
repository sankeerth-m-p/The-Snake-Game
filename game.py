from snake import Snake
import random


class Game:
    def __init__(self,width,height) -> None:
        self.width=width
        self.height=height
        self.snake=Snake(width//2,height//2)
        self.food=self.generateFood()
        self.direction=(0,1)

    def generateFood(self):
        while True:
            x=random.randint(0,self.width-1)
            y=random.randint(0,self.height-1)
            if (x,y) not in self.snake.getCoordinates():
                return(x,y)
            
    def moveSnake(self):
        new_x=self.snake.head.x +self.direction[0]
        new_y=self.snake.head.y +self.direction[1]
        if not (0<=new_x<self.width and 0 <=new_y<self.height):
            raise ValueError("game over :sanke hit the wall")
        self.snake.addHead(new_x,new_y)
        if (new_x,new_y)==self.food:
            self.food=self.generateFood()
            print("snake ate food")
        else:
            self.snake.removeTail()
    
    def update_direction(self,new_direction):
        opposite_direction=(-self.direction[0],-self.direction[1])
        if new_direction!=opposite_direction:
            self.direction=new_direction

    def check_self_collision(self):
        head_coords=(self.snake.head.x,self.snake.head.y)
        for coord in self.snake.getCoordinates()[1:]:
            if coord ==head_coords:
                raise ValueError("game over :snake collide with itself")
