from errno import WSAEHOSTDOWN
import random
when =["Yesterday","Tomorrow","Today","Next week","Before we went"]
who =["Me and Tom","Jimmy and his friends","Luis and his sister","Me and my friends", "Peter and Lincoln"]
where =["are going to the mall", "will walk across the border", "will go out to eat", "will go to the festival"]
residence =[" near their house", " close to my school", " around the corner", " 5 stops away from here", " across the road"]
happened =[" where we ate lots of food.", " hanged out", " watched a movie.", " where we learned how to play drums.", " Where we found an old creepy house."]
print(random.choice(when) + ', ' + random.choice(who) + ', ' + random.choice(where) + random.choice(residence) + ', ' + random.choice(happened))
