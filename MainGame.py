import pygame
import pygame.gfxdraw
import random
import sys
import math

pygame.init()
screenWidth = 1000
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
font = pygame.font.Font('freesansbold.ttf', 64)
font2 = pygame.font.Font('freesansbold.ttf', 25)
white = (255,255,255)
black = (0,0,0)
green = (0,200,0)
orange = (240, 75, 0)
red = (255, 0,0)
blue = (0,0,255)
colors=[]
class Platform:
    def __init__(self, starting, w,h, color):
        self.startingPoint = starting
        self.w = w
        self.h = h
        self.color = color
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.startingPoint[0], self.startingPoint[1], self.w,self.h))




class Avatar:
    speed = 2
    somethingBelow = True
    somethingAbove = False
    somethingLeft = False
    somethingRight = False
    h= 32
    w = 32
    state = 0
    def __init__(self, color, loc):
        self.color = color
        self.loc = loc

    def checkBelow(self, platforms):
        self.somethingBelow = False
        for i in range(0, len(platforms)):
            plat= platforms[i]
            if (self.loc[1]+self.h == plat.startingPoint[1]):
                if((self.loc[0] >= plat.startingPoint[0] and self.loc[0] < plat.startingPoint[0] + plat.w)or (self.loc[0]+self.w >plat.startingPoint[0] and self.loc[0]< plat.startingPoint[0])):
                    self.somethingBelow = True
        return self.somethingBelow
    def checkAbove(self,platforms):
        self.somethingAbove = False
        for i in range(0, len(platforms)):
            plat= platforms[i]
            # checks if the top of the avatar + width is touching a platform or if the avatar point is touching a platform
            if self.loc[1] == plat.startingPoint[1] + plat.h:
                if((self.loc[0] > plat.startingPoint[0] and self.loc[0] < plat.startingPoint[0] + plat.w)or (self.loc[0]+self.w >plat.startingPoint[0] and self.loc[0]< plat.startingPoint[0] )):
                    self.somethingAbove = True
        return self.somethingAbove
    def checkLeft(self, platforms):
        self.somethingLeft = False
        for i in range(0, len(platforms)):
            plat = platforms[i]
            if(self.loc[0] == plat.startingPoint[0]+plat.w and (self.loc[1] >= plat.startingPoint[1] and self.loc[1] < plat.startingPoint[1] + plat.h)or (self.loc[1]+self.h > plat.startingPoint[1] and self.loc[1]<plat.startingPoint[1])):
                self.somethingLeft = True
        return self.somethingLeft
    def checkRight(self, platforms):
        self.somethingRight = False
        for i in range(0, len(platforms)):
            plat = platforms[i]
            if(self.loc[0] + self.w== plat.startingPoint[0] and (self.loc[1] >= plat.startingPoint[1] and self.loc[1] < plat.startingPoint[1] + plat.h)or (self.loc[1]+self.h > plat.startingPoint[1] and self.loc[1]<plat.startingPoint[1])):
                self.somethingRight = True
        return self.somethingRight
    def fall(self, platforms):
        if (not self.checkBelow(platforms)):
            y =self.loc[1]
            y+=self.speed
            self.loc[1] = y
            self.state = 1
    def jump(self, platforms):
        if( not self.checkAbove(platforms)):
            y = self.loc[1]
            y -=self.speed
            self.loc[1] = y
            self.state = 2
    def moveLeft(self, platforms):
        if (not self.checkLeft(platforms)):
            x = self.loc[0]
            x-=self.speed
            self.loc[0] = x
            self.state = 3
    def moveRight(self, platforms):
        if (not self.checkRight(platforms)):
            x = self.loc[0]
            x+=self.speed
            self.loc[0] = x
            self.state = 4
    def distanceFromOtherPlayer(self, avatar):
        sX = self.loc[0]
        sY = self.loc[1]
        dX = avatar.loc[0]
        dY = avatar.loc[1]
        # √ (x2 − x1)2 + (y2 − y1)2
        distance = math.sqrt(((dX - sX)**2) + (dY - sY)**2)
        # print ((int)(distance/32))
        return (int)(distance/32)
    def slopeOfColllision(self, avatar):
        sX = self.loc[0]
        sY = self.loc[1]
        dX = avatar.loc[0]
        dY = avatar.loc[1]

        x = dX - sX
        y = dY - sY
        if (not y== 0):
            x = (dX - sX) / y
            slope = [x,y]
        else:
            slope = [x,y]
        return slope
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.loc[0], self.loc[1], self.w,self.h))
        pygame.gfxdraw.aacircle(screen, self.loc[0] + 16, self.loc[1] + 16, 48, self.color)





