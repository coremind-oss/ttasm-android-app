import pygame
from colors import *

# Sprites are kind of object that accept Surfaces where we can insert rectangles(rectangles can be images etc )

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, width=128, height=128, color= blue):
        super(Rectangle,self).__init__()
        
        self.image = pygame.Surface( (height,width) )
        self.image.fill(color)

#putting surface incide a Rectangle for further handling 

        self.rect = self.image.get_rect()
        
#setting our sound on button push

        self.sound = pygame.mixer.Sound('sound.wav')
        
# defining a position of sprite through function

    def set_rect_position(self,x,y):
        self.rect.x = x
        self.rect.y = y
      
#Putting real Logo images in image rectangle placeholder
      
    def set_image(self, filename = None):
        if (filename != None):
            self.image = pygame.image.load(filename) 
            
            self.rect = self.image.get_rect()
            
# Function that will be called when button push to play a sound
    
    def sound_button_play(self):
        self.sound.play()
        

if (__name__ == '__main__'):
    pygame.init()
    
    window_size = 640,480
    
    window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
    
    pygame.display.set_caption('TTASM')
          
    window.fill(white)
    
# Initiation of accepting sprite into group
    
    Rectangle_group = pygame.sprite.Group()
    
    a_rectangle = Rectangle()

#calling a funciton to overwrite blue rectangle with actual logo image

    a_rectangle.set_image('TTASM.png')

    
# Setting a possition of logo   
    
    a_rectangle.set_rect_position(256 , 156)   
   
# Adding a sprite Logo into group  
  
    Rectangle_group.add(a_rectangle)
 
   
# Drawing group into window object

    Rectangle_group.draw(window)

    running = True
    
    
    while(running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                a_rectangle.sound_button_play()
                print("beggining communicaiton...")
    
        pygame.display.update()
    
    pygame.quit()
            
    