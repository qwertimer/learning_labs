package main

import (
	"fmt"
	"os"
)

func main() {
	var name string
	var s, sep string
	name = "There"
	if len(os.Args) > 1 {
		name = os.Args[1]
	}
	fmt.Printf("Hi %v!\n", name)
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}
	fmt.Println(s)
}
