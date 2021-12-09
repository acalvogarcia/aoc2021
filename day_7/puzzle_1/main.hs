import Data.List.Split (splitOn)
import Data.List (sort)

main :: IO ()
main = do
  userInput <- getContents
  print $ floor . getFuelUsed $ mapInput userInput

mapInput :: Read b => [Char] -> [b]
mapInput xs = map read (splitOn "," xs)

getMedian :: (Ord p, Fractional p) => [p] -> p
getMedian [] = error "Empty list for median"
getMedian xs
  | odd len = xs !! mid
  | even len = evenMedian
    where
      sorted_xs = sort xs
      len = length xs
      mid = len `div` 2
      evenMedian = (sorted_xs !! (mid-1) + sorted_xs !! mid) / 2
getMedian _ = error "This shouldn't be here"

getFuelUsed :: (Ord a, Fractional a) => [a] -> a
getFuelUsed xs = foldl (\x y -> x + abs(y-finalPosition)) 0 xs
  where finalPosition = getMedian xs
