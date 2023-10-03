# Este algoritmo so funciona para arquivos MIDI com um unico canal
# Para MIDIs com mais de 1 canal utilize um editor MIDI para fazer a juncao dos canais
# Uma outra limitação e que o arquivo MIDI também tem que ser editado para que seja tocado so uma nota de uma vez
# A saida do Algoritmo é NOTA, TEMPO DA NOTA, NOTA, TEMPO DA NOTA, ETC...
# E tambem o numero de notas da musica

import mido

mid = mido.MidiFile('O seu arquivo midi vem aqui')
y = open("resultado.txt", "w")

nlista = []
plista = []
for msg in mid:
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
y.write("\n"+ "Numero de Notas:" + str(notas))

y.close()
