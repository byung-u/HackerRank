#!/usr/bin/env ruby
#
def end_arr_add(arr, element)
    # Add `element` to the end of the Array variable `arr` and return `arr`
    arr.push(element)
end

def begin_arr_add(arr, element)
    # Add `element` to the beginning of the Array variable `arr` and return `arr`
    arr.unshift(element)
end

def index_arr_add(arr, index, element)
    # Add `element` at position `index` to the Array variable `arr` and return `arr`
    arr.insert(index, element)
end

def index_arr_multiple_add(arr, index)
    # add any two elements to the arr at the index
    arr.insert(index, 4, 5)
end

arr = [9, 5, 1, 2, 3, 4, 0, -1]
arr.push(8)
puts arr
puts "...."

arr = [9, 5, 1, 2, 3, 4, 0, -1]
arr.insert(0, 12, 23, 24)
puts arr
puts "...."

arr = [9, 5, 1, 2, 3, 4, 0, -1]
arr.unshift(99, 12, 23, 24)
puts arr
puts "...."
