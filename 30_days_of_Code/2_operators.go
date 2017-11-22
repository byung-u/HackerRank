package main
import (
  "fmt"
  "os"
)

func Round(val float64) int {
    if val < 0 {
        return int(val-0.5)
    }
    return int(val+0.5)
}

func main() {
    var c, tip, tax float64

    _, err1 := fmt.Scanf("%f", &c)
    if err1 != nil { // handle error
        fmt.Println(err1)
        os.Exit(2)
    }

    _, err2 := fmt.Scanf("%f", &tip)
    if err2 != nil { // handle error
        fmt.Println(err2)
        os.Exit(2)
    }

    _, err3 := fmt.Scanf("%f", &tax)
    if err3 != nil { // handle error
        fmt.Println(err3)
        os.Exit(2)
    }

    total := c + c * (tip / 100) + c * (tax / 100)

    // fmt.Println(c, tip, tax)
    // fmt.Println(total)
    fmt.Printf("The total meal cost is %d dollars.\n", Round(total))

}
