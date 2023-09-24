import platform as p
FOLDER_PATH = dir_path = os.path.dirname(os.path.realpath(__file__))

mid = mido.MidiFile('O seu arquivo midi vem aqui')
y = open("resultado.txt", "w")

nlista = []
plista = []
for i, track in enumerate(mid.tracks):
    for msg in track:
        if (not msg.is_meta):
            if (msg.type == 'note_on'):
                nlista.append(msg.note)
                plista.append(int((mido.tick2second(msg.time, mid.ticks_per_beat,tempo)*1000)))
                
            elif (msg.type == 'note_off'):
                nlista.append(msg.note)
                plista.append(int((mido.tick2second(msg.time, mid.ticks_per_beat,tempo)*1000)))
                
        if msg.type == 'set_tempo':
            tempo = msg.tempo
                
for i in range(len(nlista)):
    y.write("," + str(nlista[i]) + "," + str(plista[i]))
    
notas = len(nlista)
print("\n"+ "Numero de Notas:" + str(notas))
