import os
def clear_screen():
    '''Clears Screen'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
