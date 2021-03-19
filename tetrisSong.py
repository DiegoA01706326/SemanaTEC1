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

de1 = [1, 1/2, 1/2, 1, 1/2, 1/2, 1, 1/2, 1/2, 1, 1/2, 1/2,
       1.5, 1/2, 1, 1, 1, 1, 1, 1]
de2 = de1 + [1, 1/2, 1, 1/2, 1/2, 1.5, 1/2, 1, 1/2, 1/2,
             1.5, 1/2, 1, 1, 1, 1, 1, 1]
de3 = de2 + [2, 2, 2, 2, 2, 2, 4]
de4 = de3 + [2, 2, 2, 2, 1, 1, 1, 1, 4]
de5 = de4 + [1, 1/2, 1/2, 1, 1/2, 1/2, 1, 1/2, 1/2, 1, 1/2,
             1/2, 1.5, 1/2, 1, 1, 1, 1, 1, 1]
de6 = de5 + [1, 1/2, 1, 1/2, 1/2, 1.5, 1/2, 1, 1/2, 1/2, 1.5,
             1/2, 1, 1, 1, 1, 1, 1]
duratio = de6

oe1 = [5, 4, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 4, 1]
oe2 = oe1 + [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 4, 1]
oe3 = oe2 + [5, 5, 5, 4, 5, 4, 4]
oe4 = oe3 + [5, 5, 5, 4, 5, 5, 5, 5, 5]
oe5 = oe4 + [5, 4, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 4, 1]
oe6 = oe5 + [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 4, 1]
octv = oe6

for n in range(len(song)):
    if(song[n] == "silence"):
        silence = note.Rest()
        st.append(silence)
    else:
        new_note = note.Note(song[n])
        new_note.duration.quarterLength = duratio[n]
        new_note.octave = octv[n]
        st.append(new_note)

st.insert(0, tempo.MetronomeMark(number=130))

st.write('midi', fp='tetris21.mid')
