package main

import (
	"fmt"
	"os"
)

func main() {
	var d1, d2, m1, m2, y1, y2 int

	_, err1 := fmt.Scanf("%d %d %d", &d1, &m1, &y1)
	if err1 != nil { // handle error
		fmt.Println(err1)
		os.Exit(2)
	}
	_, err2 := fmt.Scanf("%d %d %d", &d2, &m2, &y2)
	if err2 != nil { // handle error
		fmt.Println(err2)
		os.Exit(2)
	}

	if y2 >= y1 {
		fmt.Println(0)
	} else if y2 >= y1 && m2 >= m1 && d2 >= d1 {
		fmt.Println(0)
	} else if y1 == y2 && m1 == m2 {
		fmt.Println((d1 - d2) * 15)
	} else if y1 == y2 {
		fmt.Println((m1 - m2) * 500)
	} else {
		fmt.Println(10000)
	}
}
