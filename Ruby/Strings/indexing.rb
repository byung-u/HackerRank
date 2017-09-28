#!/usr/bin/env ruby
require 'scanf'

def serial_average(string)
    s = string.split('-')
    "#{s[0]}-#{((s[1].to_f + s[2].to_f)/2).round(2)}"
end

def serial_average_failed(s)
    serial = s[0, 3]
    x = s[4, 5].to_f
    y = s[10, 5].to_f
    z = '%.3f' % ((x + y)/2.to_f)
    z = '%.2f' % z.to_f.round(2)
    puts "#{serial}-#{z}"
end

serial_average('002-10.00-20.00')
serial_average('001-12.43-56.78')

#str = "Hello World!"
#puts str[str.size]
#puts str[str.size-1]
#puts str[-1]
#puts str[-2]
#puts str[0]
#puts str[0, 4]
#puts str[6, 4]
#puts str[-1, 1]
#
#str = "Heelo"
#str[str.size, 0] = " World"
#puts str
#
#tmp = 123
#puts "Hello #{tmp}"
#
