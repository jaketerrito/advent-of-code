package main 

import (
	"testing"
)

func TestGetRotationValue(t *testing.T) {
	tests := []struct {
		name string
		input string
		expected int
	}{
		{
			name: "Positive",
			input: "R32",
			expected: 32,
		},
		{
			name: "Negative",
			input: "L1234567",
			expected: -1234567,
		},
	}


	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := getRotationValue(tc.input)
			if result != tc.expected {
				t.Errorf("Result was incorrect for input %v. Expected: %v, Got: %v", tc.input, tc.expected, result)
			}
		})
	}
}


func TestTurnDial(t *testing.T) {
	tests := []struct {
		name string
		start int
		input int
		expectedPos int
		expectedZeros int
	}{
		{
			name:"A",
			start: 50,
			input: -50,
			expectedPos: 0,
			expectedZeros: 0,
		},
		{
			name: "B",
			start: 99,
			input: 1,
			expectedPos: 0,
			expectedZeros: 1,
		},
		{
			name: "C",
			start: 50,
			input: -64,
			expectedPos: 86,
			expectedZeros: 1,
		},
		{
			name: "D",
			start: 0,
			input: -1001,
			expectedPos: 99,
			expectedZeros: 11,
		},
		{
			name: "E",
			start: 99,
			input: 1001,
			expectedPos: 0,
			expectedZeros: 11,
		},
		{
			name: "F",
			start: 50,
			input: 250,
			expectedPos: 0,
			expectedZeros: 3,
		},
	}
	

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			pos, zeros := turnDial(tc.start, tc.input)
			if pos != tc.expectedPos || zeros != tc.expectedZeros {
				t.Errorf("Expected (%d, %d), got (%d, %d)",
					tc.expectedPos, tc.expectedZeros, pos, zeros)
			}
		})
	}
}

func TestTurnDialA(t *testing.T) {
	start := 50
	input := -50
	expectedPosition, expectedZeros := 0 , 0
	
	resultPosition, resultZeros := turnDial(start, input)

	if resultPosition != expectedPosition ||  resultZeros != expectedZeros {
		t.Errorf("Result was incorrect for input %v. Expected: %v - %v, Got: %v - %v", input, expectedPosition, expectedZeros, resultPosition, resultZeros)
	}
}

func TestTurnDialB(t *testing.T) {
	start := 99
	input := 1
	expectedPosition, expectedZeros :=  0, 1

	resultPosition, resultZeros := turnDial(start, input)

	if resultPosition != expectedPosition ||  resultZeros != expectedZeros {
		t.Errorf("Result was incorrect for input %v. Expected: %v - %v, Got: %v - %v", input, expectedPosition, expectedZeros, resultPosition, resultZeros)
	}
}


func TestAnalyzeRotations(t *testing.T) {
	tests := []struct {
		name string
		input []string
		expectedPart1 int
		expectedPart2 int
	}{
		{
			name:"A",
			input: []string{"L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"},	
			expectedPart1: 3,
			expectedPart2: 6,
		},
		{
			name: "B",
			input: []string{"L774"},
			expectedPart1: 0,
			expectedPart2: 8,
		},
	}
	
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			resultPart1, resultPart2 := analyzeRotations(tc.input)
			if resultPart1 != tc.expectedPart1 || resultPart2 != tc.expectedPart2 {
				t.Errorf("Result was incorrect for input %s. Expected: %v - %v, Got: %v - %v", tc.input, tc.expectedPart1, tc.expectedPart2, resultPart1, resultPart2)	
			}
		})
	}
}
