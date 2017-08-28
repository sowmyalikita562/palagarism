from string import punctuation
s="S34556O*}W_M(Y)A@"
def  check_str(s):
    for j in list(punctuation):
        s=s.lower()
        if all(letter.isalpha() for letter in s):
            pass
        else:
            l=list(s)
            p=""
            for i in l:
                if str(i).isalpha():
                    p=p+i
            s=p
    return s
