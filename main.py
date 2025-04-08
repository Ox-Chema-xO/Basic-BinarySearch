def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Si el elemento es el del medio, lo encontramos
        if arr[mid] == target:
            return mid
        
        # Si el elemento es mayor, ignoramos la mitad izquierda
        elif arr[mid] < target:
            left = mid + 1
        
        # Si el elemento es menor, ignoramos la mitad derecha
        else:
            right = mid - 1
    
    # El elemento no está presente
    return -1

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
    print("Hi, this is a implementation of binary search")
    arr = [24,6,12,9,14,1,20,7]
    x = 9 #elemento a buscar
    sorted_list = bubble_sort(arr) 
    print(f"Lista ordenada: {sorted_list}")
    result = binary_search(sorted_list, x)
    if result != -1:
        print(f"El elemento {x} está en el índice {result}")
    else:
        print(f"El elemento {x} no está en la lista")
    
if __name__ == "__main__":
    main()
