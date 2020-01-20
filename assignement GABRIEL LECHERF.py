def main(seq):
    arglist = seq.split()
    L=[]
    negationcount = 0
    for c in arglist :
        if(c=="not" or c=="bad"):
            negationcount+=1
        parse = findword(c,negationcount)
        if(parse):
            L.append(parse)
    if (2,[2,3,5]) in L and (3,[1,2,3,4,5])in L:
        L.remove((3,[1,2,3,4,5]))
    if(negationcount%2==0):
        return L[-1][0] in L[0][1]
    return not L[-1][0] in L[0][1]
           
def findword(seq,negationcount):
    seq =seq.lower()
    I = (0,[0,1,2,3,4,5])
    Good = (1,[1,4])
    EveryHuman = (2,[2,3,5])
    Human = (3,[1,2,3,4,5])
    Study = (4,[4])
    Loves = (5,[5])
    if "good" in seq or "bad" in seq:
        return Good
    elif "every" in seq:
        return EveryHuman
    elif "human" in seq:
        return Human
    elif "i" in seq and len(seq)==1:
        return I
    elif "love" in seq:
        return Loves
    elif "stud" in seq:
        return Study 
                
           
            
        
        
            
