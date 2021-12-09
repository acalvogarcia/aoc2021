import Data.List.Split (splitOn)

main :: IO ()
main = do
  userInput <- getContents
  print $ floor . getFuelUsed $ mapInput userInput

mapInput :: Read b => [Char] -> [b]
mapInput xs = map read (splitOn "," xs)

getFuelUsed :: RealFrac a => [a] -> a
getFuelUsed starters = optimalFuelUsed
  where
    moveFuel n = n*(n+1)/2
    average = sum starters / fromIntegral (length starters)
    fuelUsed x = sum [moveFuel (abs (y-fromIntegral x)) | y <- starters]
    optimalFuelUsed = min (fuelUsed $ floor average) (fuelUsed $ ceiling average)
