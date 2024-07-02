#for question number two 


# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

l=list(map(int,input("Enter the list of numbers one by one seperated by a space : ").split()))
k=int(input("Enter the value of k : "))
count=0
if k>len(l):
    print("list out of index")
else:
    for i in range(k):
        if len(l)==1:
            count+=l[0]
        else:
            if l[0]>l[-1]:
                count+=l[0]
                l=l[1:]
            elif l[0]==l[-1] and len(l)>=4:
                if l[1]>l[-1]:
                    count+=l[0]
                    l=l[1:]
                else:
                    count+=l[0]
                    l.pop()
                
            else:
                count+=l[-1]
                l.pop()
print(count)