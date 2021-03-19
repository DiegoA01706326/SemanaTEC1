
"""Song tiene como objetivo generar un stream con la canción tetris,
generando notas con distintos tonos, duraciones
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
sols = 'G#'
sis = 'B#'

"""Notas de cada estrofa"""
estrofa1 = [mi, si, do, re, do, si, la, la, do, mi, re,
            do, si, do, re, mi, do, la, la, "silence"]
estrofa2 = estrofa1 + [re, fa, la, sol, fa, mi, do, mi,
                       re, do, si, do, re, mi, do, la, la, "silence"]
estrofa3 = estrofa2 + [mi, do, re, si, do, la, sols]
estrofa4 = estrofa3 + [mi, do, re, si, do, mi, la, la, sols]
estrofa5 = estrofa4 + [mi, si, do, re, do, si, la, la, do,
                       mi, re, do, si, do, re, mi, do, la, la, "silence"]
estrofa6 = estrofa5 + [re, fa, la, sol, fa, mi, do, mi, re,
                       do, si, do, re, mi, do, la, la, "silence"]
song = estrofa6

"""Duración de cada nota por estrofa"""
duracione1 = [1, 1/2, 1/2, 1, 1/2, 1/2, 1, 1/2, 1/2, 1, 1/2, 1/2,
              1.5, 1/2, 1, 1, 1, 1, 1, 1]
duracione2 = duracione1 + [1, 1/2, 1, 1/2, 1/2, 1.5, 1/2, 1, 1/2, 1/2,
                           1.5, 1/2, 1, 1, 1, 1, 1, 1]
duracione3 = duracione2 + [2, 2, 2, 2, 2, 2, 4]
duracione4 = duracione3 + [2, 2, 2, 2, 1, 1, 1, 1, 4]
duracione5 = duracione4 + [1, 1/2, 1/2, 1, 1/2, 1/2, 1, 1/2, 1/2, 1, 1/2,
                           1/2, 1.5, 1/2, 1, 1, 1, 1, 1, 1]
duracione6 = duracione5 + [1, 1/2, 1, 1/2, 1/2, 1.5, 1/2, 1, 1/2, 1/2, 1.5,
                           1/2, 1, 1, 1, 1, 1, 1]
duracion = duracione6

"""Octava de cada nota por estrofa"""
octavae1 = [5, 4, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 4, 1]
octavae2 = octavae1 + [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 4, 1]
octavae3 = octavae2 + [5, 5, 5, 4, 5, 4, 4]
octavae4 = octavae3 + [5, 5, 5, 4, 5, 5, 5, 5, 5]
octavae5 = octavae4 + [5, 4, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5, 4, 5, 5, 5,
                       5, 4, 4, 1]
octavae6 = octavae5 + [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 4, 1]
octavas = octavae6

"""Creación de cada nota o silencio con sus respectivas duraciones y octavas"""
for n in range(len(song)):
    if(song[n] == "silence"):
        silence = note.Rest()
        st.append(silence)
    else:
        new_note = note.Note(song[n])
        new_note.duration.quarterLength = duracion[n]
        new_note.octave = octavas[n]
        st.append(new_note)

st.insert(0, tempo.MetronomeMark(number=130))

st.write('midi', fp='tetris20.mp3')
