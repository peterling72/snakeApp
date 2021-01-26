import pygame
import random

pygame.init()
width = 1000
height = 500
rows = 20
win = pygame.display.set_mode((width, height))
titleFont = pygame.font.SysFont("Comic Sans MS", 50)
menuTitle = titleFont.render("Welcome to the Snake Game",True,(0,0,0))
playFont = pygame.font.SysFont("Comic Sans MS", 45)
menuPlay = playFont.render("PLAY", True, (0,0,0))
rulesFont = pygame.font.SysFont("Comic Sans MS", 45)
menuRules = playFont.render("RULES", True, (0,0,0))
rules1 = playFont.render("Collect as many green apples as possible!", True, (139,0,0,))
rules2 = playFont.render("Don't run into yourself!", True, (139,0,0,))
rules3 = playFont.render("Use arrow keys to move!", True, (139,0,0,))
rules4 = playFont.render("Press esc to return to menu.", True, (72,61,139))
menuQuit = playFont.render("QUIT", True, (0,0,0))
selfCrashMsg = playFont.render("You crashed into yourself!", True, (0,0,0))
continueMsg = playFont.render("Press r to return to menu.", True, (72,61,139))
wallCrashMsg = playFont.render("You crashed into a wall!", True, (0,0,0))
obstacleMsg = playFont.render("You crashed into a bomb!", True, (0,0,0))
chooseModeMsg = playFont.render("Choose a mode:", True, (0,0,0))
easyMode = playFont.render("Easy Mode", True, (0,0,0))
hardMode = playFont.render("Hard Mode", True, (0,0,0))
crashSound = pygame.mixer.Sound("Crash.wav")
eatSound = pygame.mixer.Sound("Human_Eating_Watermelon.wav")
bombSound = pygame.mixer.Sound("Big_Explosion_Cut_Off.wav")
pygame.mixer.music.load("Airline.wav")
snakeIMG = pygame.image.load("actualSnake.png")
class snakeBody():
    def __init__(self,start,dirnx=1,dirny=0,color=(0,0,255)):
        self.pos = start
        self.color = color
class food():
    def __init__(self,pos,color=(0,0,0)):
        self.pos = pos
        self.color = color
    def draw(self, window):
        center = 13
        radius = 10
        circleMiddle = (self.pos[0]*25+center,self.pos[1]*25+center)
        pygame.draw.circle(window, self.color, circleMiddle, radius)
        #pygame.draw.rect(window, self.color, (self.pos[0] * 25 + 1, self.pos[1] * 25 + 1, 25 - 2, 25 - 2))
