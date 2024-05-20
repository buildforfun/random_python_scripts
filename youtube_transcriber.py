import os
import re
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_transcript(yt_vid_id, out_file):
    """
    Generates a transcript of a youtube video.

    Argument:
        yt_vid_id (str): unique video id
        out_file (str): filepath to save the transcript.

    Returns:
        bool: True if the transcript was saved successfully, False otherwise.
    """

    try:
        # Fetch the transcript and returns it as a list of dictionaries
        # dicts contains text with start and duration.
        transcript = YouTubeTranscriptApi.get_transcript(yt_vid_id)

        # Joins all the text into a single string separated by spaces
        transcript_text = " ".join([entry['text'] for entry in transcript])

        # Save the transcript text to a file
        with open(out_file, 'w', encoding='utf-8') as file:
            file.write(transcript_text)

        print("Transcript saved to: {}".format(out_file))
        return True

    except Exception as e:
        print(f"Error extracting transcript: {e}")
        return False


URL = input("URL: ")

# splits the URL string at the first '='
video_id = URL.split('=')[1]

# file path made using current directory and unique file name
output_file = os.path.join(".", "transcript"+video_id+".txt")

if get_video_transcript(video_id, output_file):
    print("Youtube transcript saved successfully.")
else:
    print("Failed to generate transcript.")
