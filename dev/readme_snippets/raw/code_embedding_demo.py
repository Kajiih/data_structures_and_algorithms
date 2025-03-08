# This is embedded in the readme!
print("The print output is formatted in a comment ->")

print("Snippets are automatically formatted and embedded in the readme with the github workflow")

# This is not executed
input("Enter a number")  # snippet: no-exec

print(f"Isn't cool {'!' * 3}?")


from data_structures_and_algorithms.disjoint_set import DisjointSet

ds = DisjointSet(6)
ds.union(0, 1)
ds.union(0, 2)
print(ds.find(2))

from data_structures_and_algorithms.kruskal import kruskal

n = 3
edges = [(0, 1, 5), (0, 2, 2), (1, 2, 1)]
print(kruskal(n, edges))
