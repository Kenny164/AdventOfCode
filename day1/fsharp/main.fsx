let rec hash (md5 : System.Security.Cryptography.MD5) root n (target : string) =
    let bytes = md5.ComputeHash( System.Text.Encoding.UTF8.GetBytes(root + n.ToString()))
    let str = System.BitConverter.ToString(bytes).Replace("-", "")
    match str.[0..target.Length-1] with
        | c when c = target -> n.ToString()
        | _ -> hash md5 root (n + 1) target

let find = hash (System.Security.Cryptography.MD5.Create()) "yzbqklnj" 1
let p1 = find "00000"
let p2 = find "000000"

printfn "Part1: %s\n\n\nPart2: %s" p1 p2