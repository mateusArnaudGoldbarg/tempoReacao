'''
UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
Sistemas de Tempo Real - Medidor de Tempo de Reação
Mateus Arnaud Santos de Sousa Goldbarg
20200000788
'''

import arcade
import random
import time
import statistics

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 80

class Red:
    def __init__(self):
        self.center = Point()
        self.center.x = SCREEN_WIDTH/2
        self.center.y = 3*SCREEN_HEIGHT/4
        self.alive = True
        self.cmd = 'up'

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.center.radius, arcade.color.RED)

class Blue:
    def __init__(self):
        self.center = Point()
        self.center.x = SCREEN_WIDTH/2
        self.center.y = 1*SCREEN_HEIGHT/4
        self.alive = True
        self.cmd = 'down'
        self.tries = 0

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.center.radius, arcade.color.BLUE)

class Yellow:
    def __init__(self):
        self.center = Point()
        self.center.x = 0.5*SCREEN_WIDTH/2
        self.center.y = 2*SCREEN_HEIGHT/4
        self.alive = True
        self.cmd = 'left'

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.center.radius, arcade.color.YELLOW)

class Green:
    def __init__(self):
        self.center = Point()
        self.center.x = 1.5*SCREEN_WIDTH/2
        self.center.y = 2*SCREEN_HEIGHT/4
        self.alive = True
        self.cmd = 'right'

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.center.radius, arcade.color.GREEN)

class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.held_keys = set()
        self.cmd = ''
        self.score = 0
        self.tries = 0
        #self.ready=False
        self.next=[]
        self.red=Red()
        arcade.set_background_color(arcade.color.BLACK)
        self.reacoes = []
        self.music = None

    def update(self, delta_time):
        #self.on_key_press()
        self.ran = random.randint(1, 100)
        if self.ran == 1 and len(self.next) == 0 and self.tries < 10:
            self.set_light()

    def on_draw(self):
        arcade.start_render()
        self.draw_score()

        if self.tries < 10:
            for light in self.next:
                light.draw()

        else:
            self.draw_result()

    def draw_result(self):
        arcade.draw_text("Fim de Teste", start_x=30, start_y=SCREEN_HEIGHT/2, font_size=60, color=arcade.color.WHITE,bold=True)
        arcade.draw_text("Tempos:", start_x=SCREEN_WIDTH/2, start_y= SCREEN_HEIGHT - 100, font_size=25, color=arcade.color.YELLOW)
        start_y = SCREEN_HEIGHT - 100
        for i in range(0,len(self.reacoes)):
            p1 = "{}ms".format(self.reacoes[i])
            start_x = SCREEN_WIDTH/2+30
            start_y -= 50
            arcade.draw_text(p1, start_x=start_x, start_y=start_y, font_size=25, color=arcade.color.YELLOW)

        score_text = "Acertos:"
        start_x = SCREEN_WIDTH/2 +200
        start_y = SCREEN_HEIGHT - 100
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=30, color=arcade.color.YELLOW)

        p1 = "{}".format(self.score)
        start_x = SCREEN_WIDTH/2 + 250
        start_y -= 50
        arcade.draw_text(p1, start_x=start_x, start_y=start_y, font_size=25, color=arcade.color.YELLOW)

        score_text = "Média:"
        start_x = SCREEN_WIDTH/2 + 360
        start_y = SCREEN_HEIGHT - 100
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=30, color=arcade.color.YELLOW)

        p1 = "{}ms".format(statistics.mean(self.reacoes))
        start_x = SCREEN_WIDTH/2 + 360
        start_y -= 50
        arcade.draw_text(p1, start_x=start_x, start_y=start_y, font_size=25, color=arcade.color.YELLOW)



    def draw_score(self):
        """
        Puts the current score on the screen
        """

        score_text = "Tentativas: {}".format(self.tries)
        start_x = 50
        start_y = SCREEN_HEIGHT - 50
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=30, color=arcade.color.YELLOW)

    def set_light(self):
        wt = random.randint(1,4)
        print(wt)
        if wt == 1:
            light = Red()
            self.inicial = int(round(time.time() * 1000))
            #self.ready=True
        if wt == 2:
            light = Blue()
            self.inicial = int(round(time.time() * 1000))
            #self.ready=True
        if wt == 3:
            light = Yellow()
            self.inicial = int(round(time.time() * 1000))
            #self.ready=True
        if wt == 4:
            light = Green()
            self.inicial = int(round(time.time() * 1000))
            #self.ready=True
        self.setup()
        self.next.append(light)


    def clean(self):
        for lights in self.next:
            if self.cmd == lights.cmd:
                self.final = int(round(time.time() * 1000))
                self.tries += 1
                self.score += 1
                self.next.remove(lights)
                self.decorrido = self.final-self.inicial
                self.cmd=''
                self.reacoes.append(self.decorrido)
                print(self.reacoes)

            else:
                self.score -= 1


        if self.cmd == ' ':
            self.cmd = 'space'
            self.tries = 0
            self.score = 0
            self.reacoes.clear()
            self.cmd = ''
            self.ran = 0


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP: #Vermelho
            self.cmd = 'up'
        if key == arcade.key.DOWN: #Azul
            self.cmd = 'down'
        if key == arcade.key.LEFT: #Amarelo
            self.cmd = 'left'
        if key == arcade.key.RIGHT: #Verde
            self.cmd = 'right'
        if key == arcade.key.SPACE: #Reset
            self.cmd = ' '

        print(self.cmd)
        self.clean()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    def play_song(self,musica):
        """
        Play noises of the game

        :param musica:
        :return:
        """
        if self.music:
            self.music.stop()
        self.music = arcade.Sound(musica,streaming=True)
        self.music.play(0.1)

    def setup(self):
        """
        Noise for shooting
        :return:
        """
        self.musica = ":resources:sounds/laser1.wav"
        self.play_song(self.musica)

# Creates the game and starts it going

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()