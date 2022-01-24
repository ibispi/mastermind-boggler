import sys
import pygame
from random import randint
from config import Color, Config

#STARTED: 17:04

class Game:

    running = True
    option_list = list()
    winning_combo = list()
    guess_list = list()
    check_list = list()
    current_row = 0
    current_column = 0
    winner = False

    def produce_winning_combo():
        if Config.option_num > len(Color.options):
            Config.option_num = len(Color.options) 

        Game.winning_combo = []
        Game.option_list = list(Color.options.keys())[:Config.option_num]
        for i in range(Config.guess_size):
            Game.winning_combo.append(
                Game.option_list[randint(0, Config.option_num-1)])

    def guess_column(guess):
        if not Game.winner:
            if guess != "blank":
                if Game.current_column != Config.guess_size-1:
                    Game.guess_list[Game.current_row][Game.current_column] = guess
                    Game.current_column = min(Game.current_column+1,Config.guess_size-1)
                elif Game.guess_list[Game.current_row][Game.current_column]=="blank":
                    Game.current_column = min(Game.current_column+1,Config.guess_size-1)
                    Game.guess_list[Game.current_row][Game.current_column] = guess
            elif guess == "blank":
                if Game.guess_list[Game.current_row][Game.current_column]=="blank":
                    Game.current_column = max(Game.current_column-1,0)
                Game.guess_list[Game.current_row][Game.current_column] = guess

    def guess_row():
        if (Game.winner):
            Game.reset()
        else:
            Game.check_list[Game.current_row] = ["blank" for i in range(Config.guess_size)]
            if "blank" in Game.guess_list[Game.current_row]:
                return
            marked_guesses = [False for i in range(Config.guess_size)]
            red_indices = set()
            for guess_column, guess in enumerate(Game.guess_list[Game.current_row]):
                if guess == Game.winning_combo[guess_column]:
                    Game.check_list[Game.current_row][guess_column] = "red"
                    marked_guesses[guess_column] = True
                    red_indices.add(guess_column)
            for guess_column, guess in enumerate(Game.guess_list[Game.current_row]):
                if guess_column not in red_indices:
                    for winning_index,winning_guess in enumerate(Game.winning_combo):
                        if not marked_guesses[winning_index] and \
                            guess == winning_guess:
                            Game.check_list[Game.current_row][winning_index] = "white"
                            marked_guesses[winning_index] = True
                            break;
            if Config.guess_size == Game.check_list[Game.current_row].count("red"):
                Game.winner = True
            else:
                Game.check_list[Game.current_row] = sorted(Game.check_list[Game.current_row])
                if (Game.current_row == Config.guess_num-1):
                    Game.winner = True
                Game.current_row = min(Game.current_row+1, Config.guess_num-1)
                Game.current_column = 0

    def reset():
        Game.winner = False
        Game.current_row = 0
        Game.current_column = 0
        Game.produce_winning_combo()
        Game.guess_list = [["blank" for i in range(Config.guess_size)]
                      for j in range(Config.guess_num)]
        Game.check_list = [["blank" for i in range(Config.guess_size)]
                      for j in range(Config.guess_num)]

    def print_help():
        print()
        print("Usage: python game.py [OPTION]")
        print()
        print("Controls:")
        print("1-8 keys to place pegs")
        print("space or enter to guess a row")
        print("escape to quit")
        print()
        print("Options:")
        print("-h or --help for help")
        print("-ww [VALUE] or --window-width [VALUE] for setting window width")
        print("-wh [VALUE] or --window-height [VALUE] for setting window height")
        print("-gs [VALUE] or --guess-size [VALUE] for setting the size of the combination to be guessed (default: 4, max: 8)")
        print("-an [VALUE] or --attempt-number [VALUE] for setting the number of attempts (default: 10, max: 20)")
        print("-on [VALUE] or --option-number [VALUE] for setting the number of different pegs (default: 4, max 8)")
        print()
        print("Examples:")
        print("python game.py")
        print("python game.py -ww 1920 -wh 1080 -gs 8 -an 20 -on 8") 
        
    def start():

        if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
            Game.print_help()
            pygame.quit()
            sys.exit()
        else:
            prev_arg = ""
            for arg in sys.argv[1:]:
                try:
                    input_num = int(arg)
                    if prev_arg != "":
                        if prev_arg == "--window-width" or prev_arg == "-ww":
                            Config.screen_size = input_num, Config.screen_size[1]
                        elif prev_arg == "--window-height" or prev_arg == "-wh":
                            Config.screen_size = Config.screen_size[0], input_num
                        elif prev_arg == "--guess-size" or prev_arg == "-gs":
                            Config.guess_size = max(min(input_num, 8), 2)
                        elif prev_arg == "--attempt-number" or prev_arg == "-an":
                            Config.guess_num = max(min(input_num, 20), 2)
                        elif prev_arg == "--option-number" or prev_arg == "-on":
                            Config.option_num = max(min(input_num, 8), 2)
                        prev_arg = ""
                except:
                    prev_arg = arg

        pygame.init()

        screen = pygame.display.set_mode(Config.screen_size)

        Game.reset()

        while Game.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_1 and Config.option_num >= 1:
                        Game.guess_column(Game.option_list[0])
                    elif event.key==pygame.K_2 and Config.option_num >= 2:
                        Game.guess_column(Game.option_list[1])
                    elif event.key==pygame.K_3 and Config.option_num >= 3:
                        Game.guess_column(Game.option_list[2])
                    elif event.key==pygame.K_4 and Config.option_num >= 4:
                        Game.guess_column(Game.option_list[3])
                    elif event.key==pygame.K_5 and Config.option_num >= 5:
                        Game.guess_column(Game.option_list[4])
                    elif event.key==pygame.K_6 and Config.option_num >= 6:
                        Game.guess_column(Game.option_list[5])
                    elif event.key==pygame.K_7 and Config.option_num >= 7:
                        Game.guess_column(Game.option_list[6])
                    elif event.key==pygame.K_8 and Config.option_num >= 8:
                        Game.guess_column(Game.option_list[7])
                    elif event.key==pygame.K_BACKSPACE:
                        Game.guess_column("blank")
                    elif event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key==pygame.K_SPACE or event.key==pygame.K_RETURN:
                        Game.guess_row()

            screen.fill(Color.background)

            rect_x = Config.screen_border[0]*Config.screen_size[0]
            rect_y = Config.screen_border[1]*Config.screen_size[1]
            rect_w = Config.screen_size[0]-rect_x*2
            rect_h = Config.screen_size[1]-rect_y*2
            pygame.draw.rect(screen, Color.foreground,
                ((rect_x,rect_y),(rect_w,rect_h)))
            circle_rect_height = rect_h / (Config.guess_num+1)
            rect_w_checks = Config.checks_to_guesses_width_ratio*rect_w
            rect_w_guesses = rect_w-rect_w_checks
            circle_rect_width = min(min(rect_w_guesses/Config.guess_size,
                                    rect_w/Config.option_num),
                                    circle_rect_height)
            rect_h_checks_and_guesses = rect_h - circle_rect_height
            circle_radius = min(Config.circle_to_rect_proportions*circle_rect_width,
                                Config.circle_to_rect_proportions*circle_rect_height)
            
            check_rect_w = circle_rect_width*Config.check_circle_ratio_to_guess
            check_rect_h = circle_rect_height*Config.check_circle_ratio_to_guess
            check_radius = circle_radius*Config.check_circle_ratio_to_guess

            pygame.draw.rect(screen, Color.black,
                ((rect_x, rect_y+circle_rect_height*Config.guess_num),
                 (rect_w, circle_rect_height+1)))

            for index, option in enumerate(Game.option_list):
                pygame.draw.circle(screen, Color.options[option],
                    (rect_x+index*circle_rect_width+circle_rect_width*0.5,
                    rect_y+circle_rect_height*Config.guess_num+circle_rect_height*0.5),
                    circle_radius)

            for row_index, row_list in enumerate(Game.guess_list):
                for guess_index, guess in enumerate(Game.guess_list[row_index]):
                    temp_color = Color.black
                    if guess != "blank":
                        temp_color = Color.options[guess]
                    pygame.draw.circle(screen, temp_color,
                    (rect_x+guess_index*circle_rect_width+circle_rect_width*0.5,
                    rect_y+row_index*circle_rect_height+
                    circle_rect_height*0.5), circle_radius)
                for check_index, check in enumerate(Game.check_list[row_index]):
                    temp_color = Color.black
                    if check != "blank":
                        temp_color = Color.guesses[check]
                    pygame.draw.circle(screen, temp_color,
                    (rect_x+Config.guess_size*circle_rect_width+circle_rect_width*0.5
                    +check_index*check_rect_w+check_rect_w*0.5,
                    rect_y+row_index*circle_rect_height+circle_rect_height*0.5),
                    check_radius)

            pygame.display.flip()

if __name__ == "__main__":
    Game.start()
