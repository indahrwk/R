def MainMenu():
    num = input('Main Menu:\n\n1. Submit \n2. Search \n3. Keluar\n\nPilihan :')
    return num


def submit(arr):
    angka = int(input("Masukkan angka : "));
    arr.sort() 

    if(arr[0] < arr[len(arr)-1] and arr[0]< arr[len(arr)-2]):
        angka = arr[0]
    else:
        angka = arr[len(arr)-1]
    return angka

def search(angka):
    inputSearch = input(" Key Search : ");
    newDict = {};
    for key in theDict:

    
while(True):
    pilihan = MainMenu() 
    if pilihan == '1':
        submit()
    elif pilihan == '2':
        search()
    elif pilihan == '3':
        print ('Keluar')
        break
        
