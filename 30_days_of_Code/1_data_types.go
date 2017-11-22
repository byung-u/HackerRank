package main

import (
	"bufio"
	"fmt"
	"os"
	//"reflect"
	"strconv"
)

func main() {

	var i uint64 = 4
	var d float64 = 4.0
	var s string = "HackerRank "

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()

		n, err := strconv.Atoi(line)
		if err == nil { // Integer
			fmt.Println(uint64(n) + i)
			continue
		}

		f, err := strconv.ParseFloat(line, 64)
		if err == nil { // Integer
			fmt.Printf("%.1f\n", f+d)
			continue
		}

		fmt.Printf("%s%s\n", s, line)
	}
}
