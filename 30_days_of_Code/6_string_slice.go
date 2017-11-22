package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var n int

	_, err1 := fmt.Scanf("%d", &n)
	if err1 != nil { // handle error
		fmt.Println(err1)
		os.Exit(2)
	}

	for i := 0; i < n; i++ {
		var s string

		_, err2 := fmt.Scanf("%s", &s)
		if err2 != nil { // handle error
			fmt.Println(err2)
			os.Exit(2)
		}
		sp := strings.Split(s, "")
		var s1, s2 []string
		for j := 0; j < len(sp); j++ {
			if j%2 == 0 {
				s1 = append(s1, sp[j])
			} else {
				s2 = append(s2, sp[j])
			}
		}

		fmt.Println(strings.Join(s1[:], ""), strings.Join(s2[:], ""))
	}
}
