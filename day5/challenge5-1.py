class Map:
    def __init__(self, active, line):
        self.active = active
        self.line = line
        self.mappings =[]
    
    def add_mapping(self, line):
        if line == []:
            self.active = False
        else:
            self.mappings.append((int(line[1]), int(line[1]) + (int(line[2])-1), int(line[0])-int(line[1])))

    def __str__(self):
        string = f"{self.line} mappings:\n"
        for start, end, change in self.mappings:
            string += f"If seed is in range from {start} to {end}, add {change} to seed.\n"
        return string

sts = Map(False, "seed-to-soil")
stf = Map(False, "soil-to-fertilizer")
ftw = Map(False, "fertilizer-to-water")
wtl = Map(False, "water-to-light")
ltt = Map(False, "light-to-temperature")
tth = Map(False, "temperature-to-humidity")
htl = Map(False, "humidity-to-location")

locations = []

with open('day5/challenge5.txt', 'r') as file:
    for line in file:
        line = line.replace('\n','').split()
        if sts.active:
            sts.add_mapping(line)
        elif stf.active:
            stf.add_mapping(line)
        elif ftw.active:
            ftw.add_mapping(line)
        elif wtl.active:
            wtl.add_mapping(line)
        elif ltt.active:
            ltt.add_mapping(line)
        elif tth.active:
            tth.add_mapping(line)
        elif htl.active:
            htl.add_mapping(line)
        elif line == []:
            continue
        elif line[0] == "seeds:":
            seeds = [int(seed) for seed in line[1:]]
        elif line [0] == sts.line:
            sts.active = True
        elif line [0] == stf.line:
            stf.active = True    
        elif line [0] == ftw.line:
            ftw.active = True
        elif line [0] == wtl.line:
            wtl.active = True
        elif line [0] == ltt.line:
            ltt.active = True    
        elif line [0] == tth.line:
            tth.active = True
        elif line [0] == htl.line:
            htl.active = True

maps = [sts, stf, ftw, wtl, ltt, tth, htl]

for seed in seeds:
    seed_mappings = [seed]
    for i in range(0, 7):
        for start, end, change in maps[i].mappings:
            if seed_mappings[i] >= start and seed_mappings[i] <= end:
                seed_mappings.append(seed_mappings[i] + change)
        if len(seed_mappings) == i + 1:
            seed_mappings.append(seed_mappings[i])
    locations.append(seed_mappings[-1])

print("Smallest location in input seeds:", min(locations))