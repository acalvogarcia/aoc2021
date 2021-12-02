main :: IO ()
main = do 
  userInput <- getContents
  let finalPosition = calculateFinalPosition $ mapInput userInput
  print $ getFinalResult finalPosition
  where getFinalResult (a,b) = a*b

mapInput :: String -> [([Char], Int)]
mapInput userInput = 
  map (makeSecondInt . words) (lines userInput)

makeSecondInt :: [[Char]] -> ([Char], Int)
makeSecondInt [x,y] =  (x,read y :: Int)
makeSecondInt _ = error "Not valid value"

newPosition :: Num a => (a, a) -> ([Char], a) -> (a, a)
newPosition acc ("forward",y) = (fst acc + y, snd acc)
newPosition acc ("down",y) = (fst acc, snd acc + y)
newPosition acc ("up",y) = (fst acc, snd acc - y)
newPosition _ _ = error "Not valid value"

calculateFinalPosition :: [([Char], Int)] -> (Int, Int)
calculateFinalPosition = foldl newPosition (0,0)