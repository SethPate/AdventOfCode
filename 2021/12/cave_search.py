
caves = { 'id' : Cave}

Cave
    is_small
    adjacent = Set('a','b')

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
            self.path = old_path.append(cave) # list of cave IDs
            self.visited_small = old_visited # visited small caves
            if cave_map[cave].is_small:
                self.visited_small.add(cave)

    paths = {}
    starting_run = Run([], 'start')
    worklist = [starting_run]
    while worklist:
        current_run = worklist.pop() # .path., .visited_small
        current_cave = current_run.path[-1] # string
        # create new runs for each adjacent cave,
        # unless the new cave is small, and we've already been there
        for neighbor in cave_map[current_cave]:
            if neighbor == 'end': # most recent cave
                paths.add(current.path.append('end'))
                pass
            if cave_map[neighbor].is_small:
                if neighbor in current_run.visited_small:
                    pass
            worklist.append(Run(current_run.path,
                                current_run.visited_small,
                                neighbor)) 
            
    
    return paths
