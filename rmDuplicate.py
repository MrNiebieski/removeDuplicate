filename = "input.txt"
outname = "output.txt"
with open(filename) as infile:
    with open(outname,"w") as fout:
    #setup as overwrite
        line_list = infile.readlines()
        for line in line_list:
            columns = line.split('\t')
            print columns[2];
            fout.write(line)
