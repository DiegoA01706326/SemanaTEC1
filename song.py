from music21 import note, stream, tempo, pitch
from fractions import Fraction

st = stream.Stream()

do = 'C'
re = 'D'
mi = 'E'
fa = 'F'
sol = 'G'
la = 'A'
si = 'B'
mis = 'E#'
sis = 'B#'

estrofa1 = [do, si, la, si, la, sol, la, sol]
estrofa2 = estrofa1 + [do, do, si, do, si, la, la, si, do, sol, mis, re]
estrofa3 = estrofa2 + [do, do, do, re, mis, fa, mis, re, mis, re, do, sis, do, do, mi, mi]
estrofa4 = estrofa3 + [do, do, do, do, re, mis, fa, mis, re, mis, re, do, sis, do, do]
song = estrofa4

de1 = [3, 3, 1, 1, 1/2, 1/4, 1/4, 3, 3, 3, 1/2, 1/4, 1/4]
de2 = de1 + [2, 1/2, 1/4, 1/4, 3, 1, 1/2, 1/2, 1, 3, 3, 3]
de3 = de2 + [3, 2, 1/2, 1/2, 1, 1, 1/2, 1/4, 1/4, 1, 1, 1, 3, 2, 1/4, 3]
de4 = de3 + [3, 3, 2, 1/2, 1/2, 1, 1, 1/2, 1/4, 1/4, 1, 1, 1, 3, 3]
duratio = de4

oe1 =[6, 5, 5, 5, 5, 5, 5, 5]
oe2 = oe1 + [6, 6, 5, 6, 5, 5, 5, 5, 6, 5, 5, 5]
oe3 = oe2 + [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 4, 5]
oe4 = oe3 + [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5]
octv = oe4

for n in range(len(song)):
  new_note = note.Note(song[n])
  new_note.duration.quarterLength = duratio[n]
  new_note.octave = octv[n]
  st.append(new_note)
  
st.insert(0, tempo.MetronomeMark(number = 180))

st.write('midi', fp ='cancion1.mid')