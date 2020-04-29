#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


#!pip install glob


# In[2]:


from glob2 import Globber


# In[3]:


#!pip install glob2


# In[4]:


#chapter 1 - https://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html
#Installing Music21 Library - https://web.mit.edu/music21/doc/installing/installWindows.html#installwindows
#!pip install music21


# In[5]:


#importing Music21 - https://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html
#https://web.mit.edu/music21/doc/usersGuide/usersGuide_08_installingMusicXML.html#usersguide-08-installingmusicxml
from music21 import *
#configure.run()


# In[6]:


#help("modules")


# In[ ]:





# In[7]:


#Some important links
#1)https://web.mit.edu/music21/doc/moduleReference/moduleEnvironment.html?highlight=environment#module-music21.environment
#2)https://groups.google.com/forum/#!topic/music21list/FmU6HeNm7AM
#3)https://github.com/cuthbertLab/music21/issues/260
#4)https://stackoverflow.com/questions/21071961/display-of-music21-musicxml-png-objects-using-ipython-notebook-enthought-canopy
#5)https://groups.google.com/forum/#!topic/music21list/ZRzGOOiM-6A


# In[8]:


#user settings - https://web.mit.edu/music21/doc/moduleReference/moduleEnvironment.html?highlight=environment#module-music21.environment
#https://web.mit.edu/music21/doc/moduleReference/moduleEnvironment.html?highlight=environment#module-music21.environment
#4)https://stackoverflow.com/questions/21071961/display-of-music21-musicxml-png-objects-using-ipython-notebook-enthought-canopy

us = environment.UserSettings() 
environment.keys()


# In[9]:


#https://groups.google.com/forum/#!topic/music21list/FmU6HeNm7AM
#us.create() # hyphen this after 1 run
#UserSettingsException: An environment configuration file already exists; simply set values to modify.
#https://groups.google.com/forum/#!topic/music21list/FmU6HeNm7AM

us['musicxmlPath'] = 'C:/Program Files/MuseScore 3/bin'
us['musescoreDirectPNGPath'] = 'C:/Program Files/MuseScore 3/bin'
us['graphicsPath'] = 'C:/Program Files/MuseScore 3/bin'
us['pdfPath'] = 'C:/Program Files/MuseScore 3/bin'
us['lilypondPath'] = 'C:/Program Files/LilyPond/usr/bin/lilypond.exe'
#us['lilypondFormat'] = 'C:/Program Files/LilyPond/usr/bin/lilypond.exe'
#us['midiPath'] = '/path/to/midi/program'


# In[10]:


us['musicxmlPath']


# In[11]:


#show - https://github.com/cuthbertLab/music21/issues/348
#show - https://stackoverflow.com/questions/49939275/python-music21-library-create-png-from-stream


# In[12]:


us['lilypondPath']


# In[13]:


us['musescoreDirectPNGPath'] 


# In[ ]:





# In[14]:


#testing is music21 is working or not
s = corpus.parse('bach/bwv65.2.xml')
s


# In[15]:


s.analyze('key')


# In[16]:


#https://lilypond.org/windows.html #download lilypond from website
#and set environment path
#s = stream.Stream()
#s.show('musicxml.png')
s.show('lily.png')


# In[17]:


#This wont work without setting environemtn for external applications like MuseScore in this example
#a lot of links required above - create environment-> so above process -> change the patrh to external application(musescore) path
#https://stackoverflow.com/questions/21071961/display-of-music21-musicxml-png-objects-using-ipython-notebook-enthought-canopy
#https://github.com/cuthbertLab/music21/issues/260
#https://stackoverflow.com/questions/21071961/display-of-music21-musicxml-png-objects-using-ipython-notebook-enthought-canopy
#https://medium.com/@dinukadesilva/how-to-use-musescore-as-a-headless-command-line-tool-c3f2f0a6f224
#https://blog.ouseful.info/2016/09/13/making-music-and-embedding-sounds-in-jupyter-notebooks/
#s.show()
s.show('midi')
#s.show('lily.png')


# In[18]:


#chapter 2 - https://web.mit.edu/music21/doc/usersGuide/usersGuide_02_notes.html#usersguide-02-notes


# In[19]:


note


# In[20]:


dir(note)


# In[21]:


f = note.Note("F5")
f


# In[22]:


f.octave


# In[23]:


f.pitch


# In[24]:


f.pitch.frequency


# In[25]:


f.pitch.pitchClassString
#That’s a bit better! So an f is about 698hz (if A4 = 440hz), and it is pitch class 5 (where C = 0, C# and Db = 1, etc.).
#A couple of things that you’ll notice:
#Your frequency probably has a bunch more numbers instead of ending with “…”. Mine gives me “698.456462866008”. In the docs, we’ll sometimes write “…” instead of putting in all those numbers (or long strings); it’s partly a way of saving space, and also because the length of a long number and even the last few digits will differ from computer to computer depending on whether it’s 32-bit or 64-bit, Mac or PC, number of sunspots last Autumn, etc. Since I don’t know what computer you’re using, don’t worry if you get slightly different results.
#There are single quotes around some of the output (like the 'F' in f.name) and none around others (like the 5 in f.octave). The quotes mean that that attribute is returning a String (a bunch of letters or numbers or simple symbols). The lack of quotes means that it’s returning a number (either an integer or if there’s a decimal point, a sneakingly decimal-like thingy called a float (or “floating-point number”) which looks and acts just like a decimal, except when it doesn’t, which is never when you’d expect.


# In[26]:


f.pitch.pitchClassString == 5 #its a string, not a number


# In[27]:


f.pitch.pitchClassString == "5" #its a string


# In[28]:


f.pitch.pitchClassString =='5' #its a sring


# In[29]:


f.pitch.pitchClass #number


# In[30]:


#Let’s go ahead and make that B-flat note. In music21, sharps are “#” as you might expect, 
#but flats are “-“. That’s because it’s otherwise hard to tell the difference between the 
#Note “b” (in this instance, you can write it in upper or lower case) and the symbol “flat”. 
#So let’s make that B-flat note:

bflat = note.Note("B-2")


# In[31]:


bflat.show('midi')


# In[32]:


bflat.pitch.accidental


# In[33]:


acc = bflat.pitch.accidental


# In[34]:


acc.alter


# In[35]:


acc.displayLocation


# In[36]:


bflat.show('lily.png')


# In[37]:


file1 = "songs_demo/song3.mid"
midi = converter.parse(file1)
notes_to_parse = midi.flat.notes
for element in notes_to_parse[:10]:
    print(element, element.offset)


# In[38]:


file2 = "songs_demo/song2.mid"
midi = converter.parse(file2)
notes_to_parse = midi.flat.notes
for element in notes_to_parse[:10]:
    print(element, element.offset)


# In[39]:


file3 = "songs_demo/song1.mid"
midi = converter.parse(file3)
notes_to_parse = midi.flat.notes
for element in notes_to_parse[:30]:
    print(element, element.offset)


# In[40]:


#Links - 
#http://manpages.ubuntu.com/manpages/bionic/man5/midicsv.5.html
#http://manpages.ubuntu.com/manpages/bionic/man1/midicsv.1.html
#http://manpages.ubuntu.com/manpages/bionic/man1/csvmidi.1.html
#https://www.fourmilab.ch/webtools/midicsv/


# In[41]:


get_ipython().system('pip install py_midicsv')


# In[42]:


import py_midicsv


# In[43]:


csv_string1 = py_midicsv.midi_to_csv("songs_demo/song1.mid")


# In[44]:


csv_string2 = py_midicsv.midi_to_csv("songs_demo/song2.mid")


# In[45]:


csv_string3 = py_midicsv.midi_to_csv("songs_demo/song3.mid")


# In[46]:


print(csv_string1)


# In[47]:


#csv_file1.csv = csv_string1


# In[48]:


trying_csvmidi = py_midicsv.csv_to_midi(csv_string1)


# In[49]:


trying_csvmidi


# In[50]:


#csv_string1 to csv file
#https://www.pdq.com/powershell/export-csv/
#https://stackoverflow.com/questions/22604564/create-pandas-dataframe-from-a-string
#Export-Csv [csv_file1.csv] csv_string1
#data = csv_string1
#df = pd.DataFrame([x.split(',') for x in data.split('\n')])
#print(df)


# In[ ]:





# In[51]:


import pandas as pd


# In[52]:


#https://www.geeksforgeeks.org/create-a-pandas-dataframe-from-lists/
pandas_file1 = pd.DataFrame(csv_string1)
pandas_file4 = pd.DataFrame(csv_string2)
pandas_file7 = pd.DataFrame(csv_string3)


# In[53]:


pandas_file1[:300:]


# In[ ]:





# In[54]:


pd.set_option('display.max_rows', 30)


# In[55]:


pandas_file1[:]


# In[56]:


pandas_file2 = pandas_file1.copy()
pandas_file5 = pandas_file4.copy()
pandas_file8 = pandas_file7.copy()


# In[57]:


#http://manpages.ubuntu.com/manpages/bionic/man5/midicsv.5.html
pandas_file2[:20:]


# In[58]:


split_data = pandas_file2[0].str.split(", ")
data = split_data.to_list()
names = ["Track", "Time", "Type", "Channel", "Note", "Velocity", "Hello", "Nonsence"]
pandas_file3 = pd.DataFrame(data, columns = names)


# In[59]:


split_data = pandas_file5[0].str.split(", ")
data = split_data.to_list()
names = ["Track", "Time", "Type", "Channel", "Note", "Velocity", "Hello", "Nonsence"]
pandas_file6 = pd.DataFrame(data, columns = names)


# In[60]:


split_data = pandas_file8[0].str.split(", ")
data = split_data.to_list()
names = ["Track", "Time", "Type", "Channel", "Note", "Velocity", "Hello"]
pandas_file9 = pd.DataFrame(data, columns = names)


# In[61]:


pandas_file3


# In[62]:


pandas_file6


# In[63]:


pandas_file9


# In[64]:


#Links - https://kite.com/python/answers/how-to-split-a-pandas-dataframe-column-in-python
#http://manpages.ubuntu.com/manpages/bionic/man5/midicsv.5.html
#https://www.geeksforgeeks.org/python-pandas-split-strings-into-two-list-columns-using-str-split/


# # Data Cleaning

# In[65]:


#https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan
#https://stackoverflow.com/questions/13682044/remove-unwanted-parts-from-strings-in-a-column
#pandas_file3['Note'] = pandas_file3['Note'].map(lambda x: x.strip('\n'))
pandas_file3.dropna(subset = ['Note', 'Velocity'])


# In[66]:


pandas_file6.dropna(subset = ['Note', 'Velocity'])


# In[67]:


pandas_file9.dropna(subset = ['Note', 'Velocity'])


# In[68]:


#https://stackoverflow.com/questions/13682044/remove-unwanted-parts-from-strings-in-a-column
#pandas_file3['Note'] = pandas_file3['Note'].map(lambda x: x.strip('\n'))
pandas_file3['Note'] = pandas_file3['Note'].str.replace('\n', '')
pandas_file3['Velocity'] = pandas_file3['Velocity'].str.replace('\n', '')
pandas_file6['Note'] = pandas_file6['Note'].str.replace('\n', '')
pandas_file6['Velocity'] = pandas_file6['Velocity'].str.replace('\n', '')
pandas_file9['Note'] = pandas_file9['Note'].str.replace('\n', '')
pandas_file9['Velocity'] = pandas_file9['Velocity'].str.replace('\n', '')
pandas_file3


# In[69]:


#http://stackoverflow.com/questions/11637384/pandas-join-merge-concat-two-dataframes
pandas_merged = pd.concat([pandas_file3, pandas_file6])
pandas_merged


# In[70]:


pandas_merged = pd.concat([pandas_merged, pandas_file9])
pandas_merged[:]


# In[71]:


pandas_merged = pandas_merged[(pandas_merged.Type != 'Tempo') & (pandas_merged.Type != 'Text_t') & (pandas_merged.Type != 'Time_signature') & (pandas_merged.Type != 'SMPTE_offset') & (pandas_merged.Type != 'Program_c') & (pandas_merged.Type != 'Header') & (pandas_merged.Type != 'Start_track\n') & (pandas_merged.Type != 'Copyright_t') & (pandas_merged.Type != 'Key_signature')]


# In[72]:


pandas_merged = pandas_merged[(pandas_merged.Type == 'Note_on_c') | (pandas_merged.Type == 'Control_c')]


# In[73]:


#https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/
pandas_merged


# In[74]:


#https://thispointer.com/pandas-sort-rows-or-columns-in-dataframe-based-on-values-using-dataframe-sort_values/
pandas_merged = pandas_merged.sort_values(by = 'Time')


# In[75]:


pandas_merged


# In[76]:


#!pip install keras


# In[77]:


#!pip install scikit-learn


# In[ ]:





# In[ ]:





# # Note and Chords Seperated

# In[78]:


notes_merged = pandas_merged[(pandas_merged.Type == 'Note_on_c')]
notes_merged


# In[79]:


chords_merged = pandas_merged[(pandas_merged.Type == 'Control_c')]
chords_merged


# In[ ]:





# # Training Neural Network

# In[80]:


#https://scikit-learn.org/stable/modules/neural_networks_supervised.html
from sklearn.neural_network import MLPClassifier
X = notes_merged[['Time']]
Y = notes_merged[['Note']]
clf1 = MLPClassifier(activation = 'relu', alpha = 1e-05, hidden_layer_sizes =(5, 2), random_state = 1)
clf1.fit(X, Y)


# # Creating a panda DataFrame to predict the notes and chords 

# In[81]:


#https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it
#columns = ['Track', 'Time', 'Type', 'Channel', 'Note', 'Velocity', 'Hello', 'Nonsence']
#newDF = pd.DataFrame(columns = columns)
#newDF


# # Doing with the excel sheet

# In[82]:


#https://exceljet.net/formula/random-number-between-two-numbers - fOR TIME
#Taken 2500 indeces
#randomly genearted timne between 1-100000


# In[83]:


newDF = pd.read_csv('notes_chords.csv')
newDF


# In[84]:


A = newDF[['Time']]
B = newDF[['Note']]
B = clf1.predict(A)


# In[85]:


newDF[['Note']] = B
newDF[:40]


# In[86]:


from sklearn.neural_network import MLPClassifier
R = notes_merged[['Time']]
S = notes_merged[['Velocity']]
clf2 = MLPClassifier(activation = 'relu', alpha = 1e-05, hidden_layer_sizes =(5, 2), random_state = 1)
clf2.fit(R, S)


# In[87]:


C = newDF[['Time']]
D = newDF[['Velocity']]
D = clf2.predict(C)


# In[88]:


newDF[['Velocity']] = D
newDF[:40]


# In[89]:


newCF = pd.read_csv('chords_notes.csv')
newCF[:40]


# In[90]:


E = chords_merged[['Time']]
F = chords_merged[['Note']]
clf3 = MLPClassifier(activation = 'relu', alpha = 1e-05, hidden_layer_sizes =(5, 2), random_state = 1)
clf3.fit(E, F)


# In[91]:


G = newCF[['Time']]
H = newCF[['Note']]
H = clf3.predict(G)
H


# In[92]:


newCF[['Note']] = H
newCF[:40]


# In[93]:


I = chords_merged[['Time']]
J = chords_merged[['Velocity']]
clf4 = MLPClassifier(activation = 'relu', alpha = 1e-05, hidden_layer_sizes =(5, 2), random_state = 1)
clf4.fit(I, J)


# In[94]:


K = newCF[['Time']]
L = newCF[['Velocity']]
L = clf4.predict(K)
L


# In[95]:


newCF[['Velocity']] = L
newCF[:40]


# # newCF(Chords) + newDF(Notes) 
# # For both chords_notes.csv AND notes_chords done predition for both
# # Notes and Velocity

# In[96]:


t = pd.concat([newCF, newDF])
t


# In[97]:


#n = t.to_string(col_space = None)


# In[98]:


import csv


# In[99]:


t = t.drop(['Hello', 'Nonsence'], axis = 1)


# In[100]:


p = t
p


# In[101]:


#https://stackoverflow.com/questions/4622234/how-to-convert-a-list-to-a-csv-in-python/4622245
#Check Ypou can convert almost any list to a csv using pandas

#csv_string1.to_csv('csvtolookfor.csv', index = False, header = False) this is wrong syntax, and logically also

bh = pd.DataFrame(csv_string1)


# In[102]:


bh


# In[103]:


bh.to_csv('csvfindfault.csv')


# In[104]:


#find_fault = py_midicsv.csv_to_midi('csvfindfault.csv')


# In[ ]:





# In[ ]:





# In[105]:


t.to_csv('complete_csvfile.csv', index = False, header = False)


# In[106]:


#https://pandas.pydata.org/pandas-docs/version/0.24.2/reference/api/pandas.DataFrame.to_csv.html
with open('complete_csvfile.csv') as f:
    s = f.read()  # add trailing new line character

d = repr(s)
print(d)
# 'a,b,c\nd,e,f\ng,h,i\n'

#with open('complete_csvfile.csv', newline='') as f:
 #   reader = csv.reader(f)
  #  data = list(reader)
   # data = [tuple(row) for row in reader]
    


# In[107]:


s


# In[108]:


