from typing import Generator, Tuple, List

def load_input_text() -> Generator[str, None, None]:
    with open("python/day2/day-2-input.txt") as f:
        input = f.readlines()
    for i in input:
        yield i.strip()


def parse_password_requirements(pass_reqs: Generator[str, None, None]) -> Generator[Tuple[List[int], str, str], None, None]:
    for req in pass_reqs:
        allowed_range, letter, password = tuple(req.split(" "))
        allowed_range = [int(a) for a in allowed_range.split("-")]
        letter = letter.strip(":")
        password = password.strip()
        yield allowed_range, letter, password

def check_password_requirements_count(parsed_password_reqs):
    for p in parsed_password_reqs:
        allowed_range, letter, password = p
        letter_count = 0
        for l in password:
            if l == letter:
                letter_count+=1
        if letter_count >= allowed_range[0] and letter_count<= allowed_range[-1]:
            yield True
        else:
            yield False


def check_password_requirements_position(parsed_password_reqs):
    for p in parsed_password_reqs:
        allowed_positions, letter, password = p
        pos1 = allowed_positions[0] - 1
        pos2 = allowed_positions[1] - 1

        if (password[pos1] == letter) ^ (password[pos2] == letter):
            yield True
        else:
            yield False


if __name__ == "__main__":
    i = load_input_text()
    reqs = parse_password_requirements(i)
    print(sum(check_password_requirements_position(reqs)))