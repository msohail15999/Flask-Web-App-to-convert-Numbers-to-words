#Number names: 1 - > One
#write a program which will take 5 input names and generate appropriate number names.

numbernames = ["","One ","Two ","Three ","Four ","Five ","Six ","Seven ","Eight ","Nine ","Ten ","Eleven ","Twelve ","Thirteen ","Fourteen ","Fifteen ","Sixteen ","Seventeen ","Eighteen ","Nineteen "]

tensname = ["","","Twenty ","Thirty ","Fourty ","Fifty ","Sixty ","Seventy ","Eigthy ","Ninety "]



def num_to_words(num,s):
    
    word = ""
    if num>19:
        word += tensname[num//10]+numbernames[num%10]
    else:
        word += numbernames[num]
    if word:
        word += s
    return word
  
def final_word(num):

    if num==0:
        return "Zero"
    
    else:
        finalword = ""
        finalword += num_to_words((num // 10000000),"Crore ") 
        finalword += num_to_words(((num // 100000)%100),"Lakh ")
        finalword += num_to_words(((num // 1000)%100),"Thousand ") 
        finalword += num_to_words(((num // 100)%10),"Hundred ")
        
        if (num > 100 and num % 100): 
            finalword += "and "; 
        
        finalword += num_to_words((num % 100), ""); 
        
        return finalword

