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
        diatonic =  self.get_major_scale("C")  # example : ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb']
        
         
        
        arrangement = self.basic_song_structure() # arragement.structure and arragement.parts are used

        generated_parts = []
        for i in range(0,len(arrangement["parts"])):
            proggresion = self.random_progression(diatonic)
            print proggresion
            print "rhythm= " + str(self.gen_rhythm(proggresion))
            generated_bar = self.gen_simple(diatonic,self.meter[1],proggresion)
            generated_parts.append(generated_bar)
        
        song = Track()
        for i in arrangement["structure"]:
            song.add_bar(generated_parts[i])
        self.gen_rhythm(self.meter)
        return song   

       
        
        
    def gen_rhythm(self,proggresion):
        rhythm = []
        rhythm.append(random.choice([2,4,8])) 
        probability = random.randint(0,100)
        for i in range(1,len(proggresion)):
            random_length = random.choice([2,4,8])
            if probability <= 70 :
                rhythm.append(rhythm[i-1])
            else:
                rhythm.append(random_length)
        
        return rhythm


        
    def gen_with_rhythm(self,proggresion,rhythm,diatonic):

        bar = Bar(diatonic[0],)


    def gen_simple(self,diatonic,note_length,proggresion):
        """generation of a simple song ,each note has the same length"""
        
        bar = Bar(diatonic[0],(len(proggresion),note_length))
        
        for i in proggresion:
            bar.place_notes(i,note_length)
        
        return bar 
    
    def basic_song_structure(self):
        """returns a random structure  """
        structure = [] 
        parts = [] # like chorus ,verse ,introduction
        for i in range(0, random.randint(2,5)): #creates nr_of_parts
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
        
        arrangement = {
            "parts" : parts,
            "structure":structure
            }
        return arrangement

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

        
    def get_major_scale(self,note):
        chord_proggresions = ["whole","whole","half","whole","whole","whole","half"]
        
        for i in range(0,len(notes)) :
            if (notes[i] == note) : 
                diatonic = notes[i:] + notes[:i]
                
        for i in range(0,len(notes)) :
            if chord_proggresions[i] == "half" :
                diatonic[i] += "#"
        return diatonic
    





    



trackin = GenerateTrack((2,2))
trackin = trackin.generate()


midi.write_Track("drums.mid",trackin,bpm=120)