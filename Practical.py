class Song:
    def __init__(self, title, artist, album, duration, genre):
        self.title = title
        self.artist =artist
        self.album = album
        self.duration = duration
        self.genre = genre

    def play(self):
        return f"{self.title}\n{self.artist}--{self.album}...\n{self.duration}"



class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.songs = []
        self.current_song = 0
        self.repeat = repeat
        self.shuffle = shuffle

    def add_song(self, song):
        if song.title in [s.title for s in self.songs]:
            print(f"'{song.title}' is already in the playlist.")
        else:
            self.songs.append(song)

    def remove_song(self, song_title):
        for s in self.songs:
            if s.title == song_title:
                self.songs.remove(s)
                print(f"'{song_title}' removed from playlist.")
                return
        print(f"'{song_title}' not found in the playlist.")

    def skip(self):
        if self.current_song < len(self.songs) - 1:
            self.current_song += 1
        elif self.repeat:
            self.current_song = 0  # wrap to beginning if repeat is enabled

    def previous(self):
        if self.current_song > 0:
            self.current_song -= 1
        elif self.repeat:
            self.current_song = len(self.songs) - 1  # wrap to last song

    def set_shuffle(self, value: bool):
        self.shuffle = value

    def set_repeat(self, value: bool):
        self.repeat = value

    def play(self):
        if not self.songs:
            print("Playlist is empty.")
            return

        if self.shuffle:
            self.current_song = random.randint(0, len(self.songs) - 1)

        song = self.songs[self.current_song]
        print(f"{self.name}:\n{song.play()}")
