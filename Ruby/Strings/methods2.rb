#!/usr/bin/env ruby


def strike(s)
    # "<strike>#{s}</strike>"
    s = s.gsub(/^/, '<strike>')
    s = s.gsub(/$/, '</strike>')
    return s
end

def mask_article(s, modi)
    modi.each do |m|
        s = s.gsub(m, strike(m))
    end
    return  s
end

def main(string)
    puts string.include? "lo"
    puts string.include? "ol"
    puts string.gsub(/[aeiou]/, '*')
    puts string.gsub(/[aeiou]/, '')
    puts "--------"
    puts strike("Meou!")
    puts "--------"
    puts mask_article("hello wolrd this is crap! and worst ever ", ["crap", "worst"])
    # mask_article("hello wolrd this is crap! and worst ever ", ["crap", "worst"])
end

main("hello")
