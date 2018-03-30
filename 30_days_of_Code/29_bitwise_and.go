package main

import (
	"fmt"
	"os"
	// "regexp"
	// "sort"
)

func main() {
	var t int
	_, err := fmt.Scanf("%d", &t)
	if err != nil { // handle error
		fmt.Println(err)
		os.Exit(2)
	}

	for i := 0; i < t; i++ {
		var n, k int
		_, err1 := fmt.Scanf("%d %d", &n, &k)
		if err1 != nil { // handle error
			fmt.Println(err1)
			os.Exit(2)
		}
		fmt.Println(n, k)
		fmt.Println(n & k)
	}
}
