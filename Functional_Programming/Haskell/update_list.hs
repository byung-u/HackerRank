-- list comprehensions
-- [x*2 | x <- [1..5]] -- [2, 4, 6, 8, 10]
-- with a conditional
-- [x*2 | x <- [1..5], x*2 > 4] -- [6, 8, 10]

f arr = [abs x | x <- arr]

-- This part handles the Input/Output and can be used as it is. Do not change or modify it.
main = do
   inputdata <- getContents
   putStrLn $ show $ f $ map (read :: String -> Int) $ lines inputdata
