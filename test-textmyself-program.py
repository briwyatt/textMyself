import sys
from textMyself import *

msg1 = sys.argv

my_message = msg1[1] if len(msg1) > 1 else "default message"



textmyself(f'{my_message}')
print('program complete successful')

