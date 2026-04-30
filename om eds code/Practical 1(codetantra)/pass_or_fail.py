def grade(total_course,marks):
	if any (mark<40 for mark in marks):
		return "Fail"
	aggregate_percentage=(sum(marks)/(total_course*100))*100
	print(f"Aggregate Percentage: {aggregate_percentage:.2f}")
	if (aggregate_percentage>75):
		return "Grade: Distinction"
	elif (60<=aggregate_percentage<75):
		return "Grade: First Division"
	elif (50<=aggregate_percentage<60):
		return "Grade: Second Division"
	elif (40<=aggregate_percentage<50):
		return "Grade: Third Division"
n=int(input())
marks=list(map(int,input().split()))
print(grade(n,marks))