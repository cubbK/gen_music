# Apparently these import statements does not work in python 3
import mingus.midi.midi_file_out as midi
from mingus.containers import NoteContainer ,Track,Bar ,Composition,Suite
from mingus.containers.instrument import MidiInstrument

import mingus ,random

# 2/4 doua note de patrimi

notes = ['C','D','E','F','G','A','B']
class GenerateTrack():
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
        self.basic_song_structure()

        return self.gen_simple(diatonic,4,proggresion)


    def gen_simple(self,diatonic,note_length,proggresion):
        """generation of a simple song ,each note has the same length"""
        track = Track()
        bar = Bar(diatonic[0],(len(proggresion),note_length))
        
        for i in proggresion:
            bar.place_notes(i,note_length)
        print bar
        return bar 
    
    def basic_song_structure(self):
        """returns a random structure  """
        structure = [] 
        parts = [] # like chorus ,verse ,introduction
        for i in range(0, random.randint(2,4)+1): #creates nr_of_parts
            parts.append(i)
        structure.append(random.choice(parts))

        for i in range(1,random.randint(10,30)):
            probability = random.randint(1,100)
            if probability >75 :
                while True:
                    ran = random.choice(parts)
                    if ran != structure[i-1]:
                        structure.append(ran)
                        break
            else :
                structure.append(structure[i-1]) 
        print "structure: " + str(structure)
        return structure

    def random_progression(self,diatonic):
        """return random proggresion of a diatonic"""
        

        random_proggresion = [diatonic[0]]
        nr_of_chords = random.randint(2,10)
        
        for i in range(1,nr_of_chords):
            initial_note = random_proggresion[len(random_proggresion)-1]
            for i in range(0,len(notes)):
                if initial_note == diatonic[i]:
                    next_note_index = random.choice(GenerateTrack.leads_to[i])
                    random_proggresion.append(diatonic[next_note_index])
        
        
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
    





    



trackin = GenerateTrack((4,4))
trackin = trackin.generate()


midi.write_Bar("test.mid",trackin,bpm=120)