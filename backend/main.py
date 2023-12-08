import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage


def create_midi(notes, metadata, filename="output.mid"):
    # Create a MIDI file with one track
    mid = MidiFile()

    for i, note_set in enumerate(notes):
        track = MidiTrack()
        mid.tracks.append(track)

        # Set the time signature and tempo in the metadata
        track.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24,
                                 notated_32nd_notes_per_beat=8))
        track.append(MetaMessage('set_tempo', tempo=metadata["tempo"]))

        # Set the instrument with a Program Change message
        track.append(Message('program_change', program=metadata["instrument"]))

        # Add the note-on and note-off messages to the track
        time = 0
        velocity = 64  # You can adjust the velocity as needed
        for j in range(len(note_set)):
            track.append(Message('note_on', note=note_set[j][0], velocity=velocity, time=time))
            track.append(Message('note_off', note=note_set[j][0], velocity=velocity,
                                 time=time + int(note_set[j][1] * mid.ticks_per_beat)))
            time += int(note_set[j][1] * mid.ticks_per_beat)

    # Save the MIDI file
    mid.save(filename)
    print(f"MIDI file '{filename}' created successfully!")


# Example usage:
notes = [[[45, 1.5], [50, 1.5]], [], [[33, 0.5]], [],
         [[51, 2]]]  # timing []
meta = {
    "instrument": 34,
    "tempo": int(500000)  # One sixty-fourth note?
}

create_midi(notes, meta)
