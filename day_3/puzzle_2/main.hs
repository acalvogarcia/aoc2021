import Data.Char (digitToInt)

main :: IO ()
main = do
  userInput <- getContents
  let oxygenAndCO2 = (getOxygenValue (mapInput userInput) 0, getCO2Value (mapInput userInput) 0)
  print $ round $ getFinalValue oxygenAndCO2

mapInput :: String -> [[Float]]
mapInput = map (map (toEnum . digitToInt)) . lines

getGasValue :: (Float -> Bool) -> [[Float]] -> Int -> [Float]
getGasValue _ [x] _ = x
getGasValue operator xs i = getGasValue operator relevantElements (i+1)
  where
    average = foldl (\acc x -> acc + x!!i) 0 xs / toEnum (length xs)
    reference = fromIntegral $ fromEnum $ operator average
    relevantElements = filter (\x -> x!!i == reference) xs

getOxygenValue :: [[Float]] -> Int -> [Float]
getOxygenValue = getGasValue (>=0.5)

getCO2Value :: [[Float]] -> Int -> [Float]
getCO2Value = getGasValue (<0.5)

getFinalValue :: ([Float], [Float]) -> Float
getFinalValue (a,b) = binaryListToNumber a * binaryListToNumber b
  where binaryListToNumber = foldl (\acc x -> acc * 2 + x) 0
