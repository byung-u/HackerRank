package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var t int
	_, err := fmt.Scanf("%d", &t)
	if err != nil { // handle error
		fmt.Println(err)
		os.Exit(2)
	}

	for i := 0; i < t; i++ {
		var n, k, attend int
		attend = 0

		_, err := fmt.Scanf("%d %d", &n, &k)
		if err != nil { // handle error
			fmt.Println(err)
			os.Exit(2)
		}

		reader := bufio.NewReader(os.Stdin)
		text, _ := reader.ReadString('\n')
		text = strings.TrimSuffix(text, "\n")
		sp := strings.Split(text, " ")
		for _, si := range sp {
			sj, err := strconv.Atoi(si)
			if err != nil {
				panic(err)
			}
			if sj < 0 { // attend
				attend += 1
			}
		}
		if attend < k {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
}
