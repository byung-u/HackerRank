#!/usr/bin/env ruby

def scoring(array)
    array.each do |user|
        user.update_score
    end
end


