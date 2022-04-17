package main

import "fmt"

func main(){
	fmt.Println("Welcome")
  var name string
  var age int
	fmt.Printf("Enter your name: ")
	fmt.Scan(&name)
	fmt.Println(name)
	
	fmt.Printf("What is your age: ")
	fmt.Scan(&age)
	fmt.Println(age)

	if (age < 10) {
	  fmt.Println("YOU are too young")
		return
	} else {
	  fmt.Println("YOU are old")
	}
	fmt.Printf("Who is better Me or Mummy?")
	var answer string
	var answer2 string 
	fmt.Scan(&answer, &answer2)
  if answer + " " + answer2 == "RTX 3090" || answer + " " + answer2 == "rtx 3090" {
	
		fmt.Println("Correct")
	}

}

