# src/analysis.py
def analyze_key_operations():
    """
    Analyzes the key operations of the Bubble Sort algorithm.
    """
    return (
        "1. Outer loop runs n times.\n"
        "2. Inner loop runs (n-i-1) times for each iteration of the outer loop.\n"
        "3. Each inner loop iteration involves a comparison and possibly a swap."
    )

def calculate_big_o_complexity():
    """
    Calculates the Big O complexity of the Bubble Sort algorithm.
    """
    return (
        "Time Complexity: O(n^2) due to the nested loops.\n"
        "Space Complexity: O(1) since only a constant amount of extra space is used."
    )

def suggest_improvements():
    """
    Suggests improvements or alternative algorithms for better performance.
    """
    return (
        "1. Quick Sort: Average-case O(n log n), worst-case O(n^2). Efficient for larger datasets.\n"
        "2. Merge Sort: O(n log n) for both average and worst-case. Stable and efficient.\n"
        "3. Insertion Sort: O(n^2) in general but O(n) for nearly sorted arrays. Simple and in-place."
    )

# Example usage
if __name__ == "__main__":
    print("Key Operations:\n", analyze_key_operations())
    print("\nBig O Complexity:\n", calculate_big_o_complexity())
    print("\nSuggestions for Improvement:\n", suggest_improvements())
