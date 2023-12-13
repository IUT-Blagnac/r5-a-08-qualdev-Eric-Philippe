import time
from typing import Tuple, List, Optional

class RangeMap(object):
    def __init__(self):
        self.sources = []
        self.destinations = []
        self.lengths = []
    
    def __getitem__(self, key: int):
        for i, s in enumerate(self.sources):
            if s <= key and s + self.lengths[i] > key:
                return self.destinations[i] + key - s
        return key
    
    def _map_range_single(self, start: int, length: int, r_start: int, r_dest: int, r_length: int) -> Optional[Tuple[int, int, int]]:
        end = start + length
        r_end = r_start + r_length

        # Check if the ranges overlap
        if r_start >= end or start >= r_end:
            return None

        # Compute the overlapping range
        overlap_start = max(start, r_start)
        overlap_end = min(end, r_end)

        # Compute the mapped values
        mapped_start = r_dest + overlap_start - r_start
        mapped_length = overlap_end - overlap_start

        return overlap_start, mapped_start, mapped_length



    def map_range(self, start: int, length: int) -> List[List[int]]:
        mapped_range = []
        source_range = []
        for i, source in enumerate(self.sources):
            v = self._map_range_single(start, length, source, self.destinations[i], self.lengths[i])
            if not v:
                continue
            s, d, l = v
            # print(start, length, source, self.destinations[i], self.lengths[i], v)
            mapped_range.append((d, l))
            source_range.append((s, l))
        
        source_range.sort()
        c_start = start
        for (s, l) in source_range:
            if c_start < s:
                mapped_range.append((c_start, s - c_start))
            c_start = s + l
        if c_start < start + length:
            mapped_range.append((c_start, start + length - c_start))
        return sorted(mapped_range)


    
    def add_range(self, source: int, destination: int, length: int):
        self.sources.append(source)
        self.destinations.append(destination)
        self.lengths.append(length)

    def __repr__(self):
        return str([self.sources, self.destinations, self.lengths])


def parse_seeds(line: str) -> List[int]:
    assert line.startswith("seeds:")
    return [int(s) for s in line[len("seeds: "):].split()]

def parse_map(line: str) -> Tuple[str, str]:
    assert "map:" in line
    mapping, _ = line.split()
    source, _, dest = mapping.split("-")
    return source, dest


def parse_range(line: str) -> Tuple[int, int, int]:
    return tuple(map(int, line.strip().split()))


def get_location(seed, maps):
    s = seed
    for (dest, source), map in maps.items():
        s = map[s]
    return s


def part_one(file_name: str) -> int:
    seeds, maps = None, {}
    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("seeds:"):
                seeds = parse_seeds(line)
            elif "map:" in line:
                source, dest = parse_map(line)
                maps[(source, dest)] = RangeMap()
            elif line:
                d, s, r = parse_range(line)
                maps[(source, dest)].add_range(s, d, r)

    return min(get_location(seed, maps) for seed in seeds)
    
def part_two(file_name: str) -> int:
    seeds, maps = None, {}
    
    with open(file_name, "r") as f:
        seeds = parse_seeds(f.readline())
        
        line = f.readline()
        while line:
            line = line.strip()
            
            if "map:" in line:
                source_name, dest_name = parse_map(line)
                maps[(source_name, dest_name)] = RangeMap()
            elif line:
                d, s, r = parse_range(line)
                maps[(source_name, dest_name)].add_range(s, d, r)
                
            line = f.readline()

    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    for (dest, source), r_map in maps.items():
        seeds = [
            interval
            for start, length in seeds
            for interval in r_map.map_range(start, length)
        ]

    seeds.sort()
    return seeds[0][0]


def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 5
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)

