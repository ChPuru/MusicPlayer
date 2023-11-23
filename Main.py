import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame
import os
import json


class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Initialize pygame
        pygame.mixer.init()

        # Create and set up GUI components
        self.create_ui()

        # Initialize playlist
        self.playlist = []

    def create_ui(self):
        # Create a listbox to display the songs
        self.song_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.song_listbox.pack(pady=10)

        # Create Play, Pause, Stop, Volume, Speed, and Skip buttons
        play_button = ttk.Button(
            self.root, text="Play", command=self.play_song)
        pause_button = ttk.Button(
            self.root, text="Pause", command=self.pause_song)
        stop_button = ttk.Button(
            self.root, text="Stop", command=self.stop_song)

        play_button.pack(pady=5)
        pause_button.pack(pady=5)
        stop_button.pack(pady=5)

        # Create Volume and Speed controls with labels
        volume_label = ttk.Label(self.root, text="Volume")
        self.volume_scale = ttk.Scale(
            self.root, from_=0, to=1, orient=tk.HORIZONTAL)

        speed_label = ttk.Label(self.root, text="Speed")
        self.speed_scale = ttk.Scale(
            self.root, from_=0.5, to=2, orient=tk.HORIZONTAL)

        volume_label.pack(pady=5)
        self.volume_scale.pack(pady=5)
        speed_label.pack(pady=5)
        self.speed_scale.pack(pady=5)

        next_button = ttk.Button(
            self.root, text="Next", command=self.next_song)
        prev_button = ttk.Button(
            self.root, text="Previous", command=self.prev_song)
        add_button = ttk.Button(
            self.root, text="Add Song", command=self.add_song_to_playlist)
        save_playlist_button = ttk.Button(
            self.root, text="Save Playlist", command=self.save_playlist)
        load_playlist_button = ttk.Button(
            self.root, text="Load Playlist", command=self.load_playlist)

        next_button.pack(pady=5)
        prev_button.pack(pady=5)
        add_button.pack(pady=5)
        save_playlist_button.pack(pady=5)
        load_playlist_button.pack(pady=5)

        # Discover media files in a directory (modify the path as needed)
        self.media_directory = "E:/pythonprojectschlng/musicplayer"
        self.songs = [f for f in os.listdir(
            self.media_directory) if f.endswith((".mp3", ".wav"))]

        # Add songs to the listbox
        for song in self.songs:
            self.song_listbox.insert(tk.END, song)

    def play_song(self):
        selected_song_index = self.song_listbox.curselection()
        if selected_song_index:
            selected_song = self.songs[selected_song_index[0]]
            song_path = os.path.join(self.media_directory, selected_song)
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
        else:
            tk.messagebox.showwarning(
                "Warning", "You must select a song to play!")

    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

    def set_speed(self, speed):
        pygame.mixer.music.set_speed(float(speed))

    def next_song(self):
        selected_song_index = self.song_listbox.curselection()
        if selected_song_index:
            current_index = selected_song_index[0]
            next_index = (current_index + 1) % len(self.songs)
            self.song_listbox.selection_clear(0, tk.END)
            self.song_listbox.selection_set(next_index)
            self.play_song()

    def prev_song(self):
        selected_song_index = self.song_listbox.curselection()
        if selected_song_index:
            current_index = selected_song_index[0]
            prev_index = (current_index - 1) % len(self.songs)
            self.song_listbox.selection_clear(0, tk.END)
            self.song_listbox.selection_set(prev_index)
            self.play_song()

    def add_song_to_playlist(self):
        selected_song_index = self.song_listbox.curselection()
        if selected_song_index:
            selected_song = self.songs[selected_song_index[0]]
            self.playlist.append(selected_song)
            # Update the playlist display or save it for future use

    def save_playlist(self):
        # Save the current playlist to a file (e.g., as a JSON file)
        playlist_file = filedialog.asksaveasfilename(defaultextension=".json")
        if playlist_file:
            with open(playlist_file, "w") as file:
                json.dump(self.playlist, file)

    def load_playlist(self):
        # Load a saved playlist from a file (e.g., as a JSON file)
        playlist_file = filedialog.askopenfilename(
            filetypes=[("JSON Files", "*.json")])
        if playlist_file:
            with open(playlist_file, "r") as file:
                self.playlist = json.load(file)


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
