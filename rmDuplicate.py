filename = "input.txt"
outname = "output.txt"
with open(filename) as infile:
    with open(outname,"w") as fout:
    #setup as overwrite
        line_list = infile.readlines()
        pre_firstName = ""
        pre_lastName = ""
        pre_email = ""
        bool_new = False
        for line in line_list:
            columns = line.split('\t')
        #this is 0-based
            firstName = columns[1]
            lastName = columns[2]
            email = columns[3]
        #now check if this redundant
            if (email != pre_email):
                bool_new = True
                pre_email = email
                pre_firstName = firstName
                pre_lastName = lastName
            else:
                bool_new = False
        #handle corner case if email is same but name is different
                ##if (firstName!=pre_firstName or lastName!=pre_lastName):
                if (firstName.lower()!=pre_firstName.lower() or lastName.lower()!=pre_lastName.lower()):
        #check if it is only a difference of captal
                    #print "Attention: this is unusual"
                    print email, pre_firstName, pre_lastName, '=>', firstName, lastName
            #phone number is XXX-XXX-XXXX
            phone1 = columns[4]
            phone2 = columns[5]
            phoneNum1 = ''.join(c for c in phone1 if c.isdigit())
            phoneNum2 = ''.join(c for c in phone2 if c.isdigit())
            if (len(phoneNum1) == 10):
                newPhone1 = '-'.join( (phoneNum1[:3],phoneNum1[3:6],phoneNum1[6:]) )
            else:
                newPhone1 = ''
            if (len(phoneNum2) == 10):
                newPhone2 = '-'.join( (phoneNum2[:3],phoneNum2[3:6],phoneNum2[6:]) )
            else:
                newPhone2 = ''
            columns[4] = newPhone1
            columns[5] = newPhone2
            #print columns[4], newPhone1
            #print columns[5], newPhone2
            newLine = '\t'.join(columns)
            if (bool_new):
                #print newLine
                #fout.write(line)
                fout.write(newLine)
