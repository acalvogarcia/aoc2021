main = do
  userInput <- getContents
  let numbers = map read (lines userInput) :: [Int]
  print $ increasesAmount numbers

increasesAmount :: (Ord a, Num a) => [a] -> Int
increasesAmount (a:b:c:d:as) = fromEnum (a + b + c < b + c + d) + increasesAmount (b:c:d:as)
increasesAmount _ = 0
