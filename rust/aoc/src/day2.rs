use std::fs::File;
use std::io::{self, BufRead};

fn load_input_text() -> io::Result<io::Lines<io::BufReader<File>>> {
    let file = File::open("day-2-input.txt")?;
    Ok(io::BufReader::new(file).lines())
}

fn parse_password_requirements(
    pass_reqs:io::Result<io::Lines<io::BufReader<File>>>
) -> Vec<PasswordRequirements> {
    let mut all_reqs: Vec<PasswordRequirements> = Vec::new();
    if let Ok(lines) = pass_reqs {
        for line in lines {
            if let Ok(reqs) = line {
                let req = convert_reqs_to_struct(reqs);
                all_reqs.push(req)
            }        
        }        
    }
    all_reqs
}

fn convert_reqs_to_struct(reqs: String) -> PasswordRequirements {
    let mut split = reqs.split_whitespace();
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
    
    PasswordRequirements {
        password:password.to_string(),
        allowed_range: allowed_range,
        letter:letter.to_string()
    }
}

#[derive(Debug)]
struct PasswordRequirements {
    password: String,
    letter: String,
    allowed_range: Vec<u32>
}

impl PasswordRequirements {
    fn check_password_requirements_count(self) -> bool {

        let char_count = self.password
                .chars()
                .map(|l| l==self.letter.chars().next().unwrap())
                .fold(0, |sum, x| {
                    if x == true {
                        sum + 1
                    } else {
                        sum
                    }
                });

        if char_count >= self.allowed_range[0] && char_count <= self.allowed_range[1] {
            return true;
        }
        return false;
    }
    fn check_password_requirements_position(self) -> bool {
        let c1 = self.password.chars().nth((self.allowed_range[0]-1) as usize).unwrap();
        let c2 = self.password.chars().nth((self.allowed_range[1]-1) as usize).unwrap();

        if (c1==self.letter.chars().next().unwrap()) ^ (c2==self.letter.chars().next().unwrap()) {
            return true;
        } else {
            return false;
        }

    }
}

pub fn solve() -> u32 {
    let i = load_input_text();
    let j = parse_password_requirements(i);
    let mut sum = 0;
    for c in j {
        if c.check_password_requirements_position() == true {
            sum = sum + 1
        } else {
            sum = sum
        }
    }
    sum
}