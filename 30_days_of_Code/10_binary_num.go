package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func countConsecutive(n int64) int {
	b := strconv.FormatInt(n, 2)
	ss := fmt.Sprintf("%b", b)
	s := ss[11 : len(ss)-1]
	sp := strings.Split(s, "0")

	var max_len int
	max_len = 0
	for i, _ := range sp {
		if max_len < len(sp[i]) {
			max_len = len(sp[i])
		}
	}
	return max_len
}

func main() {
	var n int64
	_, err1 := fmt.Scanf("%d", &n)
	if err1 != nil { // handle error
		fmt.Println(err1)
		os.Exit(2)
	}

	fmt.Println(countConsecutive(n))
}
