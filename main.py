
import mingus.midi.midi_file_out as midi
from mingus.containers import NoteContainer ,Track,Bar ,Composition,Suite
from mingus.containers.instrument import MidiInstrument

import mingus ,random

# 2/4 doua note de patrimi

notes = ['C','D','E','F','G','A','B']
class GeneratedTrack():
	
	def generate(self,meter):
		"""meter should be a touple """
		
		nr_of_bars = random.randint(3,10)

		print Diatonic("A")
			

		bar = Bar("C",meter)
		bar.place_notes("A-2",4)
		
		return bar
		

	




def Diatonic(note):
	chord_proggresions = ["major","minor","minor","major","major","minor","minor"]
	diatonic = []
	for i in range(0,len(notes)) :
		if (notes[i] == note) : 
			notes_arranged = notes[i:] + notes[:i]
			
			print mingus.core.notes.to_minor(notes[0])

	



trackin = GeneratedTrack()
trackin = trackin.generate((4,4))


midi.write_Bar("test.mid",trackin,bpm=120)