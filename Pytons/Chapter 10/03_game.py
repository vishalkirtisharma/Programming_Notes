class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveUp(self):
        pass
    def moveDown(self):
        pass


class Remote:
    pass


remote = Remote()
Player1= Player()
if (remote.isLeftpress()):
    Player.moveRight()