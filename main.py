
from mingus.midi.midi_file_out import write_Bar , write_Track ,write_Composition
from mingus.containers import NoteContainer ,Track,Bar ,Composition,Suite
from mingus.containers.instrument import MidiInstrument
import mingus ,random

# 2/4 doua note de patrimi


class GeneratedTrack():
	notes = ['C','D','E','F','G','A','B']

	

	def generate(self,meter):
		"""meter should be a touple """
		random_notes = self.random_2_notes()
		nr_of_bars = random.randint(3,10)

		for i in range(0,nr_of_bars):
			

		bar = Bar("C",meter)
		bar.place_notes("A-2",4)
		
		return bar
		

	

	def random_2_notes(self):
		note_1 = random.choice(self.notes)	
		note_2 = random.choice(self.notes)
		notes = [note_1,note_2]
		return notes


trackin = GeneratedTrack()
trackin = trackin.generate((4,4))


write_Bar("test.mid",trackin,bpm=120)