# PROJECT 1
# DTS OA - PYTHON

# 1. Buatlah fungsi letter_catalog dengan sebuah positional argument berupa list dan keyword argument 
# letter untuk nilai default 'A'. Fungsi letter_catalog akan mengembalikan sebuah list yang berisi 
# nama-nama buah yang dimulai dengan huruf yang ada keyword argument letter. 
# Jika tidak ada item di list inputan tersebut yang diawali dengan huruf yang didefinisikan di keyword 
# letter maka fungsi mengembalikan list kosong.

def letter_catalog(items,letter='A'):
  
  buah = []
  for i in items :
    if i.startswith(letter) :
      buah.append(i)
  return buah

# Cek output kode anda
letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='A')



# 2. Buatlah fungsi counter_item yang memiliki sebuah input argument berupa list. Fungsi ini 
# mengembalikan sebuah dictionary yang menghitung jumlah buah dalam list input, dengan key berupa 
# nama buah tersebut dan value berupa jumlah nama buah tersebut muncul di list input.

def counter_item(items):
  
  jlbuah = {x:items.count(x) for x in items}
  return jlbuah

# Cek output kode anda
counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries'])



# 3. Di bawah ini sudah ada tiga variables fruits, prices, dan chart.
# Buatlah sebuah dictionary yang berupa daftar harga buah dengan key berupa nama buah di variable 
# fruits dan dengan value berupa harga dari buah tersebut di variable price (sudah diurutkan sesuai 
# dengan nama-nama buah di varibale fruits, kemudian Dictionary tersebut disimpan di dalam variable 
# fruit_price.
# Selanjutnya, Buatlah fungsi total_price dengan dua input yaitu: 
# 1) dictionary yang merupakan keluaran dari fungsi counter_item dan 
# 2) dictionary harga buah fruit_price. Fungsi ini mengeluarkan sebuah total harga dari daftar buah 
# di dictionary keluaran dari counter_item.
# Hint: Gunakan fungsi counter_item di soal nomor 2.

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

fruit_price = dict(zip(fruits, prices))
dcounter = counter_item(chart)

def total_price(dcounter,fprice):
  total_price = 0
  for key, value in dcounter.items():
    total_price = total_price + fprice.get(key) * value
  return total_price

# Cek output kode anda
total_price(counter_item(chart),fruit_price)



# 4. Buatlah fungsi discounted_price dengan dua positional arguments input dari keluaran fungsi 
# totalprice dan discount dalam persen(80 berarti 80%, dst), dan satu keyword argument minprice yang 
# menunjukkan hanya dengan minimum price tersebut yang hanya di-discount, set default value minprice 
# ke 100. Fungsi tersebut menghitung nilai harga akhir setelah di-discount sebesar discount variable 
# (argument kedua). Untuk harga total yang kurang dari minprice maka keluarannya sama dengan harga 
# total tersebut tanpa discount.

def discounted_price(total,discount,minprice=100):

  if total < minprice :
    discounted_price = total
  else :
    disc = total*discount/100
    discounted_price = total - disc
  return discounted_price

# Cek output kode anda
discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100)



# 5. Buatlah fungsi print_summary dengan 2 posisional argument input, list nama2 buah (cth: seperti 
# variable chart) dan dictionary harga buah (cth: seperti variable fruit_price, yang mengeluarkan 
# tulisan ringakasan dari pembelian buah.

def print_summary(items,fprice):
  dcounter = counter_item(sorted(items))
  for key,value in dcounter.items():
    print(value,key, ":", value*fprice[key], end="\n")
  print("total :", total_price(dcounter,fprice))
  print("discount price :", discounted_price(total_price(dcounter, fprice), 10, minprice=100))

# Cek output kode anda
print_summary(chart,fruit_price)
