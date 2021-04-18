word = "bottles"     # assign the value "bottles" (a string) to a new variable called worddatetime A combination of a date and a time. Attributes: ()
for beer_num in range(99,0,-1):
    print(beer_num, word, "of beer on the wall.")   # give the result for variable "word" and the loop beer_num
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")   # process the string
    if beer_num == 1:    # if condition of comparison of beer equals 1  
        print("No more bottles of beer on the wall")   # print string if condition satisfied
    else:    # if not satisfied 
        new_num = beer_num - 1     # A new variable is assigned 
        if new_num == 1:                #condition if the new variable equals 1
            word = "bottle"    # then word is assign to a string bottle
        print(new_num, word, "of beer on the wall") # the print process of the new variable 
        
    print()        # 