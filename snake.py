import turtle
class wall:
	def __init__(self,pos1,pos2,color):
		self._pos1=pos1
		self._pos2=pos2
		self.t=turtle.Turtle()
		
		self.t.penup()
		self.t.goto(self._pos1)
		self.t.pendown()
		self.t.color(color)
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
def makewall(pos1,pos2,screen,color):
	screen.tracer(0,0)
	walls.append(wall(pos1,pos2,color))
	screen.tracer(1,10)
wallpos1=(100,0)
wallpos2=(-100,0)
def main():
	w=turtle.Screen()
	w.tracer(0,0)
	makewall((100,-200),(100,200),w,"black")
	player=turtle.Turtle()
	player2=turtle.Turtle()
	player.speed(10)
	player2.speed(10)
	player2.color("red")
	player.color("blue")
	player2.goto(-100,0)
	def LTP1 ():
		global wallpos1
		player.lt(90)
		playerpos=player.pos()
		player.fd(1)
		makewall(wallpos1,playerpos,w,"blue")
		wallpos1=player.pos()
	def RTP1 ():
		global wallpos1
		player.rt(90)
		playerpos=player.pos()
		player.fd(1)
		makewall(wallpos1,playerpos,w,"blue")
		wallpos1=player.pos()
	def LTP2 ():
		global wallpos2
		player2.lt(90)
		playerpos2=player2.pos()
		player2.fd(1)
		makewall(wallpos2,playerpos2,w,"red")
		wallpos2=player2.pos()
	def RTP2 ():
		global wallpos2
		player2.rt(90)
		playerpos2=player2.pos()
		player2.fd(1)
		makewall(wallpos2,playerpos2,w,"red")
		wallpos2=player2.pos()
	makewall((-300,-200),(-300,200),w,"black")
	makewall((100,-200),(-300,-200),w,"black")
	makewall((-300,200),(100,200),w,"black")
	w.tracer(1,10)
	running1 = True
	running2 = True
	while (running1|running2==True):
		if(running1==True):
			w.onkey(LTP1,"Left")
			w.onkey(RTP1,"Right")
			w.listen()
			player.fd(1)
			for i in walls:
				if(i.collision_check(player)):
					running1 = False
		if(running2==True):
			w.onkey(LTP2,"d")
			w.onkey(RTP2,"a")
			w.listen()
			player2.fd(1)
			for i in walls:
				if(i.collision_check(player2)):
					running2 = False
	w.exitonclick()

if __name__=='__main__':
	main()	
