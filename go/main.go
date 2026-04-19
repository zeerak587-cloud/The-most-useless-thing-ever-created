package main
import (
    "fmt"
    "os"
)

func main() {
    input := os.Args[1]
    fmt.Println("[Go] length:", len(input))
}