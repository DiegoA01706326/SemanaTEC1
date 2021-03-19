
"""Song tiene como objetivo generar un stream con la canción Primavera de
Ludovico Einaudi, generando notas con distintos tonos, duraciones
y octavas."""

from music21 import note, stream, tempo

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

"""Notas de cada estrofa"""
estrofa1 = [do, si, la, si, la, sol, la, sol]
estrofa2 = estrofa1 + [do, do, si, do, si, la, la, si, do, sol, mis, re]
estrofa3 = estrofa2 + [do, do, do, re, mis, fa, mis, re, mis,
                       re, do, sis, do, do, mi, mi]
estrofa4 = estrofa3 + [do, do, do, do, re, mis, fa, mis, re,
                       mis, re, do, sis, do, do]
song = estrofa4

"""Duración de cada nota por estrofa"""
duracione1 = [3, 3, 1, 1, 1/2, 1/4, 1/4, 3, 3, 3, 1/2, 1/4, 1/4]
duracione2 = duracione1 + [2, 1/2, 1/4, 1/4, 3, 1, 1/2, 1/2, 1, 3, 3, 3]
duracione3 = duracione2 + [3, 2, 1/2, 1/2, 1, 1, 1/2, 1/4, 1/4, 1, 1, 1,
                           3, 2, 1/4, 3]
duracione4 = duracione3 + [3, 3, 2, 1/2, 1/2, 1, 1, 1/2, 1/4, 1/4, 1, 1,
                           1, 3, 3]
duracion = duracione4

octavae1 = [6, 5, 5, 5, 5, 5, 5, 5]
octavae2 = octavae1 + [6, 6, 5, 6, 5, 5, 5, 5, 6, 5, 5, 5]
octavae3 = octavae2 + [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 4, 5]
octavae4 = octavae3 + [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5]
octavas = octavae4

"""Creación de cada nota o silencio con sus respectivas duraciones y octavas"""
for n in range(len(song)):
    new_note = note.Note(song[n])
    new_note.duration.quarterLength = duracion[n]
    new_note.octave = octavas[n]
    st.append(new_note)

st.insert(0, tempo.MetronomeMark(number=180))

st.write('midi', fp='cancion2.mid')
