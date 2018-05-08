from matplotlib import pyplot as plt

# NOTE: the pyplot module is a simple interface for matplotlib

plt.title("Sample Plot")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# First set of [] is x-axis
# Second is y-axis
plt.plot([1, 2, 3], [1, 4, 9])
plt.plot([2, 5, 3], [4, 8, 1])
plt.legend(['Data Set 1', 'Data Set 2'])
plt.show()
#plt.savefig('Sample Plot 2')