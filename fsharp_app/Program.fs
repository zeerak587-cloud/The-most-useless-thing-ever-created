open System

[<EntryPoint>]
let main args =
    let input =
        if args.Length > 0 then args.[0]
        else ""

    printfn "[F#] upper: %s" (input.ToUpper())
    printfn "[F#] reversed: %s" (new string(Array.rev (input.ToCharArray())))
    printfn "[F#] length: %d" input.Length

    0