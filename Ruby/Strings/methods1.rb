#!/usr/bin/env ruby


def process_text(string)
    # string = string.map{|a| a.chomp.strip}
    # puts string.join(' ')
    string.map{|a| a.chomp.strip}.join(' ')
end

process_text(["Hi, \n", " Are you having fun?    "])
