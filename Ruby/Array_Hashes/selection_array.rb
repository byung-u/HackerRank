#!/usr/bin/env ruby


def select_arr(arr)
  # select and return all odd numbers from the Array variable `arr`
    arr.select {|a| a.odd?}
end

def reject_arr(arr)
  # reject all elements which are divisible by 3
    arr.reject {|a| a.%(3).zero?}
end

def delete_arr(arr)
  # delete all negative elements
    arr.delete_if {|a| a < 0}
end

def keep_arr(arr)
  # keep all non negative elements ( >= 0)
    arr.keep_if {|a| a >= 0}
end

arr = [3, 4, 2, 1, 2, 3, 4, 5, 6]
puts arr.select {|a| a > 2}
puts "...."
puts arr.select {|a| a.odd? }
puts "...."
puts arr.reject {|a| a > 2}
puts "...."

arr = [3, 4, 2, 1, 2, 3, 4, 5, 6]
puts arr.drop_while {|a| a > 1}
puts "...."

arr = [3, 4, 2, 1, 2, 3, 4, 5, 6]
puts arr.delete_if {|a| a < 2}
puts "...."

arr = [3, 4, 2, 1, 2, 3, 4, 5, 6]
puts arr.keep_if {|a| a < 4}
puts "...."
