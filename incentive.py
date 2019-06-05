# importing libraries
import pandas as pd
import numpy as np

amount_s=input('How much amount should be paid to the faculty for 1 mark of score: ')
#reading file
sample=input("Enter Academic result file location:")
data=pd.read_excel(sample)

#handling missing values
data.fillna('xxx', inplace=True)

temp=''
for i in range(0,data.shape[0]):
    if data['Branch'][i]!='xxx':
        temp=data['Branch'][i]
    else:
        data.set_value(i,'Branch',temp)

#function to find maximum percentage
def max_result(max_r,r):
    if(r>max_r):
        max_r=r
    return max_r

#calculating incentives
flag='y'
while(flag=='y'):
    emp=input('Enter Employee ID:')
    flag1='y'
    count=0
    ars_temp=0
    while(flag1=='y'):
        br=input('Enter branch:')
        sub=input('Enter subject:')
        count=count+1
        temp1=0
        temp2=0
        #calculating academic result score
        ars_w=0.0
        for i in range(0,data.shape[0]):
            if (data['Branch'][i] == br and data['Empl. ID'][i] == int(emp) and data['Subject'][i] == sub):
                y=data['result'][i]
            if(data['Branch'][i]==br):
                x=max_result(temp1,data['result'][i])
                temp1=x
            if(data['Subject'][i]==sub):
                z=max_result(temp2,data['result'][i])
                temp2=z
        ars=((1-(x/100-y/100)**2*10)*3)+((1-(z/100-y/100)**2*10)*3)
        ars=ars/2
        ars_n=ars_temp+ars
        ars_temp=ars_n

        #calculating feedback score
        afs_w=0.0
        sample=input('Enter feedback location:')
        data1=pd.read_excel(sample)
        sum=0
        sum1=0
        for i in range(2,data1.shape[1]):
            sum1=0
            for j in range(0,data1.shape[0]):
                sum1+=data1.iat[j,i]
            sum=sum1/90
        afs=sum/(data1.shape[1]-2)

        flag1 = input("Is there any other subject taught by this Employee [y/n]:")

    #R&D

    ard = 3.0
    ard_w=0
    total = 0.0
    achieved = 0.0
    randd = input('Enter R and D file location of the employees:')
    data2 = pd.read_excel(randd)

    # converting column values into lowercase
    data2['Category'] = data2['Category'].str.lower()
    data2['Paper with'] = data2['Paper with'].str.lower()

    # handling missing values
    data2.fillna('xxx', inplace=True)

    temp = ''
    for i in range(0, data2.shape[0]):
        if data2['Empl. Id'][i] != 'xxx':
            temp = data2['Empl. Id'][i]
        else:
            data2.set_value(i, 'Empl. Id', temp)

    # Calculating R&D Score
    total = 0.0
    achieved = 0.0
    for i in range(0, data2.shape[0]):
        if (data2['Empl. Id'][i] == int(emp)):
            # for category international journal unpaid with ISSN/ISBN
            if (data2['Category'][i] == 'international journal-unpaid'):
                if (data2['Paper with'][i] == 'h-indexed'):
                    total += 3
                    if (data2['Index/Citation value'][i] > 10):
                        achieved += 3

                    elif (data2['Index/Citation value'][i] > 5 and data2['Index/Citation value'][i] <= 10):
                        achieved += 2.1

                    else:
                        achieved += 1.2

                elif (data2['Paper with'][i] == 'impact factor'):
                    total += 2
                    if (data2['Index/Citation value'][i] >= 3):
                        achieved += 2
                    elif (data2['Index/Citation value'][i] >= 1.00 and data2['Index/Citation value'][i]<= 2.99):
                        achieved += 1.4
                    else:
                        achieved += 0.8

                else:
                    total += 1.5
                    achieved += 0.75

            # for category international journal paid with JCR Indexed
            elif (data2['Category'][i] == 'international journal-paid'):
                if (data2['Paper with'][i] == 'h-indexed'):
                    total += 2
                    if (data2['Index/Citation value'][i] > 10):
                        achieved += 2
                    elif (data2['Index/Citation value'][i] > 5 and data2['Index/Citation value'][i] <= 10):
                        achieved += 1.4
                    else:
                        achieved += 0.8

                elif (data2['Paper with'][i] == 'impact factor'):
                    total += 1.75
                    if (data2['Index/Citation value'][i] >= 3):
                        achieved += 1.75
                    elif (data2['Index/Citation value'][i] >= 1.00 and data2['Index/Citation value'][i] <= 2.99):
                        achieved += 1.225
                    else:
                        achieved += 0.7

                else:
                    total += 1.5
                    achieved += 0.75

            # for category national journals-unpaid
            elif (data2['Category'][i] == 'national journals-unpaid'):
                if (data2['Paper with'][i] == 'h-indexed'):
                    total += 1.5
                    if (data2['Index/Citation value'][i] > 10):
                        achieved += 1.5
                    elif (data2['Index/Citation value'][i] > 5 and data2['Index/Citation value'][i] <= 10):
                        achieved += 1.05
                    else:
                        achieved += 0.6

                elif (data2['Paper with'][i] == 'impact factor'):
                    if (data2['Index/Citation value'][i] >= 3):
                        total += 1.2
                        achieved += 1.2
                    elif (data2['Index/Citation value'][i] >= 1.00 and data2['Index/Citation value'][i] <= 2.99):
                        total += 1.2
                        achieved += 0.84

                    elif (data2['Index/Citation value'][i] >= 0.01 and data2['Index/Citation value'][i] <= 0.99):
                        total += 1.2
                        achieved += 0.48

                    elif (data2['Index/Citation value'][i] == 'peer reviewed'):
                        total += 0.8
                        achieved += 0.4

                    elif (data2['Index/Citation value'][i] == 'peer refereed'):
                        total += 0.8
                        achieved += 0.4

            # for category national journals-paid
            elif (data2['Category'][i] == 'national journals-paid'):
                if (data2['Paper with'][i] == 'h-indexed'):
                    total += 1
                    if (data2['Index/Citation value'][i] > 10):
                        achieved += 1
                    elif (data2['Index/Citation value'][i] > 5 and data2['Index/Citation value'][i] <= 10):
                        achieved += 0.7
                    else:
                        achieved += 0.4
                elif (data2['Paper with'][i] == 'impact factor'):
                    if (data2['Index/Citation value'][i] >= 3):
                        total += 0.8
                        achieved += 0.8
                    elif (data2['Index/Citation value'][i] >= 1.00 and data2['Index/Citation value'][i] <= 2.99):
                        total += 0.8
                        achieved += 0.56
                    elif (data2['Index/Citation value'][i] >= 0.01 and data2['Index/Citation value'][i] <= 0.99):
                        total += 0.8
                        achieved += 0.32
                    elif (data2['Index/Citation value'][i] == 'peer reviewed'):
                        total += 0.6
                        achieved += 0.3
                    elif (data2['Index/Citation value'][i] == 'peer refereed'):
                        total += 0.6
                        achieved += 0.3

            # for category international conference proceedings (indexed)
            elif (data2['Category'][i] == 'international conference proceedings'):
                total += 0.5
                if (data2['Paper with'][i] == 'with isbn'):
                    achieved += 0.5
                elif (data2['Paper with'][i] == 'with issn'):
                    achieved += 0.5
                elif (data2['Paper with'][i] == 'without isbn'):
                    achieved += 0.4
                elif (data2['Paper with'][i] == 'without issn'):
                    achieved += 0.4

            # for category national conference proceedings (indexed)
            elif (data2['Category'][i] == 'national conference proceedings'):
                total += 0.5
                if (data2['Paper with'][i] == 'with isbn'):
                    achieved += 0.5
                elif (data2['Paper with'][i] == 'with issn'):
                    achieved += 0.5
                elif (data2['Paper with'][i] == 'without isbn'):
                    achieved += 0.4
                elif (data2['Paper with'][i] == 'without issn'):
                    achieved += 0.4

            # for category workshops organized
            elif (data2['Category'][i] == 'workshops organized'):
                total += 1
                if (data2['Paper with'][i] == 'with funding by other agencies'):
                    achieved += 1
                elif (data2['Paper with'][i] == 'without funding'):
                    achieved += 0.5

            # for category symposiums organized
            elif (data2['Category'][i] == 'symposiums organized'):
                total += 1
                if (data2['Paper with'][i] == 'with funding by other agencies'):
                    achieved += 1
                elif (data2['Paper with'][i] == 'without funding'):
                    achieved += 0.5

            # for category fdp participated
            elif (data2['Category'][i] == 'fdp participated'):
                total += 0.5
                if (data2['Paper with'][i] == 'international level'):
                    achieved += 0.5
                elif (data2['Paper with'][i] == 'national level'):
                    achieved += 0.3
                else:
                    achieved += 0.2

            # for category workshops participated
            elif (data2['Category'][i] == 'workshops participated'):
                total += 0.5
                if (data2['Paper with'][i] == 'international level'):
                    achieved += 0.5
                elif (data2['Paper with'][i] == 'national level'):
                    achieved += 0.3
                else:
                    achieved += 0.2

            # for category symposiums participated
            elif (data2['Category'][i] == 'symposiums participated'):
                total += 0.5
                if (data2['Paper with'][i] == 'international level'):
                    achieved += 0.5
                elif (data2['Paper with'][i] == 'national level'):
                    achieved += 0.3
                else:
                    achieved += 0.2



        #ard_w = (achieved / total) * ard
    if(total!=0.0):
        ard_w=(achieved/total)*ard

    #calculating other scores
    aos_w=0
    others=input('Enter other scores file location of the employees: ')
    data3=pd.read_excel(others)

    for i in range(0,data3.shape[0]):
        if(data3['Empl. Id'][i]==int(emp)):
            aos_w=data3['Faculty Discipline'][i]+data3['Student Counseling'][i]+data3['HOD and Pricipal feedback'][i]



    ars_w=ars_n/count
    afs_w=afs/count

    print("Weighted academic result score of employee ",emp," is: ",ars_w,"  afs=",afs_w," ard=",ard_w," aos_w =",aos_w)
    total_score=ars_w + afs_w + ard_w + aos_w
    total_amount=int(total_score)*int(amount_s)


    print("Total score of the employee : ",total_score )
    print("Total incentive for the employee ",emp,"is : ",total_amount)




    flag=input("Do you want to calculate incentive for any other employee [y/n]:")



