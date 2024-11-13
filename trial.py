from midiutil import MIDIFile

midi = MIDIFile(1)
track = 0
midi.addTrackName(track, 0, "Tune Track")
midi.addTempo(track, 0, 120)

chords = [     
    [60, 64, 67],  # C major (C-E-G)
    [55, 59, 62],  # G major (G-B-D)
    [53, 57, 60]   # F major (F-A-C)
]

# Add the chords first (each chord lasts 2 beats)
time = 0
for chord in chords:
    for note in chord:
        midi.addNote(track, 0, note, time, 2, 100)  # chord played for 2 beats
    time += 2  # move to the next chord

notes = [60, 62, 64, 65, 67, 69, 71, 72]
time = 6  # Start the melody after the chords

# Add the melody (each note lasts 1 beat)
for note in notes:
    midi.addNote(track, 0, note, time, 1, 100)
    time += 1

# Define rhythm (duration in beats)
rhythm = [1, 0.5, 1, 0.5, 1, 1, 0.5, 1]
time = 14  # Continue from where the melody left off

# Add melody with varied rhythm (use different notes if necessary)
for i, note in enumerate(notes):
    midi.addNote(track, 0, note, time, rhythm[i], 100)
    time += rhythm[i]  # move based on note duration

# Use varying velocities for the melody
velocities = [100, 80, 100, 120, 90, 100, 110, 95]
time = 14  # Continue from where the rhythm sequence left off

# Add the notes with varying velocities
for i, note in enumerate(notes):
    midi.addNote(track, 0, note, time, 1, velocities[i])
    time += 1

# Write to the file
with open("third_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("Melody Created!")
