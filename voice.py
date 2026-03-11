# voice.py
import asyncio
from edge_tts import Communicate
import playsound
import os

# Path for temporary speech files
TEMP_AUDIO = "speech.mp3"

async def _speak_async(text, voice="en-US-AriaNeural"):
    """Generate speech using edge-tts and save as mp3."""
    communicate = Communicate(text, voice=voice)
    await communicate.save(TEMP_AUDIO)
    playsound.playsound(TEMP_AUDIO)
    os.remove(TEMP_AUDIO)

def speak(text):
    """Wrapper to run async speak synchronously"""
    asyncio.run(_speak_async(text))