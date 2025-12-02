package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func getRotationDistance(rotation string) int {
	value, _ := strconv.Atoi(rotation[1:])

	if rotation[0] == 'L' {
		value = -value
	}

	return value
}

const dialSize = 100

func turnDial(position, distance int) (newPosition, passZeroCount int) {
	fromZero := position + distance
	passZeroCount = max(fromZero, -fromZero) / dialSize
	if fromZero < 0 {
		passZeroCount += 1
	}
	newPosition = ((fromZero % dialSize) + dialSize) % dialSize 
	return newPosition, passZeroCount
}

const initialPosition = 50

func analyzeRotations(rotations []string) (endZeroCount, totalPassZeroCount int) {
	currentPosition := initialPosition
	for _ , rotation := range rotations {
		distance := getRotationDistance(rotation)
		newPosition, passZeroCount := turnDial(currentPosition, distance)

		currentPosition = newPosition
		totalPassZeroCount += passZeroCount
		
		if currentPosition == 0 {
			endZeroCount += 1
		}
	}

	return endZeroCount, totalPassZeroCount
}

func main() {
	file, _ := os.Open("./2025/1/input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var input []string

	for scanner.Scan() {
    	input = append(input, scanner.Text())
	}

	endZeroCount, passZeroCount := analyzeRotations(input)

	fmt.Printf("Password for part 1 is %v\n", endZeroCount)
	fmt.Printf("Password for part 2 is %v\n", passZeroCount)
}


