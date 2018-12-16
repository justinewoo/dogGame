#pygame is a free and open source library 

import pygame
from random import randint

pygame.init()

MAX_NUM_BONES = 15
numBonesInGame = 1
DOG_SPEED = 10
SCREEN_SIZE_X = 700
SCREEN_SIZE_Y = 700


gameOver = False
boneList = []
spiderList = []
moreBone = 0



#********************************************
#Dog class
#********************************************
class Dog(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		
		self.image = pygame.image.load("dog3.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 10
		self.rect.y = 10
		self.speed = DOG_SPEED
		self.alive = 1
	
	
	def moveright(self):
		self.rect.x += self.speed
	
	def moveleft(self):
		self.rect.x -= self.speed
		
	def moveup(self):
		self.rect.y -= self.speed
		
	def movedown(self):
		self.rect.y += self.speed
	
	def drawdog(self):
		if self.rect.x >= SCREEN_SIZE_X:
			self.rect.x = 1
		if self.rect.y >= SCREEN_SIZE_Y:
			self.rect.y = 1
		if self.rect.x <= 0:
			self.rect.x = SCREEN_SIZE_X - self.rect.width
		if self.rect.y <= 0:
			self.rect.y = SCREEN_SIZE_Y - self.rect.height
		screen.blit(self.image, (self.rect.x, self.rect.y))
		
	def collideDog(self, sprite2):
		return self.rect.colliderect(sprite2.rect)
	
	def deadDog(self):
		self.alive = 0
		
	def isDogAlive(self):
		return self.alive
				

#********************************************
#bone class
#********************************************
class Bone(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("bone2.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = randint(0,SCREEN_SIZE_X - self.rect.width)
		self.rect.y = randint(0,SCREEN_SIZE_Y - self.rect.height)
		self.eat = 1
		
	def drawBone(self):
		screen.blit(self.image , (self.rect.x, self.rect.y))
		
	def eatBone(self):
		self.eat = 0
		
	def boneEaten(self):
		return self.eat
	
	def collideBone(self, sprite2):
		return self.rect.colliderect(sprite2.rect)


#********************************************
#Cat class	
#********************************************
class Cat(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		
		self.image = pygame.image.load("cat3.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = randint(0,SCREEN_SIZE_X - self.rect.width)
		self.rect.y = randint(0,SCREEN_SIZE_Y - self.rect.height)
		self.alive = 0
		self.killed = 0
		self.movex = 0
		self.movey = 0
		self.MAXTIME = 15
		self.timeToMove = self.MAXTIME
	
	
	def drawCat(self):
		screen.blit(self.image, (self.rect.x, self.rect.y))
	
	def isAlive(self):
		return self.alive
		
	def comeAlive(self):
		self.alive = 1
		
	def killSelf(self):
		self.alive = 0
		self.killed = 1
		
		
	def move(self):
	    
	    self.timeToMove -= 1

	    if (self.timeToMove == 0):
	    	self.rect.x += randint(-50, 50)
	    	self.rect.y += randint(-50,50)
	    	if self.rect.x >= SCREEN_SIZE_X:
	    		self.rect.x = 1
	    	if self.rect.y >= SCREEN_SIZE_Y:
	    		self.rect.y = 1
	    	if self.rect.x <= 0:
	    		self.rect.x = SCREEN_SIZE_X - self.rect.width
	    	if self.rect.y <= 0:
	    		self.rect.y = SCREEN_SIZE_Y - self.rect.height
	    	self.timeToMove = self.MAXTIME
	    	
#********************************************
#Spider class	
#********************************************
class Spider(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		
		self.image = pygame.image.load("spider2.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = randint(0, SCREEN_SIZE_X - self.rect.width)
		self.rect.y = 0
		self.movey = 10
	
	def drawSpider(self):
		screen.blit(self.image, (self.rect.x, self.rect.y))
	
	def spiderMove(self):
		self.rect.y += self.movey
		
	def collideSpider(self, sprite2):
		return self.rect.colliderect(sprite2.rect)
		
		
	
		
	
				
#********************************************
#The main program
#********************************************
size = width, height = SCREEN_SIZE_X, SCREEN_SIZE_Y
black = (0, 0, 0)
white = (255, 250, 250)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
	
#Input the number of bones to eat
inputOK = False
while not inputOK:
	inp = int(input('Enter # Bones (Max of 15):'))
	if (inp >= 1) and (inp <= MAX_NUM_BONES):
		numBonesInGame = inp
		inputOK = True
		
#create the dog and cat
myDog = Dog()    
myCat = Cat()


#Create the number of bones
for x in range(0, numBonesInGame):
	boneCollide = True
	while boneCollide == True:
		boneCollide = False
		tempBone = Bone()
		for y in boneList:
			if y.collideBone(tempBone):
				boneCollide = True
		if boneCollide == False:
				boneList.append(tempBone)



for x in range(0, 3):
	#Create the spiders and make sure they don't collide with each other
	#Also, make sure the dog doesn't collide with any spiders
	spiderCollide = True
	while spiderCollide == True:
		spiderCollide = False
		tempSpider = Spider()
		for y in spiderList:
			if y.collideSpider(tempSpider):
				spiderCollide = True
		if myDog.collideDog(tempSpider):
			spiderCollide = True
		if spiderCollide == False:
			spiderList.append(tempSpider)
			
			
while not gameOver:
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_DOWN]:
			myDog.movedown()
		if pressed[pygame.K_LEFT]:
			myDog.moveleft()
		if pressed[pygame.K_UP]:
			myDog.moveup()
		if pressed[pygame.K_RIGHT]:
			myDog.moveright()
		if pressed[pygame.K_q]:
			gameOver = True
			pygame.quit()
		

		#Update the display
		screen.fill(white)	
		
		for spiderx in spiderList:
								
			if (spiderx.rect.y < SCREEN_SIZE_Y):
				spiderx.drawSpider()
				spiderx.spiderMove()
			else: 
				spiderx.rect.y = 0
			
			if myDog.collideDog(spiderx):
				myDog.deadDog()
			if myDog.isDogAlive():
				myDog.drawdog()
				
		for bonex in boneList:
			if myDog.collideDog(bonex):
				bonex.eatBone()
			if bonex.boneEaten():
				bonex.drawBone()
				
		moreBone = 0
		for x in boneList:
			moreBone += x.boneEaten()
		
		if (moreBone == 0):
			myCat.comeAlive()	
				
		if (myCat.isAlive() == 1) and (myCat.killed == 0):
			myCat.drawCat()
			myCat.move()
			if myDog.collideDog(myCat):
				myCat.killSelf()
				screen.fill(black)
				myChar = (input('GAME OVER. Press <ENTER>'))	
				gameOver = True
				
		if not myDog.isDogAlive():
			screen.fill(black)
			end = (input('You Lost. Press <ENTER> '))
			gameOver = True
			

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = True
				pygame.quit()
			
		pygame.display.update()
		clock.tick(60)

