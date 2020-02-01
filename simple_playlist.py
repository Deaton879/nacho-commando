from collections import deque

class Song():
  def __init__(self):
    self.title = "title"
    self.artist = "artist"
    
  def prompt(self):
    self.title = input('Enter the title: ')
    self.artist = input('Enter the artist: ')
    
    
  def display(self):
    print('{} by {}'.format(self.title, self.artist))
  
playlist = deque()

def main():
  
  quit = False
  
  while (quit == False):
    print('Options:\n', 
    '1. Add a new song to the end of the playlist\n',
    '2. Insert a new song to the beginning of the playlist\n', 
    '3. Play the next song\n',
    '4. Quit')
    answer = int(input('Enter selection: '))
    print('')
    
    if (answer == 1 or answer == 2):
      song = Song()
      song.prompt()
      print('')
      
      if (answer == 1):
        playlist.append(song)
        
      elif (answer == 2):
        playlist.appendleft(song)
        
    elif (answer == 3):
      
      if playlist:
       song = playlist.popleft()
       print('Playing Song:')
       song.display()
       print('')
       
      else:
        print('The playlist is empty.\n')
        
    elif (answer == 4):
      quit = True
      print('Goodbye')
      
    else:
      print('Answer with a number: 1-4\n')

if __name__ == "__main__":
  main()
