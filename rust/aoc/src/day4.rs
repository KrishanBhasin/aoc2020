use std::fs;
use std::collections::HashMap;

fn load_input_text() -> Vec<String> {
    // read the file and unwrap to panic if the file isn't readable
    let contents = fs::read_to_string("day-4-input.txt")
        .unwrap();

    let layout: Vec<String> = 
        contents.trim().split("\n\n")
        .map(String::from) // convert from reference &str to String value
        .collect();
        
    layout
}

struct TravelCredentials {
    byr: String,
    iyr: String,
    eyr: String,
    hgt: String,
    hcl: String,
    ecl: String,
    pid: String,
    cid: Option<String>
}

fn parse_input_into_blocks(text_lines: Vec<String>) -> Vec<Vec<String>> {

    let new_lines: Vec<Vec<String>> = text_lines
                        .iter()
                        .map(|s| s.split_whitespace().map(String::from).collect())
                        .collect();
    
    return new_lines;
}

fn check_if_blocks_are_valid_travel_docs(input_blocks: Vec<Vec<String>>) -> Vec<bool> {
    let mut is_valid: Vec<bool> = Vec::new();
    for block in input_blocks {
        let mut map: HashMap<String, String> = HashMap::new();
        for k_v_entry in block {
            let k_v_split: Vec<&str> = k_v_entry.split(":").collect();
            map.insert(k_v_split[0].to_string(), k_v_split[1].to_string());
        }
        is_valid.push(check_if_key_exists(map, vec!["byr","iyr","eyr","hgt","hcl","ecl","pid"]))
    }
    return is_valid;
}

fn check_if_key_exists(map: HashMap<String, String>, keys: Vec<&str>) -> bool {
    for &section in keys.iter() {
        if !map.contains_key(section) {
            return false;
        }
    }
    return true;
}

pub fn solve() -> () {
    let input_blocks: Vec<Vec<String>> = parse_input_into_blocks(
        load_input_text()
    );
    let v = check_if_blocks_are_valid_travel_docs(input_blocks);
    let a = v.iter().fold(0, |sum, &x| {
        if x == true {
            sum + 1
        } else {
            sum
        }
    });
    println!("{:?}",a)
}