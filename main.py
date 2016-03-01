# Apparently these import statements does not work in python 3
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
        
        proggresion = self.random_progression(diatonic)
        print proggresion
       

        return self.gen_simple(diatonic,4,proggresion)


    def gen_simple(self,diatonic,note_length,proggresion):
        """generation of a simple song ,each note has the same length"""
        bar = Bar(diatonic[0],(len(proggresion),note_length))
            
        for i in proggresion:
            print bar.current_beat
            if bar.current_beat < 1 :
                bar.place_notes(i,note_length)

        return bar 
         

    def random_progression(self,diatonic):
        """return random proggresion of a diatonic"""
        

        random_proggresion = [diatonic[0]]
        nr_of_chords = random.randint(2,10)
        
        for i in range(1,nr_of_chords):
            initial_note = random_proggresion[len(random_proggresion)-1]
            for i in range(0,len(notes)):
                if initial_note == diatonic[i]:
                    next_note_index = random.choice(GeneratedTrack.leads_to[i])
                    random_proggresion.append(diatonic[next_note_index])
        random_proggresion.append(diatonic[0])
        
        return random_proggresion

        
    def Diatonic(self,note):
        chord_proggresions = ["major","minor","minor","major","major","minor","minor"]
        
        for i in range(0,len(notes)) :
            if (notes[i] == note) : 
                diatonic = notes[i:] + notes[:i]
                
        for i in range(0,len(notes)) :
            if chord_proggresions[i] == "minor" :
                diatonic[i] += "b"
        return diatonic
    





    



trackin = GeneratedTrack((4,4))
trackin = trackin.generate()


midi.write_Bar("test.mid",trackin,bpm=120)