def key_pressed(char_width=1):
    import os
    #is it a unix-like system?
    if os.name == 'posix': 
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(char_width)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    #is it a windows system?
    elif os.name == 'nt':
        from msvcrt import getch
        return "".join([getch() for i in range(char_width)])
    #system unknown, user will have to use enter key :(
    else:
        return input()
