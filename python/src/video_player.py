"""A video player class."""
import video
from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.isPlaying = False
        self.old_vid = None
        self.Video_Playing_id = "None"
        self._video_library = VideoLibrary()

    def video_name(self, video_id):
        video = self._video_library.get_video(video_id)
        return video.title

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        temp = []
        print("Here's a list of all available videos:")
        for vid in videos:

            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            temp += [f"{vid.title} ({vid.video_id}) {tags}"]

        sorted_list = sorted(temp)
        print(*sorted_list, sep="\n")

    """print("show_all_videos needs implementation")"""

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)

        if not video:
            print("Cannot play video: Video does not exist")
        else:
            if not self.isPlaying:
                print(f"Playing video: {video.title}")
                self.old_vid = video.title
                self.isPlaying = True
            elif self.isPlaying:
                print(f"Stopping video: {self.old_vid}")
                print(f"Playing video: {video.title}")
                self.old_vid = video.title

        # print("Playing video:", )
        """print("play_video needs implementation")"""

    def stop_video(self):
        """Stops the current video."""
        if not self.isPlaying:
            print(f"Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self.old_vid}")
            self.isPlaying = False
            self.old_vid = None

        #print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        #x = random.randint(0,4)
        #print(x)
        video = []
        x = self._video_library.get_all_videos()
        for a in x:
            video += [f"{a.title}"]
        #print(video)
        if self.isPlaying == False:
            print("Playing video:", random.choice(video))
        else:
            print(f"Stopping video: {self.old_vid}")
            print("Playing video:", random.choice(video))



        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
