import requests
import data
import configuration

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             headers=data.headers)

def get_atk_from_body():
    answer_server = post_new_user(data.user_body)
    # Respuesta del servidor con la data de user_body que se uso en la funcion anterior
    token_guardado = answer_server.json()["authToken"]
    # De la respuesta del servidor tomar el authoken
    return token_guardado #solo se guarda el retorno del authoken sin imprimir para
#posteriormente llamar a la funcion en la creacion del kit.


def post_new_client_kit(auth_token, kit_info):
   # auth_token = get_atk_from_body()# Funcion para la creacion del kit
    headers_with_authorization = data.headers.copy() #copiamos de data los headers
    headers_with_authorization ["Authorization"] = f"Bearer {auth_token}" #
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                json=kit_info,
                  headers=headers_with_authorization,) # Llamamos al servidor con la URL, y el call kit_path


