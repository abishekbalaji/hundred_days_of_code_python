def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    while wall_in_front():
        turn_left()
    while wall_on_right():
        if wall_in_front():
            break
        elif at_goal():
            break
        move()
    else:
        turn_right()
        move()
        turn_right()
        move()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
        
     
     
        
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()