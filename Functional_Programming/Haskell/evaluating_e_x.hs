import Control.Applicative
import Control.Monad
import System.IO

-- exp_series :: Double -> [Double]
-- exp_series a = scanl (*) 1.0 [ a/k | k <- [1..] ]
-- 
-- my_exp :: Double -> Int -> Double
-- my_exp a n = sum (take n (exp_series a))
-- 
solve :: Double -> Double
solve 0.0 = 1.0
solve x = pow 1.0 5

pow :: Double -> Integer -> Double
pow n 0 = 1.0
pow n p = n * pow n p-1

fact :: Integer -> Double
fact 0 = 1
fact 1 = 1
fact n = fromIntegral n * fact (n-1)

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    forM_ [1..n] $ \a0  -> do
        x_temp <- getLine
        let x = read x_temp :: Double
        print(solve(x))

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret          
