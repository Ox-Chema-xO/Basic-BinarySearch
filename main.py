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

def main():
    print("Hi, this is a implementation of binary search")
    
    # Ejemplo con una lista ordenada
    sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Lista ordenada: {sorted_list}")
    
    # Buscar varios elementos
    test_cases = [16, 72, 42]
    
    for target in test_cases:
        result = binary_search(sorted_list, target)
        if result != -1:
            print(f"El elemento {target} está en el índice {result}")
        else:
            print(f"El elemento {target} no está en la lista")

if __name__ == "__main__":
    main()
