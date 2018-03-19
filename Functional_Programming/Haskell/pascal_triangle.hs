module Main where
import System.IO

pas m n 
  | n == 0 = 1
  | m == n = 1
  | otherwise = pas (m-1) (n-1) + pas (m-1) n

row m = map (pas m) [0..m]
tri m = map (row) [0..(m-1)]


-- This part is related to the Input/Output and can be used as it is
-- Do not modify it
main = do
   m <- readLn :: IO Int
   print(tri m)
