import pandas as pd

df = pd.read_csv('issues_chatbot.csv')
df['Body'] = df['Body'].astype(str)
df = df[df['Body'].str.contains('conversa|utter|intent|resposta|mensagem')] 

df.to_csv('issues_conversacionais.csv')
