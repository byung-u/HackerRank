#!/usr/bin/env ruby


def neg_pos(arr, index)
    # return the element of the array at the position `index` from the end of the list
    # Clue : arr[-index]
    arr[-index]
end

def first_element(arr)
    # return the first element of the array
    # arr.first
    arr.first
end

def last_element(arr)
    # return the last element of the array
    # arr.last
    arr.last
end

def first_n(arr, n)
    # return the first n elements of the array
    arr.take(n)
end

def drop_n(arr, n)
    arr.drop(n)
    # drop the first n elements of the array and return the rest
end




arr = [9, 5, 1, 2, 3, 4, 0, -1]
puts arr[-1]
puts "...."
puts arr.first
puts "...."
puts arr.last
puts "...."
puts arr.take(3)
puts "...."
puts arr.drop(3)
