days = [["ran", "was tired"], ["ran", "was not tired"], ["didn't run", "was tired"], ["ran", "was tired"], ["didn't run", "was not tired"], ["ran", "was not tired"], ["ran", "was tired"]]
### p(A)
prob_tired = len([d for d in days if d[1]=="was tired"])/float(len(days))

### p(B)
prob_ran = len([d for d in days if d[0]=="ran"])/float(len(days))

#print prob_ran, prob_tired

#### p(B|A)

prob_ran_given_tired = len([d for d in days if d[0]=="ran" and d[1]=="was tired"])/float(len([d for d in days if d[1]=="was tired"]))
#print prob_ran_given_tired
#### p(A|B)
prob_tired_given_ran = (prob_ran_given_tired*prob_tired)/prob_ran
#print "Probability being tired given that you ran is: ",prob_tired_given_ran


days = [["ran", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["ran", "was tired", "woke up early"]]
new_day = ["ran","didn't wake up early"]

def calc_y_probability(y_label,days):
    return len([d for d in days if d[1]==y_label])/float(len(days))
def calc_ran_given_y(ran_label,y_label,days):
    return len([d for d in days if d[0]==ran_label and d[1]==y_label])/float(len(days))

def calc_woke_up_early_given_y(woke_up_early_label,y_label,days):
    return len([d for d in days if d[2]==woke_up_early_label and d[1]==y_label])/float(len(days))

y = "was tired"
prob_y = calc_y_probability(y,days)
prob_ran_given_y = calc_ran_given_y(new_day[0],y,days)
prob_woke_up_early_given_y = calc_woke_up_early_given_y(new_day[1],y,days)
denom = len([d for d in days if d[0]==new_day[0] and d[2]==new_day[1]])/float(len(days))
prob_Y_given_X = prob_y*prob_ran_given_y*prob_woke_up_early_given_y/denom
print "probability that he was not tired" prob_Y_given_X

y = "was not tired"
prob_y = calc_y_probability(y,days)
prob_ran_given_y = calc_ran_given_y(new_day[0],y,days)
prob_woke_up_early_given_y = calc_woke_up_early_given_y(new_day[1],y,days)
denom = len([d for d in days if d[0]==new_day[0] and d[2]==new_day[1]])/float(len(days))
prob_Y_given_X = prob_y*prob_ran_given_y*prob_woke_up_early_given_y/denom
print prob_Y_given_X
