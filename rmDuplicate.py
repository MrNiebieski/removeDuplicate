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
                #print firstName, lastName
                pre_email = email
                pre_firstName = firstName
                pre_lastName = lastName
            else:
                bool_new = False
        #handle corner case if email is same but name is different
                if (firstName!=pre_firstName or lastName!=pre_lastName):
        #check if it is only a difference of captal
                    print "Attention: this is unusual"
                    print columns[0], email, firstName, lastName
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
            if (bool_new):
                fout.write(line)
