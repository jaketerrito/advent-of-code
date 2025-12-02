package main 

import (
	"testing"
)

func TestGetRotationDistance(t *testing.T) {
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
			distance := getRotationDistance(tc.input)
			if distance != tc.expected {
				t.Errorf("Result was incorrect for input %v. Expected: %v, Got: %v", tc.input, tc.expected, distance)
			}
		})
	}
}


func TestTurnDial(t *testing.T) {
	tests := []struct {
		name string
		start int
		input int
		expectedPosition int
		expectedPassZeroCount int
	}{
		{
			name:"A",
			start: 50,
			input: -50,
			expectedPosition: 0,
			expectedPassZeroCount: 1,
		},
		{
			name: "B",
			start: 99,
			input: 1,
			expectedPosition: 0,
			expectedPassZeroCount: 1,
		},
		{
			name: "C",
			start: 50,
			input: -64,
			expectedPosition: 86,
			expectedPassZeroCount: 1,
		},
		{
			name: "D",
			start: 0,
			input: -1,
			expectedPosition: 99,
			expectedPassZeroCount: 0,
		},
		{
			name: "E",
			start: 99,
			input: 1001,
			expectedPosition: 0,
			expectedPassZeroCount: 11,
		},
		{
			name: "F",
			start: 50,
			input: 250,
			expectedPosition: 0,
			expectedPassZeroCount: 3,
		},
		{	
			name: "G",
			start: 50,
			input: 1000,
			expectedPosition: 50,
			expectedPassZeroCount: 10,
		},
	}
	

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			position, passZeroCount := turnDial(tc.start, tc.input)
			if position != tc.expectedPosition || passZeroCount != tc.expectedPassZeroCount {
				t.Errorf("Expected (%d, %d), got (%d, %d)",
					tc.expectedPosition, tc.expectedPassZeroCount, position, passZeroCount)
			}
		})
	}
}


func TestAnalyzeRotations(t *testing.T) {
	tests := []struct {
		name string
		input []string
		expectedEndZeroCount int
		expectedPassZeroCount int
	}{
		{
			name:"A",
			input: []string{"L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"},	
			expectedEndZeroCount: 3,
			expectedPassZeroCount: 6,
		},
		{
			name: "B",
			input: []string{"L999", "R4321", "L73"},
			expectedEndZeroCount: 0,
			expectedPassZeroCount: 54,
		},
	}
	
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			endZeroCount, passZeroCount := analyzeRotations(tc.input)
			if endZeroCount != tc.expectedEndZeroCount || passZeroCount != tc.expectedPassZeroCount {
				t.Errorf("Result was incorrect for input %s. Expected: %v - %v, Got: %v - %v", tc.input, tc.expectedEndZeroCount, tc.expectedPassZeroCount, endZeroCount, passZeroCount)	
			}
		})
	}
}
