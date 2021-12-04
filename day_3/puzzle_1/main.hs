import Data.Char (digitToInt)

main :: IO ()
main = do
  userInput <- getContents
  let gammaAndEpsilon = getGammaAndEpsilon . getAverages $ mapInput userInput
  print $ getFinalValue gammaAndEpsilon

getFinalValue :: ([Int], [Int]) -> Int
getFinalValue (a,b) = binaryListToNumber a * binaryListToNumber b
  where binaryListToNumber = foldl (\acc x -> acc * 2 + x) 0

getGammaAndEpsilon :: (Ord a, Fractional a) => [a] -> ([Int], [Int])
getGammaAndEpsilon xs = (map (\x -> fromEnum $ x>0.5) xs, map (\x -> fromEnum $ x<=0.5) xs)

getAverages :: [[Float]] -> [Float]
getAverages xs = map (/denominator) $ getMostCommon xs
  where
    getMostCommon = foldl1 (zipWith (+))
    denominator = toEnum $ length xs

mapInput :: String -> [[Float]]
mapInput = map (map (toEnum . digitToInt)) . lines
