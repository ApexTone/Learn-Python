number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Random access: [row][column]
print(number_grid[0][2])


# Nested loop
for row in number_grid:
    for item in row:
        print(item)
