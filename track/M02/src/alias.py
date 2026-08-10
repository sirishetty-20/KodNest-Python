original_scores=[]
for i in range (3):
    original_scores.append(int(input("Enter the value:")))
alias_scores=original_scores
replacement_score=int(input("Enter the replacement score:"))
alias_scores[0]=replacement_score
additional_score=int(input("Enter the additional value:"))
alias_scores.append(additional_score)
if original_scores is alias_scores:
    print("Shared Object: True")
else:
    print("Shared Object: False")