#final_list = [‘0,65275,Control_c,0,7,64\n’, ‘0,71167,Control_c,0,7,64\n’, ‘0,65035,Control_c,0,7,64\n’, ‘0,49076,Control_c,0,7,64\n’, ‘0,36847,Control_c,0,7,64\n’, ‘0,6656,Control_c,0,7,127\n’, ‘0,23114,Control_c,0,7,64\n’, ‘0,10758,Control_c,0,7,64\n’, ‘0,13012,Control_c,0,7,64\n’, ‘0,62466,Control_c,0,7,64\n’, ‘0,33532,Control_c,0,7,64\n’, ‘0,90702,Control_c,0,7,64\n’, ‘0,32904,Control_c,0,7,64\n’, ‘0,74753,Control_c,0,7,64\n’, ‘0,13960,Control_c,0,7,64\n’, ‘0,80650,Control_c,0,7,64\n’, ‘0,24388,Control_c,0,7,64\n’, ‘0,26248,Control_c,0,7,64\n’, ‘0,46392,Control_c,0,7,64\n’, ‘0,79131,Control_c,0,7,64\n’, ‘0,52135,Control_c,0,7,64\n’, ‘0,44931,Control_c,0,7,64\n’, ‘0,22076,Control_c,0,7,64\n’, ‘0,4715,Control_c,0,7,127\n’, ‘0,11478,Control_c,0,7,64\n’, ‘0,54660,Control_c,0,7,64\n’, ‘0,16572,Control_c,0,7,64\n’, ‘0,51648,Control_c,0,7,64\n’, ‘0,18177,Control_c,0,7,64\n’, ‘0,16855,Control_c,0,7,64\n’, ‘0,51526,Control_c,0,7,64\n’, ‘0,61242,Control_c,0,7,64\n’, ‘0,38627,Control_c,0,7,64\n’, ‘0,4150,Control_c,0,7,127\n’, ‘0,83669,Control_c,0,7,64\n’, ‘0,89738,Control_c,0,7,64\n’, ‘0,81825,Control_c,0,7,64\n’, ‘0,36777,Control_c,0,7,64\n’, ‘0,60791,Control_c,0,7,64\n’, ‘0,27561,Control_c,0,7,64\n’, ‘0,30004,Control_c,0,7,64\n’, ‘0,30376,Control_c,0,7,64\n’, ‘0,789,Control_c,0,7,127\n’, ‘0,71140,Control_c,0,7,64\n’, ‘0,52871,Control_c,0,7,64\n’, ‘0,14776,Control_c,0,7,64\n’, ‘0,89185,Control_c,0,7,64\n’, ‘0,98071,Control_c,0,7,64\n’, ‘0,24758,Control_c,0,7,64\n’, ‘0,3301,Control_c,0,7,127\n’, ‘0,83457,Control_c,0,7,64\n’, ‘0,18614,Control_c,0,7,64\n’, ‘0,75328,Control_c,0,7,64\n’, ‘0,72139,Control_c,0,7,64\n’, ‘0,60289,Control_c,0,7,64\n’, ‘0,46733,Control_c,0,7,64\n’, ‘0,22622,Control_c,0,7,64\n’, ‘0,71095,Control_c,0,7,64\n’, ‘0,53866,Control_c,0,7,64\n’, ‘0,25726,Control_c,0,7,64\n’, ‘0,52059,Control_c,0,7,64\n’, ‘0,72919,Control_c,0,7,64\n’, ‘0,99773,Control_c,0,7,64\n’, ‘0,16536,Control_c,0,7,64\n’, ‘0,43216,Control_c,0,7,64\n’, ‘0,4397,Control_c,0,7,127\n’, ‘0,92826,Control_c,0,7,64\n’, ‘0,64561,Control_c,0,7,64\n’, ‘0,81548,Control_c,0,7,64\n’, ‘0,98114,Control_c,0,7,64\n’, ‘0,1990,Control_c,0,7,127\n’, ‘0,23600,Control_c,0,7,64\n’, ‘0,19483,Control_c,0,7,64\n’, ‘0,57948,Control_c,0,7,64\n’, ‘0,40407,Control_c,0,7,64\n’, ‘0,45158,Control_c,0,7,64\n’, ‘0,61316,Control_c,0,7,64\n’, ‘0,53692,Control_c,0,7,64\n’, ‘0,21623,Control_c,0,7,64\n’, ‘0,11609,Control_c,0,7,64\n’, ‘0,32292,Control_c,0,7,64\n’, ‘0,28664,Control_c,0,7,64\n’, ‘0,2579,Control_c,0,7,127\n’, ‘0,12512,Control_c,0,7,64\n’, ‘0,62341,Control_c,0,7,64\n’, ‘0,61399,Control_c,0,7,64\n’, ‘0,90662,Control_c,0,7,64\n’, ‘0,39585,Control_c,0,7,64\n’, ‘0,36279,Control_c,0,7,64\n’, ‘0,72600,Control_c,0,7,64\n’, ‘0,57521,Control_c,0,7,64\n’, ‘0,79283,Control_c,0,7,64\n’, ‘0,79744,Control_c,0,7,64\n’, ‘0,53118,Control_c,0,7,64\n’, ‘0,55312,Control_c,0,7,64\n’, ‘0,16485,Control_c,0,7,64\n’, ‘0,36288,Control_c,0,7,64\n’, ‘0,93662,Control_c,0,7,64\n’, ‘0,42946,Control_c,0,7,64\n’, ‘0,73600,Control_c,0,7,64\n’, ‘0,49391,Control_c,0,7,64\n’, ‘0,37986,Control_c,0,7,64\n’, ‘0,78635,Control_c,0,7,64\n’, ‘0,15491,Control_c,0,7,64\n’, ‘0,99307,Control_c,0,7,64\n’, ‘0,45720,Control_c,0,7,64\n’, ‘0,1193,Control_c,0,7,127\n’, ‘0,27999,Control_c,0,7,64\n’, ‘0,11882,Control_c,0,7,64\n’, ‘0,20286,Control_c,0,7,64\n’, ‘0,67825,Control_c,0,7,64\n’, ‘0,11553,Control_c,0,7,64\n’, ‘0,81881,Control_c,0,7,64\n’, ‘0,88784,Control_c,0,7,64\n’, ‘0,45741,Control_c,0,7,64\n’, ‘0,1480,Control_c,0,7,127\n’, ‘0,27101,Control_c,0,7,64\n’, ‘0,50517,Control_c,0,7,64\n’, ‘0,65036,Control_c,0,7,64\n’, ‘0,91637,Control_c,0,7,64\n’, ‘0,68464,Control_c,0,7,64\n’, ‘0,14842,Control_c,0,7,64\n’, ‘0,13731,Control_c,0,7,64\n’, ‘0,36946,Control_c,0,7,64\n’, ‘0,78798,Control_c,0,7,64\n’, ‘0,28735,Control_c,0,7,64\n’, ‘0,86683,Control_c,0,7,64\n’, ‘0,43407,Control_c,0,7,64\n’, ‘0,93827,Control_c,0,7,64\n’, ‘0,25863,Control_c,0,7,64\n’, ‘0,11056,Control_c,0,7,64\n’, ‘0,10267,Control_c,0,7,64\n’, ‘0,39446,Control_c,0,7,64\n’, ‘0,42406,Control_c,0,7,64\n’, ‘0,31005,Control_c,0,7,64\n’, ‘0,77270,Control_c,0,7,64\n’, ‘0,46266,Control_c,0,7,64\n’, ‘0,24218,Control_c,0,7,64\n’, ‘0,84024,Control_c,0,7,64\n’, ‘0,57073,Control_c,0,7,64\n’, ‘0,64950,Control_c,0,7,64\n’, ‘0,31127,Control_c,0,7,64\n’, ‘0,31435,Control_c,0,7,64\n’, ‘0,39814,Control_c,0,7,64\n’, ‘0,18717,Control_c,0,7,64\n’, ‘0,14023,Control_c,0,7,64\n’, ‘0,26786,Control_c,0,7,64\n’, ‘0,43802,Control_c,0,7,64\n’, ‘0,84651,Control_c,0,7,64\n’, ‘0,6803,Control_c,0,7,127\n’, ‘0,3150,Control_c,0,7,127\n’, ‘0,67365,Control_c,0,7,64\n’, ‘0,1916,Control_c,0,7,127\n’, ‘0,89330,Control_c,0,7,64\n’, ‘0,94746,Control_c,0,7,64\n’, ‘0,4940,Control_c,0,7,127\n’, ‘0,411,Control_c,0,7,127\n’, ‘0,79365,Control_c,0,7,64\n’, ‘0,93707,Control_c,0,7,64\n’, ‘0,26055,Control_c,0,7,64\n’, ‘0,64221,Control_c,0,7,64\n’, ‘0,97434,Control_c,0,7,64\n’, ‘0,48835,Control_c,0,7,64\n’, ‘0,35056,Control_c,0,7,64\n’, ‘0,6547,Control_c,0,7,127\n’, ‘0,61881,Control_c,0,7,64\n’, ‘0,31606,Control_c,0,7,64\n’, ‘0,66687,Control_c,0,7,64\n’, ‘0,1327,Control_c,0,7,127\n’, ‘0,19412,Control_c,0,7,64\n’, ‘0,56558,Control_c,0,7,64\n’, ‘0,61106,Control_c,0,7,64\n’, ‘0,89165,Control_c,0,7,64\n’, ‘0,43137,Control_c,0,7,64\n’, ‘0,54607,Control_c,0,7,64\n’, ‘0,85433,Control_c,0,7,64\n’, ‘0,14280,Control_c,0,7,64\n’, ‘0,71462,Control_c,0,7,64\n’, ‘0,31354,Control_c,0,7,64\n’, ‘0,76376,Control_c,0,7,64\n’, ‘0,50330,Control_c,0,7,64\n’, ‘0,35037,Control_c,0,7,64\n’, ‘0,34562,Control_c,0,7,64\n’, ‘0,51087,Control_c,0,7,64\n’, ‘0,7748,Control_c,0,7,127\n’, ‘0,6932,Control_c,0,7,127\n’, ‘0,68461,Control_c,0,7,64\n’, ‘0,85950,Control_c,0,7,64\n’, ‘0,54134,Control_c,0,7,64\n’, ‘0,64468,Control_c,0,7,64\n’, ‘0,1471,Control_c,0,7,127\n’, ‘0,56180,Control_c,0,7,64\n’, ‘0,9007,Control_c,0,7,64\n’, ‘0,29538,Control_c,0,7,64\n’, ‘0,25797,Control_c,0,7,64\n’, ‘0,30730,Control_c,0,7,64\n’, ‘0,33391,Control_c,0,7,64\n’, ‘0,10255,Control_c,0,7,64\n’, ‘0,10772,Control_c,0,7,64\n’, ‘0,98313,Control_c,0,7,64\n’, ‘0,33034,Control_c,0,7,64\n’, ‘0,61396,Control_c,0,7,64\n’, ‘0,25803,Control_c,0,7,64\n’, ‘0,18268,Control_c,0,7,64\n’, ‘0,83793,Control_c,0,7,64\n’, ‘0,93952,Control_c,0,7,64\n’, ‘0,3262,Control_c,0,7,127\n’, ‘0,4571,Control_c,0,7,127\n’, ‘0,42391,Control_c,0,7,64\n’, ‘0,28114,Control_c,0,7,64\n’, ‘0,61928,Control_c,0,7,64\n’, ‘0,60052,Control_c,0,7,64\n’, ‘0,957,Control_c,0,7,127\n’, ‘0,43303,Control_c,0,7,64\n’, ‘0,27156,Control_c,0,7,64\n’, ‘0,35963,Control_c,0,7,64\n’, ‘0,50914,Control_c,0,7,64\n’, ‘0,19403,Control_c,0,7,64\n’, ‘0,70781,Control_c,0,7,64\n’, ‘0,41370,Control_c,0,7,64\n’, ‘0,89220,Control_c,0,7,64\n’, ‘0,47629,Control_c,0,7,64\n’, ‘0,15039,Control_c,0,7,64\n’, ‘0,6557,Control_c,0,7,127\n’, ‘0,88025,Control_c,0,7,64\n’, ‘0,55307,Control_c,0,7,64\n’, ‘0,61042,Control_c,0,7,64\n’, ‘0,14577,Control_c,0,7,64\n’, ‘0,50832,Control_c,0,7,64\n’, ‘0,42873,Control_c,0,7,64\n’, ‘0,44929,Control_c,0,7,64\n’, ‘0,77836,Control_c,0,7,64\n’, ‘0,17727,Control_c,0,7,64\n’, ‘0,35465,Control_c,0,7,64\n’, ‘0,5762,Control_c,0,7,127\n’, ‘0,29486,Control_c,0,7,64\n’, ‘0,4200,Control_c,0,7,127\n’, ‘0,48433,Control_c,0,7,64\n’, ‘0,55044,Control_c,0,7,64\n’, ‘0,26018,Control_c,0,7,64\n’, ‘0,14560,Control_c,0,7,64\n’, ‘0,80771,Control_c,0,7,64\n’, ‘0,81768,Control_c,0,7,64\n’, ‘0,21447,Control_c,0,7,64\n’, ‘0,16030,Control_c,0,7,64\n’, ‘0,14251,Control_c,0,7,64\n’, ‘0,10848,Control_c,0,7,64\n’, ‘0,75602,Control_c,0,7,64\n’, ‘0,8219,Control_c,0,7,127\n’, ‘0,39109,Control_c,0,7,64\n’, ‘0,15697,Control_c,0,7,64\n’, ‘0,74187,Control_c,0,7,64\n’, ‘0,33705,Control_c,0,7,64\n’, ‘0,5687,Control_c,0,7,127\n’, ‘0,341,Control_c,0,64,127\n’, ‘0,10427,Control_c,0,7,64\n’, ‘0,15072,Control_c,0,7,64\n’, ‘0,26162,Control_c,0,7,64\n’, ‘0,74071,Control_c,0,7,64\n’, ‘0,68376,Control_c,0,7,64\n’, ‘0,36508,Control_c,0,7,64\n’, ‘0,36090,Control_c,0,7,64\n’, ‘0,17689,Control_c,0,7,64\n’, ‘0,76509,Control_c,0,7,64\n’, ‘0,82532,Control_c,0,7,64\n’, ‘0,32196,Control_c,0,7,64\n’, ‘0,17012,Control_c,0,7,64\n’, ‘0,89327,Control_c,0,7,64\n’, ‘0,55053,Control_c,0,7,64\n’, ‘0,33286,Control_c,0,7,64\n’, ‘0,74331,Control_c,0,7,64\n’, ‘0,36579,Control_c,0,7,64\n’, ‘0,55839,Control_c,0,7,64\n’, ‘0,91478,Control_c,0,7,64\n’, ‘0,66838,Control_c,0,7,64\n’, ‘0,82668,Control_c,0,7,64\n’, ‘0,58995,Control_c,0,7,64\n’, ‘0,62787,Control_c,0,7,64\n’, ‘0,83137,Control_c,0,7,64\n’, ‘0,67951,Control_c,0,7,64\n’, ‘0,12506,Control_c,0,7,64\n’, ‘0,45133,Control_c,0,7,64\n’, ‘0,90678,Control_c,0,7,64\n’, ‘0,13616,Control_c,0,7,64\n’, ‘0,52599,Control_c,0,7,64\n’, ‘0,68867,Control_c,0,7,64\n’, ‘0,46165,Control_c,0,7,64\n’, ‘0,14490,Control_c,0,7,64\n’, ‘0,61387,Control_c,0,7,64\n’, ‘0,96466,Control_c,0,7,64\n’, ‘0,80117,Control_c,0,7,64\n’, ‘0,14755,Control_c,0,7,64\n’, ‘0,16831,Control_c,0,7,64\n’, ‘0,26874,Control_c,0,7,64\n’, ‘0,76744,Control_c,0,7,64\n’, ‘0,86530,Control_c,0,7,64\n’, ‘0,35770,Control_c,0,7,64\n’, ‘0,24102,Control_c,0,7,64\n’, ‘0,93373,Control_c,0,7,64\n’, ‘0,27584,Control_c,0,7,64\n’, ‘0,20960,Control_c,0,7,64\n’, ‘0,85986,Control_c,0,7,64\n’, ‘0,1153,Control_c,0,7,127\n’, ‘0,32707,Control_c,0,7,64\n’, ‘0,8196,Control_c,0,7,127\n’, ‘0,98712,Control_c,0,7,64\n’, ‘0,48536,Control_c,0,7,64\n’, ‘0,35553,Control_c,0,7,64\n’, ‘0,58158,Control_c,0,7,64\n’, ‘0,88708,Control_c,0,7,64\n’, ‘0,10731,Control_c,0,7,64\n’, ‘0,34613,Control_c,0,7,64\n’, ‘0,17051,Control_c,0,7,64\n’, ‘0,9352,Control_c,0,7,64\n’, ‘0,78583,Control_c,0,7,64\n’, ‘0,40128,Control_c,0,7,64\n’, ‘0,29359,Control_c,0,7,64\n’, ‘0,32511,Control_c,0,7,64\n’, ‘0,48225,Control_c,0,7,64\n’, ‘0,84169,Control_c,0,7,64\n’, ‘0,26615,Control_c,0,7,64\n’, ‘0,89240,Control_c,0,7,64\n’, ‘0,75493,Control_c,0,7,64\n’, ‘0,31928,Control_c,0,7,64\n’, ‘0,49757,Control_c,0,7,64\n’, ‘0,37537,Control_c,0,7,64\n’, ‘0,67044,Control_c,0,7,64\n’, ‘0,17964,Control_c,0,7,64\n’, ‘0,20564,Control_c,0,7,64\n’, ‘0,32759,Control_c,0,7,64\n’, ‘0,47260,Control_c,0,7,64\n’, ‘0,5482,Control_c,0,7,127\n’, ‘0,22522,Control_c,0,7,64\n’, ‘0,23073,Control_c,0,7,64\n’, ‘0,89697,Control_c,0,7,64\n’, ‘0,32052,Control_c,0,7,64\n’, ‘0,99728,Control_c,0,7,64\n’, ‘0,82496,Control_c,0,7,64\n’, ‘0,60840,Control_c,0,7,64\n’, ‘0,34977,Control_c,0,7,64\n’, ‘0,5233,Control_c,0,7,127\n’, ‘0,13531,Control_c,0,7,64\n’, ‘0,2949,Control_c,0,7,127\n’, ‘0,11857,Control_c,0,7,64\n’, ‘0,90761,Control_c,0,7,64\n’, ‘0,81652,Control_c,0,7,64\n’, ‘0,24040,Control_c,0,7,64\n’, ‘0,24658,Control_c,0,7,64\n’, ‘0,46153,Control_c,0,7,64\n’, ‘0,48949,Control_c,0,7,64\n’, ‘0,90904,Control_c,0,7,64\n’, ‘0,27394,Control_c,0,7,64\n’, ‘0,15765,Control_c,0,7,64\n’, ‘0,2862,Control_c,0,7,127\n’, ‘0,36345,Control_c,0,7,64\n’, ‘0,26021,Control_c,0,7,64\n’, ‘0,18183,Control_c,0,7,64\n’, ‘0,53535,Control_c,0,7,64\n’, ‘0,51320,Control_c,0,7,64\n’, ‘0,91079,Control_c,0,7,64\n’, ‘0,81226,Control_c,0,7,64\n’, ‘0,38217,Control_c,0,7,64\n’, ‘0,93061,Control_c,0,7,64\n’, ‘0,98579,Control_c,0,7,64\n’, ‘0,45046,Control_c,0,7,64\n’, ‘0,763,Control_c,0,7,127\n’, ‘0,36693,Control_c,0,7,64\n’, ‘0,86747,Control_c,0,7,64\n’, ‘0,78876,Control_c,0,7,64\n’, ‘0,74041,Control_c,0,7,64\n’, ‘0,64632,Control_c,0,7,64\n’, ‘0,25080,Control_c,0,7,64\n’, ‘0,98822,Control_c,0,7,64\n’, ‘0,49636,Control_c,0,7,64\n’, ‘0,52034,Control_c,0,7,64\n’, ‘0,96955,Control_c,0,7,64\n’, ‘0,67589,Control_c,0,7,64\n’, ‘0,99777,Control_c,0,7,64\n’, ‘0,96424,Control_c,0,7,64\n’, ‘0,21884,Control_c,0,7,64\n’, ‘0,67565,Control_c,0,7,64\n’, ‘0,10766,Control_c,0,7,64\n’, ‘0,81581,Control_c,0,7,64\n’, ‘0,22165,Control_c,0,7,64\n’, ‘0,57700,Control_c,0,7,64\n’, ‘0,178,Control_c,0,64,127\n’, ‘0,11625,Control_c,0,7,64\n’, ‘0,99498,Control_c,0,7,64\n’, ‘0,2826,Control_c,0,7,127\n’, ‘0,17725,Control_c,0,7,64\n’, ‘0,48683,Control_c,0,7,64\n’, ‘0,47216,Control_c,0,7,64\n’, ‘0,91605,Control_c,0,7,64\n’, ‘0,74105,Control_c,0,7,64\n’, ‘0,73504,Control_c,0,7,64\n’, ‘0,23125,Control_c,0,7,64\n’, ‘0,99620,Control_c,0,7,64\n’, ‘0,31588,Control_c,0,7,64\n’, ‘0,29662,Control_c,0,7,64\n’, ‘0,16312,Control_c,0,7,64\n’, ‘0,69583,Control_c,0,7,64\n’, ‘0,92734,Control_c,0,7,64\n’, ‘0,55939,Control_c,0,7,64\n’, ‘0,55680,Control_c,0,7,64\n’, ‘0,42139,Control_c,0,7,64\n’, ‘0,32905,Control_c,0,7,64\n’, ‘0,89465,Control_c,0,7,64\n’, ‘0,18855,Control_c,0,7,64\n’, ‘0,44914,Control_c,0,7,64\n’, ‘0,23727,Control_c,0,7,64\n’, ‘0,31000,Control_c,0,7,64\n’, ‘0,49367,Control_c,0,7,64\n’, ‘0,28207,Control_c,0,7,64\n’, ‘0,27382,Control_c,0,7,64\n’, ‘0,32212,Control_c,0,7,64\n’, ‘0,21342,Control_c,0,7,64\n’, ‘0,82159,Control_c,0,7,64\n’, ‘0,23602,Control_c,0,7,64\n’, ‘0,44020,Control_c,0,7,64\n’, ‘0,11266,Control_c,0,7,64\n’, ‘0,24595,Control_c,0,7,64\n’, ‘0,95792,Control_c,0,7,64\n’, ‘0,42260,Control_c,0,7,64\n’, ‘0,67481,Control_c,0,7,64\n’, ‘0,33060,Control_c,0,7,64\n’, ‘0,94875,Control_c,0,7,64\n’, ‘0,35028,Control_c,0,7,64\n’, ‘0,37907,Control_c,0,7,64\n’, ‘0,15344,Control_c,0,7,64\n’, ‘0,67330,Control_c,0,7,64\n’, ‘0,76055,Control_c,0,7,64\n’, ‘0,73662,Control_c,0,7,64\n’, ‘0,58498,Control_c,0,7,64\n’, ‘0,6159,Control_c,0,7,127\n’, ‘0,7239,Control_c,0,7,127\n’, ‘0,18673,Control_c,0,7,64\n’, ‘0,24655,Control_c,0,7,64\n’, ‘0,90327,Control_c,0,7,64\n’, ‘0,23107,Control_c,0,7,64\n’, ‘0,48570,Control_c,0,7,64\n’, ‘0,59877,Control_c,0,7,64\n’, ‘0,6253,Control_c,0,7,127\n’, ‘0,33095,Control_c,0,7,64\n’, ‘0,14197,Control_c,0,7,64\n’, ‘0,18036,Control_c,0,7,64\n’, ‘0,31713,Control_c,0,7,64\n’, ‘0,56686,Control_c,0,7,64\n’, ‘0,34191,Control_c,0,7,64\n’, ‘0,3243,Control_c,0,7,127\n’, ‘0,43610,Control_c,0,7,64\n’, ‘0,76586,Control_c,0,7,64\n’, ‘0,63382,Control_c,0,7,64\n’, ‘0,84402,Control_c,0,7,64\n’, ‘0,51007,Control_c,0,7,64\n’, ‘0,35554,Control_c,0,7,64\n’, ‘0,38188,Control_c,0,7,64\n’, ‘0,40527,Control_c,0,7,64\n’, ‘0,62552,Control_c,0,7,64\n’, ‘0,30970,Control_c,0,7,64\n’, ‘0,76427,Control_c,0,7,64\n’, ‘0,20952,Control_c,0,7,64\n’, ‘0,79419,Control_c,0,7,64\n’, ‘0,44763,Control_c,0,7,64\n’, ‘0,66240,Control_c,0,7,64\n’, ‘0,54832,Control_c,0,7,64\n’, ‘0,30232,Control_c,0,7,64\n’, ‘0,38068,Control_c,0,7,64\n’, ‘0,16536,Control_c,0,7,64\n’, ‘0,76472,Control_c,0,7,64\n’, ‘0,92469,Control_c,0,7,64\n’, ‘0,93988,Control_c,0,7,64\n’, ‘0,89616,Control_c,0,7,64\n’, ‘0,97388,Control_c,0,7,64\n’, ‘0,62204,Control_c,0,7,64\n’, ‘0,65711,Control_c,0,7,64\n’, ‘0,10222,Control_c,0,7,64\n’, ‘0,23393,Control_c,0,7,64\n’, ‘0,55065,Control_c,0,7,64\n’, ‘0,26977,Control_c,0,7,64\n’, ‘0,24937,Control_c,0,7,64\n’, ‘0,52474,Control_c,0,7,64\n’, ‘0,18206,Control_c,0,7,64\n’, ‘0,23930,Control_c,0,7,64\n’, ‘0,62697,Control_c,0,7,64\n’, ‘0,13742,Control_c,0,7,64\n’, ‘0,7544,Control_c,0,7,127\n’, ‘0,51357,Control_c,0,7,64\n’, ‘0,49118,Control_c,0,7,64\n’, ‘0,5353,Control_c,0,7,127\n’, ‘0,3249,Control_c,0,7,127\n’, ‘0,32628,Control_c,0,7,64\n’, ‘0,24086,Control_c,0,7,64\n’, ‘0,99203,Control_c,0,7,64\n’, ‘0,10950,Control_c,0,7,64\n’, ‘0,91202,Control_c,0,7,64\n’, ‘0,10724,Control_c,0,7,64\n’, ‘0,71419,Control_c,0,7,64\n’, ‘0,25231,Control_c,0,7,64\n’, ‘0,97364,Control_c,0,7,64\n’, ‘0,22905,Control_c,0,7,64\n’, ‘0,37983,Control_c,0,7,64\n’, ‘0,16244,Control_c,0,7,64\n’, ‘0,4755,Control_c,0,7,127\n’, ‘0,71266,Control_c,0,7,64\n’, ‘0,4531,Control_c,0,7,127\n’, ‘0,41787,Control_c,0,7,64\n’, ‘0,53440,Control_c,0,7,64\n’, ‘0,46780,Control_c,0,7,64\n’, ‘0,74108,Control_c,0,7,64\n’, ‘0,13684,Control_c,0,7,64\n’, ‘0,45424,Control_c,0,7,64\n’, ‘0,2688,Control_c,0,7,127\n’, ‘0,94490,Control_c,0,7,64\n’, ‘0,78589,Control_c,0,7,64\n’, ‘0,31297,Control_c,0,7,64\n’, ‘0,71169,Control_c,0,7,64\n’, ‘0,43930,Control_c,0,7,64\n’, ‘0,75422,Control_c,0,7,64\n’, ‘0,90623,Control_c,0,7,64\n’, ‘0,10116,Control_c,0,7,64\n’, ‘0,9969,Control_c,0,7,64\n’, ‘0,93654,Control_c,0,7,64\n’, ‘0,5051,Control_c,0,7,127\n’, ‘0,74857,Control_c,0,7,64\n’, ‘0,30857,Control_c,0,7,64\n’, ‘0,99774,Control_c,0,7,64\n’, ‘0,9921,Control_c,0,7,64\n’, ‘0,19479,Control_c,0,7,64\n’, ‘0,81388,Control_c,0,7,64\n’, ‘0,73918,Control_c,0,7,64\n’, ‘0,37091,Control_c,0,7,64\n’, ‘0,6411,Control_c,0,7,127\n’, ‘0,49898,Control_c,0,7,64\n’, ‘0,87924,Control_c,0,7,64\n’, ‘0,55082,Control_c,0,7,64\n’, ‘0,48599,Control_c,0,7,64\n’, ‘0,39083,Control_c,0,7,64\n’, ‘0,31193,Control_c,0,7,64\n’, ‘0,48661,Control_c,0,7,64\n’, ‘0,88910,Control_c,0,7,64\n’, ‘0,58626,Control_c,0,7,64\n’, ‘0,50634,Control_c,0,7,64\n’, ‘0,8419,Control_c,0,7,64\n’, ‘0,7645,Control_c,0,7,127\n’, ‘0,67214,Control_c,0,7,64\n’, ‘0,74073,Control_c,0,7,64\n’, ‘0,51057,Control_c,0,7,64\n’, ‘0,58749,Control_c,0,7,64\n’, ‘0,46639,Control_c,0,7,64\n’, ‘0,72366,Control_c,0,7,64\n’, ‘0,52202,Control_c,0,7,64\n’, ‘0,22614,Control_c,0,7,64\n’, ‘0,47561,Control_c,0,7,64\n’, ‘0,75680,Control_c,0,7,64\n’, ‘0,37638,Control_c,0,7,64\n’, ‘0,85442,Control_c,0,7,64\n’, ‘0,68089,Control_c,0,7,64\n’, ‘0,16570,Control_c,0,7,64\n’, ‘0,10743,Control_c,0,7,64\n’, ‘0,28612,Control_c,0,7,64\n’, ‘0,65080,Control_c,0,7,64\n’, ‘0,80227,Control_c,0,7,64\n’, ‘0,10944,Control_c,0,7,64\n’, ‘0,21439,Control_c,0,7,64\n’, ‘0,6486,Control_c,0,7,127\n’, ‘0,24898,Control_c,0,7,64\n’, ‘0,22087,Control_c,0,7,64\n’, ‘0,801,Control_c,0,7,127\n’, ‘0,24208,Control_c,0,7,64\n’, ‘0,39390,Control_c,0,7,64\n’, ‘0,17721,Control_c,0,7,64\n’, ‘0,42486,Control_c,0,7,64\n’, ‘0,85215,Control_c,0,7,64\n’, ‘0,80476,Control_c,0,7,64\n’, ‘0,64919,Control_c,0,7,64\n’, ‘0,29910,Control_c,0,7,64\n’, ‘0,4122,Control_c,0,7,127\n’, ‘0,11574,Control_c,0,7,64\n’, ‘0,99477,Control_c,0,7,64\n’, ‘0,6994,Control_c,0,7,127\n’, ‘0,46670,Control_c,0,7,64\n’, ‘0,95101,Control_c,0,7,64\n’, ‘0,28155,Control_c,0,7,64\n’, ‘0,8358,Control_c,0,7,127\n’, ‘0,61468,Control_c,0,7,64\n’, ‘0,90505,Control_c,0,7,64\n’, ‘0,64833,Control_c,0,7,64\n’, ‘0,61927,Control_c,0,7,64\n’, ‘0,99136,Control_c,0,7,64\n’, ‘0,59584,Control_c,0,7,64\n’, ‘0,56593,Control_c,0,7,64\n’, ‘0,57040,Control_c,0,7,64\n’, ‘0,85871,Control_c,0,7,64\n’, ‘0,9128,Control_c,0,7,64\n’, ‘0,48519,Control_c,0,7,64\n’, ‘0,44666,Control_c,0,7,64\n’, ‘0,44614,Control_c,0,7,64\n’, ‘0,82487,Control_c,0,7,64\n’, ‘0,91770,Control_c,0,7,64\n’, ‘0,7646,Note_on_c,0,76,0\n’, ‘0,22721,Note_on_c,0,76,0\n’, ‘0,12446,Note_on_c,0,76,0\n’, ‘0,92142,Note_on_c,0,71,0\n’, ‘0,30355,Note_on_c,0,69,0\n’, ‘0,49036,Note_on_c,0,71,0\n’, ‘0,21264,Note_on_c,0,76,0\n’, ‘0,67250,Note_on_c,0,71,0\n’, ‘0,23403,Note_on_c,0,76,0\n’, ‘0,87300,Note_on_c,0,71,0\n’, ‘0,83865,Note_on_c,0,71,0\n’, ‘0,49865,Note_on_c,0,71,0\n’, ‘0,55152,Note_on_c,0,71,0\n’, ‘0,98476,Note_on_c,0,71,0\n’, ‘0,63577,Note_on_c,0,71,0\n’, ‘0,18052,Note_on_c,0,76,0\n’, ‘0,93739,Note_on_c,0,71,0\n’, ‘0,94861,Note_on_c,0,71,0\n’, ‘0,62793,Note_on_c,0,71,0\n’, ‘0,26661,Note_on_c,0,69,0\n’, ‘0,11776,Note_on_c,0,76,0\n’, ‘0,25785,Note_on_c,0,69,0\n’, ‘0,99518,Note_on_c,0,71,0\n’, ‘0,5167,Note_on_c,0,76,0\n’, ‘0,4606,Note_on_c,0,76,0\n’, ‘0,23033,Note_on_c,0,76,0\n’, ‘0,59429,Note_on_c,0,71,0\n’, ‘0,22581,Note_on_c,0,76,0\n’, ‘0,18507,Note_on_c,0,76,0\n’, ‘0,68756,Note_on_c,0,71,0\n’, ‘0,48585,Note_on_c,0,69,0\n’, ‘0,23732,Note_on_c,0,76,0\n’, ‘0,95489,Note_on_c,0,71,0\n’, ‘0,86435,Note_on_c,0,71,0\n’, ‘0,28138,Note_on_c,0,69,0\n’, ‘0,91965,Note_on_c,0,71,0\n’, ‘0,36184,Note_on_c,0,69,0\n’, ‘0,26639,Note_on_c,0,69,0\n’, ‘0,58070,Note_on_c,0,71,0\n’, ‘0,48245,Note_on_c,0,69,0\n’, ‘0,11545,Note_on_c,0,76,0\n’, ‘0,2869,Note_on_c,0,45,0\n’, ‘0,4009,Note_on_c,0,45,0\n’, ‘0,50908,Note_on_c,0,71,0\n’, ‘0,65486,Note_on_c,0,71,0\n’, ‘0,44157,Note_on_c,0,69,0\n’, ‘0,58633,Note_on_c,0,71,0\n’, ‘0,97350,Note_on_c,0,71,0\n’, ‘0,11221,Note_on_c,0,76,0\n’, ‘0,8368,Note_on_c,0,76,0\n’, ‘0,7274,Note_on_c,0,76,0\n’, ‘0,17520,Note_on_c,0,76,0\n’, ‘0,45292,Note_on_c,0,69,0\n’, ‘0,69228,Note_on_c,0,71,0\n’, ‘0,79260,Note_on_c,0,71,0\n’, ‘0,74997,Note_on_c,0,71,0\n’, ‘0,45753,Note_on_c,0,69,0\n’, ‘0,32140,Note_on_c,0,69,0\n’, ‘0,12786,Note_on_c,0,76,0\n’, ‘0,94049,Note_on_c,0,71,0\n’, ‘0,94095,Note_on_c,0,71,0\n’, ‘0,56004,Note_on_c,0,71,0\n’, ‘0,29032,Note_on_c,0,69,0\n’, ‘0,68161,Note_on_c,0,71,0\n’, ‘0,69092,Note_on_c,0,71,0\n’, ‘0,28589,Note_on_c,0,69,0\n’, ‘0,47282,Note_on_c,0,69,0\n’, ‘0,69330,Note_on_c,0,71,0\n’, ‘0,37751,Note_on_c,0,69,0\n’, ‘0,321,Note_on_c,0,76,0\n’, ‘0,53708,Note_on_c,0,71,0\n’, ‘0,13439,Note_on_c,0,76,0\n’, ‘0,35071,Note_on_c,0,69,0\n’, ‘0,68877,Note_on_c,0,71,0\n’, ‘0,15784,Note_on_c,0,76,0\n’, ‘0,76552,Note_on_c,0,71,0\n’, ‘0,70454,Note_on_c,0,71,0\n’, ‘0,71309,Note_on_c,0,71,0\n’, ‘0,97310,Note_on_c,0,71,0\n’, ‘0,44848,Note_on_c,0,69,0\n’, ‘0,61686,Note_on_c,0,71,0\n’, ‘0,94507,Note_on_c,0,71,0\n’, ‘0,17059,Note_on_c,0,76,0\n’, ‘0,6636,Note_on_c,0,76,0\n’, ‘0,54914,Note_on_c,0,71,0\n’, ‘0,78208,Note_on_c,0,71,0\n’, ‘0,47568,Note_on_c,0,69,0\n’, ‘0,13144,Note_on_c,0,76,0\n’, ‘0,59513,Note_on_c,0,71,0\n’, ‘0,5168,Note_on_c,0,76,0\n’, ‘0,66609,Note_on_c,0,71,0\n’, ‘0,4225,Note_on_c,0,45,0\n’, ‘0,8364,Note_on_c,0,76,0\n’, ‘0,96780,Note_on_c,0,71,0\n’, ‘0,66346,Note_on_c,0,71,0\n’, ‘0,23660,Note_on_c,0,76,0\n’, ‘0,76213,Note_on_c,0,71,0\n’, ‘0,44102,Note_on_c,0,69,0\n’, ‘0,34062,Note_on_c,0,69,0\n’, ‘0,52008,Note_on_c,0,71,0\n’, ‘0,56597,Note_on_c,0,71,0\n’, ‘0,53231,Note_on_c,0,71,0\n’, ‘0,67903,Note_on_c,0,71,0\n’, ‘0,56367,Note_on_c,0,71,0\n’, ‘0,40705,Note_on_c,0,69,0\n’, ‘0,15618,Note_on_c,0,76,0\n’, ‘0,37689,Note_on_c,0,69,0\n’, ‘0,44721,Note_on_c,0,69,0\n’, ‘0,67647,Note_on_c,0,71,0\n’, ‘0,30194,Note_on_c,0,69,0\n’, ‘0,85026,Note_on_c,0,71,0\n’, ‘0,36152,Note_on_c,0,69,0\n’, ‘0,10975,Note_on_c,0,76,0\n’, ‘0,29419,Note_on_c,0,69,0\n’, ‘0,25512,Note_on_c,0,69,0\n’, ‘0,16439,Note_on_c,0,76,0\n’, ‘0,40538,Note_on_c,0,69,0\n’, ‘0,57925,Note_on_c,0,71,0\n’, ‘0,72697,Note_on_c,0,71,0\n’, ‘0,8343,Note_on_c,0,76,0\n’, ‘0,22458,Note_on_c,0,76,0\n’, ‘0,52325,Note_on_c,0,71,0\n’, ‘0,21383,Note_on_c,0,76,0\n’, ‘0,65258,Note_on_c,0,71,0\n’, ‘0,5665,Note_on_c,0,76,0\n’, ‘0,16245,Note_on_c,0,76,0\n’, ‘0,29706,Note_on_c,0,69,0\n’, ‘0,59947,Note_on_c,0,71,0\n’, ‘0,81602,Note_on_c,0,71,0\n’, ‘0,66997,Note_on_c,0,71,0\n’, ‘0,98213,Note_on_c,0,71,0\n’, ‘0,73425,Note_on_c,0,71,0\n’, ‘0,46746,Note_on_c,0,69,0\n’, ‘0,4928,Note_on_c,0,76,0\n’, ‘0,28422,Note_on_c,0,69,0\n’, ‘0,62181,Note_on_c,0,71,0\n’, ‘0,45971,Note_on_c,0,69,0\n’, ‘0,75690,Note_on_c,0,71,0\n’, ‘0,10932,Note_on_c,0,76,0\n’, ‘0,44532,Note_on_c,0,69,0\n’, ‘0,96867,Note_on_c,0,71,0\n’, ‘0,67882,Note_on_c,0,71,0\n’, ‘0,32000,Note_on_c,0,69,0\n’, ‘0,66875,Note_on_c,0,71,0\n’, ‘0,84491,Note_on_c,0,71,0\n’, ‘0,87505,Note_on_c,0,71,0\n’, ‘0,331,Note_on_c,0,76,0\n’, ‘0,51261,Note_on_c,0,71,0\n’, ‘0,44980,Note_on_c,0,69,0\n’, ‘0,24502,Note_on_c,0,69,0\n’, ‘0,17904,Note_on_c,0,76,0\n’, ‘0,58642,Note_on_c,0,71,0\n’, ‘0,42763,Note_on_c,0,69,0\n’, ‘0,15813,Note_on_c,0,76,0\n’, ‘0,91843,Note_on_c,0,71,0\n’, ‘0,26075,Note_on_c,0,69,0\n’, ‘0,72462,Note_on_c,0,71,0\n’, ‘0,75947,Note_on_c,0,71,0\n’, ‘0,15377,Note_on_c,0,76,0\n’, ‘0,3890,Note_on_c,0,45,0\n’, ‘0,58371,Note_on_c,0,71,0\n’, ‘0,61257,Note_on_c,0,71,0\n’, ‘0,8522,Note_on_c,0,76,0\n’, ‘0,59298,Note_on_c,0,71,0\n’, ‘0,54399,Note_on_c,0,71,0\n’, ‘0,71512,Note_on_c,0,71,0\n’, ‘0,66045,Note_on_c,0,71,0\n’, ‘0,12583,Note_on_c,0,76,0\n’, ‘0,93083,Note_on_c,0,71,0\n’, ‘0,46168,Note_on_c,0,69,0\n’, ‘0,52522,Note_on_c,0,71,0\n’, ‘0,84203,Note_on_c,0,71,0\n’, ‘0,15526,Note_on_c,0,76,0\n’, ‘0,24205,Note_on_c,0,69,0\n’, ‘0,93001,Note_on_c,0,71,0\n’, ‘0,8554,Note_on_c,0,76,0\n’, ‘0,30193,Note_on_c,0,69,0\n’, ‘0,76531,Note_on_c,0,71,0\n’, ‘0,38930,Note_on_c,0,69,0\n’, ‘0,87659,Note_on_c,0,71,0\n’, ‘0,11550,Note_on_c,0,76,0\n’, ‘0,40330,Note_on_c,0,69,0\n’, ‘0,108,Note_on_c,0,76,0\n’, ‘0,99896,Note_on_c,0,71,0\n’, ‘0,82963,Note_on_c,0,71,0\n’, ‘0,59718,Note_on_c,0,71,0\n’, ‘0,49315,Note_on_c,0,71,0\n’, ‘0,69276,Note_on_c,0,71,0\n’, ‘0,85640,Note_on_c,0,71,0\n’, ‘0,12241,Note_on_c,0,76,0\n’, ‘0,97137,Note_on_c,0,71,0\n’, ‘0,92721,Note_on_c,0,71,0\n’, ‘0,37656,Note_on_c,0,69,0\n’, ‘0,87005,Note_on_c,0,71,0\n’, ‘0,86106,Note_on_c,0,71,0\n’, ‘0,76232,Note_on_c,0,71,0\n’, ‘0,92677,Note_on_c,0,71,0\n’, ‘0,62082,Note_on_c,0,71,0\n’, ‘0,70941,Note_on_c,0,71,0\n’, ‘0,93513,Note_on_c,0,71,0\n’, ‘0,39405,Note_on_c,0,69,0\n’, ‘0,92022,Note_on_c,0,71,0\n’, ‘0,94111,Note_on_c,0,71,0\n’, ‘0,62108,Note_on_c,0,71,0\n’, ‘0,48798,Note_on_c,0,71,0\n’, ‘0,91930,Note_on_c,0,71,0\n’, ‘0,85533,Note_on_c,0,71,0\n’, ‘0,23984,Note_on_c,0,69,0\n’, ‘0,36746,Note_on_c,0,69,0\n’, ‘0,23790,Note_on_c,0,76,0\n’, ‘0,26662,Note_on_c,0,69,0\n’, ‘0,81033,Note_on_c,0,71,0\n’, ‘0,87052,Note_on_c,0,71,0\n’, ‘0,92425,Note_on_c,0,71,0\n’, ‘0,31644,Note_on_c,0,69,0\n’, ‘0,30337,Note_on_c,0,69,0\n’, ‘0,13163,Note_on_c,0,76,0\n’, ‘0,1357,Note_on_c,0,76,0\n’, ‘0,38937,Note_on_c,0,69,0\n’, ‘0,3662,Note_on_c,0,45,0\n’, ‘0,3611,Note_on_c,0,45,0\n’, ‘0,4911,Note_on_c,0,76,0\n’, ‘0,44403,Note_on_c,0,69,0\n’, ‘0,17012,Note_on_c,0,76,0\n’, ‘0,55285,Note_on_c,0,71,0\n’, ‘0,1376,Note_on_c,0,76,0\n’, ‘0,97492,Note_on_c,0,71,0\n’, ‘0,3472,Note_on_c,0,45,0\n’, ‘0,65732,Note_on_c,0,71,0\n’, ‘0,65249,Note_on_c,0,71,0\n’, ‘0,31719,Note_on_c,0,69,0\n’, ‘0,81969,Note_on_c,0,71,0\n’, ‘0,391,Note_on_c,0,76,0\n’, ‘0,94942,Note_on_c,0,71,0\n’, ‘0,12541,Note_on_c,0,76,0\n’, ‘0,11039,Note_on_c,0,76,0\n’, ‘0,50016,Note_on_c,0,71,0\n’, ‘0,216,Note_on_c,0,76,0\n’, ‘0,15790,Note_on_c,0,76,0\n’, ‘0,81628,Note_on_c,0,71,0\n’, ‘0,28188,Note_on_c,0,69,0\n’, ‘0,18528,Note_on_c,0,76,0\n’, ‘0,8117,Note_on_c,0,76,0\n’, ‘0,68591,Note_on_c,0,71,0\n’, ‘0,75976,Note_on_c,0,71,0\n’, ‘0,14674,Note_on_c,0,76,0\n’, ‘0,5021,Note_on_c,0,76,0\n’, ‘0,26557,Note_on_c,0,69,0\n’, ‘0,26134,Note_on_c,0,69,0\n’, ‘0,9488,Note_on_c,0,76,0\n’, ‘0,51527,Note_on_c,0,71,0\n’, ‘0,28278,Note_on_c,0,69,0\n’, ‘0,83587,Note_on_c,0,71,0\n’, ‘0,57642,Note_on_c,0,71,0\n’, ‘0,54271,Note_on_c,0,71,0\n’, ‘0,82645,Note_on_c,0,71,0\n’, ‘0,20510,Note_on_c,0,76,0\n’, ‘0,59956,Note_on_c,0,71,0\n’, ‘0,34442,Note_on_c,0,69,0\n’, ‘0,6229,Note_on_c,0,76,0\n’, ‘0,20705,Note_on_c,0,76,0\n’, ‘0,16945,Note_on_c,0,76,0\n’, ‘0,86197,Note_on_c,0,71,0\n’, ‘0,10481,Note_on_c,0,76,0\n’, ‘0,79151,Note_on_c,0,71,0\n’, ‘0,49211,Note_on_c,0,71,0\n’, ‘0,41118,Note_on_c,0,69,0\n’, ‘0,92419,Note_on_c,0,71,0\n’, ‘0,74124,Note_on_c,0,71,0\n’, ‘0,52021,Note_on_c,0,71,0\n’, ‘0,3738,Note_on_c,0,45,0\n’, ‘0,43737,Note_on_c,0,69,0\n’, ‘0,91436,Note_on_c,0,71,0\n’, ‘0,62151,Note_on_c,0,71,0\n’, ‘0,77897,Note_on_c,0,71,0\n’, ‘0,26717,Note_on_c,0,69,0\n’, ‘0,62559,Note_on_c,0,71,0\n’, ‘0,80793,Note_on_c,0,71,0\n’, ‘0,8187,Note_on_c,0,76,0\n’, ‘0,2867,Note_on_c,0,45,0\n’, ‘0,46312,Note_on_c,0,69,0\n’, ‘0,88461,Note_on_c,0,71,0\n’, ‘0,48456,Note_on_c,0,69,0\n’, ‘0,78538,Note_on_c,0,71,0\n’, ‘0,32208,Note_on_c,0,69,0\n’, ‘0,42161,Note_on_c,0,69,0\n’, ‘0,24074,Note_on_c,0,69,0\n’, ‘0,60882,Note_on_c,0,71,0\n’, ‘0,20869,Note_on_c,0,76,0\n’, ‘0,14994,Note_on_c,0,76,0\n’, ‘0,78346,Note_on_c,0,71,0\n’, ‘0,86710,Note_on_c,0,71,0\n’, ‘0,16165,Note_on_c,0,76,0\n’, ‘0,67973,Note_on_c,0,71,0\n’, ‘0,84053,Note_on_c,0,71,0\n’, ‘0,58526,Note_on_c,0,71,0\n’, ‘0,41610,Note_on_c,0,69,0\n’, ‘0,69652,Note_on_c,0,71,0\n’, ‘0,227,Note_on_c,0,76,0\n’, ‘0,18980,Note_on_c,0,76,0\n’, ‘0,24630,Note_on_c,0,69,0\n’, ‘0,62260,Note_on_c,0,71,0\n’, ‘0,13147,Note_on_c,0,76,0\n’, ‘0,14892,Note_on_c,0,76,0\n’, ‘0,55570,Note_on_c,0,71,0\n’, ‘0,20047,Note_on_c,0,76,0\n’, ‘0,31928,Note_on_c,0,69,0\n’, ‘0,91446,Note_on_c,0,71,0\n’, ‘0,30035,Note_on_c,0,69,0\n’, ‘0,69525,Note_on_c,0,71,0\n’, ‘0,24221,Note_on_c,0,69,0\n’, ‘0,1505,Note_on_c,0,76,0\n’, ‘0,71015,Note_on_c,0,71,0\n’, ‘0,48255,Note_on_c,0,69,0\n’, ‘0,14444,Note_on_c,0,76,0\n’, ‘0,52948,Note_on_c,0,71,0\n’, ‘0,29033,Note_on_c,0,69,0\n’, ‘0,20682,Note_on_c,0,76,0\n’, ‘0,14570,Note_on_c,0,76,0\n’, ‘0,41561,Note_on_c,0,69,0\n’, ‘0,88261,Note_on_c,0,71,0\n’, ‘0,24959,Note_on_c,0,69,0\n’, ‘0,63988,Note_on_c,0,71,0\n’, ‘0,16585,Note_on_c,0,76,0\n’, ‘0,39549,Note_on_c,0,69,0\n’, ‘0,94089,Note_on_c,0,71,0\n’, ‘0,27234,Note_on_c,0,69,0\n’, ‘0,93531,Note_on_c,0,71,0\n’, ‘0,69285,Note_on_c,0,71,0\n’, ‘0,13608,Note_on_c,0,76,0\n’, ‘0,10311,Note_on_c,0,76,0\n’, ‘0,56767,Note_on_c,0,71,0\n’, ‘0,83142,Note_on_c,0,71,0\n’, ‘0,79414,Note_on_c,0,71,0\n’, ‘0,60168,Note_on_c,0,71,0\n’, ‘0,92937,Note_on_c,0,71,0\n’, ‘0,50750,Note_on_c,0,71,0\n’, ‘0,72338,Note_on_c,0,71,0\n’, ‘0,18329,Note_on_c,0,76,0\n’, ‘0,35261,Note_on_c,0,69,0\n’, ‘0,86597,Note_on_c,0,71,0\n’, ‘0,74326,Note_on_c,0,71,0\n’, ‘0,61994,Note_on_c,0,71,0\n’, ‘0,33544,Note_on_c,0,69,0\n’, ‘0,60342,Note_on_c,0,71,0\n’, ‘0,97815,Note_on_c,0,71,0\n’, ‘0,6845,Note_on_c,0,76,0\n’, ‘0,88045,Note_on_c,0,71,0\n’, ‘0,5584,Note_on_c,0,76,0\n’, ‘0,81410,Note_on_c,0,71,0\n’, ‘0,97339,Note_on_c,0,71,0\n’, ‘0,34027,Note_on_c,0,69,0\n’, ‘0,87323,Note_on_c,0,71,0\n’, ‘0,95445,Note_on_c,0,71,0\n’, ‘0,71388,Note_on_c,0,71,0\n’, ‘0,41049,Note_on_c,0,69,0\n’, ‘0,57099,Note_on_c,0,71,0\n’, ‘0,86800,Note_on_c,0,71,0\n’, ‘0,11158,Note_on_c,0,76,0\n’, ‘0,36142,Note_on_c,0,69,0\n’, ‘0,83008,Note_on_c,0,71,0\n’, ‘0,86069,Note_on_c,0,71,0\n’, ‘0,77910,Note_on_c,0,71,0\n’, ‘0,52269,Note_on_c,0,71,0\n’, ‘0,44233,Note_on_c,0,69,0\n’, ‘0,92911,Note_on_c,0,71,0\n’, ‘0,44029,Note_on_c,0,69,0\n’, ‘0,3414,Note_on_c,0,45,0\n’, ‘0,86620,Note_on_c,0,71,0\n’, ‘0,99619,Note_on_c,0,71,0\n’, ‘0,39981,Note_on_c,0,69,0\n’, ‘0,91429,Note_on_c,0,71,0\n’, ‘0,95361,Note_on_c,0,71,0\n’, ‘0,3567,Note_on_c,0,45,0\n’, ‘0,33549,Note_on_c,0,69,0\n’, ‘0,89639,Note_on_c,0,71,0\n’, ‘0,53346,Note_on_c,0,71,0\n’, ‘0,17958,Note_on_c,0,76,0\n’, ‘0,82700,Note_on_c,0,71,0\n’, ‘0,12292,Note_on_c,0,76,0\n’, ‘0,84566,Note_on_c,0,71,0\n’, ‘0,36352,Note_on_c,0,69,0\n’, ‘0,72858,Note_on_c,0,71,0\n’, ‘0,70184,Note_on_c,0,71,0\n’, ‘0,20760,Note_on_c,0,76,0\n’, ‘0,67554,Note_on_c,0,71,0\n’, ‘0,29256,Note_on_c,0,69,0\n’, ‘0,60802,Note_on_c,0,71,0\n’, ‘0,15038,Note_on_c,0,76,0\n’, ‘0,4359,Note_on_c,0,45,0\n’, ‘0,56858,Note_on_c,0,71,0\n’, ‘0,83350,Note_on_c,0,71,0\n’, ‘0,68944,Note_on_c,0,71,0\n’, ‘0,43440,Note_on_c,0,69,0\n’, ‘0,43839,Note_on_c,0,69,0\n’, ‘0,92068,Note_on_c,0,71,0\n’, ‘0,84347,Note_on_c,0,71,0\n’, ‘0,3674,Note_on_c,0,45,0\n’, ‘0,51642,Note_on_c,0,71,0\n’, ‘0,51565,Note_on_c,0,71,0\n’, ‘0,73049,Note_on_c,0,71,0\n’, ‘0,94287,Note_on_c,0,71,0\n’, ‘0,81105,Note_on_c,0,71,0\n’, ‘0,97462,Note_on_c,0,71,0\n’, ‘0,29575,Note_on_c,0,69,0\n’, ‘0,13809,Note_on_c,0,76,0\n’, ‘0,97364,Note_on_c,0,71,0\n’, ‘0,16459,Note_on_c,0,76,0\n’, ‘0,51468,Note_on_c,0,71,0\n’, ‘0,17743,Note_on_c,0,76,0\n’, ‘0,40331,Note_on_c,0,69,0\n’, ‘0,7792,Note_on_c,0,76,0\n’, ‘0,49539,Note_on_c,0,71,0\n’, ‘0,63533,Note_on_c,0,71,0\n’, ‘0,682,Note_on_c,0,76,0\n’, ‘0,5510,Note_on_c,0,76,0\n’, ‘0,47725,Note_on_c,0,69,0\n’, ‘0,39924,Note_on_c,0,69,0\n’, ‘0,60594,Note_on_c,0,71,0\n’, ‘0,85777,Note_on_c,0,71,0\n’, ‘0,9608,Note_on_c,0,76,0\n’, ‘0,54271,Note_on_c,0,71,0\n’, ‘0,73695,Note_on_c,0,71,0\n’, ‘0,81108,Note_on_c,0,71,0\n’, ‘0,76506,Note_on_c,0,71,0\n’, ‘0,31927,Note_on_c,0,69,0\n’, ‘0,29605,Note_on_c,0,69,0\n’, ‘0,98495,Note_on_c,0,71,0\n’, ‘0,17817,Note_on_c,0,76,0\n’, ‘0,61868,Note_on_c,0,71,0\n’, ‘0,42271,Note_on_c,0,69,0\n’, ‘0,69249,Note_on_c,0,71,0\n’, ‘0,62151,Note_on_c,0,71,0\n’, ‘0,87381,Note_on_c,0,71,0\n’, ‘0,2215,Note_on_c,0,45,0\n’, ‘0,38963,Note_on_c,0,69,0\n’, ‘0,52815,Note_on_c,0,71,0\n’, ‘0,97044,Note_on_c,0,71,0\n’, ‘0,57460,Note_on_c,0,71,0\n’, ‘0,31655,Note_on_c,0,69,0\n’, ‘0,40054,Note_on_c,0,69,0\n’, ‘0,25338,Note_on_c,0,69,0\n’, ‘0,1039,Note_on_c,0,76,0\n’, ‘0,20839,Note_on_c,0,76,0\n’, ‘0,70236,Note_on_c,0,71,0\n’, ‘0,72723,Note_on_c,0,71,0\n’, ‘0,24476,Note_on_c,0,69,0\n’, ‘0,95910,Note_on_c,0,71,0\n’, ‘0,68476,Note_on_c,0,71,0\n’, ‘0,46204,Note_on_c,0,69,0\n’, ‘0,61888,Note_on_c,0,71,0\n’, ‘0,49507,Note_on_c,0,71,0\n’, ‘0,4619,Note_on_c,0,76,0\n’, ‘0,99038,Note_on_c,0,71,0\n’, ‘0,5905,Note_on_c,0,76,0\n’, ‘0,33010,Note_on_c,0,69,0\n’, ‘0,21934,Note_on_c,0,76,0\n’, ‘0,36195,Note_on_c,0,69,0\n’, ‘0,40779,Note_on_c,0,69,0\n’, ‘0,90951,Note_on_c,0,71,0\n’, ‘0,22349,Note_on_c,0,76,0\n’, ‘0,44802,Note_on_c,0,69,0\n’, ‘0,97783,Note_on_c,0,71,0\n’, ‘0,67300,Note_on_c,0,71,0\n’, ‘0,94927,Note_on_c,0,71,0\n’, ‘0,75876,Note_on_c,0,71,0\n’, ‘0,62201,Note_on_c,0,71,0\n’, ‘0,16877,Note_on_c,0,76,0\n’, ‘0,95789,Note_on_c,0,71,0\n’, ‘0,78033,Note_on_c,0,71,0\n’, ‘0,9866,Note_on_c,0,76,0\n’, ‘0,48023,Note_on_c,0,69,0\n’, ‘0,34237,Note_on_c,0,69,0\n’, ‘0,43436,Note_on_c,0,69,0\n’, ‘0,64950,Note_on_c,0,71,0\n’, ‘0,74649,Note_on_c,0,71,0\n’, ‘0,87633,Note_on_c,0,71,0\n’, ‘0,2127,Note_on_c,0,45,0\n’, ‘0,1126,Note_on_c,0,76,0\n’, ‘0,65980,Note_on_c,0,71,0\n’, ‘0,46862,Note_on_c,0,69,0\n’, ‘0,57820,Note_on_c,0,71,0\n’, ‘0,10389,Note_on_c,0,76,0\n’, ‘0,47658,Note_on_c,0,69,0\n’, ‘0,45491,Note_on_c,0,69,0\n’, ‘0,99584,Note_on_c,0,71,0\n’, ‘0,39729,Note_on_c,0,69,0\n’, ‘0,88753,Note_on_c,0,71,0\n’, ‘0,65465,Note_on_c,0,71,0\n’, ‘0,36018,Note_on_c,0,69,0\n’, ‘0,72598,Note_on_c,0,71,0\n’, ‘0,48244,Note_on_c,0,69,0\n’, ‘0,59750,Note_on_c,0,71,0\n’, ‘0,95137,Note_on_c,0,71,0\n’, ‘0,28713,Note_on_c,0,69,0\n’, ‘0,19655,Note_on_c,0,76,0\n’, ‘0,34974,Note_on_c,0,69,0\n’, ‘0,31698,Note_on_c,0,69,0\n’, ‘0,38293,Note_on_c,0,69,0\n’, ‘0,64441,Note_on_c,0,71,0\n’, ‘0,69959,Note_on_c,0,71,0\n’, ‘0,94521,Note_on_c,0,71,0\n’, ‘0,45678,Note_on_c,0,69,0\n’, ‘0,38956,Note_on_c,0,69,0\n’, ‘0,56375,Note_on_c,0,71,0\n’, ‘0,4532,Note_on_c,0,76,0\n’, ‘0,96840,Note_on_c,0,71,0\n’, ‘0,50075,Note_on_c,0,71,0\n’, ‘0,26950,Note_on_c,0,69,0\n’, ‘0,92607,Note_on_c,0,71,0\n’, ‘0,79734,Note_on_c,0,71,0\n’, ‘0,95945,Note_on_c,0,71,0\n’, ‘0,49142,Note_on_c,0,71,0\n’, ‘0,33089,Note_on_c,0,69,0\n’, ‘0,94785,Note_on_c,0,71,0\n’, ‘0,26451,Note_on_c,0,69,0\n’, ‘0,36127,Note_on_c,0,69,0\n’, ‘0,5970,Note_on_c,0,76,0\n’, ‘0,99484,Note_on_c,0,71,0\n’, ‘0,13429,Note_on_c,0,76,0\n’, ‘0,77857,Note_on_c,0,71,0\n’, ‘0,55258,Note_on_c,0,71,0\n’, ‘0,90227,Note_on_c,0,71,0\n’, ‘0,3857,Note_on_c,0,45,0\n’, ‘0,95115,Note_on_c,0,71,0\n’, ‘0,50622,Note_on_c,0,71,0\n’, ‘0,81171,Note_on_c,0,71,0\n’, ‘0,68755,Note_on_c,0,71,0\n’, ‘0,27767,Note_on_c,0,69,0\n’, ‘0,49666,Note_on_c,0,71,0\n’, ‘0,12842,Note_on_c,0,76,0\n’, ‘0,78965,Note_on_c,0,71,0\n’, ‘0,1303,Note_on_c,0,76,0\n’, ‘0,86018,Note_on_c,0,71,0\n’, ‘0,84857,Note_on_c,0,71,0\n’, ‘0,82664,Note_on_c,0,71,0\n’, ‘0,55808,Note_on_c,0,71,0\n’, ‘0,19410,Note_on_c,0,76,0\n’, ‘0,30294,Note_on_c,0,69,0\n’, ‘0,68828,Note_on_c,0,71,0\n’, ‘0,1145,Note_on_c,0,76,0\n’, ‘0,62302,Note_on_c,0,71,0\n’, ‘0,83499,Note_on_c,0,71,0\n’, ‘0,34513,Note_on_c,0,69,0\n’, ‘0,95595,Note_on_c,0,71,0\n’, ‘0,50643,Note_on_c,0,71,0\n’, ‘0,49007,Note_on_c,0,71,0\n’, ‘0,37636,Note_on_c,0,69,0\n’, ‘0,75878,Note_on_c,0,71,0\n’, ‘0,86794,Note_on_c,0,71,0\n’, ‘0,11536,Note_on_c,0,76,0\n’, ‘0,72693,Note_on_c,0,71,0\n’, ‘0,4302,Note_on_c,0,45,0\n’, ‘0,35446,Note_on_c,0,69,0\n’, ‘0,51467,Note_on_c,0,71,0\n’, ‘0,71405,Note_on_c,0,71,0\n’, ‘0,278,Note_on_c,0,76,0\n’, ‘0,33188,Note_on_c,0,69,0\n’, ‘0,58144,Note_on_c,0,71,0\n’, ‘0,19301,Note_on_c,0,76,0\n’, ‘0,87159,Note_on_c,0,71,0\n’, ‘0,52659,Note_on_c,0,71,0\n’, ‘0,4807,Note_on_c,0,76,0\n’, ‘0,81888,Note_on_c,0,71,0\n’, ‘0,46852,Note_on_c,0,69,0\n’, ‘0,23575,Note_on_c,0,76,0\n’, ‘0,21022,Note_on_c,0,76,0\n’, ‘0,67740,Note_on_c,0,71,0\n’, ‘0,73684,Note_on_c,0,71,0\n’, ‘0,52208,Note_on_c,0,71,0\n’, ‘0,84819,Note_on_c,0,71,0\n’, ‘0,17440,Note_on_c,0,76,0\n’, ‘0,97164,Note_on_c,0,71,0\n’, ‘0,57094,Note_on_c,0,71,0\n’, ‘0,41243,Note_on_c,0,69,0\n’, ‘0,48453,Note_on_c,0,69,0\n’, ‘0,12287,Note_on_c,0,76,0\n’, ‘0,80340,Note_on_c,0,71,0\n’, ‘0,55056,Note_on_c,0,71,0\n’, ‘0,10421,Note_on_c,0,76,0\n’, ‘0,19584,Note_on_c,0,76,0\n’, ‘0,78698,Note_on_c,0,71,0\n’, ‘0,47657,Note_on_c,0,69,0\n’, ‘0,22900,Note_on_c,0,76,0\n’, ‘0,59460,Note_on_c,0,71,0\n’, ‘0,3255,Note_on_c,0,45,0\n’, ‘0,56060,Note_on_c,0,71,0\n’, ‘0,8490,Note_on_c,0,76,0\n’, ‘0,6227,Note_on_c,0,76,0\n’, ‘0,78829,Note_on_c,0,71,0\n’, ‘0,10368,Note_on_c,0,76,0\n’, ‘0,96719,Note_on_c,0,71,0\n’, ‘0,85917,Note_on_c,0,71,0\n’, ‘0,66086,Note_on_c,0,71,0\n’, ‘0,55444,Note_on_c,0,71,0\n’, ‘0,49306,Note_on_c,0,71,0\n’, ‘0,87405,Note_on_c,0,71,0\n’, ‘0,44555,Note_on_c,0,69,0\n’, ‘0,27607,Note_on_c,0,69,0\n’, ‘0,3259,Note_on_c,0,45,0\n’, ‘0,36690,Note_on_c,0,69,0\n’, ‘0,91406,Note_on_c,0,71,0\n’, ‘0,41003,Note_on_c,0,69,0\n’, ‘0,23237,Note_on_c,0,76,0\n’, ‘0,98981,Note_on_c,0,71,0\n’, ‘0,1576,Note_on_c,0,45,0\n’, ‘0,87667,Note_on_c,0,71,0\n’, ‘0,54908,Note_on_c,0,71,0\n’, ‘0,89167,Note_on_c,0,71,0\n’, ‘0,42304,Note_on_c,0,69,0\n’, ‘0,40034,Note_on_c,0,69,0\n’, ‘0,5137,Note_on_c,0,76,0\n’, ‘0,37547,Note_on_c,0,69,0\n’, ‘0,91805,Note_on_c,0,71,0\n’, ‘0,20787,Note_on_c,0,76,0\n’, ‘0,15628,Note_on_c,0,76,0\n’, ‘0,85178,Note_on_c,0,71,0\n’, ‘0,34055,Note_on_c,0,69,0\n’, ‘0,7108,Note_on_c,0,76,0\n’, ‘0,9485,Note_on_c,0,76,0\n’, ‘0,36788,Note_on_c,0,69,0\n’, ‘0,93355,Note_on_c,0,71,0\n’, ‘0,74245,Note_on_c,0,71,0\n’, ‘0,91183,Note_on_c,0,71,0\n’, ‘0,10813,Note_on_c,0,76,0\n’, ‘0,42101,Note_on_c,0,69,0\n’, ‘0,39785,Note_on_c,0,69,0\n’, ‘0,87526,Note_on_c,0,71,0\n’, ‘0,46661,Note_on_c,0,69,0\n’, ‘0,11303,Note_on_c,0,76,0\n’, ‘0,14941,Note_on_c,0,76,0\n’, ‘0,37757,Note_on_c,0,69,0\n’, ‘0,89887,Note_on_c,0,71,0\n’, ‘0,57674,Note_on_c,0,71,0\n’, ‘0,75383,Note_on_c,0,71,0\n’, ‘0,34773,Note_on_c,0,69,0\n’, ‘0,56968,Note_on_c,0,71,0\n’, ‘0,69236,Note_on_c,0,71,0\n’, ‘0,67761,Note_on_c,0,71,0\n’, ‘0,90106,Note_on_c,0,71,0\n’, ‘0,36591,Note_on_c,0,69,0\n’, ‘0,94495,Note_on_c,0,71,0\n’, ‘0,4075,Note_on_c,0,45,0\n’, ‘0,49146,Note_on_c,0,71,0\n’, ‘0,75728,Note_on_c,0,71,0\n’, ‘0,20072,Note_on_c,0,76,0\n’, ‘0,10034,Note_on_c,0,76,0\n’, ‘0,52032,Note_on_c,0,71,0\n’, ‘0,55679,Note_on_c,0,71,0\n’, ‘0,1262,Note_on_c,0,76,0\n’, ‘0,82223,Note_on_c,0,71,0\n’, ‘0,20592,Note_on_c,0,76,0\n’, ‘0,80080,Note_on_c,0,71,0\n’, ‘0,85242,Note_on_c,0,71,0\n’, ‘0,66675,Note_on_c,0,71,0\n’, ‘0,27953,Note_on_c,0,69,0\n’, ‘0,8968,Note_on_c,0,76,0\n’, ‘0,34095,Note_on_c,0,69,0\n’, ‘0,59724,Note_on_c,0,71,0\n’, ‘0,1083,Note_on_c,0,76,0\n’, ‘0,90263,Note_on_c,0,71,0\n’, ‘0,62389,Note_on_c,0,71,0\n’, ‘0,72078,Note_on_c,0,71,0\n’, ‘0,64886,Note_on_c,0,71,0\n’, ‘0,69812,Note_on_c,0,71,0\n’, ‘0,584,Note_on_c,0,76,0\n’, ‘0,52325,Note_on_c,0,71,0\n’, ‘0,64472,Note_on_c,0,71,0\n’, ‘0,31056,Note_on_c,0,69,0\n’, ‘0,70325,Note_on_c,0,71,0\n’, ‘0,58139,Note_on_c,0,71,0\n’, ‘0,7269,Note_on_c,0,76,0\n’, ‘0,32500,Note_on_c,0,69,0\n’, ‘0,40839,Note_on_c,0,69,0\n’, ‘0,31675,Note_on_c,0,69,0\n’, ‘0,85659,Note_on_c,0,71,0\n’, ‘0,93022,Note_on_c,0,71,0\n’, ‘0,61369,Note_on_c,0,71,0\n’, ‘0,14935,Note_on_c,0,76,0\n’, ‘0,14594,Note_on_c,0,76,0\n’, ‘0,9723,Note_on_c,0,76,0\n’, ‘0,43161,Note_on_c,0,69,0\n’, ‘0,98945,Note_on_c,0,71,0\n’, ‘0,5340,Note_on_c,0,76,0\n’, ‘0,59831,Note_on_c,0,71,0\n’, ‘0,8607,Note_on_c,0,76,0\n’, ‘0,11475,Note_on_c,0,76,0\n’, ‘0,68184,Note_on_c,0,71,0\n’, ‘0,71097,Note_on_c,0,71,0\n’, ‘0,98424,Note_on_c,0,71,0\n’, ‘0,57066,Note_on_c,0,71,0\n’, ‘0,41548,Note_on_c,0,69,0\n’, ‘0,38895,Note_on_c,0,69,0\n’, ‘0,18456,Note_on_c,0,76,0\n’, ‘0,42240,Note_on_c,0,69,0\n’, ‘0,8197,Note_on_c,0,76,0\n’, ‘0,74974,Note_on_c,0,71,0\n’, ‘0,69351,Note_on_c,0,71,0\n’, ‘0,42971,Note_on_c,0,69,0\n’, ‘0,10278,Note_on_c,0,76,0\n’, ‘0,87717,Note_on_c,0,71,0\n’, ‘0,10248,Note_on_c,0,76,0\n’, ‘0,90506,Note_on_c,0,71,0\n’, ‘0,40822,Note_on_c,0,69,0\n’, ‘0,95630,Note_on_c,0,71,0\n’, ‘0,90580,Note_on_c,0,71,0\n’, ‘0,65564,Note_on_c,0,71,0\n’, ‘0,19227,Note_on_c,0,76,0\n’, ‘0,67996,Note_on_c,0,71,0\n’, ‘0,70287,Note_on_c,0,71,0\n’, ‘0,57017,Note_on_c,0,71,0\n’, ‘0,12906,Note_on_c,0,76,0\n’, ‘0,42916,Note_on_c,0,69,0\n’, ‘0,5945,Note_on_c,0,76,0\n’, ‘0,2480,Note_on_c,0,45,0\n’, ‘0,47469,Note_on_c,0,69,0\n’, ‘0,39933,Note_on_c,0,69,0\n’, ‘0,9407,Note_on_c,0,76,0\n’, ‘0,85776,Note_on_c,0,71,0\n’, ‘0,17613,Note_on_c,0,76,0\n’, ‘0,58508,Note_on_c,0,71,0\n’, ‘0,67508,Note_on_c,0,71,0\n’, ‘0,1913,Note_on_c,0,45,0\n’, ‘0,84100,Note_on_c,0,71,0\n’, ‘0,17343,Note_on_c,0,76,0\n’, ‘0,1331,Note_on_c,0,76,0\n’, ‘0,41974,Note_on_c,0,69,0\n’, ‘0,40575,Note_on_c,0,69,0\n’, ‘0,57248,Note_on_c,0,71,0\n’, ‘0,16527,Note_on_c,0,76,0\n’, ‘0,83181,Note_on_c,0,71,0\n’, ‘0,72799,Note_on_c,0,71,0\n’, ‘0,79113,Note_on_c,0,71,0\n’, ‘0,43263,Note_on_c,0,69,0\n’, ‘0,79619,Note_on_c,0,71,0\n’, ‘0,80529,Note_on_c,0,71,0\n’, ‘0,75585,Note_on_c,0,71,0\n’, ‘0,92355,Note_on_c,0,71,0\n’, ‘0,73668,Note_on_c,0,71,0\n’, ‘0,29890,Note_on_c,0,69,0\n’, ‘0,92283,Note_on_c,0,71,0\n’, ‘0,17820,Note_on_c,0,76,0\n’, ‘0,58302,Note_on_c,0,71,0\n’, ‘0,57743,Note_on_c,0,71,0\n’, ‘0,28019,Note_on_c,0,69,0\n’, ‘0,9564,Note_on_c,0,76,0\n’, ‘0,73209,Note_on_c,0,71,0\n’, ‘0,29582,Note_on_c,0,69,0\n’, ‘0,95266,Note_on_c,0,71,0\n’, ‘0,32351,Note_on_c,0,69,0\n’, ‘0,79314,Note_on_c,0,71,0\n’, ‘0,17319,Note_on_c,0,76,0\n’, ‘0,26987,Note_on_c,0,69,0\n’, ‘0,27914,Note_on_c,0,69,0\n’, ‘0,29235,Note_on_c,0,69,0\n’, ‘0,52211,Note_on_c,0,71,0\n’, ‘0,96056,Note_on_c,0,71,0\n’, ‘0,58371,Note_on_c,0,71,0\n’, ‘0,45934,Note_on_c,0,69,0\n’, ‘0,14956,Note_on_c,0,76,0\n’, ‘0,86452,Note_on_c,0,71,0\n’, ‘0,20866,Note_on_c,0,76,0\n’, ‘0,48559,Note_on_c,0,69,0\n’, ‘0,63919,Note_on_c,0,71,0\n’, ‘0,12226,Note_on_c,0,76,0\n’, ‘0,40061,Note_on_c,0,69,0\n’, ‘0,76618,Note_on_c,0,71,0\n’, ‘0,54837,Note_on_c,0,71,0\n’, ‘0,61855,Note_on_c,0,71,0\n’, ‘0,6410,Note_on_c,0,76,0\n’, ‘0,33315,Note_on_c,0,69,0\n’, ‘0,14923,Note_on_c,0,76,0\n’, ‘0,85423,Note_on_c,0,71,0\n’, ‘0,22237,Note_on_c,0,76,0\n’, ‘0,37854,Note_on_c,0,69,0\n’, ‘0,27944,Note_on_c,0,69,0\n’, ‘0,41927,Note_on_c,0,69,0\n’, ‘0,77972,Note_on_c,0,71,0\n’, ‘0,3891,Note_on_c,0,45,0\n’, ‘0,34616,Note_on_c,0,69,0\n’, ‘0,23500,Note_on_c,0,76,0\n’, ‘0,85847,Note_on_c,0,71,0\n’, ‘0,51574,Note_on_c,0,71,0\n’, ‘0,28811,Note_on_c,0,69,0\n’, ‘0,94254,Note_on_c,0,71,0\n’, ‘0,79928,Note_on_c,0,71,0\n’, ‘0,20406,Note_on_c,0,76,0\n’, ‘0,98598,Note_on_c,0,71,0\n’, ‘0,65981,Note_on_c,0,71,0\n’, ‘0,53723,Note_on_c,0,71,0\n’, ‘0,43776,Note_on_c,0,69,0\n’, ‘0,40913,Note_on_c,0,69,0\n’, ‘0,1894,Note_on_c,0,45,0\n’, ‘0,74684,Note_on_c,0,71,0\n’, ‘0,69053,Note_on_c,0,71,0\n’, ‘0,23,Note_on_c,0,76,0\n’, ‘0,23960,Note_on_c,0,69,0\n’, ‘0,6624,Note_on_c,0,76,0\n’, ‘0,90458,Note_on_c,0,71,0\n’, ‘0,53276,Note_on_c,0,71,0\n’, ‘0,17265,Note_on_c,0,76,0\n’, ‘0,69660,Note_on_c,0,71,0\n’, ‘0,44706,Note_on_c,0,69,0\n’, ‘0,16983,Note_on_c,0,76,0\n’, ‘0,58152,Note_on_c,0,71,0\n’, ‘0,77476,Note_on_c,0,71,0\n’, ‘0,50612,Note_on_c,0,71,0\n’, ‘0,92936,Note_on_c,0,71,0\n’, ‘0,80035,Note_on_c,0,71,0\n’, ‘0,38269,Note_on_c,0,69,0\n’, ‘0,80399,Note_on_c,0,71,0\n’, ‘0,9652,Note_on_c,0,76,0\n’, ‘0,94898,Note_on_c,0,71,0\n’, ‘0,90283,Note_on_c,0,71,0\n’, ‘0,65564,Note_on_c,0,71,0\n’, ‘0,30576,Note_on_c,0,69,0\n’, ‘0,7401,Note_on_c,0,76,0\n’, ‘0,71479,Note_on_c,0,71,0\n’, ‘0,40468,Note_on_c,0,69,0\n’, ‘0,56905,Note_on_c,0,71,0\n’, ‘0,59902,Note_on_c,0,71,0\n’, ‘0,25446,Note_on_c,0,69,0\n’, ‘0,36561,Note_on_c,0,69,0\n’, ‘0,29545,Note_on_c,0,69,0\n’, ‘0,61423,Note_on_c,0,71,0\n’, ‘0,2329,Note_on_c,0,45,0\n’, ‘0,81613,Note_on_c,0,71,0\n’, ‘0,53321,Note_on_c,0,71,0\n’, ‘0,9701,Note_on_c,0,76,0\n’, ‘0,829,Note_on_c,0,76,0\n’, ‘0,4814,Note_on_c,0,76,0\n’, ‘0,56574,Note_on_c,0,71,0\n’, ‘0,20074,Note_on_c,0,76,0\n’, ‘0,5613,Note_on_c,0,76,0\n’, ‘0,73385,Note_on_c,0,71,0\n’, ‘0,39269,Note_on_c,0,69,0\n’, ‘0,79029,Note_on_c,0,71,0\n’, ‘0,7309,Note_on_c,0,76,0\n’, ‘0,46750,Note_on_c,0,69,0\n’, ‘0,55165,Note_on_c,0,71,0\n’, ‘0,5578,Note_on_c,0,76,0\n’, ‘0,37084,Note_on_c,0,69,0\n’, ‘0,5962,Note_on_c,0,76,0\n’, ‘0,10617,Note_on_c,0,76,0\n’, ‘0,39643,Note_on_c,0,69,0\n’, ‘0,37702,Note_on_c,0,69,0\n’, ‘0,50866,Note_on_c,0,71,0\n’, ‘0,1236,Note_on_c,0,76,0\n’, ‘0,51041,Note_on_c,0,71,0\n’, ‘0,73409,Note_on_c,0,71,0\n’, ‘0,46297,Note_on_c,0,69,0\n’, ‘0,87175,Note_on_c,0,71,0\n’, ‘0,18954,Note_on_c,0,76,0\n’, ‘0,21927,Note_on_c,0,76,0\n’, ‘0,64772,Note_on_c,0,71,0\n’, ‘0,2961,Note_on_c,0,45,0\n’, ‘0,45920,Note_on_c,0,69,0\n’, ‘0,43433,Note_on_c,0,69,0\n’, ‘0,6027,Note_on_c,0,76,0\n’, ‘0,46438,Note_on_c,0,69,0\n’, ‘0,64350,Note_on_c,0,71,0\n’, ‘0,664,Note_on_c,0,76,0\n’, ‘0,90898,Note_on_c,0,71,0\n’, ‘0,58448,Note_on_c,0,71,0\n’, ‘0,58883,Note_on_c,0,71,0\n’, ‘0,79383,Note_on_c,0,71,0\n’, ‘0,75474,Note_on_c,0,71,0\n’, ‘0,27998,Note_on_c,0,69,0\n’, ‘0,77683,Note_on_c,0,71,0\n’, ‘0,46040,Note_on_c,0,69,0\n’, ‘0,70811,Note_on_c,0,71,0\n’, ‘0,59267,Note_on_c,0,71,0\n’, ‘0,73360,Note_on_c,0,71,0\n’, ‘0,82748,Note_on_c,0,71,0\n’, ‘0,84238,Note_on_c,0,71,0\n’, ‘0,42373,Note_on_c,0,69,0\n’, ‘0,5482,Note_on_c,0,76,0\n’, ‘0,63415,Note_on_c,0,71,0\n’, ‘0,46418,Note_on_c,0,69,0\n’, ‘0,90560,Note_on_c,0,71,0\n’, ‘0,24706,Note_on_c,0,69,0\n’, ‘0,59934,Note_on_c,0,71,0\n’, ‘0,28146,Note_on_c,0,69,0\n’, ‘0,27619,Note_on_c,0,69,0\n’, ‘0,31455,Note_on_c,0,69,0\n’, ‘0,95405,Note_on_c,0,71,0\n’, ‘0,10825,Note_on_c,0,76,0\n’, ‘0,5787,Note_on_c,0,76,0\n’, ‘0,91930,Note_on_c,0,71,0\n’, ‘0,23718,Note_on_c,0,76,0\n’, ‘0,60177,Note_on_c,0,71,0\n’, ‘0,81996,Note_on_c,0,71,0\n’, ‘0,83244,Note_on_c,0,71,0\n’, ‘0,69742,Note_on_c,0,71,0\n’, ‘0,60877,Note_on_c,0,71,0\n’, ‘0,12597,Note_on_c,0,76,0\n’, ‘0,67669,Note_on_c,0,71,0\n’, ‘0,55951,Note_on_c,0,71,0\n’, ‘0,39065,Note_on_c,0,69,0\n’, ‘0,11417,Note_on_c,0,76,0\n’, ‘0,72698,Note_on_c,0,71,0\n’, ‘0,8811,Note_on_c,0,76,0\n’, ‘0,47713,Note_on_c,0,69,0\n’, ‘0,27934,Note_on_c,0,69,0\n’, ‘0,46046,Note_on_c,0,69,0\n’, ‘0,1583,Note_on_c,0,45,0\n’, ‘0,84499,Note_on_c,0,71,0\n’, ‘0,41759,Note_on_c,0,69,0\n’, ‘0,47023,Note_on_c,0,69,0\n’, ‘0,57280,Note_on_c,0,71,0\n’, ‘0,71577,Note_on_c,0,71,0\n’, ‘0,12836,Note_on_c,0,76,0\n’, ‘0,8519,Note_on_c,0,76,0\n’, ‘0,89274,Note_on_c,0,71,0\n’, ‘0,72936,Note_on_c,0,71,0\n’, ‘0,98426,Note_on_c,0,71,0\n’, ‘0,13849,Note_on_c,0,76,0\n’, ‘0,71414,Note_on_c,0,71,0\n’, ‘0,35357,Note_on_c,0,69,0\n’, ‘0,13459,Note_on_c,0,76,0\n’, ‘0,69852,Note_on_c,0,71,0\n’, ‘0,42166,Note_on_c,0,69,0\n’, ‘0,57598,Note_on_c,0,71,0\n’, ‘0,57601,Note_on_c,0,71,0\n’, ‘0,37324,Note_on_c,0,69,0\n’, ‘0,64740,Note_on_c,0,71,0\n’, ‘0,83245,Note_on_c,0,71,0\n’, ‘0,98974,Note_on_c,0,71,0\n’, ‘0,85100,Note_on_c,0,71,0\n’, ‘0,21237,Note_on_c,0,76,0\n’, ‘0,17593,Note_on_c,0,76,0\n’, ‘0,87667,Note_on_c,0,71,0\n’, ‘0,80947,Note_on_c,0,71,0\n’, ‘0,64186,Note_on_c,0,71,0\n’, ‘0,83001,Note_on_c,0,71,0\n’, ‘0,76280,Note_on_c,0,71,0\n’, ‘0,77967,Note_on_c,0,71,0\n’, ‘0,96530,Note_on_c,0,71,0\n’, ‘0,57222,Note_on_c,0,71,0\n’, ‘0,52652,Note_on_c,0,71,0\n’, ‘0,93734,Note_on_c,0,71,0\n’, ‘0,40577,Note_on_c,0,69,0\n’, ‘0,77056,Note_on_c,0,71,0\n’, ‘0,40184,Note_on_c,0,69,0\n’, ‘0,34937,Note_on_c,0,69,0\n’, ‘0,75659,Note_on_c,0,71,0\n’, ‘0,25152,Note_on_c,0,69,0\n’, ‘0,97182,Note_on_c,0,71,0\n’, ‘0,18802,Note_on_c,0,76,0\n’, ‘0,61804,Note_on_c,0,71,0\n’, ‘0,48466,Note_on_c,0,69,0\n’, ‘0,20559,Note_on_c,0,76,0\n’, ‘0,65695,Note_on_c,0,71,0\n’, ‘0,12225,Note_on_c,0,76,0\n’, ‘0,33352,Note_on_c,0,69,0\n’, ‘0,7596,Note_on_c,0,76,0\n’, ‘0,92179,Note_on_c,0,71,0\n’, ‘0,66564,Note_on_c,0,71,0\n’, ‘0,43998,Note_on_c,0,69,0\n’, ‘0,27811,Note_on_c,0,69,0\n’, ‘0,25787,Note_on_c,0,69,0\n’, ‘0,60592,Note_on_c,0,71,0\n’, ‘0,25291,Note_on_c,0,69,0\n’, ‘0,92691,Note_on_c,0,71,0\n’, ‘0,59776,Note_on_c,0,71,0\n’, ‘0,18608,Note_on_c,0,76,0\n’, ‘0,38691,Note_on_c,0,69,0\n’, ‘0,18823,Note_on_c,0,76,0\n’, ‘0,5187,Note_on_c,0,76,0\n’, ‘0,99001,Note_on_c,0,71,0\n’, ‘0,63630,Note_on_c,0,71,0\n’, ‘0,26725,Note_on_c,0,69,0\n’, ‘0,25938,Note_on_c,0,69,0\n’, ‘0,92262,Note_on_c,0,71,0\n’, ‘0,59279,Note_on_c,0,71,0\n’, ‘0,28437,Note_on_c,0,69,0\n’, ‘0,99371,Note_on_c,0,71,0\n’, ‘0,29116,Note_on_c,0,69,0\n’, ‘0,67346,Note_on_c,0,71,0\n’, ‘0,2227,Note_on_c,0,45,0\n’, ‘0,47329,Note_on_c,0,69,0\n’, ‘0,71026,Note_on_c,0,71,0\n’, ‘0,83347,Note_on_c,0,71,0\n’, ‘0,67414,Note_on_c,0,71,0\n’, ‘0,16847,Note_on_c,0,76,0\n’, ‘0,82073,Note_on_c,0,71,0\n’, ‘0,66677,Note_on_c,0,71,0\n’, ‘0,82632,Note_on_c,0,71,0\n’, ‘0,36520,Note_on_c,0,69,0\n’, ‘0,83500,Note_on_c,0,71,0\n’, ‘0,65750,Note_on_c,0,71,0\n’, ‘0,44334,Note_on_c,0,69,0\n’, ‘0,57761,Note_on_c,0,71,0\n’, ‘0,67702,Note_on_c,0,71,0\n’, ‘0,61229,Note_on_c,0,71,0\n’, ‘0,12855,Note_on_c,0,76,0\n’, ‘0,10689,Note_on_c,0,76,0\n’, ‘0,23379,Note_on_c,0,76,0\n’, ‘0,20455,Note_on_c,0,76,0\n’, ‘0,82822,Note_on_c,0,71,0\n’, ‘0,18997,Note_on_c,0,76,0\n’, ‘0,91589,Note_on_c,0,71,0\n’, ‘0,40152,Note_on_c,0,69,0\n’, ‘0,35491,Note_on_c,0,69,0\n’, ‘0,99929,Note_on_c,0,71,0\n’, ‘0,63895,Note_on_c,0,71,0\n’, ‘0,1657,Note_on_c,0,45,0\n’, ‘0,84025,Note_on_c,0,71,0\n’, ‘0,52731,Note_on_c,0,71,0\n’, ‘0,968,Note_on_c,0,76,0\n’, ‘0,38756,Note_on_c,0,69,0\n’, ‘0,64522,Note_on_c,0,71,0\n’, ‘0,63868,Note_on_c,0,71,0\n’, ‘0,53831,Note_on_c,0,71,0\n’, ‘0,88220,Note_on_c,0,71,0\n’, ‘0,51176,Note_on_c,0,71,0\n’, ‘0,63722,Note_on_c,0,71,0\n’, ‘0,42426,Note_on_c,0,69,0\n’, ‘0,48567,Note_on_c,0,69,0\n’, ‘0,21052,Note_on_c,0,76,0\n’, ‘0,70579,Note_on_c,0,71,0\n’, ‘0,11641,Note_on_c,0,76,0\n’, ‘0,24398,Note_on_c,0,69,0\n’, ‘0,19263,Note_on_c,0,76,0\n’, ‘0,95847,Note_on_c,0,71,0\n’, ‘0,31902,Note_on_c,0,69,0\n’, ‘0,5800,Note_on_c,0,76,0\n’, ‘0,99340,Note_on_c,0,71,0\n’, ‘0,73568,Note_on_c,0,71,0\n’, ‘0,53963,Note_on_c,0,71,0\n’, ‘0,20932,Note_on_c,0,76,0\n’, ‘0,44119,Note_on_c,0,69,0\n’, ‘0,21200,Note_on_c,0,76,0\n’, ‘0,59968,Note_on_c,0,71,0\n’, ‘0,11186,Note_on_c,0,76,0\n’, ‘0,21539,Note_on_c,0,76,0\n’, ‘0,68378,Note_on_c,0,71,0\n’, ‘0,19261,Note_on_c,0,76,0\n’, ‘0,11541,Note_on_c,0,76,0\n’, ‘0,13899,Note_on_c,0,76,0\n’, ‘0,5690,Note_on_c,0,76,0\n’, ‘0,34821,Note_on_c,0,69,0\n’, ‘0,28656,Note_on_c,0,69,0\n’, ‘0,47821,Note_on_c,0,69,0\n’, ‘0,11813,Note_on_c,0,76,0\n’, ‘0,39667,Note_on_c,0,69,0\n’, ‘0,22724,Note_on_c,0,76,0\n’, ‘0,95375,Note_on_c,0,71,0\n’, ‘0,87280,Note_on_c,0,71,0\n’, ‘0,12177,Note_on_c,0,76,0\n’, ‘0,11594,Note_on_c,0,76,0\n’, ‘0,65115,Note_on_c,0,71,0\n’, ‘0,19388,Note_on_c,0,76,0\n’, ‘0,12360,Note_on_c,0,76,0\n’, ‘0,31802,Note_on_c,0,69,0\n’, ‘0,73665,Note_on_c,0,71,0\n’, ‘0,88657,Note_on_c,0,71,0\n’, ‘0,67263,Note_on_c,0,71,0\n’, ‘0,59200,Note_on_c,0,71,0\n’, ‘0,71988,Note_on_c,0,71,0\n’, ‘0,6123,Note_on_c,0,76,0\n’, ‘0,35408,Note_on_c,0,69,0\n’, ‘0,12769,Note_on_c,0,76,0\n’, ‘0,23811,Note_on_c,0,76,0\n’, ‘0,90056,Note_on_c,0,71,0\n’, ‘0,40730,Note_on_c,0,69,0\n’, ‘0,3511,Note_on_c,0,45,0\n’, ‘0,61065,Note_on_c,0,71,0\n’, ‘0,95732,Note_on_c,0,71,0\n’, ‘0,55180,Note_on_c,0,71,0\n’, ‘0,29859,Note_on_c,0,69,0\n’, ‘0,27702,Note_on_c,0,69,0\n’, ‘0,93778,Note_on_c,0,71,0\n’, ‘0,92737,Note_on_c,0,71,0\n’, ‘0,22409,Note_on_c,0,76,0\n’, ‘0,32158,Note_on_c,0,69,0\n’, ‘0,25495,Note_on_c,0,69,0\n’, ‘0,62860,Note_on_c,0,71,0\n’, ‘0,92506,Note_on_c,0,71,0\n’, ‘0,58996,Note_on_c,0,71,0\n’, ‘0,7575,Note_on_c,0,76,0\n’, ‘0,72016,Note_on_c,0,71,0\n’, ‘0,92655,Note_on_c,0,71,0\n’, ‘0,20966,Note_on_c,0,76,0\n’, ‘0,20852,Note_on_c,0,76,0\n’, ‘0,40278,Note_on_c,0,69,0\n’, ‘0,19521,Note_on_c,0,76,0\n’, ‘0,53043,Note_on_c,0,71,0\n’, ‘0,97390,Note_on_c,0,71,0\n’, ‘0,32717,Note_on_c,0,69,0\n’, ‘0,44184,Note_on_c,0,69,0\n’, ‘0,17800,Note_on_c,0,76,0\n’, ‘0,9724,Note_on_c,0,76,0\n’, ‘0,1091,Note_on_c,0,76,0\n’, ‘0,52610,Note_on_c,0,71,0\n’, ‘0,35335,Note_on_c,0,69,0\n’, ‘0,29396,Note_on_c,0,69,0\n’, ‘0,70613,Note_on_c,0,71,0\n’, ‘0,29582,Note_on_c,0,69,0\n’, ‘0,24634,Note_on_c,0,69,0\n’, ‘0,68038,Note_on_c,0,71,0\n’, ‘0,41524,Note_on_c,0,69,0\n’, ‘0,6020,Note_on_c,0,76,0\n’, ‘0,92162,Note_on_c,0,71,0\n’, ‘0,7465,Note_on_c,0,76,0\n’, ‘0,64415,Note_on_c,0,71,0\n’, ‘0,63408,Note_on_c,0,71,0\n’, ‘0,32696,Note_on_c,0,69,0\n’, ‘0,46802,Note_on_c,0,69,0\n’, ‘0,39614,Note_on_c,0,69,0\n’, ‘0,95494,Note_on_c,0,71,0\n’, ‘0,38368,Note_on_c,0,69,0\n’, ‘0,41955,Note_on_c,0,69,0\n’, ‘0,95086,Note_on_c,0,71,0\n’, ‘0,76254,Note_on_c,0,71,0\n’, ‘0,83971,Note_on_c,0,71,0\n’, ‘0,30718,Note_on_c,0,69,0\n’, ‘0,17384,Note_on_c,0,76,0\n’, ‘0,49485,Note_on_c,0,71,0\n’, ‘0,75864,Note_on_c,0,71,0\n’, ‘0,71539,Note_on_c,0,71,0\n’, ‘0,53176,Note_on_c,0,71,0\n’, ‘0,28976,Note_on_c,0,69,0\n’, ‘0,6409,Note_on_c,0,76,0\n’, ‘0,1052,Note_on_c,0,76,0\n’, ‘0,35367,Note_on_c,0,69,0\n’, ‘0,75135,Note_on_c,0,71,0\n’, ‘0,98184,Note_on_c,0,71,0\n’, ‘0,42828,Note_on_c,0,69,0\n’, ‘0,97503,Note_on_c,0,71,0\n’, ‘0,76141,Note_on_c,0,71,0\n’, ‘0,54247,Note_on_c,0,71,0\n’, ‘0,17805,Note_on_c,0,76,0\n’, ‘0,44794,Note_on_c,0,69,0\n’, ‘0,17711,Note_on_c,0,76,0\n’, ‘0,64733,Note_on_c,0,71,0\n’, ‘0,50772,Note_on_c,0,71,0\n’, ‘0,76818,Note_on_c,0,71,0\n’, ‘0,72776,Note_on_c,0,71,0\n’, ‘0,98721,Note_on_c,0,71,0\n’, ‘0,58434,Note_on_c,0,71,0\n’, ‘0,38806,Note_on_c,0,69,0\n’, ‘0,22339,Note_on_c,0,76,0\n’, ‘0,18003,Note_on_c,0,76,0\n’, ‘0,19639,Note_on_c,0,76,0\n’, ‘0,22636,Note_on_c,0,76,0\n’, ‘0,86930,Note_on_c,0,71,0\n’, ‘0,42132,Note_on_c,0,69,0\n’, ‘0,12382,Note_on_c,0,76,0\n’, ‘0,4898,Note_on_c,0,76,0\n’, ‘0,74055,Note_on_c,0,71,0\n’, ‘0,81824,Note_on_c,0,71,0\n’, ‘0,15441,Note_on_c,0,76,0\n’, ‘0,65039,Note_on_c,0,71,0\n’, ‘0,37322,Note_on_c,0,69,0\n’, ‘0,75068,Note_on_c,0,71,0\n’, ‘0,13349,Note_on_c,0,76,0\n’, ‘0,54321,Note_on_c,0,71,0\n’, ‘0,69766,Note_on_c,0,71,0\n’, ‘0,95063,Note_on_c,0,71,0\n’, ‘0,37365,Note_on_c,0,69,0\n’, ‘0,51384,Note_on_c,0,71,0\n’, ‘0,28876,Note_on_c,0,69,0\n’, ‘0,18930,Note_on_c,0,76,0\n’, ‘0,74555,Note_on_c,0,71,0\n’, ‘0,27448,Note_on_c,0,69,0\n’, ‘0,52115,Note_on_c,0,71,0\n’, ‘0,21898,Note_on_c,0,76,0\n’, ‘0,47349,Note_on_c,0,69,0\n’, ‘0,20445,Note_on_c,0,76,0\n’, ‘0,61410,Note_on_c,0,71,0\n’, ‘0,24714,Note_on_c,0,69,0\n’, ‘0,36448,Note_on_c,0,69,0\n’, ‘0,95415,Note_on_c,0,71,0\n’, ‘0,61057,Note_on_c,0,71,0\n’, ‘0,19651,Note_on_c,0,76,0\n’, ‘0,37901,Note_on_c,0,69,0\n’, ‘0,74865,Note_on_c,0,71,0\n’, ‘0,63184,Note_on_c,0,71,0\n’, ‘0,58869,Note_on_c,0,71,0\n’, ‘0,64862,Note_on_c,0,71,0\n’, ‘0,94276,Note_on_c,0,71,0\n’, ‘0,64435,Note_on_c,0,71,0\n’, ‘0,58513,Note_on_c,0,71,0\n’, ‘0,57672,Note_on_c,0,71,0\n’, ‘0,7864,Note_on_c,0,76,0\n’, ‘0,14398,Note_on_c,0,76,0\n’, ‘0,1183,Note_on_c,0,76,0\n’, ‘0,77805,Note_on_c,0,71,0\n’, ‘0,79200,Note_on_c,0,71,0\n’, ‘0,1114,Note_on_c,0,76,0\n’, ‘0,13534,Note_on_c,0,76,0\n’, ‘0,31206,Note_on_c,0,69,0\n’, ‘0,63668,Note_on_c,0,71,0\n’, ‘0,59585,Note_on_c,0,71,0\n’, ‘0,55827,Note_on_c,0,71,0\n’, ‘0,7279,Note_on_c,0,76,0\n’, ‘0,46885,Note_on_c,0,69,0\n’, ‘0,28616,Note_on_c,0,69,0\n’, ‘0,55640,Note_on_c,0,71,0\n’, ‘0,34131,Note_on_c,0,69,0\n’, ‘0,12685,Note_on_c,0,76,0\n’, ‘0,27571,Note_on_c,0,69,0\n’, ‘0,62645,Note_on_c,0,71,0\n’, ‘0,62991,Note_on_c,0,71,0\n’, ‘0,11345,Note_on_c,0,76,0\n’, ‘0,45416,Note_on_c,0,69,0\n’, ‘0,82599,Note_on_c,0,71,0\n’, ‘0,76016,Note_on_c,0,71,0\n’, ‘0,32835,Note_on_c,0,69,0\n’, ‘0,39949,Note_on_c,0,69,0\n’, ‘0,47362,Note_on_c,0,69,0\n’, ‘0,58027,Note_on_c,0,71,0\n’, ‘0,58582,Note_on_c,0,71,0\n’, ‘0,57978,Note_on_c,0,71,0\n’, ‘0,74601,Note_on_c,0,71,0\n’, ‘0,83698,Note_on_c,0,71,0\n’, ‘0,6887,Note_on_c,0,76,0\n’, ‘0,24788,Note_on_c,0,69,0\n’, ‘0,90865,Note_on_c,0,71,0\n’, ‘0,56473,Note_on_c,0,71,0\n’, ‘0,94093,Note_on_c,0,71,0\n’, ‘0,55755,Note_on_c,0,71,0\n’, ‘0,76924,Note_on_c,0,71,0\n’, ‘0,44033,Note_on_c,0,69,0\n’, ‘0,81931,Note_on_c,0,71,0\n’, ‘0,95618,Note_on_c,0,71,0\n’, ‘0,70167,Note_on_c,0,71,0\n’, ‘0,26606,Note_on_c,0,69,0\n’, ‘0,37445,Note_on_c,0,69,0\n’, ‘0,30108,Note_on_c,0,69,0\n’, ‘0,74373,Note_on_c,0,71,0\n’, ‘0,70020,Note_on_c,0,71,0\n’, ‘0,10489,Note_on_c,0,76,0\n’, ‘0,80811,Note_on_c,0,71,0\n’, ‘0,61619,Note_on_c,0,71,0\n’, ‘0,5815,Note_on_c,0,76,0\n’, ‘0,42635,Note_on_c,0,69,0\n’, ‘0,864,Note_on_c,0,76,0\n’, ‘0,11575,Note_on_c,0,76,0\n’, ‘0,51652,Note_on_c,0,71,0\n’, ‘0,86781,Note_on_c,0,71,0\n’, ‘0,72642,Note_on_c,0,71,0\n’, ‘0,90352,Note_on_c,0,71,0\n’, ‘0,15246,Note_on_c,0,76,0\n’, ‘0,84149,Note_on_c,0,71,0\n’, ‘0,13485,Note_on_c,0,76,0\n’, ‘0,56648,Note_on_c,0,71,0\n’, ‘0,76336,Note_on_c,0,71,0\n’, ‘0,85800,Note_on_c,0,71,0\n’, ‘0,55881,Note_on_c,0,71,0\n’, ‘0,82117,Note_on_c,0,71,0\n’, ‘0,13132,Note_on_c,0,76,0\n’, ‘0,6577,Note_on_c,0,76,0\n’, ‘0,56250,Note_on_c,0,71,0\n’, ‘0,2446,Note_on_c,0,45,0\n’, ‘0,90951,Note_on_c,0,71,0\n’, ‘0,20725,Note_on_c,0,76,0\n’, ‘0,19761,Note_on_c,0,76,0\n’, ‘0,65079,Note_on_c,0,71,0\n’, ‘0,56820,Note_on_c,0,71,0\n’, ‘0,21225,Note_on_c,0,76,0\n’, ‘0,50927,Note_on_c,0,71,0\n’, ‘0,43066,Note_on_c,0,69,0\n’, ‘0,70298,Note_on_c,0,71,0\n’, ‘0,9928,Note_on_c,0,76,0\n’, ‘0,36560,Note_on_c,0,69,0\n’, ‘0,21061,Note_on_c,0,76,0\n’, ‘0,75539,Note_on_c,0,71,0\n’, ‘0,70345,Note_on_c,0,71,0\n’, ‘0,33671,Note_on_c,0,69,0\n’, ‘0,89877,Note_on_c,0,71,0\n’, ‘0,27057,Note_on_c,0,69,0\n’, ‘0,94034,Note_on_c,0,71,0\n’, ‘0,77911,Note_on_c,0,71,0\n’, ‘0,1145,Note_on_c,0,76,0\n’, ‘0,82359,Note_on_c,0,71,0\n’, ‘0,6322,Note_on_c,0,76,0\n’, ‘0,40007,Note_on_c,0,69,0\n’, ‘0,8480,Note_on_c,0,76,0\n’, ‘0,49148,Note_on_c,0,71,0\n’, ‘0,34663,Note_on_c,0,69,0\n’, ‘0,92014,Note_on_c,0,71,0\n’, ‘0,40116,Note_on_c,0,69,0\n’, ‘0,83424,Note_on_c,0,71,0\n’, ‘0,19349,Note_on_c,0,76,0\n’, ‘0,93993,Note_on_c,0,71,0\n’, ‘0,88686,Note_on_c,0,71,0\n’, ‘0,74459,Note_on_c,0,71,0\n’, ‘0,50529,Note_on_c,0,71,0\n’, ‘0,76670,Note_on_c,0,71,0\n’, ‘0,68439,Note_on_c,0,71,0\n’, ‘0,71014,Note_on_c,0,71,0\n’, ‘0,18659,Note_on_c,0,76,0\n’, ‘0,65036,Note_on_c,0,71,0\n’, ‘0,40571,Note_on_c,0,69,0\n’, ‘0,50622,Note_on_c,0,71,0\n’, ‘0,30373,Note_on_c,0,69,0\n’, ‘0,15140,Note_on_c,0,76,0\n’, ‘0,63094,Note_on_c,0,71,0\n’, ‘0,12201,Note_on_c,0,76,0\n’, ‘0,42083,Note_on_c,0,69,0\n’, ‘0,5308,Note_on_c,0,76,0\n’, ‘0,32644,Note_on_c,0,69,0\n’, ‘0,39980,Note_on_c,0,69,0\n’, ‘0,41624,Note_on_c,0,69,0\n’, ‘0,6785,Note_on_c,0,76,0\n’, ‘0,18404,Note_on_c,0,76,0\n’, ‘0,92596,Note_on_c,0,71,0\n’, ‘0,75482,Note_on_c,0,71,0\n’, ‘0,28590,Note_on_c,0,69,0\n’, ‘0,65152,Note_on_c,0,71,0\n’, ‘0,20478,Note_on_c,0,76,0\n’, ‘0,22044,Note_on_c,0,76,0\n’, ‘0,21031,Note_on_c,0,76,0\n’, ‘0,39898,Note_on_c,0,69,0\n’, ‘0,35995,Note_on_c,0,69,0\n’, ‘0,68884,Note_on_c,0,71,0\n’, ‘0,59576,Note_on_c,0,71,0\n’, ‘0,91185,Note_on_c,0,71,0\n’, ‘0,3647,Note_on_c,0,45,0\n’, ‘0,27778,Note_on_c,0,69,0\n’, ‘0,19058,Note_on_c,0,76,0\n’, ‘0,63116,Note_on_c,0,71,0\n’, ‘0,78240,Note_on_c,0,71,0\n’, ‘0,42740,Note_on_c,0,69,0\n’, ‘0,49746,Note_on_c,0,71,0\n’, ‘0,12733,Note_on_c,0,76,0\n’, ‘0,36255,Note_on_c,0,69,0\n’, ‘0,14676,Note_on_c,0,76,0\n’, ‘0,56436,Note_on_c,0,71,0\n’, ‘0,87848,Note_on_c,0,71,0\n’, ‘0,3220,Note_on_c,0,45,0\n’, ‘0,9871,Note_on_c,0,76,0\n’, ‘0,35369,Note_on_c,0,69,0\n’, ‘0,19826,Note_on_c,0,76,0\n’, ‘0,62699,Note_on_c,0,71,0\n’, ‘0,29861,Note_on_c,0,69,0\n’, ‘0,96136,Note_on_c,0,71,0\n’, ‘0,49657,Note_on_c,0,71,0\n’, ‘0,68949,Note_on_c,0,71,0\n’, ‘0,50056,Note_on_c,0,71,0\n’, ‘0,96186,Note_on_c,0,71,0\n’, ‘0,20341,Note_on_c,0,76,0\n’, ‘0,720,Note_on_c,0,76,0\n’, ‘0,54113,Note_on_c,0,71,0\n’, ‘0,76234,Note_on_c,0,71,0\n’, ‘0,4218,Note_on_c,0,45,0\n’, ‘0,19820,Note_on_c,0,76,0\n’, ‘0,55114,Note_on_c,0,71,0\n’, ‘0,15379,Note_on_c,0,76,0\n’, ‘0,94537,Note_on_c,0,71,0\n’, ‘0,42740,Note_on_c,0,69,0\n’, ‘0,96255,Note_on_c,0,71,0\n’, ‘0,74216,Note_on_c,0,71,0\n’, ‘0,41445,Note_on_c,0,69,0\n’, ‘0,58035,Note_on_c,0,71,0\n’, ‘0,11536,Note_on_c,0,76,0\n’, ‘0,19130,Note_on_c,0,76,0\n’, ‘0,38788,Note_on_c,0,69,0\n’, ‘0,3045,Note_on_c,0,45,0\n’, ‘0,66383,Note_on_c,0,71,0\n’, ‘0,96593,Note_on_c,0,71,0\n’, ‘0,79274,Note_on_c,0,71,0\n’, ‘0,99251,Note_on_c,0,71,0\n’, ‘0,79270,Note_on_c,0,71,0\n’, ‘0,66261,Note_on_c,0,71,0\n’, ‘0,6861,Note_on_c,0,76,0\n’, ‘0,96261,Note_on_c,0,71,0\n’, ‘0,44249,Note_on_c,0,69,0\n’, ‘0,38748,Note_on_c,0,69,0\n’, ‘0,9204,Note_on_c,0,76,0\n’, ‘0,2694,Note_on_c,0,45,0\n’, ‘0,97110,Note_on_c,0,71,0\n’, ‘0,70271,Note_on_c,0,71,0\n’, ‘0,34938,Note_on_c,0,69,0\n’, ‘0,69832,Note_on_c,0,71,0\n’, ‘0,96132,Note_on_c,0,71,0\n’, ‘0,30545,Note_on_c,0,69,0\n’, ‘0,84562,Note_on_c,0,71,0\n’, ‘0,95615,Note_on_c,0,71,0\n’, ‘0,43861,Note_on_c,0,69,0\n’, ‘0,77964,Note_on_c,0,71,0\n’, ‘0,17902,Note_on_c,0,76,0\n’, ‘0,66994,Note_on_c,0,71,0\n’, ‘0,37454,Note_on_c,0,69,0\n’, ‘0,11819,Note_on_c,0,76,0\n’, ‘0,89279,Note_on_c,0,71,0\n’, ‘0,59200,Note_on_c,0,71,0\n’, ‘0,97329,Note_on_c,0,71,0\n’, ‘0,17490,Note_on_c,0,76,0\n’, ‘0,36529,Note_on_c,0,69,0\n’, ‘0,34307,Note_on_c,0,69,0\n’, ‘0,5595,Note_on_c,0,76,0\n’, ‘0,62770,Note_on_c,0,71,0\n’, ‘0,73749,Note_on_c,0,71,0\n’, ‘0,44725,Note_on_c,0,69,0\n’, ‘0,15004,Note_on_c,0,76,0\n’, ‘0,68803,Note_on_c,0,71,0\n’, ‘0,11505,Note_on_c,0,76,0\n’, ‘0,4002,Note_on_c,0,45,0\n’, ‘0,80780,Note_on_c,0,71,0\n’, ‘0,95328,Note_on_c,0,71,0\n’, ‘0,83962,Note_on_c,0,71,0\n’, ‘0,48537,Note_on_c,0,69,0\n’, ‘0,77138,Note_on_c,0,71,0\n’, ‘0,31853,Note_on_c,0,69,0\n’, ‘0,90113,Note_on_c,0,71,0\n’, ‘0,69380,Note_on_c,0,71,0\n’, ‘0,74028,Note_on_c,0,71,0\n’, ‘0,45663,Note_on_c,0,69,0\n’, ‘0,46616,Note_on_c,0,69,0\n’, ‘0,6928,Note_on_c,0,76,0\n’, ‘0,34454,Note_on_c,0,69,0\n’, ‘0,96801,Note_on_c,0,71,0\n’, ‘0,81646,Note_on_c,0,71,0\n’, ‘0,52553,Note_on_c,0,71,0\n’, ‘0,70235,Note_on_c,0,71,0\n’, ‘0,41686,Note_on_c,0,69,0\n’, ‘0,68898,Note_on_c,0,71,0\n’, ‘0,70821,Note_on_c,0,71,0\n’, ‘0,12055,Note_on_c,0,76,0\n’, ‘0,1449,Note_on_c,0,76,0\n’, ‘0,87695,Note_on_c,0,71,0\n’, ‘0,27756,Note_on_c,0,69,0\n’, ‘0,51932,Note_on_c,0,71,0\n’, ‘0,97681,Note_on_c,0,71,0\n’, ‘0,80963,Note_on_c,0,71,0\n’, ‘0,14060,Note_on_c,0,76,0\n’, ‘0,88327,Note_on_c,0,71,0\n’, ‘0,13665,Note_on_c,0,76,0\n’, ‘0,83086,Note_on_c,0,71,0\n’, ‘0,17316,Note_on_c,0,76,0\n’, ‘0,35051,Note_on_c,0,69,0\n’, ‘0,79219,Note_on_c,0,71,0\n’, ‘0,79145,Note_on_c,0,71,0\n’, ‘0,98274,Note_on_c,0,71,0\n’, ‘0,35093,Note_on_c,0,69,0\n’, ‘0,35481,Note_on_c,0,69,0\n’, ‘0,31133,Note_on_c,0,69,0\n’, ‘0,13142,Note_on_c,0,76,0\n’, ‘0,46080,Note_on_c,0,69,0\n’, ‘0,33997,Note_on_c,0,69,0\n’, ‘0,71735,Note_on_c,0,71,0\n’, ‘0,35654,Note_on_c,0,69,0\n’, ‘0,14411,Note_on_c,0,76,0\n’, ‘0,99069,Note_on_c,0,71,0\n’, ‘0,94888,Note_on_c,0,71,0\n’, ‘0,35800,Note_on_c,0,69,0\n’, ‘0,84794,Note_on_c,0,71,0\n’, ‘0,80794,Note_on_c,0,71,0\n’, ‘0,36593,Note_on_c,0,69,0\n’, ‘0,14204,Note_on_c,0,76,0\n’, ‘0,45877,Note_on_c,0,69,0\n’, ‘0,51251,Note_on_c,0,71,0\n’, ‘0,42064,Note_on_c,0,69,0\n’, ‘0,68342,Note_on_c,0,71,0\n’, ‘0,64557,Note_on_c,0,71,0\n’, ‘0,55571,Note_on_c,0,71,0\n’, ‘0,31770,Note_on_c,0,69,0\n’, ‘0,52104,Note_on_c,0,71,0\n’, ‘0,20319,Note_on_c,0,76,0\n’, ‘0,55832,Note_on_c,0,71,0\n’, ‘0,81324,Note_on_c,0,71,0\n’, ‘0,11456,Note_on_c,0,76,0\n’, ‘0,81809,Note_on_c,0,71,0\n’, ‘0,2941,Note_on_c,0,45,0\n’, ‘0,88430,Note_on_c,0,71,0\n’, ‘0,21549,Note_on_c,0,76,0\n’, ‘0,74537,Note_on_c,0,71,0\n’, ‘0,43997,Note_on_c,0,69,0\n’, ‘0,97417,Note_on_c,0,71,0\n’, ‘0,65711,Note_on_c,0,71,0\n’, ‘0,10330,Note_on_c,0,76,0\n’, ‘0,12926,Note_on_c,0,76,0\n’, ‘0,67930,Note_on_c,0,71,0\n’, ‘0,71582,Note_on_c,0,71,0\n’, ‘0,9194,Note_on_c,0,76,0\n’, ‘0,37550,Note_on_c,0,69,0\n’, ‘0,79945,Note_on_c,0,71,0\n’, ‘0,19326,Note_on_c,0,76,0\n’, ‘0,17033,Note_on_c,0,76,0\n’, ‘0,25840,Note_on_c,0,69,0\n’, ‘0,22855,Note_on_c,0,76,0\n’, ‘0,82381,Note_on_c,0,71,0\n’, ‘0,94280,Note_on_c,0,71,0\n’, ‘0,51355,Note_on_c,0,71,0\n’, ‘0,34104,Note_on_c,0,69,0\n’, ‘0,94984,Note_on_c,0,71,0\n’, ‘0,91821,Note_on_c,0,71,0\n’, ‘0,64858,Note_on_c,0,71,0\n’, ‘0,21709,Note_on_c,0,76,0\n’, ‘0,75395,Note_on_c,0,71,0\n’, ‘0,82874,Note_on_c,0,71,0\n’, ‘0,89671,Note_on_c,0,71,0\n’, ‘0,8945,Note_on_c,0,76,0\n’, ‘0,63900,Note_on_c,0,71,0\n’, ‘0,57795,Note_on_c,0,71,0\n’, ‘0,30457,Note_on_c,0,69,0\n’, ‘0,88842,Note_on_c,0,71,0\n’, ‘0,31498,Note_on_c,0,69,0\n’, ‘0,90157,Note_on_c,0,71,0\n’, ‘0,11215,Note_on_c,0,76,0\n’, ‘0,2788,Note_on_c,0,45,0\n’, ‘0,89771,Note_on_c,0,71,0\n’, ‘0,76450,Note_on_c,0,71,0\n’, ‘0,14997,Note_on_c,0,76,0\n’, ‘0,95323,Note_on_c,0,71,0\n’, ‘0,32751,Note_on_c,0,69,0\n’, ‘0,38499,Note_on_c,0,69,0\n’, ‘0,37420,Note_on_c,0,69,0\n’, ‘0,73309,Note_on_c,0,71,0\n’, ‘0,63101,Note_on_c,0,71,0\n’, ‘0,68883,Note_on_c,0,71,0\n’, ‘0,22349,Note_on_c,0,76,0\n’, ‘0,88609,Note_on_c,0,71,0\n’, ‘0,73739,Note_on_c,0,71,0\n’, ‘0,97687,Note_on_c,0,71,0\n’, ‘0,38552,Note_on_c,0,69,0\n’, ‘0,73060,Note_on_c,0,71,0\n’, ‘0,69377,Note_on_c,0,71,0\n’, ‘0,31997,Note_on_c,0,69,0\n’, ‘0,14716,Note_on_c,0,76,0\n’, ‘0,31529,Note_on_c,0,69,0\n’, ‘0,61386,Note_on_c,0,71,0\n’, ‘0,99323,Note_on_c,0,71,0\n’, ‘0,29394,Note_on_c,0,69,0\n’, ‘0,61624,Note_on_c,0,71,0\n’, ‘0,237,Note_on_c,0,76,0\n’, ‘0,55786,Note_on_c,0,71,0\n’, ‘0,81008,Note_on_c,0,71,0\n’, ‘0,6595,Note_on_c,0,76,0\n’, ‘0,83730,Note_on_c,0,71,0\n’, ‘0,32296,Note_on_c,0,69,0\n’, ‘0,31013,Note_on_c,0,69,0\n’, ‘0,79618,Note_on_c,0,71,0\n’, ‘0,26162,Note_on_c,0,69,0\n’, ‘0,53221,Note_on_c,0,71,0\n’, ‘0,58753,Note_on_c,0,71,0\n’, ‘0,62332,Note_on_c,0,71,0\n’, ‘0,99146,Note_on_c,0,71,0\n’, ‘0,25811,Note_on_c,0,69,0\n’, ‘0,70643,Note_on_c,0,71,0\n’, ‘0,51850,Note_on_c,0,71,0\n’, ‘0,22953,Note_on_c,0,76,0\n’, ‘0,41852,Note_on_c,0,69,0\n’, ‘0,62522,Note_on_c,0,71,0\n’, ‘0,53516,Note_on_c,0,71,0\n’, ‘0,50683,Note_on_c,0,71,0\n’, ‘0,46533,Note_on_c,0,69,0\n’, ‘0,81388,Note_on_c,0,71,0\n’, ‘0,58679,Note_on_c,0,71,0\n’, ‘0,73005,Note_on_c,0,71,0\n’, ‘0,84332,Note_on_c,0,71,0\n’, ‘0,11857,Note_on_c,0,76,0\n’, ‘0,6021,Note_on_c,0,76,0\n’, ‘0,59557,Note_on_c,0,71,0\n’, ‘0,53811,Note_on_c,0,71,0\n’, ‘0,29961,Note_on_c,0,69,0\n’, ‘0,10663,Note_on_c,0,76,0\n’, ‘0,85671,Note_on_c,0,71,0\n’, ‘0,97142,Note_on_c,0,71,0\n’, ‘0,11300,Note_on_c,0,76,0\n’, ‘0,11542,Note_on_c,0,76,0\n’, ‘0,9045,Note_on_c,0,76,0\n’, ‘0,48538,Note_on_c,0,69,0\n’, ‘0,24162,Note_on_c,0,69,0\n’, ‘0,81738,Note_on_c,0,71,0\n’, ‘0,14050,Note_on_c,0,76,0\n’, ‘0,81555,Note_on_c,0,71,0\n’, ‘0,4299,Note_on_c,0,45,0\n’, ‘0,7052,Note_on_c,0,76,0\n’, ‘0,49090,Note_on_c,0,71,0\n’, ‘0,43104,Note_on_c,0,69,0\n’, ‘0,57237,Note_on_c,0,71,0\n’, ‘0,67543,Note_on_c,0,71,0\n’, ‘0,39484,Note_on_c,0,69,0\n’, ‘0,61393,Note_on_c,0,71,0\n’, ‘0,79087,Note_on_c,0,71,0\n’, ‘0,88450,Note_on_c,0,71,0\n’, ‘0,82165,Note_on_c,0,71,0\n’, ‘0,53137,Note_on_c,0,71,0\n’, ‘0,72127,Note_on_c,0,71,0\n’, ‘0,24583,Note_on_c,0,69,0\n’, ‘0,91085,Note_on_c,0,71,0\n’, ‘0,4801,Note_on_c,0,76,0\n’, ‘0,35906,Note_on_c,0,69,0\n’, ‘0,28511,Note_on_c,0,69,0\n’, ‘0,50407,Note_on_c,0,71,0\n’, ‘0,8177,Note_on_c,0,76,0\n’, ‘0,39223,Note_on_c,0,69,0\n’, ‘0,13299,Note_on_c,0,76,0\n’, ‘0,99216,Note_on_c,0,71,0\n’, ‘0,6420,Note_on_c,0,76,0\n’, ‘0,47513,Note_on_c,0,69,0\n’, ‘0,53998,Note_on_c,0,71,0\n’, ‘0,88120,Note_on_c,0,71,0\n’, ‘0,14881,Note_on_c,0,76,0\n’, ‘0,45652,Note_on_c,0,69,0\n’, ‘0,17613,Note_on_c,0,76,0\n’, ‘0,34539,Note_on_c,0,69,0\n’, ‘0,57096,Note_on_c,0,71,0\n’, ‘0,88628,Note_on_c,0,71,0\n’, ‘0,11857,Note_on_c,0,76,0\n’, ‘0,2251,Note_on_c,0,45,0\n’, ‘0,57162,Note_on_c,0,71,0\n’, ‘0,82211,Note_on_c,0,71,0\n’, ‘0,69332,Note_on_c,0,71,0\n’, ‘0,21717,Note_on_c,0,76,0\n’, ‘0,11225,Note_on_c,0,76,0\n’, ‘0,97840,Note_on_c,0,71,0\n’, ‘0,39638,Note_on_c,0,69,0\n’, ‘0,44028,Note_on_c,0,69,0\n’, ‘0,65029,Note_on_c,0,71,0\n’, ‘0,40572,Note_on_c,0,69,0\n’, ‘0,18756,Note_on_c,0,76,0\n’, ‘0,7484,Note_on_c,0,76,0\n’, ‘0,36234,Note_on_c,0,69,0\n’, ‘0,65083,Note_on_c,0,71,0\n’, ‘0,53130,Note_on_c,0,71,0\n’, ‘0,29072,Note_on_c,0,69,0\n’, ‘0,38957,Note_on_c,0,69,0\n’, ‘0,36229,Note_on_c,0,69,0\n’, ‘0,6100,Note_on_c,0,76,0\n’, ‘0,74352,Note_on_c,0,71,0\n’, ‘0,45192,Note_on_c,0,69,0\n’, ‘0,76138,Note_on_c,0,71,0\n’, ‘0,3090,Note_on_c,0,45,0\n’, ‘0,1508,Note_on_c,0,76,0\n’, ‘0,44117,Note_on_c,0,69,0\n’, ‘0,1477,Note_on_c,0,76,0\n’, ‘0,82480,Note_on_c,0,71,0\n’, ‘0,16264,Note_on_c,0,76,0\n’, ‘0,18653,Note_on_c,0,76,0\n’, ‘0,79423,Note_on_c,0,71,0\n’, ‘0,83371,Note_on_c,0,71,0\n’, ‘0,63583,Note_on_c,0,71,0\n’, ‘0,96877,Note_on_c,0,71,0\n’, ‘0,11656,Note_on_c,0,76,0\n’, ‘0,34735,Note_on_c,0,69,0\n’, ‘0,49072,Note_on_c,0,71,0\n’, ‘0,49877,Note_on_c,0,71,0\n’, ‘0,13346,Note_on_c,0,76,0\n’, ‘0,80619,Note_on_c,0,71,0\n’, ‘0,42068,Note_on_c,0,69,0\n’, ‘0,39842,Note_on_c,0,69,0\n’, ‘0,43735,Note_on_c,0,69,0\n’, ‘0,22025,Note_on_c,0,76,0\n’, ‘0,42091,Note_on_c,0,69,0\n’, ‘0,24441,Note_on_c,0,69,0\n’, ‘0,31566,Note_on_c,0,69,0\n’, ‘0,29019,Note_on_c,0,69,0\n’, ‘0,22108,Note_on_c,0,76,0\n’, ‘0,53640,Note_on_c,0,71,0\n’, ‘0,74104,Note_on_c,0,71,0\n’, ‘0,28475,Note_on_c,0,69,0\n’, ‘0,42988,Note_on_c,0,69,0\n’, ‘0,60652,Note_on_c,0,71,0\n’, ‘0,76349,Note_on_c,0,71,0\n’, ‘0,32325,Note_on_c,0,69,0\n’, ‘0,96816,Note_on_c,0,71,0\n’, ‘0,93984,Note_on_c,0,71,0\n’, ‘0,46317,Note_on_c,0,69,0\n’, ‘0,51874,Note_on_c,0,71,0\n’, ‘0,94637,Note_on_c,0,71,0\n’, ‘0,38361,Note_on_c,0,69,0\n’, ‘0,12966,Note_on_c,0,76,0\n’, ‘0,33015,Note_on_c,0,69,0\n’, ‘0,97648,Note_on_c,0,71,0\n’, ‘0,60181,Note_on_c,0,71,0\n’, ‘0,82987,Note_on_c,0,71,0\n’, ‘0,20476,Note_on_c,0,76,0\n’, ‘0,96154,Note_on_c,0,71,0\n’, ‘0,95765,Note_on_c,0,71,0\n’, ‘0,13898,Note_on_c,0,76,0\n’, ‘0,10502,Note_on_c,0,76,0\n’, ‘0,4575,Note_on_c,0,76,0\n’, ‘0,39502,Note_on_c,0,69,0\n’, ‘0,53789,Note_on_c,0,71,0\n’, ‘0,47154,Note_on_c,0,69,0\n’, ‘0,86351,Note_on_c,0,71,0\n’, ‘0,13097,Note_on_c,0,76,0\n’, ‘0,73382,Note_on_c,0,71,0\n’, ‘0,87349,Note_on_c,0,71,0\n’, ‘0,11706,Note_on_c,0,76,0\n’, ‘0,30159,Note_on_c,0,69,0\n’, ‘0,66358,Note_on_c,0,71,0\n’, ‘0,67990,Note_on_c,0,71,0\n’, ‘0,25814,Note_on_c,0,69,0\n’, ‘0,505,Note_on_c,0,76,0\n’, ‘0,24916,Note_on_c,0,69,0\n’, ‘0,92363,Note_on_c,0,71,0\n’, ‘0,31220,Note_on_c,0,69,0\n’, ‘0,1115,Note_on_c,0,76,0\n’, ‘0,65424,Note_on_c,0,71,0\n’, ‘0,64314,Note_on_c,0,71,0\n’, ‘0,51980,Note_on_c,0,71,0\n’, ‘0,33854,Note_on_c,0,69,0\n’, ‘0,28866,Note_on_c,0,69,0\n’, ‘0,77768,Note_on_c,0,71,0\n’, ‘0,75531,Note_on_c,0,71,0\n’, ‘0,44687,Note_on_c,0,69,0\n’, ‘0,93722,Note_on_c,0,71,0\n’, ‘0,60834,Note_on_c,0,71,0\n’, ‘0,62541,Note_on_c,0,71,0\n’, ‘0,25378,Note_on_c,0,69,0\n’, ‘0,76014,Note_on_c,0,71,0\n’, ‘0,38920,Note_on_c,0,69,0\n’, ‘0,93461,Note_on_c,0,71,0\n’, ‘0,78108,Note_on_c,0,71,0\n’, ‘0,39503,Note_on_c,0,69,0\n’, ‘0,87502,Note_on_c,0,71,0\n’, ‘0,52491,Note_on_c,0,71,0\n’, ‘0,17932,Note_on_c,0,76,0\n’, ‘0,41569,Note_on_c,0,69,0\n’, ‘0,32121,Note_on_c,0,69,0\n’, ‘0,16866,Note_on_c,0,76,0\n’, ‘0,30145,Note_on_c,0,69,0\n’, ‘0,89481,Note_on_c,0,71,0\n’, ‘0,86536,Note_on_c,0,71,0\n’, ‘0,28434,Note_on_c,0,69,0\n’, ‘0,95076,Note_on_c,0,71,0\n’, ‘0,38463,Note_on_c,0,69,0\n’, ‘0,38127,Note_on_c,0,69,0\n’, ‘0,46597,Note_on_c,0,69,0\n’, ‘0,68346,Note_on_c,0,71,0\n’, ‘0,77787,Note_on_c,0,71,0\n’, ‘0,74161,Note_on_c,0,71,0\n’, ‘0,4645,Note_on_c,0,76,0\n’, ‘0,25850,Note_on_c,0,69,0\n’, ‘0,54291,Note_on_c,0,71,0\n’, ‘0,47017,Note_on_c,0,69,0\n’, ‘0,2718,Note_on_c,0,45,0\n’, ‘0,45995,Note_on_c,0,69,0\n’, ‘0,38578,Note_on_c,0,69,0\n’, ‘0,23904,Note_on_c,0,76,0\n’, ‘0,69056,Note_on_c,0,71,0\n’, ‘0,91882,Note_on_c,0,71,0\n’, ‘0,3546,Note_on_c,0,45,0\n’, ‘0,79645,Note_on_c,0,71,0\n’, ‘0,29593,Note_on_c,0,69,0\n’, ‘0,70608,Note_on_c,0,71,0\n’, ‘0,17272,Note_on_c,0,76,0\n’, ‘0,69305,Note_on_c,0,71,0\n’, ‘0,94654,Note_on_c,0,71,0\n’, ‘0,54353,Note_on_c,0,71,0\n’, ‘0,97340,Note_on_c,0,71,0\n’, ‘0,33451,Note_on_c,0,69,0\n’, ‘0,10000,Note_on_c,0,76,0\n’, ‘0,28001,Note_on_c,0,69,0\n’, ‘0,7296,Note_on_c,0,76,0\n’, ‘0,39488,Note_on_c,0,69,0\n’, ‘0,4287,Note_on_c,0,45,0\n’, ‘0,81858,Note_on_c,0,71,0\n’, ‘0,32215,Note_on_c,0,69,0\n’, ‘0,69812,Note_on_c,0,71,0\n’, ‘0,65789,Note_on_c,0,71,0\n’, ‘0,53541,Note_on_c,0,71,0\n’, ‘0,48585,Note_on_c,0,69,0\n’, ‘0,74148,Note_on_c,0,71,0\n’, ‘0,21546,Note_on_c,0,76,0\n’, ‘0,66180,Note_on_c,0,71,0\n’, ‘0,9157,Note_on_c,0,76,0\n’, ‘0,65995,Note_on_c,0,71,0\n’, ‘0,38325,Note_on_c,0,69,0\n’, ‘0,3759,Note_on_c,0,45,0\n’, ‘0,69997,Note_on_c,0,71,0\n’, ‘0,27179,Note_on_c,0,69,0\n’, ‘0,91202,Note_on_c,0,71,0\n’, ‘0,73204,Note_on_c,0,71,0\n’, ‘0,84169,Note_on_c,0,71,0\n’, ‘0,737,Note_on_c,0,76,0\n’, ‘0,31518,Note_on_c,0,69,0\n’, ‘0,99182,Note_on_c,0,71,0\n’, ‘0,99283,Note_on_c,0,71,0\n’, ‘0,21925,Note_on_c,0,76,0\n’, ‘0,76633,Note_on_c,0,71,0\n’, ‘0,92543,Note_on_c,0,71,0\n’, ‘0,23145,Note_on_c,0,76,0\n’, ‘0,98570,Note_on_c,0,71,0\n’, ‘0,24658,Note_on_c,0,69,0\n’, ‘0,17710,Note_on_c,0,76,0\n’, ‘0,84376,Note_on_c,0,71,0\n’, ‘0,76525,Note_on_c,0,71,0\n’, ‘0,85884,Note_on_c,0,71,0\n’, ‘0,59243,Note_on_c,0,71,0\n’, ‘0,11505,Note_on_c,0,76,0\n’, ‘0,44377,Note_on_c,0,69,0\n’, ‘0,61567,Note_on_c,0,71,0\n’, ‘0,97578,Note_on_c,0,71,0\n’, ‘0,61129,Note_on_c,0,71,0\n’, ‘0,337,Note_on_c,0,76,0\n’, ‘0,42878,Note_on_c,0,69,0\n’, ‘0,14269,Note_on_c,0,76,0\n’, ‘0,21912,Note_on_c,0,76,0\n’, ‘0,41569,Note_on_c,0,69,0\n’, ‘0,70631,Note_on_c,0,71,0\n’, ‘0,49339,Note_on_c,0,71,0\n’, ‘0,98126,Note_on_c,0,71,0\n’, ‘0,75322,Note_on_c,0,71,0\n’, ‘0,98228,Note_on_c,0,71,0\n’, ‘0,92822,Note_on_c,0,71,0\n’, ‘0,1926,Note_on_c,0,45,0\n’, ‘0,50431,Note_on_c,0,71,0\n’, ‘0,62344,Note_on_c,0,71,0\n’, ‘0,83587,Note_on_c,0,71,0\n’, ‘0,33343,Note_on_c,0,69,0\n’, ‘0,37541,Note_on_c,0,69,0\n’, ‘0,13212,Note_on_c,0,76,0\n’, ‘0,88816,Note_on_c,0,71,0\n’, ‘0,95601,Note_on_c,0,71,0\n’, ‘0,40940,Note_on_c,0,69,0\n’, ‘0,46523,Note_on_c,0,69,0\n’, ‘0,43380,Note_on_c,0,69,0\n’, ‘0,50176,Note_on_c,0,71,0\n’, ‘0,23911,Note_on_c,0,76,0\n’, ‘0,89631,Note_on_c,0,71,0\n’, ‘0,97674,Note_on_c,0,71,0\n’, ‘0,1618,Note_on_c,0,45,0\n’, ‘0,97968,Note_on_c,0,71,0\n’, ‘0,6114,Note_on_c,0,76,0\n’, ‘0,98815,Note_on_c,0,71,0\n’, ‘0,80774,Note_on_c,0,71,0\n’, ‘0,46716,Note_on_c,0,69,0\n’, ‘0,34677,Note_on_c,0,69,0\n’, ‘0,73055,Note_on_c,0,71,0\n’, ‘0,52824,Note_on_c,0,71,0\n’, ‘0,90186,Note_on_c,0,71,0\n’, ‘0,54061,Note_on_c,0,71,0\n’, ‘0,28310,Note_on_c,0,69,0\n’, ‘0,93795,Note_on_c,0,71,0\n’, ‘0,19609,Note_on_c,0,76,0\n’, ‘0,40607,Note_on_c,0,69,0\n’, ‘0,11922,Note_on_c,0,76,0\n’, ‘0,25810,Note_on_c,0,69,0\n’, ‘0,24936,Note_on_c,0,69,0\n’, ‘0,85966,Note_on_c,0,71,0\n’, ‘0,29610,Note_on_c,0,69,0\n’, ‘0,47152,Note_on_c,0,69,0\n’, ‘0,14433,Note_on_c,0,76,0\n’, ‘0,64247,Note_on_c,0,71,0\n’, ‘0,6871,Note_on_c,0,76,0\n’, ‘0,66845,Note_on_c,0,71,0\n’, ‘0,93084,Note_on_c,0,71,0\n’, ‘0,45504,Note_on_c,0,69,0\n’, ‘0,7738,Note_on_c,0,76,0\n’, ‘0,68665,Note_on_c,0,71,0\n’, ‘0,24278,Note_on_c,0,69,0\n’, ‘0,8021,Note_on_c,0,76,0\n’, ‘0,39756,Note_on_c,0,69,0\n’, ‘0,51428,Note_on_c,0,71,0\n’, ‘0,85617,Note_on_c,0,71,0\n’, ‘0,90722,Note_on_c,0,71,0\n’, ‘0,77449,Note_on_c,0,71,0\n’, ‘0,25066,Note_on_c,0,69,0\n’, ‘0,57218,Note_on_c,0,71,0\n’, ‘0,48129,Note_on_c,0,69,0\n’, ‘0,70690,Note_on_c,0,71,0\n’, ‘0,79467,Note_on_c,0,71,0\n’, ‘0,62570,Note_on_c,0,71,0\n’, ‘0,16452,Note_on_c,0,76,0\n’, ‘0,71585,Note_on_c,0,71,0\n’, ‘0,27217,Note_on_c,0,69,0\n’, ‘0,11327,Note_on_c,0,76,0\n’, ‘0,69337,Note_on_c,0,71,0\n’, ‘0,80740,Note_on_c,0,71,0\n’, ‘0,57732,Note_on_c,0,71,0\n’, ‘0,76232,Note_on_c,0,71,0\n’, ‘0,67548,Note_on_c,0,71,0\n’, ‘0,80093,Note_on_c,0,71,0\n’, ‘0,13195,Note_on_c,0,76,0\n’, ‘0,80365,Note_on_c,0,71,0\n’, ‘0,3383,Note_on_c,0,45,0\n’, ‘0,57000,Note_on_c,0,71,0\n’, ‘0,63191,Note_on_c,0,71,0\n’, ‘0,88462,Note_on_c,0,71,0\n’, ‘0,92797,Note_on_c,0,71,0\n’, ‘0,35962,Note_on_c,0,69,0\n’, ‘0,54851,Note_on_c,0,71,0\n’, ‘0,79149,Note_on_c,0,71,0\n’, ‘0,69752,Note_on_c,0,71,0\n’, ‘0,64603,Note_on_c,0,71,0\n’, ‘0,86882,Note_on_c,0,71,0\n’, ‘0,88865,Note_on_c,0,71,0\n’, ‘0,98655,Note_on_c,0,71,0\n’, ‘0,83445,Note_on_c,0,71,0\n’, ‘0,4645,Note_on_c,0,76,0\n’, ‘0,54337,Note_on_c,0,71,0\n’, ‘0,40516,Note_on_c,0,69,0\n’, ‘0,59416,Note_on_c,0,71,0\n’, ‘0,80063,Note_on_c,0,71,0\n’, ‘0,41635,Note_on_c,0,69,0\n’, ‘0,2739,Note_on_c,0,45,0\n’, ‘0,50885,Note_on_c,0,71,0\n’, ‘0,55895,Note_on_c,0,71,0\n’, ‘0,15747,Note_on_c,0,76,0\n’, ‘0,44934,Note_on_c,0,69,0\n’, ‘0,56346,Note_on_c,0,71,0\n’, ‘0,40194,Note_on_c,0,69,0\n’, ‘0,55081,Note_on_c,0,71,0\n’, ‘0,24092,Note_on_c,0,69,0\n’, ‘0,49166,Note_on_c,0,71,0\n’, ‘0,56010,Note_on_c,0,71,0\n’, ‘0,31703,Note_on_c,0,69,0\n’, ‘0,34442,Note_on_c,0,69,0\n’, ‘0,20895,Note_on_c,0,76,0\n’, ‘0,24080,Note_on_c,0,69,0\n’, ‘0,60344,Note_on_c,0,71,0\n’, ‘0,50599,Note_on_c,0,71,0\n’, ‘0,41717,Note_on_c,0,69,0\n’, ‘0,50307,Note_on_c,0,71,0\n’, ‘0,89438,Note_on_c,0,71,0\n’, ‘0,56751,Note_on_c,0,71,0\n’, ‘0,37457,Note_on_c,0,69,0\n’, ‘0,29375,Note_on_c,0,69,0\n’, ‘0,14710,Note_on_c,0,76,0\n’, ‘0,97913,Note_on_c,0,71,0\n’, ‘0,98360,Note_on_c,0,71,0\n’, ‘0,97911,Note_on_c,0,71,0\n’, ‘0,24918,Note_on_c,0,69,0\n’, ‘0,72184,Note_on_c,0,71,0\n’, ‘0,61984,Note_on_c,0,71,0\n’, ‘0,45369,Note_on_c,0,69,0\n’, ‘0,14247,Note_on_c,0,76,0\n’, ‘0,76788,Note_on_c,0,71,0\n’, ‘0,27399,Note_on_c,0,69,0\n’, ‘0,59691,Note_on_c,0,71,0\n’, ‘0,60787,Note_on_c,0,71,0\n’, ‘0,61930,Note_on_c,0,71,0\n’, ‘0,69644,Note_on_c,0,71,0\n’, ‘0,2350,Note_on_c,0,45,0\n’, ‘0,12307,Note_on_c,0,76,0\n’, ‘0,58683,Note_on_c,0,71,0\n’, ‘0,35884,Note_on_c,0,69,0\n’, ‘0,497,Note_on_c,0,76,0\n’, ‘0,52667,Note_on_c,0,71,0\n’, ‘0,37004,Note_on_c,0,69,0\n’, ‘0,82665,Note_on_c,0,71,0\n’, ‘0,65957,Note_on_c,0,71,0\n’, ‘0,93520,Note_on_c,0,71,0\n’, ‘0,54137,Note_on_c,0,71,0\n’, ‘0,6063,Note_on_c,0,76,0\n’, ‘0,87811,Note_on_c,0,71,0\n’, ‘0,59666,Note_on_c,0,71,0\n’, ‘0,77944,Note_on_c,0,71,0\n’, ‘0,66365,Note_on_c,0,71,0\n’, ‘0,1223,Note_on_c,0,76,0\n’, ‘0,9953,Note_on_c,0,76,0\n’, ‘0,50721,Note_on_c,0,71,0\n’, ‘0,54134,Note_on_c,0,71,0\n’, ‘0,54432,Note_on_c,0,71,0\n’, ‘0,47844,Note_on_c,0,69,0\n’, ‘0,89078,Note_on_c,0,71,0\n’, ‘0,69158,Note_on_c,0,71,0\n’, ‘0,25310,Note_on_c,0,69,0\n’, ‘0,76790,Note_on_c,0,71,0\n’, ‘0,3686,Note_on_c,0,45,0\n’, ‘0,5810,Note_on_c,0,76,0\n’, ‘0,67964,Note_on_c,0,71,0\n’, ‘0,53873,Note_on_c,0,71,0\n’, ‘0,58103,Note_on_c,0,71,0\n’, ‘0,72668,Note_on_c,0,71,0\n’, ‘0,26686,Note_on_c,0,69,0\n’, ‘0,47598,Note_on_c,0,69,0\n’, ‘0,7970,Note_on_c,0,76,0\n’, ‘0,78903,Note_on_c,0,71,0\n’, ‘0,64645,Note_on_c,0,71,0\n’, ‘0,56711,Note_on_c,0,71,0\n’, ‘0,65891,Note_on_c,0,71,0\n’, ‘0,29111,Note_on_c,0,69,0\n’, ‘0,38229,Note_on_c,0,69,0\n’, ‘0,63654,Note_on_c,0,71,0\n’, ‘0,7776,Note_on_c,0,76,0\n’, ‘0,55968,Note_on_c,0,71,0\n’, ‘0,31056,Note_on_c,0,69,0\n’, ‘0,57250,Note_on_c,0,71,0\n’, ‘0,21783,Note_on_c,0,76,0\n’, ‘0,42276,Note_on_c,0,69,0\n’, ‘0,92727,Note_on_c,0,71,0\n’, ‘0,94499,Note_on_c,0,71,0\n’, ‘0,23061,Note_on_c,0,76,0\n’, ‘0,75039,Note_on_c,0,71,0\n’, ‘0,55928,Note_on_c,0,71,0\n’, ‘0,32145,Note_on_c,0,69,0\n’, ‘0,35107,Note_on_c,0,69,0\n’, ‘0,77466,Note_on_c,0,71,0\n’, ‘0,67684,Note_on_c,0,71,0\n’, ‘0,39156,Note_on_c,0,69,0\n’, ‘0,64239,Note_on_c,0,71,0\n’, ‘0,4090,Note_on_c,0,45,0\n’, ‘0,62451,Note_on_c,0,71,0\n’, ‘0,32730,Note_on_c,0,69,0\n’, ‘0,22680,Note_on_c,0,76,0\n’, ‘0,51300,Note_on_c,0,71,0\n’, ‘0,738,Note_on_c,0,76,0\n’, ‘0,79397,Note_on_c,0,71,0\n’, ‘0,43707,Note_on_c,0,69,0\n’, ‘0,81677,Note_on_c,0,71,0\n’, ‘0,78149,Note_on_c,0,71,0\n’, ‘0,20714,Note_on_c,0,76,0\n’, ‘0,99053,Note_on_c,0,71,0\n’, ‘0,63175,Note_on_c,0,71,0\n’, ‘0,77129,Note_on_c,0,71,0\n’, ‘0,6423,Note_on_c,0,76,0\n’, ‘0,2631,Note_on_c,0,45,0\n’, ‘0,25744,Note_on_c,0,69,0\n’, ‘0,99766,Note_on_c,0,71,0\n’, ‘0,61527,Note_on_c,0,71,0\n’, ‘0,16094,Note_on_c,0,76,0\n’, ‘0,59409,Note_on_c,0,71,0\n’, ‘0,72069,Note_on_c,0,71,0\n’, ‘0,96649,Note_on_c,0,71,0\n’, ‘0,75683,Note_on_c,0,71,0\n’, ‘0,82533,Note_on_c,0,71,0\n’, ‘0,99805,Note_on_c,0,71,0\n’, ‘0,44023,Note_on_c,0,69,0\n’, ‘0,68946,Note_on_c,0,71,0\n’, ‘0,23524,Note_on_c,0,76,0\n’, ‘0,29494,Note_on_c,0,69,0\n’, ‘0,42628,Note_on_c,0,69,0\n’, ‘0,72373,Note_on_c,0,71,0\n’, ‘0,37575,Note_on_c,0,69,0\n’, ‘0,20226,Note_on_c,0,76,0\n’, ‘0,97743,Note_on_c,0,71,0\n’, ‘0,86723,Note_on_c,0,71,0\n’, ‘0,36264,Note_on_c,0,69,0\n’, ‘0,97896,Note_on_c,0,71,0\n’, ‘0,94236,Note_on_c,0,71,0\n’, ‘0,63378,Note_on_c,0,71,0\n’, ‘0,55864,Note_on_c,0,71,0\n’, ‘0,9589,Note_on_c,0,76,0\n’, ‘0,76496,Note_on_c,0,71,0\n’, ‘0,1618,Note_on_c,0,45,0\n’, ‘0,16429,Note_on_c,0,76,0\n’, ‘0,52773,Note_on_c,0,71,0\n’, ‘0,900,Note_on_c,0,76,0\n’, ‘0,65930,Note_on_c,0,71,0\n’, ‘0,3024,Note_on_c,0,45,0\n’, ‘0,57490,Note_on_c,0,71,0\n’, ‘0,21988,Note_on_c,0,76,0\n’, ‘0,15695,Note_on_c,0,76,0\n’, ‘0,43583,Note_on_c,0,69,0\n’, ‘0,94690,Note_on_c,0,71,0\n’, ‘0,77169,Note_on_c,0,71,0\n’, ‘0,43486,Note_on_c,0,69,0\n’, ‘0,80060,Note_on_c,0,71,0\n’, ‘0,7362,Note_on_c,0,76,0\n’, ‘0,82023,Note_on_c,0,71,0\n’, ‘0,18542,Note_on_c,0,76,0\n’, ‘0,48982,Note_on_c,0,71,0\n’, ‘0,60939,Note_on_c,0,71,0\n’, ‘0,27285,Note_on_c,0,69,0\n’, ‘0,16133,Note_on_c,0,76,0\n’, ‘0,53622,Note_on_c,0,71,0\n’, ‘0,22428,Note_on_c,0,76,0\n’, ‘0,47342,Note_on_c,0,69,0\n’, ‘0,99386,Note_on_c,0,71,0\n’, ‘0,23142,Note_on_c,0,76,0\n’, ‘0,54343,Note_on_c,0,71,0\n’, ‘0,56185,Note_on_c,0,71,0\n’, ‘0,30830,Note_on_c,0,69,0\n’, ‘0,22537,Note_on_c,0,76,0\n’, ‘0,40628,Note_on_c,0,69,0\n’, ‘0,14069,Note_on_c,0,76,0\n’, ‘0,24785,Note_on_c,0,69,0\n’, ‘0,22175,Note_on_c,0,76,0\n’, ‘0,42515,Note_on_c,0,69,0\n’, ‘0,84239,Note_on_c,0,71,0\n’, ‘0,10141,Note_on_c,0,76,0\n’, ‘0,97474,Note_on_c,0,71,0\n’, ‘0,1655,Note_on_c,0,45,0\n’, ‘0,76806,Note_on_c,0,71,0\n’, ‘0,73775,Note_on_c,0,71,0\n’, ‘0,43782,Note_on_c,0,69,0\n’, ‘0,65597,Note_on_c,0,71,0\n’, ‘0,62164,Note_on_c,0,71,0\n’, ‘0,11751,Note_on_c,0,76,0\n’, ‘0,20781,Note_on_c,0,76,0\n’, ‘0,96796,Note_on_c,0,71,0\n’, ‘0,50405,Note_on_c,0,71,0\n’, ‘0,98262,Note_on_c,0,71,0\n’, ‘0,36974,Note_on_c,0,69,0\n’, ‘0,87757,Note_on_c,0,71,0\n’, ‘0,97037,Note_on_c,0,71,0\n’, ‘0,40154,Note_on_c,0,69,0\n’, ‘0,8875,Note_on_c,0,76,0\n’, ‘0,39880,Note_on_c,0,69,0\n’, ‘0,97279,Note_on_c,0,71,0\n’, ‘0,45817,Note_on_c,0,69,0\n’, ‘0,96038,Note_on_c,0,71,0\n’, ‘0,45936,Note_on_c,0,69,0\n’, ‘0,30335,Note_on_c,0,69,0\n’, ‘0,89081,Note_on_c,0,71,0\n’, ‘0,87607,Note_on_c,0,71,0\n’, ‘0,42697,Note_on_c,0,69,0\n’, ‘0,55841,Note_on_c,0,71,0\n’, ‘0,62955,Note_on_c,0,71,0\n’, ‘0,86629,Note_on_c,0,71,0\n’, ‘0,63311,Note_on_c,0,71,0\n’, ‘0,74306,Note_on_c,0,71,0\n’, ‘0,11094,Note_on_c,0,76,0\n’, ‘0,11343,Note_on_c,0,76,0\n’, ‘0,16253,Note_on_c,0,76,0\n’, ‘0,34900,Note_on_c,0,69,0\n’, ‘0,18290,Note_on_c,0,76,0\n’, ‘0,94670,Note_on_c,0,71,0\n’, ‘0,13486,Note_on_c,0,76,0\n’, ‘0,56525,Note_on_c,0,71,0\n’, ‘0,94815,Note_on_c,0,71,0\n’, ‘0,81687,Note_on_c,0,71,0\n’, ‘0,21009,Note_on_c,0,76,0\n’, ‘0,42246,Note_on_c,0,69,0\n’, ‘0,32193,Note_on_c,0,69,0\n’, ‘0,89966,Note_on_c,0,71,0\n’, ‘0,9123,Note_on_c,0,76,0\n’, ‘0,9409,Note_on_c,0,76,0\n’, ‘0,44465,Note_on_c,0,69,0\n’, ‘0,51125,Note_on_c,0,71,0\n’, ‘0,67608,Note_on_c,0,71,0\n’, ‘0,62261,Note_on_c,0,71,0\n’, ‘0,43805,Note_on_c,0,69,0\n’, ‘0,588,Note_on_c,0,76,0\n’, ‘0,85821,Note_on_c,0,71,0\n’, ‘0,53974,Note_on_c,0,71,0\n’, ‘0,33751,Note_on_c,0,69,0\n’, ‘0,26628,Note_on_c,0,69,0\n’, ‘0,89158,Note_on_c,0,71,0\n’, ‘0,53009,Note_on_c,0,71,0\n’, ‘0,20338,Note_on_c,0,76,0\n’, ‘0,46973,Note_on_c,0,69,0\n’, ‘0,67474,Note_on_c,0,71,0\n’, ‘0,66263,Note_on_c,0,71,0\n’, ‘0,69470,Note_on_c,0,71,0\n’, ‘0,99923,Note_on_c,0,71,0\n’, ‘0,79264,Note_on_c,0,71,0\n’, ‘0,68411,Note_on_c,0,71,0\n’, ‘0,72464,Note_on_c,0,71,0\n’, ‘0,97461,Note_on_c,0,71,0\n’, ‘0,18298,Note_on_c,0,76,0\n’, ‘0,79707,Note_on_c,0,71,0\n’, ‘0,56984,Note_on_c,0,71,0\n’, ‘0,1937,Note_on_c,0,45,0\n’, ‘0,37887,Note_on_c,0,69,0\n’, ‘0,18295,Note_on_c,0,76,0\n’, ‘0,69936,Note_on_c,0,71,0\n’, ‘0,57353,Note_on_c,0,71,0\n’, ‘0,93527,Note_on_c,0,71,0\n’, ‘0,68223,Note_on_c,0,71,0\n’, ‘0,88844,Note_on_c,0,71,0\n’, ‘0,43437,Note_on_c,0,69,0\n’, ‘0,66405,Note_on_c,0,71,0\n’, ‘0,76710,Note_on_c,0,71,0\n’, ‘0,66177,Note_on_c,0,71,0\n’, ‘0,54204,Note_on_c,0,71,0\n’, ‘0,94271,Note_on_c,0,71,0\n’, ‘0,66860,Note_on_c,0,71,0\n’, ‘0,84761,Note_on_c,0,71,0\n’, ‘0,37797,Note_on_c,0,69,0\n’, ‘0,98481,Note_on_c,0,71,0\n’, ‘0,24597,Note_on_c,0,69,0\n’, ‘0,64560,Note_on_c,0,71,0\n’, ‘0,95350,Note_on_c,0,71,0\n’, ‘0,26202,Note_on_c,0,69,0\n’, ‘0,51983,Note_on_c,0,71,0\n’, ‘0,92676,Note_on_c,0,71,0\n’, ‘0,85849,Note_on_c,0,71,0\n’, ‘0,37399,Note_on_c,0,69,0\n’, ‘0,77449,Note_on_c,0,71,0\n’, ‘0,633,Note_on_c,0,76,0\n’, ‘0,14135,Note_on_c,0,76,0\n’, ‘0,49540,Note_on_c,0,71,0\n’, ‘0,63207,Note_on_c,0,71,0\n’, ‘0,56941,Note_on_c,0,71,0\n’, ‘0,87092,Note_on_c,0,71,0\n’, ‘0,4088,Note_on_c,0,45,0\n’, ‘0,54163,Note_on_c,0,71,0\n’, ‘0,57703,Note_on_c,0,71,0\n’, ‘0,97758,Note_on_c,0,71,0\n’, ‘0,62729,Note_on_c,0,71,0\n’, ‘0,9400,Note_on_c,0,76,0\n’, ‘0,83148,Note_on_c,0,71,0\n’, ‘0,82879,Note_on_c,0,71,0\n’, ‘0,95623,Note_on_c,0,71,0\n’, ‘0,88270,Note_on_c,0,71,0\n’, ‘0,71922,Note_on_c,0,71,0\n’, ‘0,65733,Note_on_c,0,71,0\n’, ‘0,25575,Note_on_c,0,69,0\n’, ‘0,3098,Note_on_c,0,45,0\n’, ‘0,60458,Note_on_c,0,71,0\n’, ‘0,84328,Note_on_c,0,71,0\n’, ‘0,60912,Note_on_c,0,71,0\n’, ‘0,22741,Note_on_c,0,76,0\n’, ‘0,13173,Note_on_c,0,76,0\n’, ‘0,8622,Note_on_c,0,76,0\n’, ‘0,91328,Note_on_c,0,71,0\n’, ‘0,62820,Note_on_c,0,71,0\n’, ‘0,84400,Note_on_c,0,71,0\n’, ‘0,94496,Note_on_c,0,71,0\n’, ‘0,23746,Note_on_c,0,76,0\n’, ‘0,53088,Note_on_c,0,71,0\n’, ‘0,74164,Note_on_c,0,71,0\n’, ‘0,85476,Note_on_c,0,71,0\n’, ‘0,99523,Note_on_c,0,71,0\n’, ‘0,26640,Note_on_c,0,69,0\n’, ‘0,17889,Note_on_c,0,76,0\n’, ‘0,59422,Note_on_c,0,71,0\n’, ‘0,60837,Note_on_c,0,71,0\n’, ‘0,11983,Note_on_c,0,76,0\n’, ‘0,70730,Note_on_c,0,71,0\n’, ‘0,94317,Note_on_c,0,71,0\n’, ‘0,14531,Note_on_c,0,76,0\n’, ‘0,73066,Note_on_c,0,71,0\n’, ‘0,72833,Note_on_c,0,71,0\n’, ‘0,54920,Note_on_c,0,71,0\n’, ‘0,47699,Note_on_c,0,69,0\n’, ‘0,50326,Note_on_c,0,71,0\n’, ‘0,15818,Note_on_c,0,76,0\n’, ‘0,91240,Note_on_c,0,71,0\n’, ‘0,502,Note_on_c,0,76,0\n’, ‘0,45513,Note_on_c,0,69,0\n’, ‘0,7535,Note_on_c,0,76,0\n’, ‘0,32296,Note_on_c,0,69,0\n’, ‘0,84805,Note_on_c,0,71,0\n’, ‘0,8571,Note_on_c,0,76,0\n’, ‘0,67543,Note_on_c,0,71,0\n’, ‘0,74982,Note_on_c,0,71,0\n’, ‘0,75015,Note_on_c,0,71,0\n’, ‘0,65859,Note_on_c,0,71,0\n’, ‘0,72627,Note_on_c,0,71,0\n’, ‘0,61466,Note_on_c,0,71,0\n’, ‘0,8360,Note_on_c,0,76,0\n’, ‘0,9064,Note_on_c,0,76,0\n’, ‘0,1961,Note_on_c,0,45,0\n’, ‘0,28598,Note_on_c,0,69,0\n’, ‘0,91604,Note_on_c,0,71,0\n’, ‘0,49785,Note_on_c,0,71,0\n’, ‘0,12939,Note_on_c,0,76,0\n’, ‘0,64664,Note_on_c,0,71,0\n’, ‘0,87620,Note_on_c,0,71,0\n’, ‘0,2109,Note_on_c,0,45,0\n’, ‘0,53809,Note_on_c,0,71,0\n’, ‘0,37583,Note_on_c,0,69,0\n’, ‘0,10578,Note_on_c,0,76,0\n’, ‘0,79533,Note_on_c,0,71,0\n’, ‘0,26857,Note_on_c,0,69,0\n’, ‘0,86749,Note_on_c,0,71,0\n’, ‘0,23255,Note_on_c,0,76,0\n’, ‘0,39517,Note_on_c,0,69,0\n’, ‘0,27188,Note_on_c,0,69,0\n’, ‘0,56044,Note_on_c,0,71,0\n’, ‘0,34569,Note_on_c,0,69,0\n’, ‘0,73075,Note_on_c,0,71,0\n’, ‘0,57616,Note_on_c,0,71,0\n’, ‘0,72224,Note_on_c,0,71,0\n’, ‘0,41753,Note_on_c,0,69,0\n’, ‘0,45229,Note_on_c,0,69,0\n’, ‘0,60283,Note_on_c,0,71,0\n’, ‘0,78548,Note_on_c,0,71,0\n’, ‘0,80479,Note_on_c,0,71,0\n’, ‘0,24919,Note_on_c,0,69,0\n’, ‘0,34959,Note_on_c,0,69,0\n’, ‘0,94162,Note_on_c,0,71,0\n’, ‘0,66199,Note_on_c,0,71,0\n’, ‘0,12404,Note_on_c,0,76,0\n’, ‘0,73858,Note_on_c,0,71,0\n’, ‘0,48650,Note_on_c,0,71,0\n’, ‘0,41905,Note_on_c,0,69,0\n’, ‘0,19650,Note_on_c,0,76,0\n’, ‘0,74812,Note_on_c,0,71,0\n’, ‘0,12545,Note_on_c,0,76,0\n’, ‘0,26848,Note_on_c,0,69,0\n’, ‘0,62050,Note_on_c,0,71,0\n’, ‘0,98201,Note_on_c,0,71,0\n’, ‘0,69894,Note_on_c,0,71,0\n’, ‘0,67841,Note_on_c,0,71,0\n’, ‘0,50993,Note_on_c,0,71,0\n’, ‘0,84644,Note_on_c,0,71,0\n’, ‘0,52578,Note_on_c,0,71,0\n’, ‘0,76017,Note_on_c,0,71,0\n’, ‘0,46580,Note_on_c,0,69,0\n’, ‘0,6644,Note_on_c,0,76,0\n’, ‘0,9661,Note_on_c,0,76,0\n’, ‘0,95087,Note_on_c,0,71,0\n’, ‘0,22096,Note_on_c,0,76,0\n’, ‘0,20193,Note_on_c,0,76,0\n’, ‘0,83344,Note_on_c,0,71,0\n’, ‘0,54949,Note_on_c,0,71,0\n’, ‘0,25755,Note_on_c,0,69,0\n’, ‘0,50357,Note_on_c,0,71,0\n’, ‘0,97654,Note_on_c,0,71,0\n’, ‘0,39395,Note_on_c,0,69,0\n’, ‘0,61481,Note_on_c,0,71,0\n’, ‘0,45133,Note_on_c,0,69,0\n’, ‘0,6675,Note_on_c,0,76,0\n’, ‘0,19525,Note_on_c,0,76,0\n’, ‘0,23775,Note_on_c,0,76,0\n’, ‘0,82078,Note_on_c,0,71,0\n’, ‘0,12119,Note_on_c,0,76,0\n’, ‘0,39896,Note_on_c,0,69,0\n’, ‘0,99284,Note_on_c,0,71,0\n’, ‘0,87327,Note_on_c,0,71,0\n’, ‘0,73902,Note_on_c,0,71,0\n’, ‘0,2731,Note_on_c,0,45,0\n’, ‘0,75533,Note_on_c,0,71,0\n’, ‘0,12588,Note_on_c,0,76,0\n’, ‘0,17047,Note_on_c,0,76,0\n’, ‘0,16569,Note_on_c,0,76,0\n’, ‘0,40556,Note_on_c,0,69,0\n’, ‘0,79709,Note_on_c,0,71,0\n’, ‘0,28801,Note_on_c,0,69,0\n’, ‘0,47983,Note_on_c,0,69,0\n’, ‘0,4566,Note_on_c,0,76,0\n’, ‘0,71636,Note_on_c,0,71,0\n’, ‘0,60793,Note_on_c,0,71,0\n’, ‘0,82880,Note_on_c,0,71,0\n’, ‘0,21590,Note_on_c,0,76,0\n’, ‘0,75335,Note_on_c,0,71,0\n’, ‘0,33679,Note_on_c,0,69,0\n’, ‘0,53055,Note_on_c,0,71,0\n’, ‘0,40554,Note_on_c,0,69,0\n’, ‘0,93496,Note_on_c,0,71,0\n’, ‘0,29671,Note_on_c,0,69,0\n’, ‘0,35423,Note_on_c,0,69,0\n’, ‘0,47966,Note_on_c,0,69,0\n’, ‘0,32507,Note_on_c,0,69,0\n’, ‘0,63769,Note_on_c,0,71,0\n’, ‘0,59519,Note_on_c,0,71,0\n’, ‘0,49717,Note_on_c,0,71,0\n’, ‘0,61581,Note_on_c,0,71,0\n’, ‘0,25251,Note_on_c,0,69,0\n’, ‘0,46313,Note_on_c,0,69,0\n’, ‘0,74690,Note_on_c,0,71,0\n’, ‘0,18048,Note_on_c,0,76,0\n’, ‘0,91568,Note_on_c,0,71,0\n’, ‘0,33235,Note_on_c,0,69,0\n’, ‘0,73162,Note_on_c,0,71,0\n’, ‘0,83453,Note_on_c,0,71,0\n’, ‘0,23457,Note_on_c,0,76,0\n’, ‘0,89640,Note_on_c,0,71,0\n’, ‘0,21861,Note_on_c,0,76,0\n’, ‘0,82494,Note_on_c,0,71,0\n’, ‘0,36196,Note_on_c,0,69,0\n’, ‘0,70588,Note_on_c,0,71,0\n’, ‘0,95748,Note_on_c,0,71,0\n’, ‘0,37146,Note_on_c,0,69,0\n’, ‘0,95377,Note_on_c,0,71,0\n’, ‘0,38755,Note_on_c,0,69,0\n’, ‘0,7616,Note_on_c,0,76,0\n’, ‘0,12809,Note_on_c,0,76,0\n’, ‘0,18871,Note_on_c,0,76,0\n’, ‘0,70547,Note_on_c,0,71,0\n’, ‘0,93282,Note_on_c,0,71,0\n’, ‘0,98588,Note_on_c,0,71,0\n’, ‘0,88319,Note_on_c,0,71,0\n’, ‘0,56459,Note_on_c,0,71,0\n’, ‘0,52766,Note_on_c,0,71,0\n’, ‘0,3169,Note_on_c,0,45,0\n’, ‘0,71260,Note_on_c,0,71,0\n’, ‘0,66450,Note_on_c,0,71,0\n’, ‘0,83012,Note_on_c,0,71,0\n’, ‘0,43815,Note_on_c,0,69,0\n’, ‘0,37207,Note_on_c,0,69,0\n’, ‘0,3016,Note_on_c,0,45,0\n’, ‘0,44719,Note_on_c,0,69,0\n’, ‘0,16879,Note_on_c,0,76,0\n’, ‘0,4016,Note_on_c,0,45,0\n’, ‘0,63445,Note_on_c,0,71,0\n’, ‘0,18569,Note_on_c,0,76,0\n’, ‘0,1702,Note_on_c,0,45,0\n’, ‘0,50132,Note_on_c,0,71,0\n’, ‘0,85175,Note_on_c,0,71,0\n’, ‘0,20639,Note_on_c,0,76,0\n’, ‘0,39710,Note_on_c,0,69,0\n’, ‘0,20967,Note_on_c,0,76,0\n’, ‘0,59266,Note_on_c,0,71,0\n’, ‘0,53981,Note_on_c,0,71,0\n’, ‘0,38064,Note_on_c,0,69,0\n’, ‘0,52526,Note_on_c,0,71,0\n’, ‘0,25131,Note_on_c,0,69,0\n’, ‘0,8132,Note_on_c,0,76,0\n’, ‘0,84033,Note_on_c,0,71,0\n’, ‘0,51157,Note_on_c,0,71,0\n’, ‘0,24974,Note_on_c,0,69,0\n’, ‘0,41612,Note_on_c,0,69,0\n’, ‘0,98782,Note_on_c,0,71,0\n’, ‘0,13964,Note_on_c,0,76,0\n’, ‘0,13329,Note_on_c,0,76,0\n’, ‘0,36904,Note_on_c,0,69,0\n’, ‘0,35901,Note_on_c,0,69,0\n’, ‘0,10909,Note_on_c,0,76,0\n’, ‘0,84557,Note_on_c,0,71,0\n’, ‘0,62048,Note_on_c,0,71,0\n’, ‘0,65806,Note_on_c,0,71,0\n’, ‘0,17686,Note_on_c,0,76,0\n’, ‘0,41313,Note_on_c,0,69,0\n’, ‘0,34144,Note_on_c,0,69,0\n’, ‘0,35557,Note_on_c,0,69,0\n’, ‘0,85760,Note_on_c,0,71,0\n’, ‘0,51743,Note_on_c,0,71,0\n’, ‘0,19311,Note_on_c,0,76,0\n’, ‘0,52813,Note_on_c,0,71,0\n’, ‘0,11629,Note_on_c,0,76,0\n’, ‘0,15714,Note_on_c,0,76,0\n’, ‘0,70296,Note_on_c,0,71,0\n’, ‘0,89048,Note_on_c,0,71,0\n’, ‘0,18521,Note_on_c,0,76,0\n’, ‘0,30661,Note_on_c,0,69,0\n’, ‘0,86093,Note_on_c,0,71,0\n’, ‘0,76463,Note_on_c,0,71,0\n’, ‘0,29344,Note_on_c,0,69,0\n’, ‘0,12080,Note_on_c,0,76,0\n’, ‘0,37836,Note_on_c,0,69,0\n’, ‘0,16982,Note_on_c,0,76,0\n’, ‘0,58569,Note_on_c,0,71,0\n’, ‘0,11335,Note_on_c,0,76,0\n’, ‘0,14252,Note_on_c,0,76,0\n’, ‘0,78713,Note_on_c,0,71,0\n’, ‘0,1557,Note_on_c,0,45,0\n’, ‘0,98353,Note_on_c,0,71,0\n’, ‘0,32040,Note_on_c,0,69,0\n’, ‘0,72397,Note_on_c,0,71,0\n’, ‘0,34943,Note_on_c,0,69,0\n’, ‘0,77207,Note_on_c,0,71,0\n’, ‘0,89637,Note_on_c,0,71,0\n’, ‘0,34386,Note_on_c,0,69,0\n’, ‘0,33759,Note_on_c,0,69,0\n’, ‘0,14203,Note_on_c,0,76,0\n’, ‘0,85017,Note_on_c,0,71,0\n’, ‘0,62890,Note_on_c,0,71,0\n’, ‘0,93492,Note_on_c,0,71,0\n’, ‘0,82288,Note_on_c,0,71,0\n’, ‘0,89421,Note_on_c,0,71,0\n’, ‘0,59628,Note_on_c,0,71,0\n’, ‘0,73083,Note_on_c,0,71,0\n’, ‘0,4800,Note_on_c,0,76,0\n’, ‘0,3306,Note_on_c,0,45,0\n’, ‘0,41540,Note_on_c,0,69,0\n’, ‘0,35760,Note_on_c,0,69,0\n’, ‘0,24725,Note_on_c,0,69,0\n’, ‘0,3282,Note_on_c,0,45,0\n’, ‘0,24757,Note_on_c,0,69,0\n’, ‘0,29845,Note_on_c,0,69,0\n’, ‘0,9096,Note_on_c,0,76,0\n’, ‘0,10562,Note_on_c,0,76,0\n’, ‘0,83503,Note_on_c,0,71,0\n’, ‘0,20158,Note_on_c,0,76,0\n’, ‘0,98224,Note_on_c,0,71,0\n’, ‘0,2652,Note_on_c,0,45,0\n’, ‘0,51721,Note_on_c,0,71,0\n’, ‘0,74633,Note_on_c,0,71,0\n’, ‘0,18482,Note_on_c,0,76,0\n’, ‘0,67146,Note_on_c,0,71,0\n’, ‘0,81125,Note_on_c,0,71,0\n’, ‘0,68858,Note_on_c,0,71,0\n’, ‘0,81379,Note_on_c,0,71,0\n’, ‘0,23217,Note_on_c,0,76,0\n’, ‘0,62925,Note_on_c,0,71,0\n’, ‘0,1534,Note_on_c,0,45,0\n’, ‘0,99107,Note_on_c,0,71,0\n’, ‘0,73345,Note_on_c,0,71,0\n’, ‘0,16646,Note_on_c,0,76,0\n’, ‘0,24858,Note_on_c,0,69,0\n’, ‘0,65660,Note_on_c,0,71,0\n’, ‘0,45479,Note_on_c,0,69,0\n’, ‘0,82640,Note_on_c,0,71,0\n’, ‘0,82111,Note_on_c,0,71,0\n’, ‘0,51308,Note_on_c,0,71,0\n’, ‘0,52759,Note_on_c,0,71,0\n’, ‘0,39870,Note_on_c,0,69,0\n’, ‘0,35077,Note_on_c,0,69,0\n’, ‘0,55163,Note_on_c,0,71,0\n’, ‘0,49371,Note_on_c,0,71,0\n’, ‘0,31401,Note_on_c,0,69,0\n’, ‘0,86237,Note_on_c,0,71,0\n’, ‘0,40083,Note_on_c,0,69,0\n’, ‘0,39197,Note_on_c,0,69,0\n’, ‘0,66283,Note_on_c,0,71,0\n’, ‘0,80786,Note_on_c,0,71,0\n’, ‘0,383,Note_on_c,0,76,0\n’, ‘0,35146,Note_on_c,0,69,0\n’, ‘0,84953,Note_on_c,0,71,0\n’, ‘0,40518,Note_on_c,0,69,0\n’, ‘0,78789,Note_on_c,0,71,0\n’, ‘0,73117,Note_on_c,0,71,0\n’, ‘0,88193,Note_on_c,0,71,0\n’, ‘0,53569,Note_on_c,0,71,0\n’, ‘0,97212,Note_on_c,0,71,0\n’, ‘0,61572,Note_on_c,0,71,0\n’, ‘0,9400,Note_on_c,0,76,0\n’, ‘0,59834,Note_on_c,0,71,0\n’, ‘0,47631,Note_on_c,0,69,0\n’, ‘0,74373,Note_on_c,0,71,0\n’, ‘0,52389,Note_on_c,0,71,0\n’, ‘0,95523,Note_on_c,0,71,0\n’, ‘0,39654,Note_on_c,0,69,0\n’, ‘0,51010,Note_on_c,0,71,0\n’, ‘0,58705,Note_on_c,0,71,0\n’, ‘0,1526,Note_on_c,0,45,0\n’, ‘0,12988,Note_on_c,0,76,0\n’]


