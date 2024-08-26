# src/sorting_algorithm.py
def simple_sort(arr):
    """
    Sorts an array of integers in ascending order using Bubble Sort.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage (not part of the analysis)
if __name__ == "__main__":
    example_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", example_array)
    simple_sort(example_array)
    print("Sorted array:", example_array)
