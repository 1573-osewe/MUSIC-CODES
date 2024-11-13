from midiutil import MIDIFile


# create a midi file with one track
midi = MIDIFile(1)
track = 0
midi.addTrackName(track, 0, "Melody Track")
midi.addTempo(track, 0, 120) # set the tempo to 120


#define some notes for a melody
notes = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI numbers for C major scale
duration = 1 # each note last one beat

# Add notes to the track
time = 0
for note in notes:
    midi.addNote(track, 0, note, time, duration, 100) # 100 is the volume
    time += duration # move to the next beat

# write to a midi file 
with open("second_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("Melody created!")