running = True
p = Platform([0,screenHeight - 100], 1000,100,white)
p2 = Platform([-1000, 100], 1100, 1000, white)
p3 = Platform([900, 100], 1000, 1000, white)
level = random.randint(0,3)
if level <=1:
    p4= Platform([550,300], 100,32,white)
    p5 = Platform([350, 300], 100,32,white)
    p6 = Platform([450, 150], 100,32,white)
    p7= Platform([50, 300], 100,32, white)
    p8 = Platform([850,300], 100,32,white)
    p9 = Platform([150, 400], 100,32,white)
    p10 = Platform([750, 400], 100,32,white)
    platforms = [p, p2, p3, p4, p5, p6, p7, p8, p9, p10]
elif level == 2:
    p4 = Platform([100, 400], 250, 32,white)
    p5 = Platform([850, 200], 50,32,white)
    p6 = Platform([600, 350], 50,32,white)
    platforms = [p,p2,p3,p4,p5,p6]
else:
    p4 = Platform([300, 300], 400, 32,white)
    p5 = Platform([100,450], 32,32,white)
    platforms = [p,p2,p3,p4,p5]
avatar = Avatar(blue,[1000-32, 100-32])
avatar2 = Avatar(red,  [0, 100-32])
counter = 50
counter2 = 50
counter3 = 0
counter4 = 0
def createPlatforms(platforms):
    # reason this isnt implemented more is because it causes some ghost platforms
    while(len(platforms) < 10):
        # between the two walls
        xLoc = random.randint(100, 850)
        # between floor and top level
        yLoc = random.randint(100, screenHeight - 132)
        p = Platform([xLoc,yLoc], 100, 32,white)
        platforms.append(p)
        # if checkIfViable(platforms, p):
        #     platforms.append(p)
def checkIfViable(platforms, p):
    viable = True
    for i in range(0, len(platforms)):
        plat = platforms[i]
        platT = plat.startingPoint[1] - 32
        platD = plat.startingPoint[1]+32+plat.h
        platL = plat.startingPoint[0]-32
        platR=  plat.startingPoint[0]+32+plat.w
        if ((p.startingPoint[0] > platL and p.startingPoint[0] <platR) and (p.startingPoint[1] < platT and p.startingPoint[1] > platD)or (p.startingPoint[0]+p.w > platL and p.startingPoint[0]+p.w <platR) and (p.startingPoint[1]+p.h < platT and p.startingPoint[1] +p.h> platD)):
            viable = False
    return viable

def drawEverything(platforms, avatar, avatar2):
    for Platform in platforms:
        Platform.draw()
    avatar.draw()
    avatar2.draw()
