#File is to import data from NTRS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import pickle
url='https://ntrs.nasa.gov/search?q=safety&page=%7B%22size%22:25,%22from%22:0%7D'
data={}

l=["Document ID","Document Type","External Source(s)","Authors","Date Acquired","Publication Date","Publication Information","Subject Category","Report/Patent Number","Meeting Information","Accession Number","Funding Number(s)","Distribution Limits","Copyright","Technical Review","Keywords"]
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : 'C:\\Users\\sudha\\Downloads\\NASA Space Apps Challenge\\pdf'}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chromeOptions)

k=0
final_df=[]
data={}
for j in range(100):
    url=f'https://ntrs.nasa.gov/search?q=safety&page=%7B%22size%22:25,%22from%22:{k}%7D'
    driver.get(url)
    time.sleep(3)
    
    val=driver.find_elements("xpath",'//div[@class="data"]')
    label=driver.find_elements("xpath",'//div[@class="label"]')
    chip=driver.find_elements("xpath",'//mat-chip[@class="mat-chip mat-focus-indicator mat-primary mat-standard-chip ng-star-inserted"]')
    
    for i in val:
        try:
            if int(i.text):
                doc_id=i.text
                print(doc_id)
                continue
        except:
            if data.get(doc_id)!=None:
                data[doc_id].append(i.text)
            else:
                data.update({doc_id:[i.text]})
    

    # m=0
    # m1=0
    
    # b=False
    # for k1 in range(25):
        
    #     for k2 in range(len(l)):
    #         # try:
    #         j=label[m1]
    #         i=val[m]
            
            

    #         if j.text==l[k2]:
    #             if j.text=="Authors":
    #                 if d.get(l[k2])!=None:
    #                     d[l[k2]].append(None)
    #                 else:
    #                     d.update({l[k2]:[None]})
    #                 m1+=1
    #                 continue
    #             # if j.text=="Meeting Information":
    #             #     if d.get(l[k2])!=None:
    #             #         d[l[k2]].append(None)
    #             #     else:
    #             #         d.update({l[k2]:[None]})
    #             #     m1+=1
    #             #     continue
                    
                        
    #             # elif j.text=="Subject Category":
    #             #     if d.get(l[k2])!=None:
    #             #         d[l[k2]].append(None)
    #             #     else:
    #             #         d.update({l[k2]:[None]})
    #             #     m1+=1
    #             #     continue
    #             elif j.text=="Report/Patent Number":
    #                 if d.get(l[k2])!=None:
    #                     d[l[k2]].append(None)
    #                 else:
    #                     d.update({l[k2]:[None]})
    #                 m1+=1
    #                 continue
    #             elif j.text=="Keywords":
    #                 if d.get(l[k2])!=None:
    #                     d[l[k2]].append(None)
    #                 else:
    #                     d.update({l[k2]:[None]})
    #                 m1+=1
    #                 continue
    #             elif j.text=="Distribution Limits":
    #                 if d.get(j.text)!=None:
    #                     d[j.text].append("Public")
    #                 else:
    #                     d.update({j.text:["Public"]})
    #                 m1+=1
    #                 continue
    #             else:
    #                 if d.get(j.text)!=None:
    #                     d[j.text].append(i.text)
    #                 else:
    #                     d.update({j.text:[i.text]})
    #                 m+=1
    #                 m1+=1
    #         else:
                
    #             if d.get(l[k2])!=None:
    #                 d[l[k2]].append(None)
    #             else:
    #                 d.update({l[k2]:[None]})
    #         # except:
    #             # if d.get(l[k2])!=None:
    #             #         d[l[k2]].append(None)
    #             # else:
    #             #     d.update({l[k2]:[None]})
    #             # b=True
    #             # continue
                
    #     if b==True:
    #         break
                
        
            
            

        
  
            
    # final_df.append(pd.DataFrame(data=d))
    # final=pd.concat(final_df)
    # final.to_csv("data.csv")
    #pickle.dumps("output.pickle",data)  
    print(data)
    with open('output.pickle', 'wb') as f:
        pickle.dump(data, f)
    with open("page.txt",'a') as f:
        f.write(str(k))
    for btn in driver.find_elements("xpath",f'//a[@title="Download Document"]'):
        btn.click()
        time.sleep(200)
          
  
    k+=25
    
time.sleep()
driver.close()

