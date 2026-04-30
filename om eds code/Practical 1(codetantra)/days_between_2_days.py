from datetime import datetime
d1 = input().strip()
d2 = input().strip()
date1=datetime.strptime(d1,"%Y-%m-%d")
date2=datetime.strptime(d2,"%Y-%m-%d")
diff=date2-date1
print(diff.days)