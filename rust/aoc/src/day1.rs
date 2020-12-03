use std::fs;
use itertools::Itertools;


fn load_input_text() -> Vec<i32> {
    // read the file and unwrap to panic if the file isn't readable
    let contents = fs::read_to_string("day-1-input.txt")
        .unwrap();

    let numbers: Vec<i32> = 
        contents.trim().split('\n')
        .map(String::from) // convert from reference &str to String value
        .map(|s| s.parse().unwrap()) // parse into i32 type (inferred)
        .collect();
        
    numbers
}


fn locate_matching_group( value_to_match: i32, input_list: Vec<i32>, number_to_match: i32) -> Vec<i32> {
    let combs = input_list
        .into_iter()
        .combinations(number_to_match as usize);
    
    for c in combs {
        if c.iter().fold(0, |a, &b| a + b) == value_to_match {
            return c
        }
    }
    panic!("Not found!")
}

pub fn solve() -> i32 {
    let contents = load_input_text();
    let matches = locate_matching_group(2020, contents, 3);
    let answer = matches.iter().fold(1, |a, &b| a*b);
    answer
}