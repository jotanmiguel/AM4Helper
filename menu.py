print("Welcome!")
cmd = input(">")

import APIs.AM4Tools as am4tools
import tools.DistCalculator as dc

print(dc.calcDistance(am4tools.SearchAirport("LPPT"), am4tools.SearchAirport("LPMA")))

 