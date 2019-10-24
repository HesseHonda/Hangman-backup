import os
import time

frameList = [
'''
          0----0
          |    |
               |
               |
               |
               |
               |
              === ''',

'''
          0----0
          |    |
          O    |
               |
               |
               |
               |
              === ''',

'''
          0----0
          |    |
          O    |
          |    |
               |
               |
               |
              === ''',

'''
          0----0
          |    |
          O    |
         /|    |
               |
               |
               |
              === ''',

'''
          0----0
          |    |
          O    |
         /|\   |
               |
               |
               |
              === ''',

'''
          0----0
          |    |
          O    |
         /|\   |
         /     |
               |
               |
              === ''',

'''
          0----0
          |    |
          O    |
         /|\   |
         / \   |
               |
               |
              === ''',
































]

while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(.3)