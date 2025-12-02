package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func getRotationValue(rotation string) int {
	value, _ := strconv.Atoi(rotation[1:])

	if rotation[0] == 'L' {
		value = -value
	}

	return value
}

const dialSize = 100

func turnDial(position, increment int) (newPosition, passZeroCount int) {
	newPosition = (position + increment) % (dialSize)
	if newPosition < 0 {
		newPosition = dialSize + newPosition
	}

	passZeroCount = increment / dialSize
	if passZeroCount < 0 {
		passZeroCount = -passZeroCount
	}

	if increment > 0 && newPosition < position {
		passZeroCount += 1
	} else if increment < 0 && newPosition > position {
		passZeroCount += 1
	}
	return newPosition, passZeroCount

}

const initialPosition = 50

func analyzeRotations(rotations []string) (passwordPart1, passwordPart2 int) {
	position := initialPosition
	var passZeroCount int
	for _ , rotation := range rotations {
		position, passZeroCount = turnDial(position, getRotationValue(rotation))
		
		if position == 0 {
			passwordPart1 += 1
		}
		passwordPart2 += passZeroCount

		fmt.Printf("%s -> %v\n", rotation, position)
	}

	return passwordPart1, passwordPart2
}

func main() {
	file, _ := os.Open("./2025/1/input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var input []string

	for scanner.Scan() {
    	input = append(input, scanner.Text())
	}

	passwordPart1, passwordPart2 := analyzeRotations(input)

	fmt.Printf("Password for part 1 is %v\n", passwordPart1)
	fmt.Printf("Password for part 2 is %v\n", passwordPart2)
}


