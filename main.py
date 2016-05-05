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
        

    def generate(self):
        
        
        nr_of_bars = random.randint(3,10)	
        diatonic =  self.get_major_scale("A")  # example : ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb']
        
         
        
        arrangement = self.basic_song_structure() # arragement.structure and arragement.parts are used

        generated_parts = []
        for i in range(0,len(arrangement["parts"])):
            proggresion = self.random_progression(diatonic,"-2")
            rhythm = self.gen_rhythm(proggresion)

            generated_bar_with_rhythm = self.gen_with_rhythm(proggresion,rhythm,diatonic)

            print "proggresiion ="+ str(proggresion)
            print "rhythm= " + str(rhythm)
            

            
            generated_bar = self.gen_simple(diatonic,4,proggresion)
            generated_parts.append(generated_bar_with_rhythm)
        
        song = Track()
        for i in arrangement["structure"]:
            song.add_bar(generated_parts[i])

        self.gen_rhythm(proggresion)
        return song   

       
        
        
    

    def gen_rhythm(self,proggresion):
        rhythm = [] #the final rhythm 
        beat = []

        #randmizarea beatului
        for i in range(random.randint(2,8)):
            beat.append( random.choice([4,8,16]))
        
        while True:
            if len(rhythm) < len(proggresion):
                rhythm.extend(beat)
            else : 
                break
        
        
        how_much_to_cut = len(rhythm)- len(proggresion)
        final_length = len(rhythm) - how_much_to_cut

        rhythm = rhythm[:final_length]
            
        


        return rhythm 


        
    def gen_with_rhythm(self,proggresion,rhythm,diatonic):
        self.get_meter_from_rhythm(rhythm)
        bar = Bar(key = diatonic[0],meter = self.get_meter_from_rhythm(rhythm))

        for i in range(len(proggresion)):
            bar.place_notes(proggresion[i],rhythm[i])

        return bar


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

    def random_progression(self,diatonic,pitch):
        """return random proggresion of a diatonic"""
        

        random_proggresion = [diatonic[0] +pitch ]
        nr_of_chords = random.randint(2,10)
        
        for i in range(1,nr_of_chords):
            initial_note = random_proggresion[len(random_proggresion)-1]
            for i in range(0,len(notes)):
                if initial_note == diatonic[i] + pitch:
                    next_note_index = random.choice(GenerateTrack.leads_to[i])
                    random_proggresion.append(diatonic[next_note_index] + pitch)
        
        
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
    
    def get_meter_from_rhythm(self,rhythm):

        rhythm_16 = []
        for i in rhythm:
            if i == 16 :
                rhythm_16.append(i)
            elif i == 8 :
                rhythm_16.extend([16,16]) 
            elif i == 4 :
                rhythm_16.extend([16,16,16,16]) 
            elif i == 2 :
                rhythm_16.extend([16,16,16,16,16,16,16,16]) 
        #2/4   2 note de patrimi
        meter = (len(rhythm_16),16)
        
        return meter



    



trackin = GenerateTrack()
trackin = trackin.generate()


midi.write_Track("drums1.mid",trackin,bpm=100)