import Data.List (group, sort)
import Data.List.Split (splitOn)

main :: IO ()
main = do
  userInput <- getContents
  print $ getSafePointsAmount $ getTravelledPoints $ mapInput userInput

mapInput :: String -> [[[Int]]]
mapInput = map (map mapPoint . splitOn " -> ") . lines
  where
    mapPoint x = map read (splitOn "," x) :: [Int]

getTravelledPointsFromMovement :: [[Int]] -> [[Int]]
getTravelledPointsFromMovement [[a,b], [c,d]]
  | a==c && b==d = [[a,b]]
  | b==d && a<c = [a,b]:getTravelledPointsFromMovement [[a+1, b], [c,d]]
  | b==d && a>c = [a,b]:getTravelledPointsFromMovement [[a-1, b], [c,d]]
  | a==c && b<d = [a,b]:getTravelledPointsFromMovement [[a, b+1], [c,d]]
  | a==c && b>d = [a,b]:getTravelledPointsFromMovement [[a, b-1], [c,d]]
  | otherwise = []
getTravelledPointsFromMovement _ = error "This shouldn't be here"

getTravelledPoints :: [[[Int]]] -> [[[Int]]]
getTravelledPoints = map getTravelledPointsFromMovement

getSafePointsAmount :: [[[Int]]] -> Int
getSafePointsAmount = length . filter (\xs -> length xs > 1) . group . sort . concat