# createPlatforms(platforms)
# printed = False
while (running):
    screen.fill(black)
    avatar.state = 0
    avatar2.state = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        avatar.moveLeft(platforms)
    if keys[pygame.K_RIGHT]:
        avatar.moveRight(platforms)
    if keys[pygame.K_a]:
        avatar2.moveLeft(platforms)
    if keys[pygame.K_d]:
        avatar2.moveRight(platforms)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_s:
            #     running = False
            if event.key == pygame.K_UP:
                if(avatar.checkBelow(platforms)):
                    counter = 1
            if event.key==pygame.K_w:
                if avatar2.checkBelow(platforms):
                    counter2 = 1
    avatarRect = pygame.Rect(avatar.loc[0] - 32, avatar.loc[1] - 32, 48 * 2, 48 * 2)
    avatar2Rect = pygame.Rect(avatar2.loc[0] - 32, avatar2.loc[1] - 32, 48 * 2, 48 * 2)
    if (counter < 75):
        avatar.jump(platforms)
        counter +=1
        drawEverything(platforms, avatar,avatar2)
        pygame.display.update(avatar2Rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            avatar.moveLeft(platforms)
        if keys[pygame.K_RIGHT]:
            avatar.moveRight(platforms)
        if keys[pygame.K_a]:
            avatar2.moveLeft(platforms)
        if keys[pygame.K_d]:
            avatar2.moveRight(platforms)
    else:
        avatar.fall(platforms)
    if counter2 < 75:
        avatar2.jump(platforms)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            avatar.moveLeft(platforms)
        if keys[pygame.K_RIGHT]:
            avatar.moveRight(platforms)
        if keys[pygame.K_a]:
            avatar2.moveLeft(platforms)
        if keys[pygame.K_d]:
            avatar2.moveRight(platforms)
        counter2 +=1
        # drawEverything(platforms, avatar, avatar2)
        # pygame.display.update(avatarRect)
    else:
        avatar2.fall(platforms)
    distance = avatar.distanceFromOtherPlayer(avatar2)
    #slope = avatar.slopeFromOtherPlayer(avatar2)
    if (distance<=2):
        slope = avatar.slopeOfColllision(avatar2)
        x = slope[0]
        y = slope[1]
        for i in range (0, 150):
            if(distance < 10):

                if (avatar.state ==0):
                    if (avatar2.loc[1] < avatar.loc[1]):
                        if (not avatar2.checkAbove(platforms)):
                            avatar2.jump(platforms)
                    else:
                        if (not avatar2.checkBelow(platforms)):
                            avatar2.fall(platforms)

                        # checks if avatar is to the left and pushes left
                    if (avatar2.loc[0] < avatar.loc[0]):
                        if (not avatar2.checkLeft(platforms)):
                            avatar2.moveLeft(platforms)
                    else:
                        if (not avatar2.checkRight(platforms)):
                            avatar2.moveRight(platforms)
                elif(avatar2.state ==0):
                    if (avatar.loc[1] < avatar2.loc[1]):
                        if(not avatar.checkAbove(platforms)):
                            avatar.jump(platforms)
                    else:
                        if (not avatar.checkBelow(platforms)):
                            avatar.fall(platforms)

                        # checks if avatar is to the left and pushes left
                    if (avatar.loc[0] < avatar2.loc[0]):
                        if(not avatar.checkLeft(platforms)):
                            avatar.moveLeft(platforms)
                    else:
                        if (not avatar.checkRight(platforms)):
                            avatar.moveRight(platforms)
                else:
                    # if avatar 1 is above avatar 2, pushes avatar 1 up
                    if (avatar.loc[1] < avatar2.loc[1]):
                        if(not avatar.checkAbove(platforms)):
                            avatar.jump(platforms)
                    else:
                        if (not avatar.checkBelow(platforms)):
                            avatar.fall(platforms)

                        # checks if avatar is to the left and pushes left
                    if (avatar.loc[0] < avatar2.loc[0]):
                        if(not avatar.checkLeft(platforms)):
                            avatar.moveLeft(platforms)
                    else:
                        if (not avatar.checkRight(platforms)):
                            avatar.moveRight(platforms)

                    if (avatar2.loc[1] < avatar.loc[1]):
                        if (not avatar2.checkAbove(platforms)):
                            avatar2.jump(platforms)
                    else:
                        if (not avatar2.checkBelow(platforms)):
                            avatar2.fall(platforms)

                        # checks if avatar is to the left and pushes left
                    if (avatar2.loc[0] < avatar.loc[0]):
                        if (not avatar2.checkLeft(platforms)):
                            avatar2.moveLeft(platforms)
                    else:
                        if (not avatar2.checkRight(platforms)):
                            avatar2.moveRight(platforms)
            drawEverything(platforms, avatar,avatar2)
            pygame.display.update()
            distance = avatar.distanceFromOtherPlayer(avatar2)


    if (avatar.loc[0] < 0):
        text = "Noice"
        label = font.render(text, 1, white)
        screen.blit(label, (300, 200))
    elif(avatar2.loc[0]>1000):
        text = "toit"
        label = font.render(text, 1, white)
        screen.blit(label, (300, 200))
    else:
        text = "Try to move the avatars to the opposite sides of the map"
        text2 = "if it is not possible, just restart"
        label = font2.render(text,1,white)
        screen.blit(label,(50,25))
        label2 = font2.render(text2,1,white)
        screen.blit(label2,(125,60))
    avatar.speed = 2
    avatar2.speed = 2
    drawEverything(platforms, avatar,avatar2)
    # avatar.fall(platforms)
    pygame.display.update()
