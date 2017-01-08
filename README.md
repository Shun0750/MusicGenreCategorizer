# MusicGenreCategorizer
MusicGenreCategorizer is a tool for categorizing music genre automatically.   
So far it can categorize only 2 genre - HeavyMetal or Dance

# Setup
It use the python library for audio analysis.  

### pyAudioAnalysis 
https://github.com/tyiannak/pyAudioAnalysis

Please install this library first.  

# Dataset
Put heavy metal songs to the directory `./audio/metal` and put dance music to `./audio/dance`.  
Each song shuld be within 10seconds and saved as .wav file.

# Learning
```
$ python classification.py
```
This command will make audio feature set data called 'svmSMtemp'. It is used in categorizing phase. 

# Categorizing
```
$ python record.py
```
This command will start analyzing music from microphone. If you want to analyze built-in audio, you had better use Soundflower (https://github.com/mattingalls/Soundflower). 
# License
MIT
