# Demonstration of breadth-first search in O(V + E)

from collections import deque


def my_bfs(name: str) -> True:
    search_queue = deque()
    search_queue += graph[name]
    searched: list[str] = []
    while search_queue:
        person: str = search_queue.popleft()
        if person not in searched:
            if len(name) == 5:
                print(person, "is the first letter winner!")
                return True

            else:
                # Pass to the next node
                search_queue += graph[person]
                searched.append(person)

    return False


graph = {}
graph["me"] = ["Anna", "Boris", "Nikolai"]
graph["Anna"] = ["Petro"]
graph["Boris"] = ["Antony", "Petro"]
graph["Nikolai"] = ["Tommy", "John"]
graph["Petro"] = []
graph["Antony"] = []
graph["Tommy"] = []
graph["John"] = []

my_bfs("Boris")
