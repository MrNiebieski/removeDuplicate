filename = "input.txt"
outname = "output.txt"
with open(filename) as infile:
    with open(outname,"w") as fout:
    #setup as overwrite
        line_list = infile.readlines()
        pre_firstName = ""
        pre_lastName = ""
        pre_email = ""
        for line in line_list:
            columns = line.split('\t')
        #this is 0-based
            firstName = columns[1]
            lastName = columns[2]
            email = columns[3]
            #phone number is XXX-XXX-XXXX
            phone1 = columns[4]
            phone2 = columns[5]
            phoneNum1 = ''.join(c for c in phone1 if c.isdigit())
            phoneNum2 = ''.join(c for c in phone2 if c.isdigit())
            # print len(phoneNum2)
            if (len(phoneNum1) == 10):
                newPhone1 = '-'.join( (phoneNum1[:3],phoneNum1[3:6],phoneNum1[6:]) )
            else:
                newPhone1 = ''
            if (len(phoneNum2) == 10):
                newPhone2 = '-'.join( (phoneNum2[:3],phoneNum2[3:6],phoneNum2[6:]) )
            else:
                newPhone2 = ''
            #print columns[4], newPhone1
            #print columns[5], newPhone2

            fout.write(line)
