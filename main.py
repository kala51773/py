# 这是一个示例 Python 脚本。
import requests
import bs4


def gethtml(url):
    return requests.get(url)


def getinfo(Response):
    soup = bs4.BeautifulSoup(Response, features='html.parser')
    list = soup.select('.j_joblist .e')
    print(type(list))
    arr=[];
    for i in list:
        porson=[]
        el = i.select('.el')
        for j in el:
            title = j.select_one('.t .jname').text  # 工作标题
            porson.append(title)
            time = j.select_one('.t .time').text  # 发布时间
            porson.append(time)
            sal = j.select_one('.info .sal').text
            porson.append(sal)

            xinxi = j.select_one('.info .d').text
            porson.append(xinxi)

            try:
                daiyu = j.select_one('.tags').text
            except:
                daiyu=""

            porson.append(daiyu )
            info = j.select_one('.info').text  # 招聘信息
            porson.append(info)
            # print(info)

            # print(xinxi)
        er = i.select('.er')
        for j in er:
            公司 = j.select_one('.cname').text
            porson.append(公司)
            公司类型 = j.select_one('.dc').text
            porson.append(公司类型)
            try:
                经营内容 = j.select_one('int').text
            except:
                经营内容 = ""
            porson.append(经营内容)

        arr.append(porson)
    return arr




# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # work = "java"
    # url = '''
    # https://search.51job.com/list/170200%252c170300,000000,0000,00,9,99,'''+work+''',2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
    # '''
    # response = gethtml(url)
    html = open('html.html')
    arr = getinfo(html)
    print(len(arr))
    index =0
    for i in arr:
        print("第"+str(index) +"个人")
        for j in i:
            print(j)
        index+=1
