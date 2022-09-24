# Speech to text using Google Cloud Speech API
# https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries
# https://cloud.google.com/speech-to-text/docs/async-recognize
# https://cloud.google.com/speech-to-text/docs/async-recognize#speech-async-recognize-gcs-python
# https://cloud.google.com/speech-to-text/docs/async-recognize#speech-async-recognize-gcs-python

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import argparse

# Instantiates a client
client = speech.SpeechClient()

parser = argparse.ArgumentParser(description='Convert audio to text')
parser.add_argument('-f', '--file', help='Audio file')
args = parser.parse_args()

# The name
file_name = args.file

# Loads the audio into memory
with open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))

