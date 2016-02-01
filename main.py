
from mingus.midi.midi_file_out import write_Bar , write_Track
from mingus.containers import NoteContainer ,Track,Bar
import mingus

# 2/4 doua note de patrimi

meter = (4,4)
class GenerateBar():

	def generate(self,meter):
		"""meter should be a touple .
		(4,4)and(3,4) are recommended"""

		b = Bar('E', (4, 4))

		b.place_notes("C-1", 4)
		b.place_notes("C-2", 4)
		b.place_notes("C-3", 2)
		

		track_1 = Track()
		track_1.add_bar(b)
		track_1.add_bar(b)
		track_1.add_bar(b)
		return track_1



trackin = GenerateBar()
trackin = trackin.generate(meter)


write_Track("test.mid",trackin,bpm=120)