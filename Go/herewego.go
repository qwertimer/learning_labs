package main

import "fmt"

func main() {
	// Variables and constants
	fmt.Println("Hello World")

	var age int = 40
	var favNum float64 = 1.68
	randNum := 1

	fmt.Println(age, favNum, randNum)

	var num0ne = 1.000
	var num99 = 0.999
	const pi float64 = 3.14159
	fmt.Print(num0ne - num99)

	var (
		varA = 2
		var3 = 3
	)
	var myName string = "Tim"
	fmt.Println(varA, var3, pi, len(myName))

	var is40 bool = true

	// if statements
	if is40 == true {
		fmt.Println("hello")
	} else if is40 == false {
		fmt.Println("h")
	} else {
		fmt.Println("F")
	}

	// for loop
	i := 0
	for i <= 10 {
		fmt.Println(i)
		i++
	}

	for j := 0; j < 5; j++ {
		fmt.Println(j)
	}

	//switch cases
	yourAge := 29
	switch yourAge {
	case 16:
		fmt.Println("Hello")
	case 18:
		fmt.Println("Hi")
	default:
		break
	}

	//slices
	numSlice := []int{5, 4, 3, 2, 1}
	numSlice2 := numSlice[3:5]

	fmt.Println("numSlice2[0] = ", numSlice2[0])

	numSlice3 := make([]int, 5, 10) // slice of type int, first value, max length 10
	numSlice3 = append(numSlice, 0, -1)
	fmt.Println(numSlice3)
	//map
	//collection of key value pairs (Dictionary in python

	presAge := make(map[string]int)
	presAge["apple"] = 3
	fmt.Println(presAge)
	numbers := []float64{4, 3, 2, 1}
	fmt.Println("Sum : ", addThemUp(numbers))

}

func addThemUp(numbers []float64) float64 {
	sum := 0.0
	for _, val := range numbers {
		sum += val
	}
	return sum
}
