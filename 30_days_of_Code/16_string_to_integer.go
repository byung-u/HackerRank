package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var s string
	_, err1 := fmt.Scanf("%s", &s)
	if err1 != nil { // handle error
		fmt.Println(err1)
		os.Exit(2)
	}
	if _, err2 := strconv.Atoi(s); err2 == nil {
		fmt.Println(s)
	} else {
		fmt.Println("Bad String")
	}
}
