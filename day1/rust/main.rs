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
    //historic_total.insert(0);
    let part2_cycle = input.iter().cycle();

    for x in part2_cycle {
        if historic_total.contains(&running_total) {break;}
        historic_total.insert(running_total);
        running_total += x;
    }




// Output    
    println!("Part 1: \t{}", part1);
    println!("Part 2: \t{:?}", running_total);
}