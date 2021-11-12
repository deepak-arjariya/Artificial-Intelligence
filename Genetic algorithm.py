import random
import math
K=int(input())
p=int(input())
t=int(input())
n=K*p*t
c=float(input())
dist_mat=[]

for i in range(0,n):   
     dist_mat.append([float(j) for j in input().split()])

def fitness(list):
    score_mat=[];
    for i in range(t):
        score=0;
        for j in range(p-1):
            for l in range(j+1,p):
                for s in range(i*p*K+j*K,i*p*K+(j+1)*K):
                    for m in range(i*p*K+l*K,i*p*K+(l+1)*K):
                        x=list[s]
                        y=list[m]
                        score+=dist_mat[x][y]
        for j in range(p):
            for l in range(i*p*K+j*K,i*p*K+(j+1)*K-1):
                for s in range(l+1,i*p*K+(j+1)*K):
                    x=list[l]
                    y=list[s]
                    score+=1-dist_mat[x][y]
        score_mat.append(score)
    return score_mat


def mutate(listz):
    random.shuffle(listz)
    return listz

def mate(list1,list2):
    list1.sort()
    list2.sort()
    if(list1==list2):
        listz=list1
    else:
        listz=list1+list2 
    random.shuffle(listz)
    return listz

def find_sum(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum

def get_prob(list):
    sum=find_sum(list)
    ans=()
    for i in range(len(list)):
        ans=ans+((1.5-(list[i]/sum)),)
    return ans



def get_2Dlist(list):
    ans=[]
    for i in range(t):
        a=list[i*K*p:(i+1)*K*p]
        ans.append(a)
    return ans

def get_1Dlist(list):
    ans=[]
    for i in range(len(list)):
        for j in range(len(list[i])):
            ans.append(list[i][j])
    return ans

def get_high_prob(list):
    sum=find_sum(list)
    ans=()
    for i in range(len(list)):
        ans=ans+(((list[i]/sum)),)
    return ans
    
# genetic mutation and changing time slots with low goodness value

def solve(listg,ans):
    sol=None
    it=0
    listexp=listg
    itera=n*10
    while(it<itera):
        score=fitness(listexp)
        sum=find_sum(score)
        if(ans<sum):
            ans=sum
            sol=listexp
        prob=get_prob(score)
       
        ans_list=get_2Dlist(listexp)
       
        ans_sb=ans_list
        
        x=math.floor(t/2)
        if(x%2!=0):
            x+=1
        new_list1=random.choices(ans_list, weights=prob, k=x)
       
        new_list=[]
        new_high_list=[]
        for i in range(len(new_list1)):
            if(new_list1[i] not in new_list):
                new_list.append(new_list1[i])

        
        i=0
        while(i<len(new_list)):
            if(new_list[i] in ans_list):
                ans_list.remove(new_list[i])
            if(i+1 < len(new_list) and new_list[i+1] in ans_list):
                ans_list.remove(new_list[i+1])
            if(i+1<len(new_list)):
                g=new_list[i+1]
            else:
                g=[]
            listx=mate(new_list[i],g)
            list2=get_1Dlist(ans_list)
            listz=list2 + listx
            score=fitness(listz)
            sum=find_sum(score)
            if(ans<sum):
                ans=sum
                sol=listz
                listexp=listz
            i+=2
        for i in range(len(new_list)):
            if(new_list[i] in ans_sb):
                ans_sb.remove(new_list[i])
        listd=get_1Dlist(ans_sb)
        for i in range(len(new_list)):
            listz=mutate(new_list[i])
            listd=listd + listz
        score=fitness(listd)
        sum=find_sum(score)
        if(ans<sum):
            ans=sum
            sol=listd
            listexp=listd
        it+=1
    return sol,ans

# mating between both low goodness value time slots and high goodness value time slots
        
def solve2(listg,ans):
    sol=listg
    it=0
    listexp=listg
    itera=n*3
    while(it<itera):
        score=fitness(listexp)
        sum=find_sum(score)
        if(ans<sum):
            ans=sum
            sol=listexp
        prob=get_prob(score)
        high_prob=get_high_prob(score)
        ans_list=get_2Dlist(listexp)
        ans_high_list=ans_list
        ans_sb=ans_list
       
        x=math.floor(t/2)
        if(x%2!=0):
            x+=1
        x=math.floor(x/2)
        new_list1=random.choices(ans_list, weights=high_prob, k=x)
        new_high_list1=random.choices(ans_high_list,weights=prob,k=x)
        new_list=[]
        new_high_list=[]
        for i in range(len(new_list1)):
            if(new_list1[i] not in new_list):
                new_list.append(new_list1[i])
        for i in range(len(new_high_list1)):
            if(new_high_list1[i] not in new_high_list):
                new_high_list.append(new_high_list1[i])
        new_list=new_list+new_high_list
        i=0
        while(i<len(new_list)):
            if(new_list[i] in ans_list):
                ans_list.remove(new_list[i])
            if(i+1 < len(new_list) and new_list[i+1] in ans_list):
                ans_list.remove(new_list[i+1])
            if(i+1<len(new_list)):
                g=new_list[i+1]
            else:
                g=[]
            listx=mate(new_list[i],g)
            list2=get_1Dlist(ans_list)
            listz=list2 + listx
            score=fitness(listz)
            sum=find_sum(score)
            if(ans<sum):
                ans=sum
                sol=listz
                listexp=listz
            i+=2
        for i in range(len(new_list)):
            if(new_list[i] in ans_sb):
                ans_sb.remove(new_list[i])
        listd=get_1Dlist(ans_sb)
        for i in range(len(new_list)):
            listz=mutate(new_list[i])
            listd=listd + listz
        score=fitness(listd)
        sum=find_sum(score)
        if(ans<sum):
            ans=sum
            sol=listd
            listexp=listd
        it+=1
    return sol,ans

cont=list(range(n))       
list=list(range(n)) 


ans=0


sol,ans=solve(list,ans)
sol,ans=solve2(sol,ans)

for i in range(p):
    for j in range(t):
        for l in range(K):
            it=j*p*K+i*K+l
            print(sol[it]+1,end=" ")
        if(j!=t-1):
            print("|",end=' ')
        
    print()


