inwords={ 0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 
          7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve',
          13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 
          17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty',
          30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',
          80:'Eighty',90:'Ninety', 100:'Hundred'}
          
suffix={1000:'Thousand',
        1000000:'Million', 
        1000000000:'Billion',
        1000000000000:'Trillion', 
        1000000000000000:'Quadrillion',
        1000000000000000000:'Sextillion',
        1000000000000000000000:'Septillion',
        1000000000000000000000000:'Octillion',
        1000000000000000000000000000:'Nonillion',
        1000000000000000000000000000000:'Decillion'}



def getTensAndOnes(n):
    if n<100 and n>0:
        r=n%10
        if n<21 or r==0:
            return inwords[n]
        else:
            q=n-r
            return inwords[q]+' '+inwords[r]
    else:
        return ''
    
def getHundred(n):
    if n<1000 and n>99:
        r=n%100
        q=n//100
        if r==0:
            return getTensAndOnes(q) +' '+ inwords[100]
        else:
            return getTensAndOnes(q)+' '+inwords[100]+' and '+getTensAndOnes(r)
    else:
        return getTensAndOnes(n)
            
            
def getInWords(n, i):
    if n==0:
        return inwords[n]
    if n<1000:
        return getHundred(n)
    d=i//1000
    r=n%d
    q=n//d
    if r==0:
        return getInWords(q, d)+' '+suffix[d]
    else:
        return getInWords(q, d)+' '+suffix[d]+', '+getInWords(r, d)   

def main():       
    n=int(input().strip())
    c=len(str(n))
    l = 10**(c-1)
    i=1000
    while i<=l:
        i*=1000
    print(getInWords(n, i))
    
if __name__ == "__main__":
    main()