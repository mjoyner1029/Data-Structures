# src/main.py
from sorting_algorithm import simple_sort
from analysis import analyze_key_operations, calculate_big_o_complexity, suggest_improvements

def main():
    # Example array to be sorted
    example_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", example_array)
    simple_sort(example_array)
    print("Sorted array:", example_array)

    # Perform analysis
    print("\nKey Operations:\n", analyze_key_operations())
    print("\nBig O Complexity:\n", calculate_big_o_complexity())
    print("\nSuggestions for Improvement:\n", suggest_improvements())

if __name__ == "__main__":
    main()
