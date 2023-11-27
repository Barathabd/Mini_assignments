Students_scores=(input("Enter a list of scores: ").split())
for n in range(0,len(Students_scores)):
    Students_scores[n]=int(Students_scores[n])
print(Students_scores)
Highest_score=0
for score in Students_scores:
    if score>Highest_score:
        Highest_score=score
print(f"Highest score in the class is : {Highest_score}")