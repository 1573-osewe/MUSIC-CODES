from midiutil import MIDIFile

# Initialize MIDI file with two tracks (piano and guitar)
midi = MIDIFile(2)
midi.addTempo(0, 0, 120)  # Track 0 (piano) at 120 BPM
midi.addTempo(1, 0, 120)  # Track 1 (guitar) at 120 BPM

# Define notes for chords and melody
piano_chords = [
    (60, 64, 67),  # C Major chord
    (62, 65, 69),  # D Minor chord
    (64, 67, 71),  # E Minor chord
    (65, 69, 72),  # F Major chord
]

guitar_chords = [
    (55, 59, 62),  # G Major chord
    (57, 60, 64),  # A Minor chord
    (59, 62, 65),  # B Minor chord
    (60, 64, 67),  # C Major chord
]

# Function to add chords to the MIDI track
def add_chords(track, chords, start_time, duration):
    time = start_time
    for chord in chords:
        for note in chord:
            midi.addNote(track, 0, note, time, duration, 100)
        time += duration

# Add piano chords (track 0)
add_chords(0, piano_chords, start_time=0, duration=1)

# Add guitar chords (track 1)
add_chords(1, guitar_chords, start_time=4, duration=1)

# Add a simple melody line for the piano (track 0)
melody_notes = [60, 62, 64, 65, 67, 69, 71, 72]
for i, note in enumerate(melody_notes):
    midi.addNote(0, 0, note, start_time=8 + i * 0.5, duration=0.5, volume=90)

# Save to a MIDI file
with open("longer_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)
print("MIDI file created as 'longer_melody.mid'")
