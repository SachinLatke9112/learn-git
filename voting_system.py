nominee1 = input("Enter the name of Nominee 1 :")
nominee2 = input("Enter the name of Nominee 2 :")

nm1_vote = 0
nm2_vote = 0
voter_id = [1,2,3,4,5,6,7,8,9,10]

total_voter = len(voter_id)

while True:
    if voter_id == []:
        print("Voting session is done !!")
        if(nm1_vote > nm2_vote):
            percentage = (nm1_vote/total_voter)*100
            print(nominee1,"has won election with ",percentage,"%")
            break
        elif(nm2_vote > nm1_vote):
            percentage = (nm2_vote/total_voter)*100
            print(nominee2,"has won election with ",percentage,"%")
            break
        else:
            print("Both having equal no of votes !!!! So some rule of those !! ")
            break
    
    voter = int(input("Enter the your voter_Id : "))
    if voter in voter_id:
        print("You are Voter !! ")
        voter_id.remove(voter)
        print("*-------------------*---------------------*")
        print("To give vote to ",nominee1 , "Press 1")
        print("To give vote to ",nominee2 , "Press 2")
        print("*-------------------*---------------------*")
        vote = int(input("Enter your important vote: "))
        if(vote == 1):
            nm1_vote+=1
            print(nominee1,"Thank you for your vote! !!")
        elif(vote == 2):
            nm2_vote+=1
            print(nominee2,"Thank you for your vote !!")
        elif(vote > 2):
            print("Check your pressed Key !!")
    else:
        print("You are not voter or You are voted already !! ")