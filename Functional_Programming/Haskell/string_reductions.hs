import Data.List

-- main = interact nub
-- The last statement in a 'do' block must be an expression

main :: IO ()
main = do c <- getChar
          putChar c
