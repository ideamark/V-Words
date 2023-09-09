import os
import json
import whisper

from settings import audio_folder, text_folder
from common import clear_folder, replace_ext


# refer to: https://github.com/openai/whisper
model = whisper.load_model('base')

clear_folder(text_folder)
for audio_name in os.listdir(audio_folder):
    audio_path = os.path.join(audio_folder, audio_name)
    result = model.transcribe(audio=audio_path, verbose=True, word_timestamps=True)
    json_path = os.path.join(text_folder, replace_ext(audio_name, 'json'))
    with open(json_path, 'w') as fp:
        json.dump(result, fp)
