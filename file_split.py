file = open('C:\\Users\\pavan.boppana\\Documents\\Learning\\Programming\\Fun\\test_file.txt')
lines = file.readlines()

lv_count = 0

lv_file_Count = 1
lv_file_name = "C:\\Users\\pavan.boppana\\Documents\\Learning\\Programming\\Fun\\split_" + str(lv_file_Count) +'.txt'
file = open(lv_file_name,'w')

for line in lines:
    line = line.split(',')
    line[1] = int(line[1])
    if ( lv_count + line[1] ) > 500:
        lv_count = 0
        lv_file_Count = lv_file_Count + 1
        lv_file_name = "C:\\Users\\pavan.boppana\\Documents\\Learning\\Programming\\Fun\\split_" + str(lv_file_Count) +'.txt'
        file = open(lv_file_name,'w')
    lv_count = lv_count + line[1]
    file.write(line[0] + ":" + str(line[1]) + '\n')



