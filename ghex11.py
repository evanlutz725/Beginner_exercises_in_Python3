#Python3 Windows
#based on example 11 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("We're going to decide how many luxury items you can buy based on your expected income."
"We will determine how many PS4s, Samsung Phones, TVs, or GameSkins you can buy."
"A PS4 costs $200, a Samsung Phone costs $900, a TV costs $500, a GameSkin costs $9.99.",
"We will assume you don't get paid extra for overtime.")

while True:
	try:
		hourly_rate=float(input("How much do you make per hour in USD? "))
		if hourly_rate>0:
			break
		raise ValueError
	except ValueError:
		print ("Please enter a valid number.")
		
while True:
	try:
		week_hours=float(input("How many hours per week do you work? "))
		if week_hours>0:
			break
		raise ValueError
	except ValueError:
		print ("Please enter a valid number.")
		
while True:
	try:
		saving_weeks=float(input("How many weeks do you want to be saving for your luxury items? "))
		if saving_weeks>0:
			break
		raise ValueError
	except ValueError:
		print ("Please enter a valid number.")
		
while True:
	try:
		spend_percent=float(input("What percentage of your income do you want to spend on luxury items? Enter a decimal. "))
		if spend_percent>0 and spend_percent<=1:
			break
		raise ValueError
	except ValueError:
		print ("Please enter a valid number.")

spend_total=hourly_rate*week_hours*saving_weeks*spend_percent
		
print ("You said you make $", hourly_rate, "/hour, you work", week_hours, "hours/week,"
" you want to save for", saving_weeks, "weeks, and you want to spend", spend_percent*100,
"percent of that money on luxury items.")

print ("Based on what you told me, you want to spend a total of $",
spend_total, ", so you could buy", int(spend_total/200), "PS4s,",
int(spend_total/900), "Samsung phones, ", int(spend_total/500),
"TVs, or", int(spend_total/9.99), "GameSkins!")
