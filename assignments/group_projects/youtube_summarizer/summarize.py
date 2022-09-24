# Script for summarizing a YouTube video

# Path: youtube_summarizer\summarize.py
# Compare this snippet from youtube_summarizer\app.py:

import argparse


parser = argparse.ArgumentParser(description='Summarize a YouTube video')
parser.add_argument('-t', '--transcript', help='Transcript of the video')
args = parser.parse_args()

transcript = args.transcript

print("Summarizing the transcript...")
# summarize the transcript passed in
with open('transcript.txt', 'w') as file:
    for line in transcript.splitlines():
        file.write(line)


