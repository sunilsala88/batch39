


def get_highest(numbers:list)->int:
    """
    use this function to get highest number in any list
    input:list ,output:int(higest number in that list)
    """
    high=numbers[0]
    for i in numbers:
        if high<i:
            high=i
    return high


numbers=[22,55,77,66,33]
h1=get_highest(numbers)
print(h1)

numbers.pop()

def get_occ(word:str,char:str)->int:
    """
    this function takes 2 input 
    first is the word 
    send is the char that you want to serch in the word
    this function counts the occurance of the char in the word
    """

    count=0
    for i in word:
        if i==char:
            count=count+1

    return count

n1=get_occ('hlello','l')
print(n1)




numbers=[22,55,77,66,33]
rev_list=[]
for i in numbers:
    rev_list.insert(0,i)
print(rev_list)


print(list(range(4,-1,-1)))
rev_list=[]
for i in range(len(numbers)-1,-1,-1):
    rev_list.append(numbers[i])
print(rev_list)

print(list(range(-1,-6,-1)))
rev_list=[]
for i in range(-1,-(len(numbers)+1),-1):
    rev_list.append(numbers[i])
print(rev_list)


def rev_string(word:str)->str:
    rev_str=''
    for i in word:
        rev_str=i+rev_str

    return rev_str

s1=rev_string('hello')
print(s1)
#palindrome

def check_palindrome(string1:str)->bool:
    string2=rev_string(string1)
    if string1==string2:
        return True
    else:
        return False

print(check_palindrome('madame'))