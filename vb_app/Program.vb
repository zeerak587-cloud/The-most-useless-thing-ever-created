Module Program
    Sub Main(args As String())
        Dim input As String = If(args.Length > 0, args(0), "")

        Console.WriteLine("[VB.NET] upper: " & input.ToUpper())
        Console.WriteLine("[VB.NET] reversed: " & StrReverse(input))
        Console.WriteLine("[VB.NET] length: " & input.Length)
    End Sub
End Module