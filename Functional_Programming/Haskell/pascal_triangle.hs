module Main where
import System.IO

printPascal xs n
    | n==0      = return ()
    | otherwise = do putStrLn [y | ys <- map show xs, y <- ys ++ " "]
                     printPascal ([1] ++ [x+y | (x,y) <- zip xs (tail xs)] ++ [1]) (n-1)

main = do n <- readLn :: IO Int
          printPascal [1] n

-- pas m n 
--   | n == 0 = 1
--   | m == n = 1
--   | otherwise = pas (m-1) (n-1) + pas (m-1) n
-- 
-- row m = map (pas m) [0..m]
-- tri m = map (row) [0..(m-1)]
-- 
-- 
-- -- This part is related to the Input/Output and can be used as it is
-- -- Do not modify it
-- main = do
--    m <- readLn :: IO Int
--    print(tri m)
