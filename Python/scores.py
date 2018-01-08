from random import randint
grade = randint(0,100)
print "Scores and Grades"
if grade < 60:
    print"Score:", grade, "; Your grade is F"
else:
    if grade>60 and grade<=69:
        print "Score:", grade, "; Your grade is D"
    else:
        if grade>69 and grade<=79:
            print "Score:", grade, "; Your grade is C"
        else:
            if grade>79 and grade<=89:
                print "Score:", grade, "; Your grade is B"
            else:
                if grade>89 and grade<=100:
                    print "Score:", grade, "; Your grade is A"
print "End of the program. Bye"
