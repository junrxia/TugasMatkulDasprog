N, A_to_Bee, Bee_to_C, C_to_D, D_to_E = map(int, input("masukkan kekuatan lompatan B dan jarakn pilar(kekuatan lompatan, jarak pilar a ke bee, jarak pilar bee ke c, jarak pilar c ke d, jarak pilar d ke e): ").split())

if (N < 1) or (A_to_Bee < 1) or (Bee_to_C < 1) or (C_to_D < 1) or (D_to_E < 1):
    print("angka yang dimasukkan tidak valid")
else:
    if N >= A_to_Bee and N >= Bee_to_C and N >= C_to_D and N >= D_to_E:
        print("YES HE CAN")
    else:
        print("NO HE CAN'T")