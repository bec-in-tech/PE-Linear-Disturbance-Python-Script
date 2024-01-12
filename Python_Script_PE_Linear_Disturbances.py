How to use Python Scripts: 

1. Open attribute table for final PE linear disturbances. 
2. Select column that needs to be updated (ex: Priority Level, Action Prescription)
3. Right click column and open "Field Calculator" 
4. In "Field Calculator" 


PriorityCalc(!Status!, !Use!, !Use_Level!)

def PriorityCalc(Status, Use, Use_Level):
    if Status == 'Closed' and Use == 'In Use'and Use_Level == 'Light':
        return 3
 
    if Status == 'Closed' and Use == 'In Use'and Use_Level == 'Moderate':
        return 2

    if Status == 'Closed' and Use == 'In Use'and Use_Level == 'High':
        return 1

    if Status == 'Closed' and Use == 'In Use'and Use_Level == 'Non-existent':
        return 0 

    else: 
        return 0


PriorityCalc(!Status!, !Use!, !Use_Level!)

def PriorityCalc(Status, Use, Use_Level):
    if Status == 'Closed' and Use == 'In Use'and Use_Level == 'Light':
      return 1

    elif Status == 'Closed' and Use == 'In Use' and Use_Level == 'Moderate':
      return 3

    elif Status == 'Closed' and Use == 'In Use' and Use_Level == 'Heavy':
      return 5

    elif Status == 'Closed' and Use == 'Not in Use' and Use_Level == ' ': 
      return 0 

    else:
      return 0


ActionCalc(!Use_Level!)

def ActionCalc(Use_Level):
    if Use_Level == 'Light':
      return 'Passive restoration, raking, VM if BSC is present'
   
    elif Use_Level == 'Moderate': 
      return 'Signs, VM/rock scatter, barrier'

    elif Use_Level == 'Heavy': 
      return 'Barriers, signs, VM/rock scatter, ripping, seeding'

    else:
      return 'N/A'


ActionCalc(!Use_Level!, !Use!, !Status!)

def ActionCalc(Use_Level, Use, Status):
    if Use_Level == 'Light' and Use == 'In Use' and Status == 'Closed': 
      return 'Passive restoration, raking, VM if BSC is present'

    elif Use_Level == 'Moderate' and Use == 'In Use' and Status == 'Closed':
      return 'Signs, VM/rock scatter, barrier'

    elif Use_Level == 'Heavy' and Use == 'In Use' and Status == 'Closed':
      return 'Barriers, signs, VM/rock scatter, ripping, seeding'

    elif Use_Level == 'Light' and Use == 'In Use' and Status == 'Open': 
      return 'None'

    elif Use_Level == 'Moderate' and Use == 'In Use' and Status == 'Open':
      return 'None'

    elif Use_Level == 'Heavy' and Use == 'In Use' and Status == 'Open':
      return 'None'

    elif Use_Level == ' ' and Use == 'Not in Use' and Status == 'Closed':
      return 'None' 

    elif Use_Level == ' ' and Use == 'In Use' and Status == 'Open': 
      return 'None'

    else:
      return 'N/A'


UseLevelCalc (!Use!)

def UseLevelCalc (Use): 
    if Use == 'Not in Use':
        return 'Non-existent'

    else: 
        return 'N/A'


UseLevelCalc (!Status!, !Use!)

def UseLevelCalc (Status, Use):
    if Status == 'Closed' and Use == 'Not in Use': 
      return 'Non-existent'



REPLACE

!Route_Type!.replace("Unimproved/ 2 Track", "Unimproved/2 Track")



OID	Route_Type	Wash	Surface_Pr	Suitablity	Obs_Use_1	Use_Level	Condition	Route_Widt	Recorder	Comment	Date	Length_mi	Field_Chec	Status	Use	Shape_Leng	Miles	Priority	Latitude	Longitude	Action
0	Single Track	Not a Wash	 	 	 	 	 	 	 	 	<Null>	0.070669	 	Closed	In Use	113.731233	0.070669	0	35.533729	-115.062273	N/A