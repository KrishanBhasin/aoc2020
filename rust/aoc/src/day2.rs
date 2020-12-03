use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::any::type_name;

fn load_input_text() -> io::Result<io::Lines<io::BufReader<File>>> {
    let file = File::open("day-2-input.txt")?;
    Ok(io::BufReader::new(file).lines())
}

fn parse_password_requirements(
    pass_reqs:io::Result<io::Lines<io::BufReader<File>>>
) -> () {
    if let Ok(lines) = pass_reqs {
        for line in lines {
            if let Ok(reqs) = line {
                let mut split = reqs.split(" ");
                let allowed_range: Vec<u32 > = split.next()
                                                .unwrap()
                                                .split("-")
                                                .map(|x| x.parse())
                                                .map(|x| x.unwrap())
                                                .collect();
                let letter = split.next()
                                    .unwrap()
                                    .strip_suffix(":")
                                    .unwrap();
                let password = split.next().unwrap();
                let pw = password_requirements_object {
                    password:password.to_string(),
                    allowed_range: allowed_range,
                    letter:letter.to_string()
                };
            }        
        }        
    }
}

struct password_requirements_object {
    password: String,
    letter: String,
    allowed_range: Vec<u32>
}

pub fn solve() -> () {
    let i = load_input_text();
    let j = parse_password_requirements(i);
}