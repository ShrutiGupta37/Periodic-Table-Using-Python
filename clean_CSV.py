import csv
def clean_csv():
    cleaned_data=[]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '[', ']']

    def clean_data(ele,col,row):
        index=0
        name=''
        number=''
        symbol=''
        weight=''

        while index<len(ele) and ele[index] not in numbers:
           if (ele[index]=='Â'):
                index+=2
           else:
                name +=ele[index]
                index+=1

        while index <len(ele) and ele[index] in numbers:
            number+=ele[index]
            index+=1
        
        while index<len(ele) and ele[index] not in numbers:
           if (ele[index]=='â'):
                index+=3

           else:
                symbol +=ele[index]
                index+=1
        while index <len(ele):
            if ele[index] in numbers:
                weight+=ele[index]
                index+=1

        return[name,number,symbol,weight,col,row]

    with open("Periodic Data.csv",newline='')as csvfile:
        reader=csv.reader(csvfile)
        count=0
        for row in reader:
            if count>1:
                for i in range(len(row)):
                    if(len(row[i])>1):
                        cleaned_data.append(clean_data(row[i],i,count))
            count+=1
    print(cleaned_data)
    
    return cleaned_data
clean_csv()