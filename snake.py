import turtle
class wall:
	def __init__(self,pos1,pos2):
		self._pos1=pos1
		self._pos2=pos2
		self.t=turtle.Turtle()
		
		self.t.penup()
		self.t.goto(self._pos1)
		self.t.pendown()
		self.t.goto(self._pos2)
		self.t.hideturtle()
		self._x1=self._pos1[0]
		self._y1=self._pos1[1]
		self._x2=self._pos2[0]
		self._y2=self._pos2[1]
		
	def collision_check(self,turtle):
		self._turtlex=turtle.xcor()
		self._turtley=turtle.ycor()
		self._dist=(((self._x1-self._x2)**2+(self._y1-self._y2)**2)**0.5)
		self._dist2=(((self._x1-self._turtlex)**2+(self._y1-self._turtley)**2)**0.5)
		self._dist3=(((self._turtlex-self._x2)**2+(self._turtley-self._y2)**2)**0.5)
		if(self._dist2+self._dist3==self._dist):
			
			return True
		
walls = []
def makewall(pos1,pos2,screen):
	screen.tracer(0,0)
	walls.append(wall(pos1,pos2))
	screen.tracer(1,10)
wallpos1=(0,0)
def main():
	w=turtle.Screen()
	w.tracer(0,0)
	makewall((100,-200),(100,200),w)
	player=turtle.Turtle()
	def LT ():
		global wallpos1
		player.lt(90)
		playerpos=player.pos()
		player.fd(1)
		makewall(wallpos1,playerpos,w)
		wallpos1=player.pos()
	def RT ():
		global wallpos1
		player.rt(90)
		playerpos=player.pos()
		player.fd(1)
		makewall(wallpos1,playerpos,w)
		wallpos1=player.pos()
	makewall((-300,-200),(-300,200),w)
	makewall((100,-200),(-300,-200),w)
	makewall((-300,200),(100,200),w)
	w.tracer(1,10)
	running = True
	while (running):
		w.onkey(LT,"Left")
		w.onkey(RT,"Right")
		w.listen()
		
		player.fd(1)
		for i in walls:
			if (i.collision_check(player)):
				running = False
	w.exitonclick()

if __name__=='__main__':
	main()	
