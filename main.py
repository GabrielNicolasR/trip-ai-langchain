import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "praia"

modelo_de_prompt = PromptTemplate(
    template="""
    Crie um roteiro de viagem de {dias} dias,
    para uma família com {criancas} crianças,
    que gostam de {atividade}
    """
)

prompt = modelo_de_prompt.format(
    dias=numero_dias,
    criancas=numero_criancas,
    atividade=atividade,
)

print("Prompt : \n", prompt)

modelo = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    temperature=0.5,
    api_key=api_key,
)

resposta = modelo.invoke(prompt)
print(resposta.content)
