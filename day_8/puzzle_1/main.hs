import Data.List.Split (splitOn)

main :: IO ()
main = do
  userInput <- getContents
  print $ getResult $ mapInput userInput

mapInput :: String -> [[[[Char]]]]
mapInput = map (map (splitOn " ") . splitOn " | ") . lines

getResult :: [[[[a]]]] -> Int
getResult = sum . map (\x -> length . filter (\y -> length y `elem` [2,3,4,7]) $ x!!1)
