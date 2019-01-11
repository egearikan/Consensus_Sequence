##fasta file depends on user

NoGap=open("baisc.fa","r")
con=open("consensus.fa","w")
sequences = list()
consensusSeq = ''

    for line in NoGap:
        if line.startswith('>'):
            continue
        else:
            sequences.append(line)

    for i in range(len(sequences[0])):
        chardict = dict()
        for c in range(len(sequences)):
            char = sequences[c][i]
            if char=='-':
                continue
            if char in chardict:
                chardict[char] += 1 
            else:
                chardict[char] = 1
        consensusSeq += sorted(chardict.keys(), reverse=True, key=chardict.get)[0]

    con.write(">Consensus Sequence\n")
    con.write(consensusSeq)
