from midi2audio import FluidSynth
from pydub import AudioSegment

# provide path to the downloaded soundfont file.
soundfont_path = "C:\Digital Music Creation\FluidR3_GM_GS"

#Initialize Fluidsynth with the soundfont
fs = FluidSynth(soundfont_path)

#convert the MIDI file to WAV
fs.midi_to_audio("simple_melody.mid", "simple_melody.wav")

#optionally convert WAV to mp3
audio = AudioSegment.from_wav("simple_melody.wav")
audio.export("simple_melody.mp3", format = "mp3")

print("MIDI conversion to audio complete!")