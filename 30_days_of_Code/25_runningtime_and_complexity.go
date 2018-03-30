package main

import (
	"fmt"
	"math"
	"os"
)

func is_prime(n int) bool {
	if n < 2 {
		return false
	} else if n == 2 {
		return true
	} else if n%2 == 0 {
		return false
	}

	var sr int // square root
	sr = int(math.Sqrt(float64(n))) + 1

	for i := 3; i < sr; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var n int
	_, err1 := fmt.Scanf("%d", &n)
	if err1 != nil { // handle error
		fmt.Println(err1)
		os.Exit(2)
	}

	for i := 0; i < n; i++ {
		var num int

		_, err2 := fmt.Scanf("%d", &num)
		if err2 != nil { // handle error
			fmt.Println(err2)
			os.Exit(2)
		}

		if is_prime(num) == true {
			fmt.Println("Prime")
		} else {
			fmt.Println("Not prime")
		}
	}
}
