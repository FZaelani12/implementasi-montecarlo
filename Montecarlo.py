print ("Nama : Fiqry Zaelani S")
print ("NRP : 15-2017-112")
print ()

import pandas as pd
import numpy as np
import random

data = np.array([[0, 25], [1, 30], [2, 20], [3, 10], [4,15]])
mingguke = data[:0]
frekuensi = data[:, 1]

sigma_f = 0
for i in range(len(frekuensi)):
    sigma_f = sigma_f + frekuensi[i]

print("ΣFrekuensi   :", sigma_f)
print()

prob = []
sum_f = 0
for a in range(len(frekuensi)):
    sum_f = frekuensi[a] / sigma_f
    print("probabilitas minggu ke -", a, "=", sum_f)
    prob.append(sum_f)
print()

prob_k = []
sum_p = 0
for a in range(len(frekuensi)):
    sum_p = sum_p + prob[a]
    print("probabilitas kumulatif minggu ke -", a, "=", sum_p)
    prob_k.append(sum_p)

print()

interval_min = []
min_v = 0
for a in range(len(frekuensi)):
    if (a == 0):
        interval_min.append(min_v)
        print("Interval Minggu ke -", a, " = ", min_v, "-", prob_k[a])
    else:
        min_v = prob_k[a - 1] + 0.001
        interval_min.append(min_v)
        print("Interval Minggu ke -", a, " = ", min_v, "-", prob_k[a])
print()
print()

minggu_baru = 101
p_minggu = []
angka_acak = []
permintaan = []

for a in range(16):
    p_minggu.append(minggu_baru)
    acak = random.random()
    angka_acak.append(acak)
    if (acak < 0.2):
        jenis = 0
        permintaan.append(jenis)
    elif (acak < 0.6):
        jenis = 1
        permintaan.append(jenis)
    elif (acak < 0.8):
        jenis = 2
        permintaan.append(jenis)
    elif (acak < 0.9):
        jenis = 3
        permintaan.append(jenis)
    elif (acak <= 1):
        jenis = 4
        permintaan.append(jenis)
    minggu_baru += 1

print("Minggu Ke-", "|", "Angka Acak", "|", "Permintaan")
for a in range(16):
    print(p_minggu[a], "|", angka_acak[a], "|", permintaan[a])