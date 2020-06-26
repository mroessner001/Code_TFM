import re
def number_check(segment1, segment2):
    nums = re.compile(r"[+-]?\d+(?:\.\d+)?")
    
    numsSegment1=re.findall(nums,segment1)
    numsSegment2=re.findall(nums,segment2)
    
    
    numsSegment1.sort() 
    numsSegment2.sort() 
    print(numsSegment1,numsSegment2)
    if not numsSegment1==numsSegment2:
        print("numbers mismatch")
        
    else:
        print("Numbers OK")
    


number_check("123 Hello!!", "Hola 456.7")
