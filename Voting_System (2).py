import time
 
# NOMINEE NAMES
nominee_1="AMNOL ALI"
nominee_2="SHEHAM"
# NOMIEES VOTES 
nom_1_vote=0
nom_2_vote=0

# VOTERS LIST
voter_id=[]
txt_file=open("data.txt")
for row in txt_file:
    a=int(row.split(".")[0])
    voter_id.append(a)
txt_file.close()
total=(len(voter_id))



while True:
    if voter_id==[] or time.strftime("%H:%M")=="05:00":
        print("--------VOTING SESSION OVER-------")
        print(voter_id)
        if nom_1_vote>nom_2_vote:
            print(f"{nominee_1} won by {nom_1_vote} out of {total}")
            break
            
        elif nom_2_vote>nom_1_vote:
            print(f"{nominee_2} won by {nom_2_vote} out of {total}")
            break
                         

    else:   
        voter=int(input("Enter Your ID : "))
        if voter in voter_id:
            print("YOU ARE A VOTER")
            vote = int(input("Enter your vote 1 or 2 : "))
            if vote==1:
                nom_1_vote+=1
                print("THANKS! FOR CASTING VOTE")
                voter_id.remove(voter)
            elif vote==2:
                nom_2_vote+=1
                print("THANKS! FOR CASTING VOTE")
                voter_id.remove(voter)
            else:
                print("CORRECT YOUR NOMINEE")
    
        else:
            print("You are not a Voter or You have Casted your vote??")
        