class snake(object):
    body = []
    #turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = snakeBody(pos)
        self.body.append(self.head)
        #self.dirnx = 0
        #self.dirny = 1
    def moveRight(self):
        coordinates = (self.body[0].pos[0]+1, self.body[0].pos[1])
        if(self.body[0].pos[0]+1 > 39):
            return -2
        addToFront = snakeBody(coordinates)
        for a in range(len(self.body)-1):
            x = a +1
            if(self.body[x].pos == addToFront.pos):
                return -1
        self.body.insert(0, addToFront)
        #if(len(self.body)!=1):
        self.body.pop()
        return 1
    def moveUp(self):
        coordinates = (self.body[0].pos[0] , self.body[0].pos[1]-1)
        if(self.body[0].pos[1]-1 < 0):
            return -2
        addToFront = snakeBody(coordinates)
        for a in range(len(self.body)-1):
            x = a +1
            if(self.body[x].pos == addToFront.pos):
                return -1
        self.body.insert(0, addToFront)
        # if(len(self.body)!=1):
        self.body.pop()
        return 1
    def moveDown(self):
        coordinates = (self.body[0].pos[0], self.body[0].pos[1] + 1)
        if(self.body[0].pos[1]+1 > 19):
            return -2
        addToFront = snakeBody(coordinates)
        for a in range(len(self.body)-1):
            x = a +1
            if(self.body[x].pos == addToFront.pos):
                return -1
        self.body.insert(0, addToFront)
        # if(len(self.body)!=1):
        self.body.pop()
        return 1
    def moveLeft(self):
        coordinates = (self.body[0].pos[0] - 1, self.body[0].pos[1])
        if(self.body[0].pos[0]-1 < 0):
            return -2
        addToFront = snakeBody(coordinates)
        for a in range(len(self.body)-1):
            x = a +1
            if(self.body[x].pos == addToFront.pos):
                return -1
        self.body.insert(0, addToFront)
        # if(len(self.body)!=1):
        self.body.pop()
        return 1
    def addBody(self,lastdirection):
        lastIndex = len(self.body)-1
        if (lastdirection[0]==0):
            coordinates = (self.body[lastIndex].pos[0]-1,self.body[lastIndex].pos[1])
            addToBack = snakeBody(coordinates)
            self.body.append(addToBack)
        elif (lastdirection[0]==1):
            coordinates = (self.body[lastIndex].pos[0] + 1, self.body[lastIndex].pos[1])
            addToBack = snakeBody(coordinates)
            self.body.append(addToBack)
        elif (lastdirection[0]==2):
            coordinates = (self.body[lastIndex].pos[0], self.body[lastIndex].pos[1]+1)
            addToBack = snakeBody(coordinates)
            self.body.append(addToBack)
        elif (lastdirection[0]==3):
            coordinates = (self.body[lastIndex].pos[0], self.body[lastIndex].pos[1] - 1)
            addToBack = snakeBody(coordinates)
            self.body.append(addToBack)

    def draw(self, window):
        for i in range(len(self.body)):
            pygame.draw.rect(window, self.color, (self.body[i].pos[0] * 25 + 1, self.body[i].pos[1] * 25 + 1, 25 - 2, 25 - 2))

    def cleanup(self, pos):
        self.body.clear()
        #self.head = snakeBody(pos)
        #self.body.append(self.head)
def checkIfxOnSnake(x, listOfPositions):
    for i in range(len(listOfPositions)):
        if(x == listOfPositions[i].pos[0]):
            return True
    return False
def checkIfyOnSnake(y, listOfPositions):
    for i in range(len(listOfPositions)):
        if(y == listOfPositions[i].pos[1]):
            return True
    return False
def randomSnackPositions(snake):
    posOfSnake = snake.body
    while True:
        x = random.randint(1,38)
        y = random.randint(1,18)
        if((checkIfxOnSnake(x, posOfSnake) == True) and (checkIfyOnSnake(y, posOfSnake) == True)):
            continue
        else:
            break
    return (x,y)
def displayGameOver(x, lengthOfSnake):
    clock = pygame.time.Clock()
    lengthMsg = playFont.render("Your length was: " + lengthOfSnake, True, (0, 0, 0))
    gameOver = True
    if(x==0):
        while gameOver:
            win.fill((67,110,238))
            win.blit(selfCrashMsg, (235,20))
            win.blit(lengthMsg, (300, 100))
            win.blit(continueMsg, (235,400))
            clock.tick(20)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 1
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_r]):
                return 0
    elif(x==1):
        while gameOver:
            win.fill((67,110,238))
            win.blit(wallCrashMsg, (250,20))
            win.blit(lengthMsg, (300, 100))
            win.blit(continueMsg, (235,400))
            clock.tick(20)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 1
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_r]):
                return 0
    else:
        while gameOver:
            win.fill((67, 110, 238))
            win.blit(obstacleMsg, (250, 20))
            win.blit(lengthMsg, (300, 100))
            win.blit(continueMsg, (235, 400))
            clock.tick(20)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 1
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_r]):
                return 0
def displayPlayWin():
    runPlayWin = True
    while runPlayWin:
        clock = pygame.time.Clock()
        clock.tick(20)
        win.fill((67,110,238))
        win.blit(chooseModeMsg, (340,20))
        win.fill((48,120,20), (219,180,260,100))
        win.blit(easyMode, (235, 200))
        win.fill((48,120,20), (519,180, 260,100))
        win.blit(hardMode, (535,200))
        win.blit(rules4, (220, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return -1
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    mousePos = pygame.mouse.get_pos()
                    if(mousePos[0]>219 and mousePos[0]<479 and mousePos[1]>180 and mousePos[1]<280):
                        return 1
                    elif(mousePos[0]>519 and mousePos[0]<779 and mousePos[1]>180 and mousePos[1]<280):
                        return 2
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_ESCAPE]):
                return 0
