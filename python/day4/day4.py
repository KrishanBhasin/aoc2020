from dataclasses import dataclass

### this only works with TWO `\n`s at the end of the input file
### need a cleverer fix than adding a new line to the end of it!
def generate_single_passport_text():
    lines_to_yield = []
    for row in open("python/day4/day-4-input.txt", "r"):
        if row.strip():
            lines_to_yield.append(row.strip())
        else:
            yield lines_to_yield
            lines_to_yield = []

@dataclass
class TravelCredentials:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str = None

    def __post_init__(self):
        validate_byr(self.byr)
        validate_iyr(self.iyr)
        validate_eyr(self.eyr)
        validate_hgt(self.hgt)
        validate_hcl(self.hcl)
        validate_ecl(self.ecl)
        validate_pid(self.pid)
        validate_cid(self.cid)

        

def validate_byr(i):
    i = int(i)
    assert 1920 <= i <= 2002

def validate_iyr(i):
    i = int(i)
    assert 2010 <= i <= 2020

def validate_eyr(i):
    i = int(i)
    assert 2020 <= i <= 2030

def validate_hgt(i):
    unit = i[-2:]
    assert unit in ["cm","in"]
    value = int(i[:-2])
    if unit == "cm":
        assert 150 <= value <= 193
    elif unit == "in":
        assert 59 <= value <= 76

def validate_hcl(i):
    assert i[0] == "#"
    val = i[1:]
    assert len(val) == 6
    try:
        val = int(val,16) #check its valid hex
    except ValueError as e:
        raise AssertionError

def validate_ecl(i):
    assert i in ['amb','blu','brn','gry','grn','hzl','oth']

def validate_pid(i):
    assert len(i) == 9
    int(i)

def validate_cid(i):
    pass

def parse_generated_passport_text_into_dict(yielded_lines):
    for line in yielded_lines:
        block = [
            item 
            for sublist in line
            for item in sublist.split(" ")
            ]

        # too lazy to make this a nice dict comprehension
        kv_pair = {}
        for item in block:
            i = item.split(":")
            kv_pair[i[0]] = i[1]
        yield kv_pair

def parse_passport_dict_into_dataclass(kv_pairs):
    for kv in kv_pairs:
        try:
            TravelCredentials(**kv)
            yield True
        except (TypeError, AssertionError) as e:
            yield False


if __name__ == "__main__":
    t = generate_single_passport_text()
    y = parse_generated_passport_text_into_dict(t)
    p = parse_passport_dict_into_dataclass(y)
    
    print(sum(p)) 