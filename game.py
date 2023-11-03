class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if abs((x1 + bsize/2) - (x2 + bsize/2)) < bsize/2 and abs((y1 + bsize/2) - (y2 + bsize/2)) < bsize/2:
            return True
        return False