import subprocess

file = open("list.txt", "w")

encoder={
	"furniazA1-est":"A1",
	"tomniaB2-est":"B2",
	"koronazniaC3-ast":"C3",
	"tisztitaniaD4-est":"D4",
	"implantalniazE5-re":"E5",
	"birizgalniazF6-ot":"F6"
}

#hossz = input("Hany muveletet szeretnel elvegezni?")
teendok=input("Mit fogunk szegeny beteggel csinalni?").replace(' ','').split(',')
#print(teendok)
#print(teendok[0])
#ops=[]
for i in range(len(teendok)):
	#ops.append(input("Muveletkod:"))
	file.write("file 'vids/%s.avi'\n" % encoder.get(teendok[i]))

file.close()

#subprocess.call('ffmpeg -f concat -i list.txt -c copy video_draft.avi', shell=True)