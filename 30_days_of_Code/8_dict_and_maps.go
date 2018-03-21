package main

import (
	"bufio"
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

	var m map[string]int
	m = make(map[string]int)

	for i := 0; i < n; i++ {
		var name string
		var phone_num int

		_, err2 := fmt.Scanf("%s %d", &name, &phone_num)
		if err2 != nil { // handle error
			fmt.Println(err2)
			os.Exit(2)
		}

		m[name] = phone_num
	}

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		input_name := scanner.Text()

		if m[input_name] == 0 {
			fmt.Println("Not found")
		} else {
			fmt.Printf("%s=%d\n", input_name, m[input_name])
		}
	}
}
