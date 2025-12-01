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

const maxPosition = 99

func turnDial(position, increment int) (newPosition, zeros int) {
	newPosition = position + increment

	zeros = (newPosition - position)

	newPosition = newPosition % (maxPosition + 1)

	
	return newPosition, zeros
}

const initialPosition = 50

func analyzeRotationsPart1(rotations []string) (password int) {
	position := initialPosition
	for _ , rotation := range rotations {
		position, _ = turnDial(position, getRotationValue(rotation))
		if position == 0 {
			password += 1
		}
	}

	return password
}
func main() {
	file, _ := os.Open("./2025/1/input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var input []string

	for scanner.Scan() {
    	input = append(input, scanner.Text())
	}

	passwordPart1 := analyzeRotationsPart1(input)

	fmt.Printf("Password for part 1 is %v", passwordPart1)
}


