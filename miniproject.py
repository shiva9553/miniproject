name = input("enter your name")
yourclass = input("enter your class")
yoursection=input("enter your section")
yourschool=input("enter your school")
techer=input("enter your teacher name")
date = str(input("enter date"))
subject=input("enter subject")
dateofleave=input("enter date of leave")
reason=input("enter your reason")

letter=f'''
Date: {date}

To,
the {techer}
{yourschool}
My self {name} from {yoursection} studying {yourclass}

due to {reason} grant me a leave on {dateofleave}

{name} from {yourclass},{yourschool}

Thankyou sir/madam
yours sincerely,
    {name}


'''
print(letter)