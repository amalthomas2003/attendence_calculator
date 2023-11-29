import sys,re
from collections import defaultdict
sys.stdin=open("att.txt","r")
dict1=defaultdict(int)

#################################subject id : subject name (map)

sub_map_data="""1	101009/IT500A	 SOFTWARE DESIGN WITH UML
2	101009/IT500B	 COMPILER DESIGN
3	101009/MS500C	 FUNDAMENTALS OF MANAGEMENT
4	101009/MS500D	 BUSINESS STRATEGY
5	101009/EN500E	 BUSINESS COMMUNICATION & VALUE SCIENCE III
6	101009/IT503F	 MACHINE LEARNING
7	101009/IT522G	 COMPILER DESIGN LAB (LEX & YACC)
8	100004/IT501H	 WIRELESS COMMUNICATION
9	101009/IT522S	 MACHINE LEARNING LAB
10	101009/IT522T	 MINI PROJECT"""
sub_map_dict=dict()
for  _ in sub_map_data.split("\n"):
    sub_map_dict[str(_.split()[1])]=str(_.split()[2])
########################################################################
    



def endwith(string):
    pattern=r"\d{4}$"
    return bool(re.search(pattern, string))

while True:
    try:
        for _ in input().split():
            if not endwith(_):
                dict1[_]+=1
            else:
                pass
            
    except:
        break
def line():
    print("---"*16)
for _ in sub_map_dict:
    if _ not in dict1:
        dict1[_]=0

print("Subject Name".ljust(45),"No of Hours Lost")
line()
dict1=dict(sorted(dict1.items(),key=lambda x : x[1],reverse=True))
#print(dict1)
for i,j in dict1.items():
    print(f"{sub_map_dict[i].ljust(45)}{j}")
line()
print(f" Total Hours Lost".ljust(45)+f"{sum(dict1.values())}")
