import matplotlib.pyplot as plt

if __name__ == "__main__":
    """
    plt.plot([28, 35, 21, 10])  # y-axis of graph
    plt.show()

    # x-axis and y-axis in ordered pair
    plt.plot([1, 2, 3, 4], [28, 35, 21, 10])
    plt.show()
    """
    plt.plot([1, 2, 3, 4], [28, 35, 21, 10],
             "ro-")  # o=scattered, r=red -=connected line
    plt.plot([1, 2, 3, 4], [10, 20, 50, 10], "go-")  # g=green
    plt.show()
