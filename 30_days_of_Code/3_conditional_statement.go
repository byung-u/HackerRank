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

	if n%2 == 1 {
		fmt.Println("Weird")
	} else {
		if 2 <= n && n < 5 {
			fmt.Println("Not Weird")
		} else if 3 <= n && n <= 20 {
			fmt.Println("Weird")
		} else {
			fmt.Println("Not Weird")
		}
	}
}
