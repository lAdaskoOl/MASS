'''
import pygame as pg

pg.init()

screen = pg.display.set_mode((500, 300))

counter = 60
c = 0

running = True
while running:
    screen.fill((255, 255, 255))

    pg.font.init()
    myfont = pg.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(counter), False, (0, 0, 0))
    screen.blit(textsurface, (230, 100))

    c += 1
    if c == 100:
        counter -= 1
        c = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()
    pg.event.pump()
    pg.time.delay(10)

pg.quit()
'''

import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print('Speak anything: ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
        except:
            print('Could not recognize your voice')