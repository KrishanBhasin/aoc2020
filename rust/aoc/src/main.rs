mod day1;

fn main() {
    let contents = day1::load_input_text();
    let matches = day1::locate_matching_group(2020, contents, 3);
    let answer = matches.iter().fold(1, |a, &b| a*b);
    println!("{:?}",answer)
}
