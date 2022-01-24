import sys
import game

class Config:
    screen_size = 800, 800
    screen_border = 0.075, 0.075
    circle_to_rect_proportions = 0.35
    check_circle_ratio_to_guess = 0.6
    checks_to_guesses_width_ratio = 0.4
    guess_size = 4#8
    guess_num = 10
    option_num = 4#8

class Color:
    options = {
        "blue" : (0,0,200),
        "yellow" : (200,200,0),
        "green" : (0,200,0),
        "violet" : (200,0,200),
        "other0" : (100,100,200),
        "other1" : (200,100,50),
        "other2" : (200,0,0),
        "other3" : (200,200,200)
    }
    guesses = {
        "white" : (200,200,200),
        "red" : (200,0,0)
    }
    background = (30,30,30)
    black = (0,0,0)
    grey = (100,100,100)
    foreground = (50, 50, 75)

if __name__ == "__main__":
    game.Game.start()
