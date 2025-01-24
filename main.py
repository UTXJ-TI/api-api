'''Inicializar el proyecto en FastAPI.'''
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Usuario,Genero,Role,UpdateUsuario
app = FastAPI()
db: List[Usuario] = [
    Usuario(
            id = uuid4(),
            nombre = "Marco Antonio",
            apellidos = "Santos Quiroz",
            genero = Genero.Masculino,
            roles = [Role.admin],
	  ),
	Usuario(
            id = uuid4(),
            nombre = "Hugo Yibran",
            apellidos = "Dominguez Leon",
            genero = Genero.Otro,
            roles = [Role.user],
	  ),
    Usuario(
            id = uuid4(),
            nombre = "Hector",
            apellidos = "Luna Santos",
            genero = Genero.Masculino,
            roles = [Role.user],
	  ),
]
@app.get("/")
async def root():
    '''Bienvenida.'''
    return("Bienvenida","Hola simples mortales de JS")
@app.get("/api/usuarios")
async def get_usuarios():
      return db
@app.post("/api/usuarios")
async def inser_usuarios(usuario: Usuario):
     db.append(usuario)
     return {"id":usuario.id}
@app.delete("/api/usuarios/{id}")
async def delete_usuarios(id: UUID):
    for usuario in db:
        if usuario.id == id:
            db.remove(usuario)
        return
    raise HTTPException(status_code=404, detail=f"Error al eliminar, id {id} falla.")
@app.put("/api/usuarios/{id}")
async def upadte_usuarios(user_update: UpdateUsuario, id: UUID):
    for usuario in db:
        if usuario.id == id:
            if user_update.nombre is not None:
                usuario.nombre = user_update.nombre
            if user_update.apellidos is not None:
                usuario.apellidos = user_update.apellidos
            if user_update.genero is not None:
                usuario.genero = user_update.genero
            if user_update.roles is not None:
                usuario.roles = user_update.roles
        return usuario.id
    raise HTTPException(status_code=404, detail=f"Error al eliminar, id {id} falla.")