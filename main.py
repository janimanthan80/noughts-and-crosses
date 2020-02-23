print("\t\t\tLet's get started!\n")

def tic_tac_toe():
  select = {"1": "-", 
            "2": "-", 
            "3": "-",
            "4": "-", 
            "5": "-", 
            "6": "-",
            "7": "-", 
            "8": "-", 
            "9": "-"}

  print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
  + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
  + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

  print("\nPlease enter Capital 'O' and 'X' to play this game and enjoy your game....!")
  choose1 = "O"
  choose2 = "X"
  
  for i in range(0,9):
    enter = input("\nEnter Your your seat number: ")
    if enter == "1":
      
      enter1 = input("Enter Your choice: ")
      if enter1 == choose1:
        select["1"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["1"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"]) 

    if enter == "2":

      enter1 = input("Enter Your Choice: ")
      if enter1 == choose1:
        select["2"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["2"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"]) 


    
    if enter == "3":

      enter1 = input("Enter Your Choice: ")
      if enter1 == choose1:
        select["3"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["3"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"]) 


    
    if enter == "4":

      enter1 = input("Enter Your Choice: ")
      if enter1 == choose1:
        select["4"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["4"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])          

    
    if enter == "5":

      enter1 = input("Enter Your Choice: ")
      if enter1 == choose1:
        select["5"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["5"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])    
        
    
    
    if enter == "6":

      enter1 = input("Enter Your Choice: ")
      if enter1 == choose1:
        select["6"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["6"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])


    
    if enter == "7":

      enter1 = input("Enter Your Choice: ")
      if enter1 == choose1:
        select["7"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["7"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"]) 


    
    if enter == "8":

      enter1 = input("Enter Your Choice: ")
      if enter1 == choose1:
        select["8"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["8"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])  


    
    if enter == "9":

      enter1 = input("Enter Your Choice: ")
      if enter1 == choose1:
        select["9"] = choose1
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])

      if enter1 == choose2:
        select["9"] = choose2  
        print(select["1"] + "\t" + select["2"] + "\t" + select["3"]
        + "\n" + select["4"] + "\t" + select["5"] + "\t" + select["6"]
        + "\n" + select["7"] + "\t" + select["8"] + "\t" + select["9"])   
    
    if select["1"] == choose1 and select["2"] == choose1 and select["3"] == choose1:
      print("YeYYY You won this game") 

      break 

    elif select["4"] == choose1 and select["5"] == choose1 and select["6"] == choose1:
      print("YeYYY You won this game") 

      break

    elif select["7"] == choose1 and select["8"] == choose1 and select["9"] == choose1:
      print("YeYYY You won this game") 

      break  

    elif select["1"] == choose1 and select["4"] == choose1 and select["7"] == choose1:
      print("YeYYY You won this game") 

      break

    elif select["2"] == choose1 and select["5"] == choose1 and select["8"] == choose1:
      print("YeYYY You won this game") 

      break

    elif select["3"] == choose1 and select["6"] == choose1 and select["9"] == choose1:
      print("YeYYY You won this game") 

      break
    
      
    elif select["3"] == choose1 and select["5"] == choose1 and select["7"] == choose1:
      print("YeYYY You won this game") 

      break

    elif select["1"] == choose1 and select["5"] == choose1 and select["9"] == choose1:
      print("YeYYY You won this game") 

      break     


    elif select["1"] == choose2 and select["2"] == choose2 and select["3"] == choose2:
      print("YeYYY You won this game") 

      break

    elif select["4"] == choose2 and select["5"] == choose2 and select["6"] == choose2:
      print("YeYYY You won this game") 

      break

    elif select["7"] == choose2 and select["8"] == choose2 and select["9"] == choose2:
      print("YeYYY You won this game") 

      break  

    elif select["1"] == choose2 and select["4"] == choose2 and select["7"] == choose2:
      print("YeYYY You won this game") 

      break

     

    elif select["2"] == choose2 and select["5"] == choose2 and select["8"] == choose2:
      print("YeYYY You won this game") 

      break

    elif select["3"] == choose2 and select["6"] == choose2 and select["9"] == choose2:
      print("YeYYY You won this game") 

      break     

    elif select["1"] == choose2 and select["5"] == choose2 and select["9"] == choose2:
      print("YeYYY You won this game") 

      break     

    elif select["3"] == choose2 and select["5"] == choose2 and select["7"] == choose2:
      print("YeYYY You won this game") 

      break       
  
  else:
    print("Match Draw!")
 
tic_tac_toe()            
