from demos.config.database_connection import mongo_client


db = mongo_client["test-openai"]
collection = db["users"]


def save_to_chat(new_chat_list, user_phone):

    result = collection.update_one(
        {"user_phone": user_phone},
        {"$set": {"chats": new_chat_list}},
        upsert=True
    )

    if result.upserted_id is not None:
        print("Usuario creado:", user_phone)
    elif result.matched_count > 0:
        print("Usuario encontrado y actualizado:", user_phone)
    else:
        print("Error al buscar/crear usuario")

    mongo_client.close()
        
def find_user(user_phone):
    usuario = collection.find_one({"user_phone": user_phone})

    if usuario:
        return usuario
    else:
        print("Usuario no encontrado")