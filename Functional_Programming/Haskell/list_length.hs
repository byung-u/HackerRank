len :: [a] -> Int
len lst = length lst

-- This part handles the Input/Output and can be used as it is. Do not change or modify it.
main = do
   inputdata <- getContents
   putStrLn $ show $ len $ map (read :: String -> Int) $ lines inputdata
