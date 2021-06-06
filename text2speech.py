from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = ['person','zebra','zebra']
if len(mytext)==1:
	new="There is "+mytext[0]+" in the  view"
else:
	in_list=set(mytext)
	dic={}
	for i in in_list:
		dic[i]=mytext.count(i)
	li=[]
	for i in dic:
		li.append(f'{dic[i]} {i}')
	txt=' ,'.join(li)
	new='There are '+txt+' in the view'


language = 'en'
  

myobj = gTTS(text=new, lang=language) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 