def render():
    #win.fill((0, 0, 0))
    win.fill((153, 153, 153))
    blockSize = 25
    x = 0
    y = 0
    for a in range(0, rows):
        y = y + blockSize
        pygame.draw.line(win, (255, 255, 255), (0, y), (width, y))
    for a in range(0, (rows * 2)):
        x = x + blockSize
        pygame.draw.line(win, (255, 255, 255), (x, 0), (x, height))
def createObstacles(snack, snake):
    returnList = []
    #posOfSnake = snake.body
    posOfSnack = snack.pos
    while(len(returnList)!=5):
        x = random.randint(3, 36)
        y = random.randint(1,18)
        if((x==20 and y ==10) or (x==21 and y ==10) or (x==22 and y ==10) or (x==23 and y ==10) or (x==posOfSnack[0] and y==posOfSnack[1])):
            continue
        else:
            obstacle = food((x,y), color=(255,0,0))
            returnList.append(obstacle)
    return returnList
def checkForObstacleCollision(coorOfHead, listOfObst):
    x = coorOfHead[0]
    y = coorOfHead[1]
    for i in range(len(listOfObst)):
        if(listOfObst[i].pos[0] ==x and listOfObst[i].pos[1] ==y):
            return True
    return False

def main():
    runningEasy = False
    runningHard = False
    clock = pygame.time.Clock()
    menuRun = True
    if(pygame.mixer.music.get_busy()==False):
        pygame.mixer.music.play()
    while menuRun:
        win.fill((67,110,238))
        win.blit(menuTitle, (188,20))
        win.fill((48,120,20), (400,100,200,100))
        win.blit(menuPlay, (448, 120))
        win.fill((48,120,20), (400, 230, 200, 100))
        win.blit(menuRules, (430, 250))
        win.fill((48,120,20), (400, 360, 200,100))
        win.blit(menuQuit, (433, 375))
        win.blit(snakeIMG, (60,120))
        win.blit(snakeIMG, (750,120))
        clock.tick(20)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    mousePos = pygame.mouse.get_pos()
                    if(mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>100 and mousePos[1]<200):
                        menuRun = False
                        x = displayPlayWin()
                        if(x==-1):#user clicked the red x
                            return
                        elif(x==0):#user pressed esc, return to mainmenu
                            main()
                            return
                        elif(x==1):
                            runningEasy = True
                        elif(x==2):
                            runningHard = True
                        break
                    elif (mousePos[0] > 400 and mousePos[0] < 600 and mousePos[1] > 230 and mousePos[1] < 330):
                        rulesRunning = True
                        while rulesRunning:
                            win.fill((67,110,238))
                            win.blit(rules1, (100,20))
                            win.blit(rules2, (260,120))
                            win.blit(rules3, (250,220))
                            win.blit(rules4, (220,400))
                            pygame.display.update()
                            clock.tick(20)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    return
                            keys = pygame.key.get_pressed()
                            if (keys[pygame.K_ESCAPE]):
                                rulesRunning = False
                    elif(mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>360 and mousePos[1]<460):
                        pygame.quit()
                        return
    s = snake((0,0,255), (20,10))
    snack = food(randomSnackPositions(s), color=(0, 255, 0))
    render()
    s.draw(win)
    snack.draw(win)
    listOfObstacles = []
    successInput = 1
    lastdirection = [0]  # 0 is right, 1 is left, 2 is up, 3 is down
    if(runningEasy):
        pygame.display.update()
    else:
        listOfObstacles = createObstacles(snack, s)
        for i in range(len(listOfObstacles)):
            listOfObstacles[i].draw(win)
        pygame.display.update()
    while runningEasy:
        pygame.mixer.music.stop()
        pygame.time.delay(50)
        clock.tick(10)
        pygame.event.pump()
        quit = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = 1
        if (quit == 1):
            pygame.quit()
            return
            #break
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT]):
            successInput = s.moveRight()
            lastdirection[0] = 0
        elif (keys[pygame.K_LEFT]):
            successInput = s.moveLeft()
            lastdirection[0] = 1
        elif (keys[pygame.K_UP]):
            successInput = s.moveUp()
            lastdirection[0] = 2
        elif (keys[pygame.K_DOWN]):
            successInput = s.moveDown()
            lastdirection[0] = 3
        elif (keys[pygame.K_ESCAPE]):
            runningEasy = False
        elif (lastdirection[0]==0):
            successInput = s.moveRight()
        elif (lastdirection[0]==1):
            successInput = s.moveLeft()
        elif (lastdirection[0]==2):
            successInput = s.moveUp()
        elif (lastdirection[0]==3):
            successInput = s.moveDown()
        if(successInput == -1):#collided into self
            pygame.mixer.Sound.play(crashSound)
            a = displayGameOver(0, str(len(s.body)))
            if(a == 1):
                return
            break
        elif(successInput == -2):#collided into wall
            pygame.mixer.Sound.play(crashSound)
            a = displayGameOver(1,str(len(s.body)))
            if(a == 1):
                return
            break
        if(s.body[0].pos == snack.pos):
            pygame.mixer.Sound.play(eatSound)
            snack = food(randomSnackPositions(s), color=(0, 255, 0))
            s.addBody(lastdirection)
        #for event in pygame.event.get():
           # if event.type == pygame.QUIT:
             #   pygame.quit()
        #else:
           # s.body.pop()
        render()
        s.draw(win)
        snack.draw(win)
        pygame.display.update()
    while runningHard:
        pygame.mixer.music.stop()
        pygame.time.delay(50)
        clock.tick(30)
        pygame.event.pump()
        quit = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = 1
        if (quit == 1):
            pygame.quit()
            return
            #break
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT]):
            successInput = s.moveRight()
            lastdirection[0] = 0
            #successInput = s.moveLeft()
            #lastdirection[0] = 1
        elif (keys[pygame.K_LEFT]):
            successInput = s.moveLeft()
            lastdirection[0] = 1
            #successInput = s.moveRight()
            #lastdirection[0] = 0
        elif (keys[pygame.K_UP]):
            successInput = s.moveUp()
            lastdirection[0] = 2
            #successInput = s.moveDown()
            #lastdirection[0] = 3
        elif (keys[pygame.K_DOWN]):
            successInput = s.moveDown()
            lastdirection[0] = 3
            #successInput = s.moveUp()
            #lastdirection[0] = 2
        elif (keys[pygame.K_ESCAPE]):
            runningHard = False
        elif (lastdirection[0]==0):
            successInput = s.moveRight()
        elif (lastdirection[0]==1):
            successInput = s.moveLeft()
        elif (lastdirection[0]==2):
            successInput = s.moveUp()
        elif (lastdirection[0]==3):
            successInput = s.moveDown()
        if(successInput == -1):#collided into self
            pygame.mixer.Sound.play(crashSound)
            a = displayGameOver(0, str(len(s.body)))
            if(a == 1):
                return
            break
        elif(successInput == -2):#collided into wall
            pygame.mixer.Sound.play(crashSound)
            a = displayGameOver(1, str(len(s.body)))
            if(a == 1):
                return
            break
        if(s.body[0].pos == snack.pos):
            pygame.mixer.Sound.play(eatSound)
            snack = food(randomSnackPositions(s), color=(0, 255, 0))
            s.addBody(lastdirection)
        elif(checkForObstacleCollision(s.body[0].pos, listOfObstacles) == True):
            pygame.mixer.Sound.play(bombSound)
            a = displayGameOver(3,str(len(s.body)))
            if(a == 1):
                return
            break
        #for event in pygame.event.get():
           # if event.type == pygame.QUIT:
             #   pygame.quit()
        #else:
           # s.body.pop()
        render()
        s.draw(win)
        snack.draw(win)
        for i in range(len(listOfObstacles)):
            listOfObstacles[i].draw(win)
        pygame.display.update()
    s.cleanup((20,10))
    main()
    return

if __name__ == '__main__':
    main()