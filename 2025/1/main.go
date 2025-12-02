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

func turnDial(position, distance int) (newPosition, zeroCount int) {
	fromZero := position + distance
	// Full rotations made 
	zeroCount = max(fromZero, -fromZero) / dialSize
	// If the dial has gone to zero or below, and it didnt start at 0, count that
	if fromZero <= 0 && position != 0{
		zeroCount += 1
	}
	newPosition = ((fromZero % dialSize) + dialSize) % dialSize 
	return newPosition, zeroCount
}

const initialPosition = 50

func analyzeRotations(rotations []string) (endZeroCount, totalZeroCount int) {
	currentPosition := initialPosition
	for _ , rotation := range rotations {
		distance := getRotationDistance(rotation)
		newPosition, zeroCount := turnDial(currentPosition, distance)

		currentPosition = newPosition
		totalZeroCount += zeroCount
		
		if currentPosition == 0 {
			endZeroCount += 1
		}
		fmt.Printf("%v -> %v with result at %v - %v\n", rotation, currentPosition, endZeroCount, totalZeroCount)
	}

	return endZeroCount, totalZeroCount
}

func main() {
	file, _ := os.Open("./2025/1/input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var input []string

	for scanner.Scan() {
    	input = append(input, scanner.Text())
	}

	endZeroCount, zeroCount := analyzeRotations(input)

	fmt.Printf("Password for part 1 is %v\n", endZeroCount)
	fmt.Printf("Password for part 2 is %v\n", zeroCount)
}


