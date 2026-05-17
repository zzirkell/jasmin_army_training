from pathlib import Path
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

try:
    import pygame
except ImportError:
    pygame = None
"""
Mini Exam 03: Clear Eyes Playlist Mood Analyzer

Theme:
A small playlist/mood analyzer.

Important:
This exercise does not use real song lyrics.
It only uses made-up mood tags and fake line lengths.

Goal:
Use lists, dictionaries, sets, loops, conditions, averages, and functions.

No classes yet.
"""

#IGNORE THAT
def get_melody_path():
    """
    Returns the expected path to the melody file.

    Prefer .ogg because pygame usually handles it better than mp3.
    """

    current_file = Path(__file__).resolve()
    before_classes_folder = current_file.parent.parent
    assets_folder = before_classes_folder / "assets"

    possible_files = [
        "clear_eyes_melody.ogg",
        "clear_eyes_melody.wav",
        "clear_eyes_melody.mp3",
    ]

    for file_name in possible_files:
        melody_path = assets_folder / file_name

        if melody_path.exists():
            return melody_path

    return assets_folder / "clear_eyes_melody.ogg"


def start_melody():
    """
    Starts playing the melody in the background.

    The music will continue until stop_melody() is called.
    No external music player window should open.
    """

    if pygame is None:
        print()
        print("pygame is not installed.")
        print("Install it with:")
        print("pip install pygame")
        print("The program will continue without music.")
        print()
        return False

    melody_path = get_melody_path()

    if not melody_path.exists():
        print()
        print("Melody file was not found.")
        print("Expected one of these files:")
        print("00_before_classes/assets/clear_eyes_melody.ogg")
        print("00_before_classes/assets/clear_eyes_melody.wav")
        print("00_before_classes/assets/clear_eyes_melody.mp3")
        print("The program will continue without music.")
        print()
        return False

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(str(melody_path))
        pygame.mixer.music.play(-1)  # -1 means repeat forever
        return True
    except Exception as error:
        print()
        print("Could not play the melody.")
        print(f"Reason: {error}")
        print("The program will continue without music.")
        print()
        return False


def stop_melody():
    """
    Stops the melody.
    """

    if pygame is not None:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def wait_until_user_stops_music():
    """
    Keeps the program open until the user types the stop command.
    """

    print()
    print("Music is playing.")
    print("Type stop_this_shit and press Enter to stop it.")

    user_input = ""

    while user_input != "stop_this_shit":
        user_input = input("> ")

        if user_input != "stop_this_shit":
            print("To stop the music, type exactly: stop_this_shit")

    stop_melody()
    print("Music stopped.")

#STOP IGNORING HERE AND CHECK THE CODE BELOW
def count_mood_tags(mood_tags):
    mood_counts = {}
    for mood in mood_tags:
        if mood not in mood_counts:
            mood_counts[mood] = 1
        else:
            mood_counts[mood] += 1
    return mood_counts

def calculate_average_line_length(line_lengths):
    return sum(line_lengths) / len(line_lengths)

def find_long_lines(line_lengths, minimum_length):
    long_lines = []
    for line in line_lengths:
        if line >= minimum_length:
            long_lines.append(line)
    return long_lines

def main():
    print("Mini Exam 03: Clear Eyes Playlist Mood Analyzer")
    print("-----------------------------------------------")

    music_started = start_melody()

    mood_tags = [
        "clear",
        "clear",
        "love",
        "confused",
        "lonely",
        "sad",
        "love",
        "breaking",
        "love",
        "lonely",
        "high",
        "cold",
        "chasing",
        "sad",
        "clear",
    ]

    line_lengths = [
        16,
        32,
        34,
        29,
        39,
        23,
        21,
        40,
        26,
        29,
        33,
        27,
        36,
        22,
        28,
    ]

    mood_counts = count_mood_tags(mood_tags)
    average_length = calculate_average_line_length(line_lengths)
    long_lines = find_long_lines(line_lengths, 30)

    unique_moods = set(mood_tags)

    print(f"Mood counts: {mood_counts}")
    print(f"Unique moods: {unique_moods}")
    print(f"Average line length: {round(average_length, 2)}")
    print(f"Long line lengths: {long_lines}")

    print()

    if "clear" in unique_moods:
        print("The text has a clear/seeing theme.")

    if "love" in unique_moods and "breaking" in unique_moods:
        print("The text mixes love and breakup themes.")

    if average_length >= 30:
        print("The selected lines are quite long on average.")
    else:
        print("The selected lines are rather short on average.")

    if len(unique_moods) >= 5:
        print("There are many different moods in this text.")

    if music_started:
        wait_until_user_stops_music()

if __name__ == "__main__":
    main()