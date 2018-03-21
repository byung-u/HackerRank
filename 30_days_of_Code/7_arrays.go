package main

import (
	"bufio"
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

	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	text = strings.TrimSuffix(text, "\n")

	sp := strings.Split(text, " ")
	for i := len(sp) - 1; i >= 0; i-- {
		fmt.Print(sp[i])
		fmt.Print(" ")
	}
	fmt.Print("\n")
}
