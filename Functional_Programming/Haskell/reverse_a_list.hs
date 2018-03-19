rev [] = []
rev (x:xs) = rev xs ++ [x]

main = do 
    n <- readLn :: IO Int 
    inputdata <- getContents 
    let 
        numbers = map read (lines inputdata) :: [Int] 
    print (rev(numbers))
