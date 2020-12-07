

def generate_single_boarding_pass():
    for row in open("python/day5/day-5-input.txt"):
        yield row.strip()

def check_row(b):
    row_code = list(b[0:7])
    for i, letter in enumerate(row_code):
        #convert to binary in place
        row_code[i] = '1' if letter == "B" else '0'

    # parse binary into base10
    row_num = int("".join(row_code),2)
    return row_num

def check_column(b):
    col_code = list(b[7:])
    for i, letter in enumerate(col_code):
        #convert to binary in place
        col_code[i] = '1' if letter == "R" else '0'

    # parse binary into base10
    col_num = int("".join(col_code),2)
    return col_num


def parse_boarding_pass_code(boarding_passes):
    for b in boarding_passes:
        row = check_row(b)
        column = check_column(b)
        seat_id = calculate_seat_id(row, column)
        yield(row, column, seat_id)

def calculate_seat_id(r, c):
    return (r * 8) + c

def find_missing_seats(r,c,sid):
    

if __name__ == "__main__":
    b = generate_single_boarding_pass()
    b = parse_boarding_pass_code(b)
    print(max(b))
