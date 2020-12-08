def generate_single_block():
    lines_to_yield = []
    for row in open("python/day6/day-6-input.txt", "r"):
        lines_to_yield.append(row)
        if len(lines_to_yield)>=2  and lines_to_yield[-2].endswith("\n") and lines_to_yield[-1]=="\n":
            
            del lines_to_yield[-1]
            
            yield lines_to_yield
            lines_to_yield = []

def deduplicate_block_letters(block_of_answers):
    for block in block_of_answers:
        b = [list(a.strip()) for a in block]
        b = [item for sublist in b for item in sublist]
        b = list(set(b))
        yield b

def generate_length_of_list(deduped_answers):
    for ans in deduped_answers:
        yield len(ans)

def get_common_answers_from_block(block_of_answers):
    for block in block_of_answers:
        shared = set(block[0].strip()).intersection(*[b.strip() for b in block[1:]])
        yield shared

if __name__ == "__main__":
    b = generate_single_block()
    b = get_common_answers_from_block(b)
    b = generate_length_of_list(b)

    print(sum(b))
