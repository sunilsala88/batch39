


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