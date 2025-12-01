package main 

import (
	"testing"
)

func TestGetRotationValue(t *testing.T) {
	input := "R32"
	expected := 32
	result := getRotationValue(input)

	if result != expected {
		t.Errorf("Result was incorrect for input %v. Expected: %v, Got: %v", input, expected, result)
	}
}

func TestTurnDial(t *testing.T) {
	start := 99
	input := 1
	expected := 0
	result, _ := turnDial(start, input)
	if result != expected {
		t.Errorf("Result was incorrect for input %v. Expected: %v, Got: %v", input, expected, result)
	}
}

func TestTurnDialZeros(t *testing.T) {
	start := 1
	input := 99
	expectedPosition, expectedZeros :=  0, 1

	resultPosition, resultZeros := turnDial(start, input)

	if resultPosition != expectedPosition ||  resultZeros != expectedZeros {
		t.Errorf("Result was incorrect for input %v. Expected: %v - %v, Got: %v - %v", input, expectedPosition, expectedZeros, resultPosition, resultZeros)
	}

}

func TestAnalyzeRotationsPart1(t *testing.T) {
	input := []string{"L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"}
	expected := 3

	result := analyzeRotationsPart1(input)

	if result != expected {
		t.Errorf("Result was incorrect for input %s. Expected: %v, Got: %v", input, expected, result)	
	}
}
