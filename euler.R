#Jan 1, 1900 was a Monday
#Jan 1, 1901 was a Tuesday
#Leap year is divisible by 4 unless it's a century, then by 400.
#Sundays on first of the month from Jan 1 1901 to Dec 31, 2000

1:31 -> Jan -> Mar -> May -> July -> Aug -> Oct -> Dec
1:30 -> Sept -> Apr -> June -> Nov
1:28 -> Feb
1:29 -> FebLeap
c("T","W","Th","F","Sat","Sun","Mon") -> Weekdays
c(Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec) -> RegYear
c(Jan, FebLeap, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec) -> LeapYear

cbind(Weekdays, rep(c(rep(RegYear,3), LeapYear), 25)) -> eight_years
table(subset(eight_years, Weekdays=="Sun")) -> results
#Sunday appears 171 times as the first of the month
