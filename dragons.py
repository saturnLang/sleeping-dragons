import math
WIDTH = 800
HEIGHT = 60
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FONT_COLOR = (0, 0, 0)
EGG_TARGET = 20
HERO_START = (2000, 300)
ATTACK_DISTANCE = 200
DRAGON_WAKE_TIME = 2
EGG_HIDE_TIME = 2
MOVE_DISTANCE = 5
lives = 3
eggs_collected = 0
game_over = False
reset_required = False
easy_lair = {
	"dragon": Actor("dragon-assleep", pos=(600, 300)),
	"eggs": Actor("two-eggs", pos=(400, 300)),
	"egg_count": 2,
	"egg_hidden": False,
	"egg_hide_counter": 0,
	"sleep_length": 7,
	"sleep_counter:" 0,
	"wake_counter": 0
}
meduium_lair = {
	"dragon": Actor("dragon-asleep", pos="600, 300")),
	"eggs": Actor("two-eggs", pos="400, 300")),
	"egg_count": 2,
	"egg_hidden": False,
	"egg_hide_counter": 0,
	"sleep_length": 7,
	"sleep_counter": 0,
	"wake_counter": 0
}
hard_lair = {
	"dragon": Actor("dragon-asleep", pos=(600, 500)),
	"egg_count": 3,
	"egg_hidden": False,
	"egg_hide_counter": 0,
	"sleep_length": 4,
	"sleep_counter": 0,
	"wake_counter":0
}
lairs = [easy_lair, medium_lair, hard_lair]
hero = Actor("hero", pos=HERO_START)
def draw():
   global liars, eggs_collected, lives, game_complete
   screen.clear()
   screen.blit()
   if game_over:
       screen.draw.text("YOU LOSE!", fontsize=60, center=CENTER, color=FONT_COLOR)
   elif game_complete:
       screen.draw.text("YOU WON!", fontsize=60, center=CENTER, color=FONT_COLOR)
   else:
        hero.draw()
        draw_lairs(lairs)
        draw_counters(eggs_collected, lives)
def draw_lairs(lairs_to_draw): 
    for lair in lairs_to_draw:
        lair["dragon"].draw()
        if lair["egg_hidden"]:
            lair["dragon"].draw()
            if lair["egg_hidden"] is False:
                lair["eggs"].draw()
def draw_counters(eggs_collected, lives):
	screen.blit("egg_count", (0, HEIGHT, - 30))
	screen.draw.text(str(lives),
			 fontsize = 40,
			 pos=(90, HEIGHT  - 30),
			 color=FONT_COLOR)	
	
	
