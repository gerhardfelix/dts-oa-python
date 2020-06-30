'''
PROJECT 2
DTS OA - PYTHON

1. Buatlah sebuah fungsi isPointInCircle dengan posisional argument x,y,r dan keyword argument center dengan default value sebuah tupple dua nilai (0,0). 
Untuk menentukan apakah titik (x,y) berada di dalam atau di luar lingkaran L(center,r). Keluaran fungsi isPointInCircle merupakan suatu nilai boolean, 
True Jika titik (x,y) berada di dalam lingkaran dan False Jika berada di luar. 
Note: titik yang berada tepat di lingkaran dikategorikan sebagai dalam, maka True.
'''

def isPointInCircle(x,y,r,center=(0,0)):
  x0 = center[0]
  y0 = center[1]

  persamaan = (x-x0)**2 + (y-y0)**2 <= r**2

  if (x-x0)**2 + (y-y0)**2 <= r:
    return persamaan
  else:
    return persamaan
    
# CEK OUTPUT KODE ANDA
print(isPointInCircle(1,1,1,center=(0,0)),isPointInCircle(1,0,1,center=(0,0)),
      isPointInCircle(1,1,1,center=(1,0)),isPointInCircle(0,0,1,center=(1,1)))


'''
2. generateRandomSquarePoints dengan dua positional argumen n dan length, dan keyword argument center default: tupple(0,0). Fungsi ini akan mengeluarkan 
suatu list dengan jumlah n titik random [x,y] yang berada di dalam suatu kotak persegi dengan panjang length dan titik tengah center. 
Keluaran fungsi merupakan list dari n titik random [x,y], cth: [[x1,y1],...,[xn,yn]].

hint:
Jarak titik tengah center ke tepi persegi sama dengan length/2.
Untuk menghasilkan nilai random, gunakan random.uniform, penjelasan random.uniform. Untuk menentukan nilai a dan b dari fungsi random.uniform, coba perhatikan gambar di cell bawah dengan center=(0,0). Note: harus fleksible ketika titik center berubah.
Gunakan list comprehension untuk men-generate n titik x,y tersebut.
Untuk menyelesaikan hanya butuh ubah satu baris kode, ganti None value, dengan kode anda.
'''

import random

def generateRandomSquarePoints(n,length,center=(0,0)):
  # MULAI KODEMU DI SINI
  minx = center[0]-length/2
  miny = center[1]-length/2
  xmax = minx+length
  ymax = miny+length
  
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  points = [[random.uniform(minx,xmax),random.uniform(miny,ymax)] for i in range(n)]
  return points

# CEK OUTPUT KODE ANDA
random.seed(0)
# generate 100 point di dalam persegi dengan panjang sisi 1 dan berpusat di (0,0)
points = generateRandomSquarePoints(100,1)
print(points[10:15])


'''
3. Buatlah fungsi MCCircleArea dengan positional argument r dan keyword argument dengan default n=100 dan center=(0,0), untuk menghitung luas lingkaran 
dengan jari-jari r dengan mengestimasi dari n titik random. Keluaran fungsi merupakan suatu nilai yang menunjukkan estimasi luas lingkaran tersebut.

hint:
gunakan fungsi yang sudah dibuat di atas isPointInCircle dan generateRandomSquarePoints.
perhatikan gambar lingkaran dan persegi di atas, jari-jari  r  lingkaran sama dengan setengah dari panjang sisi persegi.
lingkaran dan persegi memiliki pusat yang sama.
'''

def MCCircleArea(r,n=100,center=(0,0)):
  length= 2*r
  luaspersegi = length**2
  titik = 0
  for x,y in generateRandomSquarePoints(n, length, center):
    if(isPointInCircle(x, y, r, center)) :
      titik+=1
  luaslingkaran = (titik/n)*luaspersegi
  return luaslingkaran

# CEK OUTPUT KODE ANDA
random.seed(0)
print(MCCircleArea(1,100),MCCircleArea(1,10,center=(10,10)))


'''
4. Buatlah fungsi LLNPiMC untuk mengestimasi nilai pi dengan positional argumen nsim dan nsample. nsample merupakan jumlah sample titik-titik random untuk 
menghitung luas lingkaran berjari-jari 1 (maka Luas =  π ) dan nsim merupakan jumlah simulasi untuk menghitung nilai rata-rata atau mean dari estimasi 
nilai  π . Keluaran fungsi merupakan nilai mean dari simulasi tersebut (estimasi nilai  π ).
'''

def LLNPiMC(nsim,nsample):
  x=[]
  for i in range (nsim):
    x.append(MCCircleArea(1, nsample))
  pi = (sum(x))/nsim
  return pi

#CEK OUTPUT KODE ANDA
import math
random.seed(0)
estpi = LLNPiMC(10000,500)
print('est_pi:',estpi)
print('act_pi:',math.pi)


'''
5. Buatlah fungsi relativeError, dengan argument act yang merupakan nilai aktual, dan est yang merupakan nilai estimasi.
'''

def relativeError(act,est):
  e = (est-act)/act
  return abs(e)*100
  
#CEK OUTPUT KODE ANDA
print('error relatif:',relativeError(math.pi,estpi),'%')
