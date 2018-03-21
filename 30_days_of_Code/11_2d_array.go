package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	arr := make([][]int, 6)
	for i := range arr {
		arr[i] = make([]int, 6)
	}

	for i := 0; i < 6; i++ {
		text, _ := reader.ReadString('\n')
		text = strings.TrimSuffix(text, "\n")

		sp := strings.Split(text, " ")
		for j := 0; j < 6; j++ {

			n, err := strconv.Atoi(sp[j])
			if err != nil {
				fmt.Println("error")
				continue
			}
			arr[i][j] = n
			fmt.Println(i, j, arr[i][j])
		}
	}

	var total, max_total int
	max_total = -1 << 15 // MinInt16
	for i := 0; i < 6-2; i++ {
		for j := 0; j < 6-2; j++ {
			total = 0

			for k := 0; k < 3; k++ {
				total += arr[i][j+k]
			}
			total += arr[i+1][j+1]

			for k := 0; k < 3; k++ {
				total += arr[i+2][j+k]
			}
			// fmt.Println(i, total)
			if max_total < total {
				max_total = total
			}
		}
	}
	fmt.Println(max_total)
}
