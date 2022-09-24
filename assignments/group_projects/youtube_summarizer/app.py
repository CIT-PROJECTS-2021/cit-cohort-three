# Youtube Transcript Summarizer

import os
import sys
import json
import argparse
import requests
import subprocess
import youtube_dl
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play
from pydub.utils import make_chunks
from pydub.silence import detect_nonsilent
from pydub.silence import detect_silence

# Global Variables
# Youtube API Key

# Youtube API Key
API_KEY = ''

# Youtube Video ID
VIDEO_ID = ''

class YoutubeSummarizer:

    def __init__(self, video_id, api_key):
        self.video_id = video_id
        self.api_key = api_key

    def get_video_transcript(self):
        """Get the transcript for the video"""
        url = f'https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId={self.video_id}&key={self.api_key}'
        response = requests.get(url)
        data = json.loads(response.text)
        try:
            caption_id = data['items'][0]['id']
        except IndexError:
            print('No captions found for this video')
            sys.exit(1)
        url = f'https://www.googleapis.com/youtube/v3/captions/{caption_id}?key={self.api_key}'
        response = requests.get(url)
        data = json.loads(response.text)
        transcript = data['snippet']['text']
        return transcript

    def get_video_audio(self):
        """Get the audio for the video"""
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.youtube.com/watch?v={self.video_id}'])

    def get_speech_chunks(self):
        """Split the audio into chunks of speech"""
        sound = AudioSegment.from_wav('audio.wav')
        chunks = make_chunks(sound, 3000)
        return chunks

    def get_speech_transcript(self, chunks):
        """Get the transcript for each chunk of speech"""
        transcripts = []
        for i, chunk in enumerate(chunks):
            chunk.export(f'chunk{i}.wav', format='wav')
            command = f'python3 speech_to_text.py -f chunk{i}.wav'
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            transcripts.append(output.decode('utf-8'))
        return transcripts

    def get_speech_summary(self, transcripts):
        """Summarize the transcript for each chunk of speech"""
        summary = []
        for transcript in transcripts:
            command = f'python3 summarize.py -t "{transcript}"'
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            summary.append(output.decode('utf-8'))
        return summary

    def get_video_summary(self):
        """Summarize the video"""
        video_summary = []
        transcript = self.get_video_transcript()
        command = f'python3 summarize.py -t "{transcript}"'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        video_summary.append(output.decode('utf-8'))
        return video_summary

    def get_speech_summary_audio(self, summary):
        """Get the audio for the speech summary"""
        audio = AudioSegment.from_wav('audio.wav')
        nonsilent_ranges = detect_nonsilent(audio, min_silence_len=100, silence_thresh=-40)
        summary_audio = []
        for i, nonsilent_range in enumerate(nonsilent_ranges):
            start = nonsilent_range[0]
            end = nonsilent_range[1]
            summary_audio.append(audio[start:end])
        return summary_audio




def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Summarize a YouTube video')
    parser.add_argument('video_id', help='YouTube video ID')
    parser.add_argument('api_key', help='YouTube API key')
    args = parser.parse_args()
    video_id = args.video_id
    api_key = args.api_key
    summarizer = YoutubeSummarizer(video_id, api_key)
    transcript = summarizer.get_video_transcript()
    print(transcript)
    summarizer.get_video_audio()
    chunks = summarizer.get_speech_chunks()
    transcripts = summarizer.get_speech_transcript(chunks)
    summary = summarizer.get_speech_summary(transcripts)
    video_summary = summarizer.get_video_summary()
    summary_audio = summarizer.get_speech_summary_audio(summary)
    for audio in summary_audio:
        play(audio)
    print(' '.join(video_summary))

if __name__ == '__main__':
    main()