import cave_build as dan

"""
{'id' : Cave} -> list of paths
"""
def part_a(cave_map):
    paths = all_paths(cave_map)
    return len(paths)

"""
{'id' : Cave} -> [path, path, ...]
All paths beginning with 'start' and ending with 'end'.
Small caves (lower case letters) can only be visited once.

Must track visited caves per unique path.
"""
def all_paths(cave_map):
    class Run:
        """
        old_path: The path taken by the run that led to this cave.
                [str, str, str...]
        old_visited: Set of all small caves visited on this run.
                {str, str, str...}
        cave: The newly entered cave; a string.
        """
        def __init__(self, old_path, old_visited, cave):
            self.path = [c for c in old_path]
            self.path.append(cave)
            self.visited_small = set(old_visited) # visited small caves
            if cave_map[cave].is_small:
                self.visited_small.add(cave)

    paths = [] 
    starting_run = Run([], set(), 'start')
    worklist = [starting_run]
    while worklist:
        current_run = worklist.pop() # .path., .visited_small
        current_cave = current_run.path[-1] # string
        # create new runs for each adjacent cave,
        # unless the new cave is small, and we've already been there
        for neighbor in cave_map[current_cave].adjacent_nodes:
            if neighbor == 'end': # most recent cave
                new_path = list(current_run.path)
                new_path.append('end')
                paths.append(new_path)
                continue
            if cave_map[neighbor].is_small:
                if neighbor in current_run.visited_small:
                    continue
            worklist.append(Run(current_run.path,
                                current_run.visited_small,
                                neighbor)) 

    return paths

if __name__ == "__main__":
    cave_map = dan.get_cave_map()
    a = part_a(cave_map)
    print(a)
