package main

import (
	"testing"
	"github.com/stretchr/testify/assert"

)
func TestCountInvalidIds(t *testing.T) {
	tests := []struct{
		input idRange
		expectedResult []int
	}{
		{
			input: idRange{
				start: 11,
				end: 22,
			},
			expectedResult: []int{11,22},
		},
		{
			input: idRange{
				start: 95,
				end: 115,
			},
			expectedResult: []int{99},
		},
		{
			input: idRange{
				start: 998,
				end: 1012,
			},
			expectedResult: []int{1010},
		},
		{
			input: idRange{
				start: 1188511880,
				end: 1188511890,
			},
			expectedResult: []int{1188511885},
		},
		{
			input: idRange{
				start: 222220,
				end: 222224,
			},
			expectedResult: []int{222222},
		},
		{
			input: idRange{
				start: 1698522,
				end: 1698528,
			},
			expectedResult: []int{},
		},
		{
			input: idRange{
				start: 446443,
				end: 446449,
			},
			expectedResult: []int{446446},
		},
		{
			input: idRange{
				start: 38593856,
				end: 38594862,
			},
			expectedResult: []int{38593859},
		},
	}
	for _, test := range tests {
		assert.Equal(t, test.expectedResult, getInvalidIds(test.input), "Input: %v", test.input)
	}
}


func TestSumInvalidIds(t *testing.T) {
	input := "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
	expected := 1227775554

	assert.Equal(t, expected, getSumInvalidIds(input))

}
