import pygame as pg

pg.init()
width = 600
height = 400
screen = pg.display.set_mode((width, height))

class UserInterface:

    def __init__(self, screen, width, height):
        self.delay = 100
        self.screen = screen
        self.width = width
        self.height = height
        self.button = (self.width/2 - 100, self.height-100, 200, 80)

    def run(self):

        running = True
        while running:
            self.screen.fill((255, 255, 255))

            pg.draw.rect(self.screen, (0, 255, 0), self.button, 0)

            x, y = pg.mouse.get_pos()
            if x >= self.width / 2 - 100 and x <= self.width / 2 + 100 and y >= self.height - 100 and y <= self.height + 80:
                pg.draw.rect(self.screen, (255, 255, 0), self.button, 0)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if x >= self.width/2-100 and x <= self.width/2+100 and y >= self.height-100 and y <= self.height+80:
                    if pg.mouse.get_pressed()[0]:
                        print("YOYOYO") #TODO: connect the interface to the socket server


            pg.display.flip()
            pg.event.pump()
            pg.time.delay(self.delay)

        pg.quit()

user = UserInterface(screen=screen, width=width, height=height)
user.run()
