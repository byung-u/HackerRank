#!/usr/bin/env ruby


def skip_animals(animals, skip)
    result = Array.new
    animals.each_with_index do |item, index|
        next if index < skip
        result.push("#{index}:#{item}")
    end
    return result
end


skip_animals(['leopard', 'bear', 'fox', 'wolf'], 2)
