import json, requests 

url = requests.get("https://qexo.lvbyte.top/pub/friends/")  #获取友链
test = url.test   #解析json数据
data = json.loads(test)     #获取data数据
data2 = data['data'] #data2为进入json data类中

#以上代码为解析Qexo友链json数据为python数据

#Friends_circle为friends字典   Friends_links为friends列表，其中应有len(data2)个嵌套的Friends列表   Friends列表为Qexo友链
#len(data2)为友链数量

Friends_circle={}  #定义列表和字典
Friends_links=[]
Friends=[]

num=len(data2)
count=0
for _ in range(num):  #重复输入友链数据至Friend_circle字典中
    Friends=[1,2,3]  #初始化Friends列表
    Friends[0]=data2[count]['name']   #Friends列表数据注入
    Friends[1]=data2[count]['url']
    Friends[2]=data2[count]['image']   
    Friends_links.append(Friends)
    Friends_circle ={"friends":  Friends_links   }
    Friends=[1,2,3]
    count=count+1  #进位

print(Friends_circle)
Friends_json=json.dumps(Friends_circle)
print("Json数据为：",Friends_json)
with open('friends.json', 'w') as f:
    f.write(Friends_json)
    f.close()
