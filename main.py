def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    return arr


def main():
    arr = [24,6,12,9,14,1,20,7]
    x = 9 #elemento a buscar
    print(f"Arreglo al inicio:{arr}")
    print(f"Arreglo ordenado:{bubble_sort(arr)}")
    
if __name__ == "__main__":
    main()