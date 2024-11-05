import sender_stand_request
import data
from data import kit_body
from sender_stand_request import post_new_client_kit

    #Verificar que el kit con este nombre se ha creado exitosamente:
def positive_assert(kit_body):
    #Crear un nuevo kit
    resp_kit = post_new_client_kit(sender_stand_request.get_atk_from_body(),kit_body)
    #Verificar el código de respuesta
    assert resp_kit.status_code == 201
    #Verificar si el nombre en la respuesta coincide con el nombre en la solicitud
    assert resp_kit.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    # Llama a la función post_new_client_kit con un token de autenticación obtenido
    # de sender_stand_request y el cuerpo del kit proporcionado.
    resp_kit = post_new_client_kit(sender_stand_request.get_atk_from_body(),kit_body)
    # Verifica que la respuesta tenga un código de estado 400, indicando que se ha
    # producido un error por una solicitud incorrecta.
    assert resp_kit.status_code == 400

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body1)

# Prueba 2. "Comprobar que el kit ha sido creado exitosamente, con el parámetro "name" con 255 caracteres)
def test_create_kit_511_letters_in_name_get_success_response():
   # kit_body = ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(data.kit_body2)

# Prueba 3. "Comprobar que devuelve el error 400 con el parámetro "name" que contiene una cadena vacía)
def test_create_kit_empty_name_get_error_response():
  ##  kit_body = get_kit_body("")
    negative_assert_code_400(data.kit_body3)

# Prueba 4. "Comprobar que devuelve el error 400 (El parámetro "name" que contiene 256 caracteres)
def test_create_kit_512_letters_in_name_get_error_response():
  #  kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(data.kit_body4)

# Prueba 5. "Comprobar que el kit ha sido creado exitosamente, en el parámetro "name" que contiene caracteres especiales)
def test_create_kit_as_special_symbol_in_name_get_success_response():
  #  kit_body = get_kit_body("'№%@',")
    positive_assert(data.kit_body5)

# Prueba 6. "Comprobar que el kit se ha creado exitosamente, el parámetro "name"contiene palabras con espacios)
def test_create_kit_has_space_in_name_get_success_response():
 ##   kit_body = get_kit_body(" A Aaa ")
    positive_assert(data.kit_body6)

# Prueba 7. "Comprobar que el kit se ha creado exitosamente, el parámetro "name" contiene una cadena de números)
def test_create_kit_has_number_in_name_get_success_response():
  #  kit_body = get_kit_body("123")
    positive_assert(data.kit_body7)

# Prueba 8. "Comprobar que devuelve el error 400, el parámetro "name" está ausente en el cuerpo de la solicitud)
def test_create_kit_no_name_get_error_response():
 #   kit_body = data.kit_body.copy()
 #   kit_body.pop("name")
    negative_assert_code_400(data.kit_body8)

# Prueba 9. "Comprobar que devuelve el error al crear el kit, con el tipo de parámetro "name": número)
def test_create_kit_number_type_name_get_error_response():
##    kit_body = get_kit_body(123)
    negative_assert_code_400(data.kit_body9)

