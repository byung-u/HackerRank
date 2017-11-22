package main

import (
	"fmt"
	"os"
)

func main() {
	var n int

	_, err1 := fmt.Scanf("%d", &n)
	if err1 != nil { // handle error
		fmt.Println(err1)
		os.Exit(2)
	}

	for i := 1; i < 11; i++ {
		fmt.Printf("%d x %d = %d\n", n, i, n*i)
	}
}
