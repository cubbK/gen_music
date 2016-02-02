
from mingus.midi.midi_file_out import write_Bar , write_Track ,write_Composition
from mingus.containers import NoteContainer ,Track,Bar ,Composition,Suite
from mingus.containers.instrument import MidiInstrument
import mingus ,random

# 2/4 doua note de patrimi

meter = (4,4)
class GeneratedTrack():
	notes = ['C','D','E','F','G','A','B']
	def generate(self,meter):
		"""meter should be a touple .
		(4,4)and(3,4) are recommended"""

		

	def choose_structure(self):
		structures = [
			['intro','verse','chorus','chorus','verse',],
			['intro','chorus','chorus','outro']
		]
		self.structure = structures[0]	

	def verse(self,meter):
		instrument = MidiInstrument()
		instrument.instrument_nr = 1
		verse = Track()
		bar_1 = Bar(meter)
		self.random_note()

	def random_note(self):
		print random.choice(self.notes)	
	




trackin = GeneratedTrack()
trackin = trackin.verse((4,4))


#write_Suite("test.mid",trackin,bpm=120)