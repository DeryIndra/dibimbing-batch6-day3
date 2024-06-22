# from datetime import datetime

#Private variabel menggunakan double underscore __
#Constractor
# class Mobil:
#     def __init__(self, merek, tipe, harga, warna, 
#                  tahun_pembuatan):
#         self.merek = merek
#         self.tipe = tipe
#         self.harga = harga
#         self.warna = warna
#         self.tahun_pembuatan = tahun_pembuatan
#         self.roda = 4
#         self.umur = datetime.now().year - self.tahun_pembuatan
#         self.posisi = 0

#     def klakson(self):
#         print("tiiiinnnnn...")

#     def maju(self):
#         self.posisi += 1

#     def mundur(self):
#         self.posisi -=1

# audi = Mobil()
# nissan = Mobil()
# volvo = Mobil()

# nissan_march = Mobil("nissan", "march", 100_000_000, "putih", 2011)

# print("merek : ", nissan_march.merek)
# print("tipe : ", nissan_march.tipe)
# print("harga : ", nissan_march.harga)
# print("warna : ", nissan_march.warna)
# print("tahun pembuatan : ", nissan_march.tahun_pembuatan)
# print("roda : ", nissan_march.roda)
# print("umur : ", nissan_march.umur)


# nissan_march.warna = "hitam"
# print("warna : ", nissan_march.warna)

# nissan_march.model = "City Car"
# print("model : ", nissan_march.model)

# ========================================================

# nissan_march.klakson = klakson
# nissan_march.klakson()

# print("posisi: ", nissan_march.posisi)

# nissan_march.maju()
# print("posisi: ", nissan_march.posisi)

# nissan_march.mundur()
# print("posisi: ", nissan_march.posisi)

# ========================================================

# import time
# import random
# from multiprocessing import Pool

# def square(x):
#     print("start:", x)
#     time.sleep(random.randint(0,10))
#     print("finish", x)
#     return x * x

# with Pool(processes=4) as pool:
#     result = pool.map(square, range(10))
# print(result)

# square(5)

# Scenario
# Si A punya toko pakaian, bisnis tokonya bisa menjual berbagai macam pakaian, bisa menerima program affiliasi dan ada membership untuk loyal customer.

# 1. Jual - Beli regular
# - Get harga barang
# - Get Stock barang
# - Get nama barang

# 2. Affiliate Program
# - Get harga barang
# - Get Stock barang
# - Get nama barang
# - Sales percentage

# 3. Loyalty Program
# - Get harga barang
# - Get Stock barang
# - Get nama barang
# - Discount percentage

from abc import ABC, abstractmethod

# abstraction layer
class Product(ABC):
    @abstractmethod
    def harga(self):
        pass

    @abstractmethod
    def stock(self):
        pass

    @abstractmethod
    def nama(self):
        pass

# inherit product
# class GeneralProduct(Product):
#     def __init__(self, nama_product, harga_product, stock_product) -> None:
#         super().__init__()
#         self.nama_product = nama_product
#         self.harga_product = harga_product
#         self.stock_product = stock_product

#     def nama(self):
#         print(f"Harganya adalah {self.nama_product}")

#     def harga(self):
#         print(f"Harganya adalah {self.harga_product}")

#     def stock(self):
#         print(f"Stockny masih {self.stock_product}")

#     lipstik = GeneralProduct("lipstik", 50000, 10)


class GeneralProduct(Product):
  def __init__(self, harga_product, stock_product, nama_product) -> None:
    super().__init__()
    self.harga_product = harga_product
    self.stock_product = stock_product
    self.nama_product = nama_product

  def harga(self):
    print(f"Harganya adalah {self.harga_product}")

  def stock(self):
    print(f"Stocknya masih {self.stock_product}")

  def nama(self):
    print(f"Nama product: {self.nama_product}")


lipstik = GeneralProduct(50000, 10, 'lipstik')
lipstik.nama()
lipstik.stock()
lipstik.harga()