# In[109]:


s


# In[110]:


#https://kite.com/python/answers/how-to-parse-a-csv-string-in-python
lines = s.splitlines()
lines


# In[118]:


#mid_object_lines = py_midicsv.csv_to_midi(lines)


# In[119]:


#with open("notlast.mid", "wb") as output_file:
   # midi_writer = pm.FileWriter(output_file)
    #midi_writer.write(mid_object_lines)


# In[ ]:





# In[ ]:





# In[120]:


import py_midicsv as pm


# In[121]:


import os


# In[217]:


#https://pypi.org/project/py-midicsv/
#https://github.com/bburdette/ChordPredictor
#https://music.stackexchange.com/questions/75845/converting-csv-files-to-midi
#https://www.wheelodex.org/projects/py-midicsv/

#csvmidi [-u -v -x -z] complete_csvfile.csv viboger.mid
#https://github.com/bburdette/ChordPredictor
#https://pypi.org/project/py-midicsv/
#https://www.wheelodex.org/projects/py-midicsv/

viboger = py_midicsv.csv_to_midi('complete_csvfile.csv')


# In[ ]:





# In[218]:


viboger


# In[144]:


#IMPORTANT - Add these two rows in csv file 
#0	0	Header	0	0	480
#1	0	Start_track	None	None	None


