#!/usr/bin/env ruby


def element_at(arr, index)
    # return the element of the Array variable `arr` at the position `index`
    # arr.at(index) # or
    # arr[index]
    arr[index]
end

def inclusive_range(arr, start_pos, end_pos)
    arr[start_pos..end_pos]
    # return the elements of the Array variable `arr` between the start_pos and end_pos (both inclusive)
end

def non_inclusive_range(arr, start_pos, end_pos)
    arr[start_pos...end_pos]
    # return the elements of the Array variable `arr`, start_pos inclusive and end_pos exclusive
end

def start_and_length(arr, start_pos, length)
    arr[start_pos, length]
    # return `length` elements of the Array variable `arr` starting from `start_pos`
end

arr = [9, 5, 1, 2, 3, 4, 0, -1]
puts arr[4]
puts arr.at(4)
puts "...."
puts arr[1..3]
puts "...."
puts arr[1...3]
puts "...."
puts arr[1,3]
