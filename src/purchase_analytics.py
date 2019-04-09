import sys
import csv

 

def main():
    
    # The function to split the lines in each rows into columns
    def split_outside(line):
        for out in  csv.reader([line], quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL):
            pass
        return out
    
    # The dictionary the maps productID to a list of
    # [ product_name , aisle_id , department_id ]
    #file_dir = './input/products.csv'
    file_dir = sys.argv[2]
    products = {}
    with open(file_dir, encoding='utf-8') as f:
        line0 = split_outside(f.readline())
        for oneline in f:
            oneline = split_outside(oneline)
            products[oneline[0]]=oneline[1:]
            
    
            
    #The dictionary that counts the orders based on department
    count_P   = {} 
    #The dictionary that counts the orders based on department, which were reordered
    count_P_1 = {} 
    
    # Since there are only 21 department
    # We can just prepare the keys in advance 
    for i in range(21):
        count_P[str(i+1)]   = 0
        count_P_1[str(i+1)] = 0
    #Read orders one by one
    #file_dir = './input/order_products.csv'
    file_dir = sys.argv[1]

    with open(file_dir, encoding='utf-8') as f:
        line0 = split_outside(f.readline())
        del line0
        for oneline in f:
            oneline = split_outside(oneline)
            prod_id = oneline[1]
            dep = products[prod_id][2]
            
            # count the orders
            count_P[dep] +=1
            if oneline[3]=='0':
                count_P_1[dep]+=1
                
    
    #merge the count_P and count_P_1
    report = []
    for i in range(21):
        i = str(i+1)
        if count_P[i]>0:
            if count_P_1[i]>0:
                ratio_i = '%.2f' % round((count_P_1[i] / count_P[i]) , 2)
                report.append([i,str(count_P[i]),str(count_P_1[i]),ratio_i])
            else:
                report.append([i,str(count_P[i]),"0","0.00"])
    
    
    #write csv
    #file_dir = './output/report.csv'
    file_dir = sys.argv[3]
    with open(file_dir,'w+') as f:
        f.write("department_id,number_of_orders,number_of_first_orders,percentage")
        f.write("\n")
        for line in report:
            line_s = line[0]+","+line[1]+","+line[2]+","+line[3]+"\n"
            f.write(line_s)

    #print("Completed")


if __name__ == "__main__":
    main()
    
    
    