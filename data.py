#File is to import data from NTRS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
url='https://ntrs.nasa.gov/search?q=safety&page=%7B%22size%22:25,%22from%22:0%7D'
data={}

l=["Document ID","Document Type","External Source(s)","Authors","Date Acquired","Publication Date","Publication Information","Subject Category","Report/Patent Number","Meeting Information","Accession Number","Funding Number(s)","Distribution Limits","Copyright","Technical Review","Keywords"]
driver = webdriver.Chrome()

k=0
final=[]
for i in range(2):
    url=f'https://ntrs.nasa.gov/search?q=safety&page=%7B%22size%22:25,%22from%22:{k}%7D'
    driver.get(url)
    time.sleep(3)
    d={}
    val=driver.find_elements("xpath",'//div[@class="data"]')
    label=driver.find_elements("xpath",'//div[@class="label"]')
    
    m=0
    
    print(len(val),len(l)*25)
    b=False
    for k1 in range(25):
        
        for k2 in range(len(l)):
            try:
                j=label[m]
                i=val[m]
                print(j.text,l[k2],m)
                if j.text==l[k2]:
                    
                    if d.get(j.text)!=None:
                        d[j.text].append(i.text)
                    else:
                        d.update({j.text:[i.text]})
                    m+=1
                else:
                    
                    if d.get(l[k2])!=None:
                        d[l[k2]].append(None)
                    else:
                        d.update({l[k2]:[None]})
            except:
                if d.get(l[k2])!=None:
                        d[l[k2]].append(None)
                else:
                    d.update({l[k2]:[None]})
                b=True
                continue
                
        if b==True:
            break
                
        
            
            

        
        
            
            # btn=driver.find_element("xpath",f'//a[@href=\'/api/citations/{d.get("Document ID")}/downloads/{d.get("Document ID")}.pdf?attachment=true\']')
            # btn.click()
    for i in d.values():
        print(len(i))    
    final_df=pd.DataFrame(data=d)
    final_df.to_csv("data.csv")
    break
    k+=25
print("this",driver.title)
time.sleep(3)
driver.close()

