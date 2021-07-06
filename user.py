import pygame as pg

pg.init()
width = 600
height = 400
screen = pg.display.set_mode((width, height))
pg.display.set_caption("MASS (Mr. Adasko's Security System)")

class UserInterface:

    def __init__(self, screen, width, height):
        self.delay = 10
        self.screen = screen
        self.width = width
        self.height = height
        self.button = (self.width/2 - 100, self.height-100, 200, 80)
        self.counter = 1

    def not_connected(self):
        self.screen.fill((255, 255, 255))

        pg.draw.rect(self.screen, (0, 255, 0), self.button, 0)

        pg.font.init()  # you have to call this at the start, if you want to use this module.
        myfont = pg.font.SysFont('Times New Roman', 30)

        textsurface = myfont.render('Connect', False, (0, 0, 0))
        screen.blit(textsurface, (self.width / 2 - 50, self.height - 85))

        x, y = pg.mouse.get_pos()
        if x >= self.width / 2 - 100 and x <= self.width / 2 + 100 and y >= self.height - 100 and y <= self.height + 80:
            pg.draw.rect(self.screen, (255, 255, 0), self.button, 0)
            textsurface = myfont.render('Connect', False, (255, 0, 0))
            screen.blit(textsurface, (self.width / 2 - 50, self.height - 85))

    def connected(self):
        self.screen.fill((255, 255, 255))

        pg.draw.rect(self.screen, (0, 255, 0), self.button, 0)

        pg.font.init()  # you have to call this at the start, if you want to use this module.
        myfont = pg.font.SysFont('Times New Roman', 30)

        textsurface = myfont.render('Disconnect', False, (0, 0, 0))
        screen.blit(textsurface, (self.width / 2 - 65, self.height - 85))

        x, y = pg.mouse.get_pos()
        if x >= self.width / 2 - 100 and x <= self.width / 2 + 100 and y >= self.height - 100 and y <= self.height + 80:
            pg.draw.rect(self.screen, (255, 255, 0), self.button, 0)
            textsurface = myfont.render('Disconnect', False, (255, 0, 0))
            screen.blit(textsurface, (self.width / 2 - 65, self.height - 85))

    def run(self):

        running = True
        while running:

            if self.counter % 2 == 0:
                self.connected()
            else:
                self.not_connected()

            x, y = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if x >= self.width/2-100 and x <= self.width/2+100 and y >= self.height-100 and y <= self.height+80:
                    if pg.mouse.get_pressed()[0]:
                        print("YOYOYO") #TODO: connect the interface to the socket server
                        self.counter += 1

            pg.display.flip()
            pg.event.pump()
            pg.time.delay(self.delay)

        pg.quit()

user = UserInterface(screen=screen, width=width, height=height)
user.run()
