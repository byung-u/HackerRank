import Control.Monad
import Data.List -- imports nub

valid :: [(Int, Int)] -> Bool
valid f = let (d, r) = unzip f in (length . nub) d == length d

main = do
    t <- fmap (read::String->Int) getLine
    forM [1..t] (\_->do
        n <- fmap (read::String->Int) getLine
        func <- forM [1..n] (\_->do fmap ((\[a, b]->(a,b)).map (read::String->Int).words) getLine :: IO (Int, Int))
        putStrLn $ if valid func then "YES" else "NO")
