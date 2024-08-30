import pygame
from blobSetup import Blob

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WIDTH = 400
HEIGHT = 600
STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOB = 4
STARTING_GREEN_BLOBS = 5
game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob: The BAll")
clock = pygame.time.Clock()


class Blue_blob(Blob):

    def __init__(self,color,x_boundary,y_boundary,size):
        super().__init__(color,x_boundary,y_boundary,size)
        self.color = BLUE

class Red_blob(Blob):

    def __init__(self,color,x_boundary,y_boundary,size):
        super().__init__(color,x_boundary,y_boundary,size)
        self.color = RED

class Green_blob(Blob):

    def __init__(self,color,x_boundary,y_boundary,size):
        super().__init__(color,x_boundary,y_boundary,size)
        self.color = GREEN

def environment(Blob_list):
    game_display.fill(WHITE)
    for Blobs in Blob_list:
        for Blob_id in Blobs:
            Blob = Blobs[Blob_id]
            pygame.draw.circle(game_display,Blob.color,[Blob.x,Blob.y],Blob.size)
            Blob.move()
            Blob.check_bounds()
    pygame.display.update()

def main():
    blue_blobs = dict(enumerate([Blue_blob(BLUE,WIDTH,HEIGHT,(5,9)) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Red_blob(RED,WIDTH,HEIGHT,(5,9)) for i in range(STARTING_RED_BLOB)]))
    green_blobs = dict(enumerate([Green_blob(GREEN,WIDTH,HEIGHT,(5,9)) for i in range(STARTING_GREEN_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 

        environment([blue_blobs,red_blobs,green_blobs])
        clock.tick(60)
        
        

if __name__ == '__main__':
    main()
    