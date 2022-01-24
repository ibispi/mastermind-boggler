# mastermind-boggler
Customizeable Mastermind Game

Requires:
python, version 3.7
pygame, version 2.0

Usage: change directory to the directory of this game and then type: python game.py
(instead of python, type in the alias for python on your computer, this will depend on your OS)

Controls:
1-8 keys to place pegs
space or enter to guess a row
escape to quit

Options:
-h or --help for help
-ww \[VALUE\] or --window-width \[VALUE\] for setting window width
-wh \[VALUE\] or --window-height \[VALUE\] for setting window height
-gs \[VALUE\] or --guess-size \[VALUE\] for setting the size of the combination to be guessed (default: 4, max: 8)
-an \[VALUE\] or --attempt-number \[VALUE\] for setting the number of attempts (default: 10, max: 20)
-on \[VALUE\] or --option-number \[VALUE\] for setting the number of different pegs (default: 4, max 8)

Examples:
python game.py
python game.py -ww 1920 -wh 1080 -gs 8 -an 20 -on 8