#https://www.twilio.com/blog/working-with-midi-data-in-python-using-mido
#https://pypi.org/project/MIDIUtil/

# Important - https://github.com/timwedde/py_midicsv


# In[125]:


trying_csvmidi


# In[126]:


#https://github.com/timwedde/py_midicsv
# Save the parsed MIDI file to disk

#https://stackoverflow.com/questions/29718532/how-to-interpret-values-of-parameters-of-midi-file-analysis-especially-the-data

with open("trysongone.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(trying_csvmidi)


# In[ ]:





# In[219]:


#https://github.com/timwedde/py_midicsv
# Save the parsed MIDI file to disk

#https://kite.com/python/answers/how-to-parse-a-csv-string-in-python

#https://stackoverflow.com/questions/29718532/how-to-interpret-values-of-parameters-of-midi-file-analysis-especially-the-data
with open("example_converted.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(viboger)


# In[198]:


#trying_method = py_midicsv.csv_to_midi('csvfindfault.csv')


# In[ ]:


#https://pandas.pydata.org/pandas-docs/version/0.24.2/reference/api/pandas.DataFrame.to_csv.html
#with open('infinitysong.csv') as f:
#    ge = f.read()


# In[ ]:


#ge


# In[ ]:


#lines1 = ge.splitlines()
#lines1


# In[ ]:


#mid_object_lines = py_midicsv.csv_to_midi(lines1)


# In[ ]:





# # Stranger Things

# In[146]:


csv_morbius = py_midicsv.midi_to_csv('songs_demo/song1.mid')


# In[147]:


csv_morbius


# In[148]:


midi_morbius = py_midicsv.csv_to_midi(csv_morbius)


# In[149]:


midi_morbius


# In[150]:


with open("midi_morbius_song.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_morbius)


# In[151]:


csv_bily = py_midicsv.midi_to_csv('songs_demo/song3.mid')


# In[152]:


csv_bily


# In[153]:


midi_bily = py_midicsv.csv_to_midi(csv_bily)


# In[154]:


midi_bily


# In[155]:


pandas_morbius = pd.DataFrame(csv_morbius)


# In[156]:


pandas_morbius


# In[173]:


pandas_morbius.to_csv('csv_morbius.csv', index = True, header = True)


# In[176]:


midi_morbius2 = py_midicsv.csv_to_midi('csv_morbius.csv')


# In[ ]:


with open('csv_morbius.csv') as f:
    s_morbius = f.read()


# In[159]:


s_morbius


# In[ ]:





# In[160]:


with open('csv_morbius.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
         print ', '.join(row)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




