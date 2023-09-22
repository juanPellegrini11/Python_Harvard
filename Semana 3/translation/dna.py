inputFile = "dna.txt"
f = open(inputFile, "r")
seq = f.read()
seq = seq.replace("\n", "")
seq = seq.replace("\r", "")
print(seq[40:50])