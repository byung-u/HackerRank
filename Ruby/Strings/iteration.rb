#!/usr/bin/env ruby
require 'scanf'


def count_multibyte_char(string)
    cnt = 0
    string.each_char do |x|
        if x.bytesize > 1
            cnt += 1
        end
    end
    cnt
end

count_multibyte_char("¥1000")
money = "¥1000"
# puts money.each_byte {|x| p x} # first char represented by two bytes
# puts money.each_char {|x| p x} # first char represented by two bytes
