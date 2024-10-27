from node import Node
class Snake:
    def __init__(self,inital_x,intial_y) -> None:
        self.head=Node(inital_x,intial_y)
        self.tail=self.head
        self.length=1

    def addHead(self,x,y):
        newNode=Node(x,y)
        newNode.next=self.head
        self.head=newNode
        self.length+=1

    def removeTail(self):
        if self.length==1:
            return
        current=self.head
        while current.next!=self.tail:
            current=current.next
        current.next=None
        self.tail=current
        self.length-=1
    def getCoordinates(self):
        coordinates=[]
        current=self.head
        while current:
            coordinates.append((current.x,current.y))
            current=current.next
        return coordinates