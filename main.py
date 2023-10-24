from fastapi import FastAPI
import random

app = FastAPI()

mao = 0
historico = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/terminou/")
async def terminou():
    if mao == 21:
        return {"message": "ganhou"}
    elif mao < 21:
        return {"message": "pegue mais cartas"}
    else:
        return {"message": "voce estourou"}

@app.get("/historico/")
async def historico_part():
    return {"partidas": historico}

@app.get("/historico/{id}")
async def historico_id(id):
    return {"partida": historico[int(id)]}


@app.put("/nova_carta/")
async def nova_carta():
    global mao
    carta = random.randint(1, 11)
    mao = mao + carta
    return {"message": f"a nova carta foi {carta}"}

@app.post("/novo_jogo/")
async def novo_jogo():
    global mao
    historico.append(mao) 
    mao = 0
    return {"message": "novo jogo criado"}