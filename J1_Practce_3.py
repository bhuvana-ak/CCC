# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#5  (Packages delivered)
#2  (Collisions)
'''
PThe Scenario: Barley the dog is happy or sad based on the treats he receives. Treats come in three sizes: Small (S), Medium (M), and Large (L).A small treat is worth 1 point.A medium treat is worth 2 points.A large treat is worth 3 points.The Goal: Calculate Barley’s happiness score using the formula:$$1 \times S + 2 \times M + 3 \times L$$If the score is 10 or greater, Barley is happy.If the score is less than 10, Barley is sad.

3 (Small)
1 (Medium)
0 (Large)
'''
small=1
big=2
medium=2
largetreats=1
smalltreats=2
mediumtreats=3
total=largetreats*big+mediumtreats*medium+smalltreats*small
if total>10:
    score="happy"
elif total<=10:
    score="sad"
print("score=",score)