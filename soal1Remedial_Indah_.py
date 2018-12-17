def MainMenu():
    num = input('Main Menu:\n\n1. Lihat Array Utama \n2. Sort Array Utama \n3. Keluar\n\nPilihan :')
    return num

def ArrUtama():
    angka = int(input("Masukkan angka : "));
    arrgen = []
    arrgan = []
    for number in mylist:
        if(number%2 == 0):
            result.append[arrgen]
        else:
            result.append[arrgan]
        return angka

def ArrSort(arr):
    print("Lihat Array Utama")
    arr.sort()
	for i in range(len(arr)):
		if sum(arr[:i]) == sum(arr[i+1:]):
			return i
	return -1
    
mylist = []

while(True):
    pilihan = MainMenu() 
    if pilihan == '1':
        ArrUtama()
    elif pilihan == '2':
        ArrSort()
    elif pilihan == '3':
        print ('Keluar')
        break
        

