import Data.List (transpose)
import Data.List.Split (splitOn)

main :: IO ()
main = do
  userInput <- getContents
  print $ getResult $ mapInput (lines userInput)

checkLineCompleted :: (Num a, Eq a) => [a] -> [a] -> Bool
checkLineCompleted line drawn = all (`elem` drawn) line

checkCardCompleted :: (Num a, Eq a) => [[a]] -> [a] -> Bool
checkCardCompleted card drawn = any (`checkLineCompleted` drawn) card || any (`checkLineCompleted` drawn) (transpose card)

getWinner :: (Num b, Eq b) => [b] -> [[[b]]] -> [b] -> ([[b]], b, [b])
getWinner drawn allCards numbersToDraw
  | not (null completedCards) = (head completedCards, numberToCheck, numbersDrawn)
  | otherwise = getWinner numbersDrawn allCards (tail numbersToDraw)
  where
    completedCards = filter (`checkCardCompleted` numbersDrawn) allCards
    numbersDrawn = numberToCheck:drawn
    numberToCheck = head numbersToDraw

getResult :: (Num a, Eq a) => ([[[a]]], [a]) -> a
getResult (allCards, numbersToDraw) = sum (map (sum . getLineNotWinners) winnerCard) * winnerNumber
  where
    getLineNotWinners xs = filter (`notElem` numbersDrawn) xs
    (winnerCard, winnerNumber, numbersDrawn) = getWinner [] allCards numbersToDraw

mapInput :: [[Char]] -> ([[[Int]]], [Int])
mapInput xs = (getCards xs, getNumbersToDraw xs)
  where
    getNumbersToDraw xs = map read (splitOn "," $ head xs) :: [Int]
    getCards xs = map (map strToIntLine) (getChunks $ drop 2 xs)
    strToIntLine line = map read (words line) :: [Int]
    getChunks [] = []
    getChunks xs = let (chunk, rest) = break (=="") xs in chunk:getChunks (drop 1 rest)
