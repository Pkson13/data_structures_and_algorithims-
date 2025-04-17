#include <stdio.h>
#include <stdlib.h>

int* merge(int *first, int* second, int size_first, int size_second) {
    int* merged = malloc((size_first + size_second) * sizeof(int));
    int i = 0, j = 0, k = 0;

    while (i < size_first && j < size_second) {
        if (first[i] < second[j]) {
            merged[k++] = first[i++];
        } else {
            merged[k++] = second[j++];
        }
    }

    while (i < size_first) merged[k++] = first[i++];
    while (j < size_second) merged[k++] = second[j++];

    return merged;
}

int* merge_sort(int* array, int size) {
    if (size <= 1) return array;

    int mid = size / 2;

    int* first = malloc(mid * sizeof(int));
    int* second = malloc((size - mid) * sizeof(int));

    for (int i = 0; i < mid; i++) first[i] = array[i];
    for (int i = mid; i < size; i++) second[i - mid] = array[i];

    int* sorted_first = merge_sort(first, mid);
    int* sorted_second = merge_sort(second, size - mid);

    int* merged = merge(sorted_first, sorted_second, mid, size - mid);

    free(first);
    free(second);
    return merged;
}

int main() {
    int arry[] = {25, 68, 43, 2, 4, 1, 4, 7, 89, 9, 99, 100};
    int size = sizeof(arry) / sizeof(int);

    int* sorted = merge_sort(arry, size);

    printf("Sorted array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", sorted[i]);
    }
    printf("\n");

    free(sorted);
    return 0;
}
