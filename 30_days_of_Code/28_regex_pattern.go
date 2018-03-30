package main

import (
	"fmt"
	"os"
	"regexp"
	"sort"
)

func main() {
	var result []string
	var validName = regexp.MustCompile(`[a-z]`)
	var validEmail = regexp.MustCompile(`[a-z]@gmail.*`)
	var t int
	_, err := fmt.Scanf("%d", &t)
	if err != nil { // handle error
		fmt.Println(err)
		os.Exit(2)
	}

	for i := 0; i < t; i++ {
		var name, email string
		_, err1 := fmt.Scanf("%s %s", &name, &email)
		if err1 != nil { // handle error
			fmt.Println(err1)
			os.Exit(2)
		}
		if validName.MatchString(name) == false {
			continue
		} else if validEmail.MatchString(email) == false {
			continue
		} else if len(name) > 20 {
			continue
		} else if len(email) > 50 {
			continue
		}
		result = append(result, name)
	}
	// fmt.Println(result)
	sort.Strings(result)
	for _, r := range result {
		fmt.Println(r)
	}
}
