
import os
import pandas as pd
import openai

data = pd.read_csv("coc_q.csv")
data
data.head(10)
data.dropna(inplace = True) 
data = data.drop_duplicates()
data
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stpwrds = set(stopwords.words('english'))
def clean_text(text):
  new_text = [word for word in text.split(" ") if word not in stpwrds]
  return " ".join(new_text)


import re

open("data.json", "w").close()
import json
test = []

old_id = 0

d= dict()
i = 0
with open("data.json", 'a') as f:
    while(i<=data.shape[0]):  
        if i==len(data):
            break
        new_id = data.loc[i]["ID"] 
        st = "{\"prompt\": \"" 
        new_data = data[data["ID"]==new_id]
        prom = clean_text(new_data["question"].values[0])
        st = "{\"prompt\": \"" + prom + "\\n\\n###\\n" 
        for ids in range(new_data.shape[0]): 
                if ids == 0:
                    st+= "\\nCustomer: " + new_data.iloc[ids]["question"] +"\\nAgent: "
                    st+="\""
                    st+= ","+"\"completion\""+":"+"\" " +new_data.iloc[ids]["answer"]+"\\n\""
                    st+="}"
                    st+="\n"
                    f.write(st)
                else:
                    st = "{\"prompt\": \"" + prom + "\\n\\n###\\n" 
                    for sub_ids in range(ids+1):
                        if sub_ids==0:
                            st += "\\nCustomer: " + new_data.iloc[sub_ids]["question"] +"\\nAgent: "+new_data.iloc[sub_ids]["answer"]+"\\n" 
                        elif sub_ids!=ids:
                            st += "Customer: " + new_data.iloc[sub_ids]["question"] +"\\nAgent: "+new_data.iloc[sub_ids]["answer"]+"\\n" 
                        else:
                            st+= "Customer: " + new_data.iloc[ids]["question"] +"\\nAgent: "
                            st+="\""
                            st+= ","+"\"completion\""+":"+"\" " +new_data.iloc[ids]["answer"]+"\\n\""
                            st+="}"
                            st+="\n"
                            f.write(st)

                i+=1


OPENAI_API_KEY="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"


os.environ["OPENAI_API_KEY"] ="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"

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

def final_result(question):
    prom = f'\nCustomer: {question}\nAgent:' 
    print(prom)

    response = client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": question,
            }
        ],
        model="gpt-3.5-turbo",
    )


    choice = response.choices[0]
    message = choice.message
    response_text = message.content.strip()
    return response_text




