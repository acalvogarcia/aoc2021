main = do
  userInput <- getContents
  let numbers = map read (lines userInput) :: [Int]
  print $ increasesAmount numbers

increasesAmount :: Ord a => [a] -> Int
increasesAmount (a:b:as) = fromEnum (a < b) + increasesAmount (b:as)
increasesAmount _ = 0
