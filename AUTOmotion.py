import tkinter as tk
import math

A = list('あぁゃかがさざただなはばぱまやらわ')
I = list("いぃきぎしじちぢにひびぴみり")
U = list("うぅゅくぐすずつづぬふぶぷゆむる")
E = list("えぇけげせぜてでねへべぺめれ")
O = list("おぉょこごそぞとどのほぼぽもよろを")
n = list("ばびぶべぼぱぴぷぺぽまみむめも")
small = list("ゃゅょ")
stay = ["ー","っ"]
dic = [A,I,U,E,O]
jp = list("あいうえお")
Value = bytearray([0x00,0x00,0x80,0x3F])
ZERO = bytearray([0x00,0x00,0x00,0x00])

def act(a,b,f):   #act(文字、前フレーム) 戻り値 そのフレームのバイナリ、現フレーム
  n = 0
  if (a in jp)or(a=="ん"):
    fl = b+f
  if a == "ぅ":
    fl = b
    a = "う"
  if a=="n":
    fl = b
    a = "ん"
  z = bytearray([])
  for i in range(len(jp)):
    z += bytes(jp[i], 'SHIFT-JIS')
    z += n.to_bytes(13,"little")
    z += (b+f).to_bytes(4,"little")
    if a == jp[i]:
      z += Value
    else:
      z += ZERO
  print(z)
  return z,fl

def run(event):
  Static4.place_forget()
  Date = bytearray\
 ([0x56, 0x6F, 0x63, 0x61, 0x6C, 0x6F, 0x69, 0x64, 0x20, 0x4D, 0x6F, 0x74, 0x69, 0x6F, 0x6E, 0x20, \
   0x44, 0x61, 0x74, 0x61, 0x20, 0x30, 0x30, 0x30, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00, 0x8E, 0xA9, \
   0x93, 0xAE, 0x8C, 0xFB, 0x83, 0x70, 0x83, 0x4E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, \
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
  voice = []
  text = EditBox.get()
  flame = flamescale.get()
  sflame = math.ceil(flame/2)

  voice.append("ん")
  for i in range(len(text)):
    if text[i] == "ん":
      voice.append("ん")
    if text[i] == "わ":
      voice.append("ぅ")
    if text[i] in n:
      voice.append("n")
    if text[i] in small:
      text.pop()
    if text[i] in stay:
      if i!=0:
        voice.append(voice[i-1])
    for d in range(len(dic)):
      if text[i] in dic[d]:
        if Val1.get() == True and d == 1:
          voice.append("い")
        voice.append(jp[d])
        break
  voice.append("ん")
  if Val1.get() == True:
    text += "(え無し)"

  if len(voice) == 2:
    Static3.place(relx=0.5,rely=0.7,anchor=tk.CENTER)
    return
  else :
    Static3.place_forget()

  Date += ((len(voice))*5).to_bytes(4,"little")
  before = -1*flame
  for k in range(len(voice)):
    if voice[k] == ("ぅ" or "n"):
      x,before = act(voice[k],before,sflame)
    else:
      x,before = act(voice[k],before,flame)
    Date += x
  Date += bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])

  f = open("".join(text)+".vmd", "wb")
  f.write(Date)

  Static4.place(relx=0.5,rely=0.7,anchor=tk.CENTER)
  Static4["text"]=text=text + u"\nのモーションファイルを作成しました"
  return

root = tk.Tk()
root.title(u"MMD口パク君")
root.geometry("400x300")

EditBox = tk.Entry(width=50)
EditBox.pack()

Static1 = tk.Label(text=u'セリフを入力')
Static1.pack()

Static2 = tk.Label(text=u'1音にかけるフレーム数')
Static2.place(relx=0.5,rely=0.3,anchor=tk.CENTER)

flamescale = tk.Scale(root, orient=tk.HORIZONTAL, from_ = 2, to = 30, length = 300)
flamescale.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

Val1 = tk.BooleanVar()
Val1.set(False)
CheckBox1 = tk.Checkbutton(text=u"「え」を「い」に置き換える", variable=Val1)
CheckBox1.place(relx=0.5,rely=0.4,anchor=tk.CENTER)

Button = tk.Button(text=u'モーションファイル生成')
Button.bind("<Button-1>",run) 
Button.place(relx=0.65,rely=0.85)

Static3 = tk.Label(text=u"セリフが入力されていないか\n無効な文字のみで構成されています")

Static4 = tk.Label()

voice = []



root.mainloop()