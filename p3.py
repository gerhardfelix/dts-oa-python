'''
1. Buatlah fungsi caesar_encript, dengan argumen txt (string) dan shift (intiger) seperti dibawah ini. Yang melakukan peng-ekripsian menggunakan 
metode Caesar terhadap string txt. Keluaran dari fungsi ini berupa string terenkripsi / chiper text.
'''

def caesar_encript(txt,shift):
  chiper = "" 
  for i in range(len(txt)): 
    char = txt[i]
    if (char.isspace()):
      chiper += ' '
    elif (char.isupper()):
      chiper += chr((ord(char) + shift-65) % 26 + 65) 
    elif (char.islower()):
      chiper += chr((ord(char) + shift-97) % 26 + 97) 
    elif char != char.isalpha:
      chiper += char
  return chiper 

# Fungsi Decript caesar
def caesar_decript(chiper,shift):
  return caesar_encript(chiper,-shift)

# Sanity check!!!
msg = 'Haloz DTS mania, MANTAPSZZZ!'
cpr = caesar_encript(msg,4)
txt = caesar_decript(cpr,4)

print('plain text:',txt)
print('chiper text:',cpr)


'''
2. Buatlah fungsi deshuffle_order, dengan argument sftxt (string) dan order (list). Yang akan mengembalikan urutan string kembali seperti semula 
sebelum di-shuffle. Sedemikian hingga:
deshuffle_order(shuffle_order(txt,order),order) == txt
hint: list method .index()
'''
 
def shuffle_order(txt,order):
  return ''.join([txt[i] for i in order])
 
def deshuffle_order(sftxt,order):
  balik=[order]*len(sftxt)
  for x, y in enumerate(order):
    balik[y]=sftxt[x]
  return ''.join(balik)

# Sanity check!!!
print(shuffle_order('abcd',[2,1,3,0]))
print(deshuffle_order('cbda',[2,1,3,0]))


'''
3. Buatlah fungsi send_batch dengan argument txt (string), batch_order (list), dan shift (int). Fungsi ini akan memecah text menjadi bagian-bagian yang lebih kecil sesuai dengan panjang dari batch_order, di mana batch_order tersebut merupakan list index untuk men-shuffle setiap batch dengan menggunakan fungsi di nomor 2. Keluaran fungsi ini berupa list batch teks terenkripsi.
Note: tambahkan underscore di akhir (sebelum dipecah menjadi batches) jika panjang txt belum memenuhi kelipatan panjang satu batch yaitu len(batch_order).
Hint: Lihat intro 3 dan gambar, gunakan library math jika diperlukan
'''

import math

def send_batch(txt,batch_order,shift=3):
  batch_cpr = []
  for i in range(len(txt)):
    if i % len(batch_order) == 0:
      temp = txt[i : i+len(batch_order)]
      while len(temp) <= len(batch_order):
        temp += "_"
          
      batch_cpr.append(caesar_encript(shuffle_order(temp,batch_order), shift))

  return batch_cpr
  
def receive_batch(batch_cpr,batch_order,shift=3):
  batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
  return ''.join(batch_txt).strip('_')
  
# Sanity check!!!
msg_cpr = send_batch('halo DTS mania, mantaaap!!!',[2,1,3,0],4)
msg_txt = receive_batch(msg_cpr,[2,1,3,0],4)
print(msg_txt,msg_cpr,sep='\n')
