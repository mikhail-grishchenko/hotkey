import keyboard
import time

print("=============\nSome text here\n=============")
print('insert + 1: Some text here.\n'
      'insert + 2: Some text here.\n'
      'insert + 3: Some text here.\n'
      'insert + 4: Some text here.\n'
      'insert + 5: Some text here.\n'
      'insert + 6: Some text here.\n'
      'insert + 7: Some text here.\n'
      'insert + 8: Some text here.\n'
      'insert + 9: Some text here.\n'
      )

keyboard.press('numlock')
while True:
    if keyboard.is_pressed('insert+1'):
        keyboard.write('Some text here\n')
    elif keyboard.is_pressed('insert+2'):
        keyboard.write('Some text here.\n')
    elif keyboard.is_pressed('insert+3'):
        keyboard.write('Some text here.\n')
    elif keyboard.is_pressed('insert+4'):
        keyboard.write('Some text here.\n')
    elif keyboard.is_pressed('insert+5'):
        keyboard.write('Some text here.\n')
    elif keyboard.is_pressed('insert+6'):
        keyboard.write('Some text here.\n')
    elif keyboard.is_pressed('insert+7'):
        keyboard.write('Some text here.\n')
    elif keyboard.is_pressed('insert+8'):
        keyboard.write('Some text here.\n')
    elif keyboard.is_pressed('insert+9'):
        keyboard.write('Some text here.\n')
    time.sleep(0.1)