def pascal_triangle(n):
    # Check for invalid input
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    # Generate each row of the triangle
    for i in range(1, n):
        # Calculate the next row based on the previous row
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        # Calculate the middle elements of the row
        for j in range(1, i):
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)
