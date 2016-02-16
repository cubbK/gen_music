
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

		diatonic =  Diatonic("C")
			

		bar = Bar(diatonic[0],meter)
		for i in diatonic:
			bar.place_notes(i,8)
		
		return bar
		

	




def Diatonic(note):
	chord_proggresions = ["major","minor","minor","major","major","minor","minor"]
	
	for i in range(0,len(notes)) :
		if (notes[i] == note) : 
			diatonic = notes[i:] + notes[:i]
			
	for i in range(0,len(notes)) :
		if chord_proggresions[i] == "minor" :
			diatonic[i] += "b"
	return diatonic
	



trackin = GeneratedTrack()
trackin = trackin.generate((4,4))


midi.write_Bar("test.mid",trackin,bpm=120)