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

    def generate_test(self):
        bar1 = Bar()
        bar1.place_notes("A-4", 4)
        bar2 =Bar()
        bar2.place_notes("B-4", 4)
        bar3 = Bar()
        bar3.place_notes("C-4", 4)
        song = Track()
        bars = [bar1,bar2,bar3]
        structure = [0,1,2,0,1,2,2,1,0]
        for i in structure:
            song.add_bar(bars[i])
        print song
        return song



    def generate(self):
        """meter should be a touple """
        
        nr_of_bars = random.randint(3,10)	
        diatonic =  self.getMajorScale("C")  # example : ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb']
        
         
        
        arrangement = self.basic_song_structure() # arragement.structure and arragement.parts are used

        generated_parts = []
        for i in range(0,len(arrangement["parts"])):
            proggresion = self.random_progression(diatonic)
            generated_bar = self.gen_simple(diatonic,self.meter[1],proggresion)
            generated_parts.append(generated_bar)
        
        song = Track()
        for i in arrangement["structure"]:
            song.add_bar(generated_parts[i])
        return song   

       
        
        


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
        print "structure = " + str(structure)
        print "Parts" + str(parts)
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

        
    def getMajorScale(self,note):
        chord_proggresions = ["whole","whole","half","whole","whole","whole","half"]
        
        for i in range(0,len(notes)) :
            if (notes[i] == note) : 
                diatonic = notes[i:] + notes[:i]
                
        for i in range(0,len(notes)) :
            if chord_proggresions[i] == "half" :
                diatonic[i] += "#"
        return diatonic
    





    



trackin = GenerateTrack((4,4))
trackin = trackin.generate()


midi.write_Track("drums.mid",trackin,bpm=120)