def hashkey_conversion():
    st = input("请粘贴hash key数字串：") #"026874cc72f39c3a87983f951056f22a"
    while len(st)!=32:
        print("你输入的数据位数不对，请重新输入！")
        st = input("请粘贴hash key数字串")

    print("输入正确，处理如下：")
    for i in range(len(st)):
        if i % 2 == 0:
            print("0x"+st[i],end="")
        else:
            if i == len(st)-1:
                print(st[i],end="")
            else:
                print(st[i],end=",")
				
def cus_ip():
    st = input("请粘贴customer IP 数字串：") #"026874cc72f39c3a87983f951056f22a"
    while len(st)!=32:
        print("你输入的数据位数不对，请重新输入！")
        st = input("请粘贴customer IP 数字串：")

    print("输入正确，处理如下：")
    model_01 = st[0:8]
    model_02 = st[8:16]
    model_03 = st[16:24]
    model_04 = st[24:32]
    print("IP_Cntrol_Mapping_1[8] = "+model_01)
    print("IP_Cntrol_Mapping_2[8] = "+model_02)    
    print("IP_Cntrol_Mapping_3[8] = "+model_03)
    print("IP_Cntrol_Mapping_4[8] = "+model_04)    

if __name__ == "__main__":

	print("****脚本先处理CUSTOMER IP,再处理Customer_hash****")
	cus_ip()
	hashkey_conversion()