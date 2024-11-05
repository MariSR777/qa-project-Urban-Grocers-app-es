# Proyecto Urban Grocers 

Este proyecto automatiza creación de kits de productos para la aplicación Urban Grocers,
validando varias características el campo "name"

"" Requisitos:
1) PyCharm 2024.2.3
2) Requests
3) Pytest
4) apidocs

"" Instrucciones para la ejecución
1) Se clona el repositorio
2) Asegurar que se tienen todas dependencias instaladas
3) Se ejecutan las pruebas

"" Descripción e los archivos
1) 'configuration.py": Configuración de rutas y URL
2) 'data.py': datos y encabezados.
3) sender_stand_request.py: Contiene las funciones de envío de solicitudes
4) create_kit_name_kit_test.py: Este archivo contiene las pruebas automatizadas

	a) Función positive_assert:Tiene como objetivo validar que la creación un nuevo kit
	   se realizó correctamente  que la respuesta coincide con la solicitud
	b) kit_body: Este parámetro representa los datos del kit que se desea crear.
	c) post_new_client_kit: Esta función realiza la solicitud HTTP para crear el kit, 
	   utilizando un token de autenticación y el cuerpo del kit.
	d) assert: Verifica  primer aserción que el código de estado sea 201(creado), lo que 	   indica que la operación fue exitosa.
	   La segunda aserción comprueba que el nombre en la respuesta JSON coincide con el 	   nombre que se envío en la solicitud. 
	-----------------

        a) Contiene la Función negative_assert_code_400: Tiene como objetivo probar una
	   condición negativa, es decir, asegurarse de que la solicitud al servidor genera 
	   un error específico (código 400).
	b) Kit_body: Es un parámetro que representa el cuerpo de la solicitud que se está  	   enviando, espera que de como resultado un error.
	c) post_new_client_kit: Esta solicitud realiza solicitud HTTP y se le pasan el token 
	   de autenticación cuerpo del kit.
	d) assert: Se utiliza para comprobar que la respuesta tiene el código de estado 	   esperado (400). Si no es así, la prueba fallará, indicando que la entrada no
           produjo resultado esperado.


5) 'gitignore': Contiene la lista de archivos y carpetas que deben ignorarse.