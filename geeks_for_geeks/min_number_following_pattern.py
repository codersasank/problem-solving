class Solution:
    def printMinNumberForPattern(ob,S):
        n = len(S) ; idx = 1
        split_idx = list() ; split_sequences = list()
        for i in range(n-1):
            if S[i]!=S[i+1]:
                split_idx.append(i)
        prev = 0 ; cuts = len(split_idx)-1 ; cnt = 0
        while cnt<=cuts:
            split_sequences.append( S[prev:split_idx[cnt]+1] )
            prev = split_idx[cnt]+1 ; cnt += 1
        split_sequences.append( S[prev:n] )
        #print ( split_sequences )
        cnt = 0 ; digits = list()
        split_sequences[0] = split_sequences[0][0] + split_sequences[0]
        for sequence in split_sequences:
            #print ( digits )
            seq_len = len(sequence)
            if sequence[0]=='D':
                if cnt !=0:
                    digits = digits[0:cnt-1] + list(range(idx+seq_len-1,idx-1,-1)) + [digits[cnt-1]]
                else:
                    digits = list(range(idx+seq_len-1,idx-1,-1))
            else:
                digits += list(range(idx,idx+seq_len))
            cnt += seq_len  ; idx += seq_len
        digits = [str(dig) for dig in digits]
        return ''.join(digits)
