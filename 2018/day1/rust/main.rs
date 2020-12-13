//use std::fs;
use std::collections::HashSet;

fn main(){
// Setup
    let input: Vec<isize> = std::fs::read_to_string("../../inputs/day1.txt")
        .expect("Something went wrong reading the file")
            .lines()
            .map(|x| x.parse::<isize>().unwrap())
            .collect();


// Part 1
    let part1: isize = input.iter().sum();


// Part 2
    let mut running_total: isize = 0;
    let mut historic_total: HashSet<isize> = HashSet::new();

    for x in input.iter().cycle() {
        if !historic_total.insert(running_total) {break;}
        running_total += x;
    }
    

// Output    
    println!("Part 1: \t{}", part1);
    println!("Part 2: \t{:?}", running_total);
}