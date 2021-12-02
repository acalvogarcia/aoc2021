main :: IO ()
main = do 
  userInput <- getContents
  let finalPosition = calculateFinalPosition $ mapInput userInput
  print $ getFinalResult finalPosition
  where getFinalResult (a,b,_) = a*b

mapInput :: String -> [([Char], Int)]
mapInput userInput = 
  map (makeSecondInt . words) (lines userInput)

makeSecondInt :: [[Char]] -> ([Char], Int)
makeSecondInt [x,y] =  (x,read y :: Int)
makeSecondInt _ = error "Not valid value"

newPosition :: Num a => (a, a, a) -> ([Char], a) -> (a, a, a)
newPosition (a,b,c) ("forward",y) = (a + y, b + y*c, c)
newPosition (a,b,c) ("down",y) = (a, b, c + y)
newPosition (a,b,c) ("up",y) = (a, b, c - y)
newPosition _ _ = error "Not valid value"

calculateFinalPosition :: [([Char], Int)] -> (Int, Int, Int)
calculateFinalPosition = foldl newPosition (0,0,0)