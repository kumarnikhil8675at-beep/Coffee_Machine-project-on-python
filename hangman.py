word='python'
new=['_']*len(word)

worng=1
while True:
    user=input("enter the word: ")
    if(len(user)!=1):
        print("Enter only single word")
    else:
        if(user in word):
            if(user in new):
                print("Alredy enter please try differnt letter")
            else: 
                for i,val in enumerate(word):
                    if (user==val):
                        new[i]=val
        
                print(''.join(new))
        
                if(list(word)==new):
                    print("you win")
                    break

        else:
            if(worng==6):
                print("you lose")
                print("Ecuatual word is : ",word)
                break
            else:
                worng+=1
                print("try one more time")