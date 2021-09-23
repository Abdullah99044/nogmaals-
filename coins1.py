# name of student: Abdullah Al Kathiry
# number of student: 99044455
# purpose of program: Geld wisselen met munten
# function of program: 
# structure of program: 

while True:
  toPay = int(float(input('Amount to pay: ')) * 100) #Het bedrag dat de gebruiker moet betalen
  paid = int(float(input('Paid amount: '))  * 100) #Het bedrag dat de gebruiker heeft betaald
  change = paid - toPay #De resultaten van de betaling

  if change > 0: #Als change (de resultaten) groter is dan nul
    coinValue = 50 #Muntwaarde is vijftig
    
    while change > 0 and coinValue > 0: #terwijl het wisselgeld groter is dan nul en de muntwaarde groter is dan nul
      nrCoins = change // coinValue #Nr coins is change delen coinvalue
      while True: #nieuwe loop
        if nrCoins > 0: #Als nrcoins groters is dan nul
          print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Schrijf retourmaximum (aantal munten) en muntenwaarde in centen
          nrCoinsReturned = int(float(input('How many coins of ' + str(coinValue) +  ' cents did you return? '))) #invoer hoeveel munten heb je teruggegeven?
          change -= nrCoinsReturned * coinValue #Change  delen nrCoinsReturned en vermenigvuldig  coinValue
          if nrCoinsReturned == nrCoins: # als nrCoinsReturned gelijk aan nrCoins schrijf done
            print("done")
            break
          else: #anders de gebruiker moet het nog een keer doen
            print("Do it one more time")

  # comment on code below: 
        elif coinValue == 500: #Als muntwaarde is 500 cents 
          coinValue = 300                             #Dan muntwaarde is 300 cent
        elif coinValue == 300: #Als muntwaarde is 300
          coinValue = 200                             #Dan muntwaarde is 200 cent
        elif coinValue == 200: #Als muntwaarde is 200
          coinValue = 100                             #Dan muntwaarde is 100 cent
        elif coinValue == 100: #Als muntwaarde is  100
          coinValue = 50                              #Dan muntwaarde is 50 cent
        elif coinValue == 50: #Als muntwaarde is 50
          coinValue = 20                              #Dan muntwaarde is 20 cent
        elif coinValue == 20: #Als muntwaarde is 20
          coinValue = 10                              #Dan muntwaarde is 10 cent
        elif coinValue == 10: #Als muntwaarde is 10
          coinValue = 5                               #Dan muntwaarde is 5 cent
        elif coinValue == 5: #Als muntwaarde is 5
          coinValue = 2                               #Dan muntwaarde is 2 cent
        elif coinValue == 2: #Als muntwaarde is 2
          coinValue = 1                               #Dan muntwaarde is 1 cent
        else:
          coinValue = 0 #Anders muntwaarde is nul  
  elif change > 0: #Als change is groter dan nul
    print('Change not returned: ', str(change) , ' cents') #schrijf wijziging niet geretourneerd + change(resultaten)
  elif toPay > paid: 
    #als het bedrag dat de gebruiker moet betalen groeter dan het bedrag dat de gebruiker heeft betaald
    print("Payment is not enough! you have to pay:", str(change) + "cents")
    #schrijf 'Betalen is niet genoeg' en het bedrag dat hij moet betalen
    while True: #loop
      toPay = int(float(input('Paid amount: ')))
      #invoer het bedrag dat hij moet nog betalen
      if toPay == change : #als de gebruiker heeft betald het bedrag die hij  moet betalen
        print("done") #schrijf done
        break #stop het loop
      else: #Anders schrijf 'Betalen is niet genoeg' 
        print("Payment is not enough! you have to pay:", str(change) + "cents")  
  else:
    #Anders schrijf "done" en een overzicht van alle teruggegeven muntstukken
    print('done') 
    treugGegeven = toPay - paid
    print("Treug gegeven met munten" , treugGegeven , "cents")
    break