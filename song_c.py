import pygame

def play_song(index, songs):
    """Load and play the song at the specified index."""
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play(-1)  # Loop indefinitely


class play_music:
  def __init__(self):
    self.songs = [r"music\music1.mp3", r"music\music2.mp3", r"music\music3.mp3"]
    self.current_song_index = 0
    self.volume = 0.5

  # Set up the mixer and load the first song
  def start(self):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(self.volume)

  def next_song(self):
      """Switch to the next song in the list."""
      self.current_song_index = (self.current_song_index + 1) % len(self.songs)
      play_song(self.current_song_index, self.songs)

  def previous_song(self):
      # Switch to the previous song in the list
      self.current_song_index = (self.current_song_index - 1) % len(self.songs)
      play_song(self.current_song_index, self.songs)

  def adjust_volume(self,change):
      # Adjust the volume up or down.
      self.volume = max(0, min(1, self.volume + change)) # Clamp between 0 and 1
      pygame.mixer.music.set_volume(self.volume)


