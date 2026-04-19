import System.Environment (getArgs)
import Data.Char (toUpper)

main = do
    args <- getArgs
    let input = if null args then "" else head args

    putStrLn $ "[Haskell] upper: " ++ map toUpper input
    putStrLn $ "[Haskell] reversed: " ++ reverse input
    putStrLn $ "[Haskell] length: " ++ show (length input)