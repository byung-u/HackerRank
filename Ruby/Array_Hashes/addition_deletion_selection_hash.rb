#!/usr/bin/env ruby


hackerrank.store(543121, 100)
hackerrank.keep_if {|key, value| key.is_a? Integer}
hackerrank.delete_if {|key, value| key.even?}




h1 = Hash.new
h1.default = 0
puts h1
puts "-------"

h2 = {1 => 1, 2 => 4, 3 => 9, 4 => 16, 5 => 25}
puts h2
puts "-------"
h2.keep_if {|key, value| key % 2 == 0} # or h.delete_if {|key, value| key % 2 != 0}
puts h2
puts "-------"


h2 = {1 => 1, 2 => 4, 3 => 9, 4 => 16, 5 => 25}
puts h2
puts "-------"
h2.delete_if {|key, value| key % 2 == 0}
puts h2
puts "-------"
