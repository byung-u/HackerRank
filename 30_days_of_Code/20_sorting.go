package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n int
	var swap int
	var temp int
	var input_arr = []int{}
	_, err1 := fmt.Scanf("%d", &n)
	if err1 != nil { // handle error
		fmt.Println(err1)
		os.Exit(2)
	}

	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	text = strings.TrimSuffix(text, "\n")
	sp := strings.Split(text, " ")

	for _, i := range sp {
		j, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}
		input_arr = append(input_arr, j)
	}

	swap = 0
	for i := 0; i < len(input_arr)-1; i++ {
		for j := i + 1; j < len(input_arr); j++ {
			if input_arr[i] > input_arr[j] {
				swap++
				temp = input_arr[i]
				input_arr[i] = input_arr[j]
				input_arr[j] = temp
			}
		}
	}
	fmt.Println("Array is sorted in", swap, "swaps.")
	fmt.Println("First Element:", input_arr[0])
	fmt.Println("Last Element:", input_arr[len(input_arr)-1])
}
