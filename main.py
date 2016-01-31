
from mingus.midi.midi_file_out import write_Bar
from mingus.containers import NoteContainer
from mingus.containers import Bar
import mingus



b = Bar()

b.place_notes(["A-4","G-4"], 4)

b.place_notes("C-5", 4)

b.place_notes(["E-5", "G-5", "A-5"], 2)

write_Bar("test.mid",b,bpm=120)