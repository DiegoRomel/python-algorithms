def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio) # divide os arrays até haver só um elemento
        mergesort(lista, meio, fim) # divide os arrays até haver só um elemento
        merge(lista, inicio, meio, fim) # junta os arrays de forma ordenada


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            lista[k] = right[j]
            j = j + 1
        elif j >= len(right):
            lista[k] = left[i]
            i = i + 1
        elif left[i] < right[j]:
            lista[k] = left[i]
            i = i + 1
        else:
            lista[k] = right[j]
            j = j + 1


if __name__ == "__main__":
    random_array = [2, 5, 1, 8, 10, 3, 6]
    mergesort(random_array)
    print(random_array)
