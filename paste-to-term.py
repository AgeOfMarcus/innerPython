'''
From: https://repl.it/@mat1/code-plagiarism

Slightly modified by me
'''
import sys
import termios
import time

def init(newmode=None):
    stream = sys.stdin # for detecting keys immediately instead of waiting for enter key pressed
    if newmode:
        termios.tcsetattr(sys.stdin, 1, newmode)
        return
    mode = termios.tcgetattr(stream)
    oldmode = termios.tcgetattr(stream)
    mode[3] = mode[3] &~ (termios.ECHO | termios.ICANON | termios.IEXTEN | termios.ISIG)
    mode[6][termios.VMIN] = 0 # async mode
    termios.tcsetattr(sys.stdin, 1, mode)
    return oldmode

def get_paste(prompt, checkchars=True, oldmode=None):
	oldmode = oldmode or init()
	code = ''
	started_typing = False

	read = None

	print(prompt)
	while True:
		read = sys.stdin.read(1)
		code += read
		if not started_typing:
			if read:
				started_typing = True
			else:
				time.sleep(0.1)
		else:
			if not read:
				break
	
	if len(code) == 1 and checkchars:
		print('\033[H\033[2JYou only typed one character. Please try again (use copy paste, don\'t type it out)\n')
		return get_paste(prompt, checkchars=checkchars, oldmode=oldmode)

	init(oldmode)
	return code