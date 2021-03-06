from helper import Coordinate_map, lines

USA_map = Coordinate_map(lines("""
[TCL]  33.23   87.62  Tuscaloosa,AL
[FLG]  35.13  111.67  Flagstaff,AZ
[PHX]  33.43  112.02  Phoenix,AZ
[PGA]  36.93  111.45  Page,AZ
[TUS]  32.12  110.93  Tucson,AZ
[LIT]  35.22   92.38  Little Rock,AR
[SFO]  37.62  122.38  San Francisco,CA
[LAX]  33.93  118.40  Los Angeles,CA
[SAC]  38.52  121.50  Sacramento,CA
[SAN]  32.73  117.17  San Diego,CA
[SBP]  35.23  120.65  San Luis Obi,CA
[EKA]  41.33  124.28  Eureka,CA
[DEN]  39.75  104.87  Denver,CO
[DCA]  38.85   77.04  Washington/Natl,DC
[MIA]  25.82   80.28  Miami Intl,FL
[TPA]  27.97   82.53  Tampa Intl,FL
[JAX]  30.50   81.70  Jacksonville,FL
[TLH]  30.38   84.37  Tallahassee,FL
[ATL]  33.65   84.42  Atlanta,GA
[BOI]  43.57  116.22  Boise,ID
[CHI]  41.90   87.65  Chicago,IL
[IND]  39.73   86.27  Indianapolis,IN
[DSM]  41.53   93.65  Des Moines,IA
[SUX]  42.40   96.38  Sioux City,IA
[ICT]  37.65   97.43  Wichita,KS
[LEX]  38.05   85.00  Lexington,KY
[NEW]  30.03   90.03  New Orleans,LA
[BOS]  42.37   71.03  Boston,MA
[PWM]  43.65   70.32  Portland,ME
[BGR]  44.80   68.82  Bangor,ME
[CAR]  46.87   68.02  Caribou Mun,ME
[DET]  42.42   83.02  Detroit,MI
[STC]  45.55   94.07  St Cloud,MN
[DLH]  46.83   92.18  Duluth,MN
[STL]  38.75   90.37  St Louis,MO
[JAN]  32.32   90.08  Jackson,MS
[BIL]  45.80  108.53  Billings,MT
[BTM]  45.95  112.50  Butte,MT
[RDU]  35.87   78.78  Raleigh-Durh,NC
[INT]  36.13   80.23  Winston-Salem,NC
[OMA]  41.30   95.90  Omaha/Eppley,NE
[LAS]  36.08  115.17  Las Vegas,NV
[RNO]  39.50  119.78  Reno,NV
[AWH]  41.33  116.25  Wildhorse,NV
[EWR]  40.70   74.17  Newark Intl,NJ
[SAF]  35.62  106.08  Santa Fe,NM
[NYC]  40.77   73.98  New York,NY
[BUF]  42.93   78.73  Buffalo,NY
[ALB]  42.75   73.80  Albany,NY
[FAR]  46.90   96.80  Fargo,ND
[BIS]  46.77  100.75  Bismarck,ND
[CVG]  39.05   84.67  Cincinnati,OH
[CLE]  41.42   81.87  Cleveland,OH
[OKC]  35.40   97.60  Oklahoma Cty,OK
[PDX]  45.60  122.60  Portland,OR
[MFR]  42.37  122.87  Medford,OR
[AGC]  40.35   79.93  Pittsburgh,PA
[PVD]  41.73   71.43  Providence,RI
[CHS]  32.90   80.03  Charleston,SC
[RAP]  44.05  103.07  Rapid City,SD
[FSD]  43.58   96.73  Sioux Falls,SD
[MEM]  35.05   90.00  Memphis Intl,TN
[TYS]  35.82   83.98  Knoxville,TN
[CRP]  27.77   97.50  Corpus Chrst,TX
[DRT]  29.37  100.92  Del Rio,TX
[IAH]  29.97   95.35  Houston,TX
[SAT]  29.53   98.47  San Antonio,TX
[LGU]  41.78  111.85  Logan,UT
[SLC]  40.78  111.97  Salt Lake Ct,UT
[SGU]  37.08  113.60  Saint George,UT
[CNY]  38.77  109.75  Moab,UT
[MPV]  44.20   72.57  Montpelier,VT
[RIC]  37.50   77.33  Richmond,VA
[BLI]  48.80  122.53  Bellingham,WA
[SEA]  47.45  122.30  Seattle,WA
[ALW]  46.10  118.28  Walla Walla,WA
[GRB]  44.48   88.13  Green Bay,WI
[MKE]  42.95   87.90  Milwaukee,WI
[CYS]  41.15  104.82  Cheyenne,WY
[SHR]  44.77  106.97  Sheridan,WY
"""))
