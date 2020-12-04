use std::fs;

fn load_input_text() -> Vec<String> {
    // read the file and unwrap to panic if the file isn't readable
    let contents = fs::read_to_string("day-3-input.txt")
        .unwrap();

    let layout: Vec<String> = 
        contents.trim().split('\n')
        .map(String::from) // convert from reference &str to String value
        .collect();
        
    layout
}

#[derive(Debug)]
struct Point {
    x: usize,
    y: usize
}

#[derive(Debug)]
struct Move {
    x: usize,
    y: usize
}

#[derive(Debug)]
struct LocalGeology {
    layout: Vec<String>,
    position: Point,
    movement: Move
}

impl LocalGeology {
    fn move_position(mut self) -> LocalGeology {
        self.position = Point{x: self.position.x + self.movement.x, y: self.position.y + self.movement.y};
        self.position.x = self.position.x % self.layout[0].chars().count();

        self
    }

    fn is_on_tree(&self) -> bool {
        let row: &str = &self.layout[self.position.y];
        let cell: String = row.chars().nth(self.position.x).unwrap().to_string();
        if cell == "#" {
            return true;
        }
        return false;
    }

    fn has_reached_end(&self) -> bool {
        if self.position.y >= (self.layout.len()-1) {
            return true
        }
        return false;
    }

    fn slide_to_end(&self) -> () {
        ()
    }

}


pub fn solve() -> u32 {
    let movement_choices = [(1,1),(3,1),(5,1),(7,1),(1,2)];
    let mut movement_tree_sum: Vec<u32> = Vec::new();


    for choice in movement_choices.iter() {
        let start_position = Point{x:0, y:0};
        let mut r = LocalGeology{
            layout: load_input_text(),
            position: start_position,
            movement: Move{x: choice.0, y: choice.1}
        };
        let mut sum = 0;

        loop {
            if r.has_reached_end() == true {
                break;
            }
            r = r.move_position();
            sum += r.is_on_tree() as u32
        }
        movement_tree_sum.push(sum);
        println!("Done {:?}! Sum is {}", choice, sum);
    }

    let total = movement_tree_sum.iter().fold(1, |acc,x| acc * x);
    total
}