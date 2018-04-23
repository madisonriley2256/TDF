from gamelib import*
game=Game(800,600,"Trump Dance Off")
bk=Image("floor.jpg",game)
game.setBackground(bk)
logo=Image("hi.jpg",game)
logo.resizeBy(170)
play=Image("play.png",game)
play.moveTo(150,450)



t=Image("trump.png",game)
t.resizeBy(-80)
t.setSpeed(1,80)

t2=Image("trump.png",game)
t2.resizeBy(-80)
t2.setSpeed(1,80)




#howto=Image("howto.png",game)
#howto.resizeBy(-90)
#howto.moveTo(650,150)
boy=Image("boy.png",game)
floor=Image("floor.jpg",game)
floor.resizeBy(90)
#star=Animation("staran
down=Image("down.png",game)
up=Image("up.png",game)
left=Image("left.png",game)
right=Image("play.png",game)
down.moveTo(200,100)
up.moveTo(350,100)
right.moveTo(500,100)
left.moveTo(750,100)
down.resizeBy(-95)
up.resizeBy(-70)
right.resizeBy(-95)
left.resizeBy(-90)
boy.resizeBy(-30)
girl=Image("girl.png",game)
girl.resizeBy(-20)


t2=[]
for index in range(20):
    t2.append(Image("trump.png",game))
for index in range(5):
    x=randint(1,700)
    y=randint(100,4000)
    t2[index].moveTo(x,-y)
    t2[index].setSpeed(2,180)
    t2[index].resizeBy(-80)

    
arrowsup=[]
for index in range(20):
    arrowsup.append(Image("up.png",game))
for index in range(20):
    x=randint(1,700)
    y=randint(100,4000)
    arrowsup[index].moveTo(x,-y)
    arrowsup[index].setSpeed(2,180)
    arrowsup[index].resizeBy(-70)




arrowsdown=[]
for index in range(5):
    arrowsdown.append(Image("down.png",game))
for index in range(5):
    x=randint(1,700)
    y=randint(100,4000)
    arrowsdown[index].moveTo(x,-y)
    arrowsdown[index].setSpeed(2,180)
    arrowsdown[index].resizeBy(-95)



arrowsleft=[]
for index in range(5):
    arrowsleft.append(Image("left.png",game))
for index in range(5):
    x=randint(1,700)
    y=randint(100,4000)
    arrowsleft[index].moveTo(x,-y)
    arrowsleft[index].setSpeed(2,180)
    arrowsleft[index].resizeBy(-90)




arrowsright=[]
for index in range(20):
    arrowsright.append(Image("up.png",game))
for index in range(20):
    x=randint(1,700)
    y=randint(100,4000)
    arrowsright[index].moveTo(x,-y)
    arrowsright[index].setSpeed(2,180)
    arrowsright[index].resizeBy(-95)
  

game.update(60)

#moneys=[]
#for index in range(5):
   # moneys.append(Image("money.jpg",game))
    


#TITLE SCREEN
while not game.over:
    game.processInput()
    logo.draw()
    play.draw()
    boy.draw()
    #howto.draw()
    
    
    game.drawText("HAVE FUN AND BEAT TRUMP!",550,450)
    game.drawText("PRESS BUTTON BELOW TO PLAY",30,350)
    game.drawText("Use the arrows to move",550,400)
    game.drawText("the characters to defeat Trump!",495,415)
    game.drawText("TRUMP DANCE OFF",320,150)


    if play.collidedWith(mouse) and mouse.LeftButton:
        game.over = True

        
    game.update(60)
    
game.over = False

#LEVEL 1






boy.moveTo(100,500)
girl.moveTo(500,500)



while not game.over:
    game.processInput()
    #boy.moveTo(500,100)
    floor.draw()
    boy.draw()
    girl.draw()
    #down.draw()
    #up.draw()
    #left.draw()
    #right.draw()
    #dora.draw()
   

    
    t.move(True)
    for index in range(5):
        arrowsup[index].move()
        if boy.collidedWith(arrowsup[index]):
            boy.height+=1
            boy.width+=1
            boy.moveTo(randint(100,550),randint(100,500))


        
    for index in range(5):
        arrowsdown[index].move()
        if boy.collidedWith(arrowsdown[index]):
            boy.height+=1
            boy.width+=1
            boy.moveTo(randint(100,580),randint(100,500))
            
    for index in range(5):
        arrowsleft[index].move()
        if boy.collidedWith(arrowsleft[index]):
            boy.height+=1
            boy.width+=1
            boy.moveTo(randint(100,570),randint(100,500))
            
    for index in range(5):
        arrowsright[index].move()
        if boy.collidedWith(arrowsright[index]):
            boy.height+=1
            boy.width+=1
            boy.moveTo(randint(100,590),randint(100,500))


    for index in range(5):
        arrowsup[index].move()
        if girl.collidedWith(arrowsup[index]):
            girl.height+=1
            girl.width+=1
            girl.moveTo(randint(100,530),randint(100,500))

            
            


        
    for index in range(5):
        arrowsdown[index].move()
        if girl.collidedWith(arrowsdown[index]):
            girl.height+=1
            girl.width+=1
            girl.moveTo(randint(100,520),randint(100,500))
            
    for index in range(5):
        arrowsleft[index].move()
        if girl.collidedWith(arrowsleft[index]):
            girl.height+=1
            girl.width+=1
            girl.moveTo(randint(100,570),randint(100,500))
            
    for index in range(5):
        arrowsright[index].move()
        if girl.collidedWith(arrowsright[index]):
            girl.height+=1
            girl.width+=1
            girl.moveTo(randint(100,510),randint(100,500))


    for index in range(5):
        t2[index].move()
        if girl.collidedWith(t2[index]):
            girl.resizeBy(-5) 

            

        
    if keys.Pressed[K_UP]:
        girl.y -= 4#Up 4 pixels
    if keys.Pressed[K_DOWN]:
        girl.y += 4
    if keys.Pressed[K_RIGHT]:
        girl.x += 4
    if keys.Pressed[K_LEFT]:
        girl.x -= 4



    if keys.Pressed[K_w]:
        boy.y -= 4#Up 4 pixels
    if keys.Pressed[K_s]:
        boy.y += 4
    if keys.Pressed[K_d]:
        boy.x += 4
    if keys.Pressed[K_a]:
        boy.x -= 4

    if boy.collidedWith(t):
        boy.height-=4
        boy.width-=4

        
    if girl.collidedWith(t):
        girl.height-=3
        girl.width-=3

    if t.collidedWith(girl):
        t.height-=3
        t.width-=3

        
        t.resizeBy(1)
    

    bk2=Image("trump win bk.jpg",game)
    lose=Image("trump wins.png",game)
    game.setBackground(bk2)
        
    

    if boy.height<=10:
        game.over=True


        bk2=Image("trump win bk.jpg",game)
        lose=Image("trump wins.png",game)
        game.setBackground(bk2)
        bk2.draw()

        game.drawText("Trump won... Better luck next time.",250,100)
        lose.resizeBy(-60)
        lose.moveTo(350,400)
        lose.draw()
        

    if t.height<=10:

        bk3=Image("we won bk.jpg",game)
        game.setBackground(bk3)
        bk3.draw()
   
        game.drawText("Good job, you beat Trump!",250,100)
        boy=Image("boy.png",game)
        boy.draw()


        game.over=True

    game.update(10)

