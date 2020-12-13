
struct Scoreboard {
    scores: Vec<usize>,
    elves: Vec<usize>,
    idx: usize
}

impl Scoreboard {
    fn new(init_scores: Vec<usize>) -> Scoreboard {
        let elf_vec = init_scores.iter().enumerate().map(|(x,_)| x).collect();
        Scoreboard {scores: init_scores, elves: elf_vec, idx: 0}
    }
}

impl Iterator for Scoreboard {
    type Item = usize;

    fn next(&mut self) -> Option<Self::Item> {
        let score = self.scores[self.idx];
        self.idx += 1;
        let new_score: usize = self.elves.iter()
            .map(|&e| self.scores[e])
            .sum();
        
        if new_score >= 10 {
			self.scores.push(new_score / 10);
		}
		self.scores.push(new_score % 10);

        //self.scores.push(new_score);
        for e in &mut self.elves {
            *e = (*e + self.scores[*e] + 1) % self.scores.len();
        }
        Some(score)
    }
}

fn part1(input: usize, score_board: Scoreboard) -> String {
    let scores: Vec<usize> = score_board.take(input+10).collect();
    scores[input..(input+10)].iter().map(|x| x.to_string()).collect::<String>()
}

fn main(){
    let score_board = Scoreboard::new(vec![3, 7]);
    let part1_answer: String = part1(681901, score_board);



// Output
    // for out1 in score_board.take(10) {
    //     println!("{:?}\t", out1);
    // }

    println!("Part 1: \t{:?}", part1_answer);
    //println!("Part 2: \t{:?}", running_total);
}