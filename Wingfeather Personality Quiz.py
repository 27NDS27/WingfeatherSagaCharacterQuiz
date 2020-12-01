from time import *
Janner = 0
Tink = 0
Leeli = 0
input('Hello! [ENTER]')
input('Welcome to the Wingfeather personality quiz!')
input('Take this quiz to see which Wingfeather character you are most like!')
print('***************************************************************************')
sleep(0.1)
print('BOOKS')
sleep(0.1)
print('What you think of books:')
sleep(0.1)
print('a: Yes! I just finished the last five!')
sleep(0.1)
print('b: I guess books with pictures are cool')
sleep(0.1)
print('c: Do you have any music books?')
sleep(0.1)
print(' ')
books = input('Enter the letter that fits you best: ')
if books == 'a':
    Janner += 1
elif books == 'b':
    Tink += 1
elif books == 'c':
    Leeli += 1
sleep(0.5)
print('***************************************************************************')
sleep(0.1)
print('ART')
sleep(0.1)
print('What you think of art:')
sleep(0.1)
print('a: Art books are cool')
sleep(0.1)
print('b: Art is a part of me!')
sleep(0.1)
art = input('c: Art is nice to look at, but it\'s not my thing: ')
if art == 'a':
    Janner += 1
elif art == 'b':
    Tink += 1
elif art == 'c':
    Leeli += 1
sleep(0.5)
print('***************************************************************************')
sleep(0.1)
print('MUSIC')
sleep(0.1)
print('What you think of music:')
sleep(0.1)
print('a: I like reading songs')
sleep(0.1)
print('b: Music sounds nice')
sleep(0.1)
music = input('c: I love music! Music makes me so happy: ')
if music == 'a':
    Janner += 1
elif music == 'b':
    Tink += 1
elif music == 'c':
    Leeli += 1
sleep(0.5)
print('***************************************************************************')
sleep(0.1)
print('Time for the results!')
sleep(0.5)
print('Loading...')
sleep(1)
print('Fetching results...')
sleep(1)
print('Calculating...')
sleep(1)
if Leeli == Janner and Janner == Tink and Tink == Leeli:
    print('You are the similar to all the Wingfeather Children! You love reading, music and art! You play music, draw, and read almost everyday.')
elif Tink == Janner and not Janner == Leeli and not Tink == Leeli:
    print('You are the similar to both Janner and Tink Wingfeather! You love reading and art and draw and read almost everyday. Music is okay, but it\'s not your thing.')
elif Leeli == Tink and not Tink == Janner and not Janner == Leeli:
    print('You are the similar to both Kalmar "Tink" and Leeli Wingfeather! You love art and music, draw almost everyday, and play at least one instrument. Reading is okay, but you\'re more into music and art.')
elif Janner == Leeli and not Tink == Janner and not Tink == Leeli:
    print('You are similar to both Janner and Leeli Wingfeather! You love art and music, and read almost everyday. Art is okay, but it\'s not your thing.')
elif Janner > Tink and Janner > Leeli:
    print('You are the most like Janner Wingfeather! You love reading, but art and music are okay but not your thing.')
elif Tink > Janner and Tink > Leeli:
    print('You are the most like Kalmar "Tink" Wingfeather! You love art and draw all the time, but reading and music are okay, but you\'re not particularly interested in either.')
elif Leeli > Janner and Leeli > Tink:
    print('You are the most like Leeli Wingfeather! You love music, and play at least one instrument. Reading and art are okay, but you\'re not particularly into in either.')
elif Leeli == Janner:
    print('You are the similar to both Janner and Leeli Wingfeather! You love reading and music and play at least one instrument. Art is okay, but it\'s not your thing.')

input('[ENTER]')
print('Thank you for playing the Wingfeather personality quiz!')
sleep(2)
print('Until next time!')
