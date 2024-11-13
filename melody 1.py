from midiutil import MIDIFile

# creating a midi file with one track
midi = MIDIFile(1)

# SET track, tempo and time signature
track = 0
time = 0 # start at the begining
midi.addTrackName(track, time, "simple Track")
midi.addTempo(track, time, 120) # set the tempo ( eg. 120 bpm)

midi.addNote(track, 0, 60, time, 1, 100) #C4
midi.addNote(track, 0, 62, time + 1, 1, 100) #D4
midi.addNote(track, 0, 64, time + 2, 1, 100) #E4
midi.addNote(track, 0, 65, time + 3, 1, 100) #F4
midi.addNote(track, 0, 67, time + 4, 1, 100) #G4

# save the MIDI file
with open("simple_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)
    
                  