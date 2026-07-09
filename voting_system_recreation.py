# Max candidate is preferred to be 9
candidate_list = ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Candidate 5", "Candidate 6", "Candidate 7", "Candidate 8", "Candidate 9"]


# Vote count
total_votes = 0
total_vote_count = []
for name in candidate_list:
    total_vote_count.append(0)
invalid_votes = 0

# Voting system
user_vote = None
while user_vote != 999887:    
    sn = 1
    
    # Greet user! (Because yes)
    print("\nWelcome to voting portal! Please read the names of the candidates and cast your votes carefully. Invalid votes will be discarded!\n\n")
    
    # Start of table
    print("+", "-"*5, "+", "-"*26, "+", sep="")
    print("|", "SN.", "|", " "*9, "Name", " "*9, "|")
    print("+", "-"*5, "+", "-"*26, "+", sep="")

    # Listing candidate
    for name in candidate_list:
        # Padding calculation
        total_padding_name = 26 - len(name)
        left_padding_name = total_padding_name//2
        right_padding_name = total_padding_name - left_padding_name
        total_padding_sn = 5 - len(str(sn))
        left_padding_sn = total_padding_sn//2
        right_padding_sn = total_padding_sn - left_padding_sn
    
        # Drawing table with candidate name
        print("|", " "*left_padding_sn, sn, " "*right_padding_sn, "|", " "*left_padding_name, name, " "*right_padding_name, "|", sep="")
        print("+", "-"*5, "+", "-"*26, "+", sep="")
        
        sn += 1

    # Vote chooser
    user_vote = int(input("Cast you vote (Enter SN and press enter):\n> "))
    if user_vote == 999887:
        print()
    elif user_vote > len(candidate_list) or user_vote <= 0:
        print("\nVote failed! Please try again, restarting portal...")
        invalid_votes += 1
        total_votes += 1
    else:
        print("\nYou successfully voted:", candidate_list[user_vote - 1], "\n\n\n\n\n\n")
        total_vote_count[user_vote - 1] += 1 
        total_votes += 1

# Results (displays up to 1,000,000 votes without breaking formatting)
display = 0
print("Results are:\n\n")

print("Total votes:", total_votes)
print("Valid votes:", total_votes - invalid_votes)
print("Invalid votes:", invalid_votes)
print("\n\n")

print("+", "-"*26, "+", "-"*7, "+", sep="")
print("|", " "*9, "Name", " "*9, "|", "Votes", "|")
print("+", "-"*26, "+", "-"*7, "+", sep="")

for name in candidate_list:
    # Padding calculation
    total_padding_name = 26 - len(name)
    left_padding_name = total_padding_name//2
    right_padding_name = total_padding_name - left_padding_name
    total_padding_vote = 7 - len(str(total_vote_count[display]))
    left_padding_vote = total_padding_vote//2
    right_padding_vote = total_padding_vote - left_padding_vote
    
    # Drawing table with results
    print("|", " "*left_padding_name, candidate_list[display], " "*right_padding_name, "|", " "*left_padding_vote, total_vote_count[display], " "*right_padding_vote, "|", sep="")
    print("+", "-"*26, "+", "-"*7, "+", sep="")
    
    display += 1
    if display == len(candidate_list):
        break
