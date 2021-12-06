import Data.List.Split (splitOn)
import qualified Data.Map as Map

main :: IO ()
main = do
  userInput <- getContents
  print $ getLanternfishAmount 256 $ getInputMap $ mapInput userInput

mapInput :: [Char] -> [Int]
mapInput xs = map read (splitOn "," xs) :: [Int]

getInputMap :: (Ord a, Num a, Enum a) => [a] -> Map.Map a Int
getInputMap xs = Map.fromList [ (day, count day xs) | day <- [0..8]]
  where count day xs = length $ filter (==day) xs

getLanternfishAmount :: (Eq t, Num t, Ord k, Num k, Num p, Enum k) => t -> Map.Map k p -> p
getLanternfishAmount 0 map = sum $ Map.elems map
getLanternfishAmount day map = getLanternfishAmount (day-1) newMap
  where
    newMap = Map.fromList $ (8, bornLanternfish):(6, bornLanternfish + Map.findWithDefault 0 7 map):[ (i, Map.findWithDefault 0 (i+1) map) | i <- 7:[0..5]]
    bornLanternfish = Map.findWithDefault 0 0 map
