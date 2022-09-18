package main

import (
	"fmt"
	"log"
)

// Notes: We can then redirect stdout and error to files with
// 2> and 1>
func main() {
	fmt.Println("Hello World") //prints to stdout
	println("Hello World")     // prints to stderr
	log.Println("Hello World") // prints to stderr or file
}
