-- data Car = Car {make :: String, model :: String, year :: Int}
newtype Car make model year = Car (make, model, year) deriving (Eq, Show)

instance (Num make, Num model, Num year) => Num (Car make model year) where
  Car (make1, model1, year1) + Car (make2, model2, year2) = Car (make1, model1, year1 + year2)
  Car (make1, model1, year1) - Car (make2, model2, year2) = Car (make1, model1, year1 - year2)
  Car (make1, model1, year1) * Car (make2, model2, year2) = Car (make1, model1, year1 * year2)
  abs (Car (make, model, year)) = Car (make, model, abs year)
  signum (Car (make, model, year)) = Car (make, model, signum year)
  fromInteger i = Car (fromInteger i, fromInteger i, fromInteger i)