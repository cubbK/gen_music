
import mingus.midi.midi_file_out as midi
from mingus.containers import NoteContainer ,Track,Bar ,Composition,Suite
from mingus.containers.instrument import MidiInstrument

import mingus ,random

# 2/4 doua note de patrimi

notes = ['C','D','E','F','G','A','B']
class GeneratedTrack():
	leads_to = [
		[0,1,2,3,4,5,6] , 
		[0,4,6],
		[0,3,5],
		[0,1,4,6],
		[0,5],
		[0,1,2,3,4],
		[0]
	]

	def __init__(self,meter):
		self.meter = meter

	def generate(self):
		"""meter should be a touple """
		
		nr_of_bars = random.randint(3,10)	

		diatonic =  self.Diatonic("C")  # example : ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb']
		print diatonic

		bar = Bar(diatonic[0],self.meter)

		random_proggresion = [diatonic[0]]
		nr_of_chords = random.randint(5,15)

		for i in range(1,nr_of_chords):
			print "hey"
			#random_proggresion.append(diatonic[random.choice(leads_to)]) 
			
		def get_diatonic_index(note):
			print "hello"	
			
			

		
		
		return bar
		
	def Diatonic(self,note):
		chord_proggresions = ["major","minor","minor","major","major","minor","minor"]
		
		for i in range(0,len(notes)) :
			if (notes[i] == note) : 
				diatonic = notes[i:] + notes[:i]
				
		for i in range(0,len(notes)) :
			if chord_proggresions[i] == "minor" :
				diatonic[i] += "b"
		return diatonic
	





	



trackin = GeneratedTrack((8,4))
trackin = trackin.generate()


midi.write_Bar("test.mid",trackin,bpm=120)