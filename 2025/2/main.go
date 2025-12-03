package main

import (
	"strconv"
	"fmt"
	"os"
	"strings"
)

type idRange struct {
	start int
	end int
}

func getInvalidIds(currentRange idRange) []int {
	var midPoint int
	var strI string
	invalidIds := []int{}
	for i := currentRange.start; i <= currentRange.end; i ++ {
		strI = strconv.Itoa(i)
		if len(strI) % 2 == 0 {
			midPoint = len(strI) / 2
			if strI[:midPoint] == strI[midPoint:] {
				invalidIds = append(invalidIds, i)
			}
		}
	}
	return invalidIds
}

func getRange(rangeString string) (currentRange idRange) {
	rangeSplit := strings.Split(string(rangeString), "-")

	start, _ := strconv.Atoi(rangeSplit[0])
	end, _ := strconv.Atoi(rangeSplit[1])

	return idRange{
		start: start,
		end: end,
	}
}


func parseInputStr(input string) []idRange {
	idRanges := []idRange{}

	parts := strings.Split(input, ",")
	for _, part := range parts {
		idRange := getRange(part)
		idRanges = append(idRanges, idRange)

	}

	return idRanges
}

func getSumInvalidIds(input string) int {
	idRanges := parseInputStr(input)
	
	sum := 0
	for _, currentRange := range idRanges {
		invalidIds := getInvalidIds(currentRange)
		for _, id := range invalidIds {
			sum += id
		}
	}

	return sum
}

func main() {
	input, _ := os.ReadFile("./2025/2/input.txt")

	sum := getSumInvalidIds(strings.TrimSpace(string(input)))

	fmt.Print(sum)
}
