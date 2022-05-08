import csv

def write_into_csv(info_list):
    with open('stu_info.csv','a', newline='') as csv_files:
        writer = csv.writer(csv_files)
        
       # if csv_files.tell()==0
       #     writer.writerow("Name", "Age", "Contact", "Email-ID")
        
        writer.writerow(info_list)

if __name__ == '__main__': 
    con=True
    count=1
    while(con):
        
        stu_info= input("Enter student information for student #{} in the folowing format(Name age contact_no. email_id):".format(count))
        print("The entered information is: \nName: {} \nAge: {} \nContact Number: {}\n E.mail ID: {}"
        .format(stu_info[0], stu_info[1], stu_info[2], stu_info[3]))
        
        choice= input("Is the netered information correct?(yes/no)")
        if choice == "yes"
            stu_info_list= stu_info_split(' ')
            write_into_csv(stu_info_list)
            
            con_check= input("Enter (yes/no) if you want to enter information for another student:\n")
            if con_check == "yes"
                con=True
                count= count+1
            
            elif con_check == "no"
                con=False
          
        elif choice == "no"
            print("Re-enter the information correctly:")
