package main

import (
	"fmt"
	"log"

	"github.com/qwertimer/learning_labs/Go/rwxrob/hello/foo"
)

func main() {
	//println("Hello from stderr")
	fmt.Println("Hello World!")
	log.Println("Debug: Hello World!")
	foo.Hello()
}
