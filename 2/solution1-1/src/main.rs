use std::{
    fs::{self, File},
    io::Read,
    path::Path,
};

fn main() {
    let input_path = Path::new("/home/richardkenyon/projects/aoc2024/2/input.txt");

    // parse lines
    let file_contents = fs::read_to_string(input_path).unwrap();
    for line in file_contents.lines() {
        let mut report_numbers_split = line.split_ascii_whitespace();
        let mut prev_num: i32 = report_numbers_split.next().unwrap().parse().unwrap();

        while let next_num = report_numbers_split.next().unwrap().parse().unwrap() {}
    }
}
