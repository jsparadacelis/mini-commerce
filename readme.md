# Descripción Comercio


Phanton commerce es un comercio qué funciona como aplicación web. la cual se comunica con la Tpaga API para realizar transacciones con sus productos. La aplicación está concebida como un proyecto Django, conformada por tres aplicaciones: usuarios, pagos y productos. La aplicación de pagos es la que se comunica con la Tpaga API para realizar transacciones sobre una orden creada en específico.

### Modelo de BD

![](ERDDiagram.png)

###  Tiempo estimado : 4 días 


###  Operaciones y tiempo invertido 

1) Creación de módulos - **10h** 
2) Escribiendo las vistas por cada paso de la transacción - **8h - 10h**
3) Implementando un pequeño sistema de registro y autenticación **3h - 4h**
4) Realizando pruebas en Heroku D: - **3h**

#### Creación de Modulos

El proyecto está concebido como un proyeto de Django. El proyecto está conformado por tres aplicaciónes: usuarios, pagos y productos. El modulo de pagos se comunica con la API de Tpaga para realizar las operaciones que tienen que ver con la creación, modificación y eliminación de ordenes generadas por los usuarios de la aplicación web. Realmente, la implementación de los modulos me llevó aproximadamente unas **10 horas** sumando todos los instantes en los que trabajé en ellos. Podría decirse que esta parte de la implementación, la desarrollé a manera incremental a medida que se me iban ocurriendo cosas,cómo poder registrar usuarios y qué cada usuario tuviera varias ordenes asociadas a el mismo. Cambios cómo ese también significan cambios en el modelo de la Base de Datos de la aplicación. 

#### Escribiendo las vistas

Las vistas en Django, permiten la gestión de los datos en el proyecto para posteriormente poder visualizarlos en las plantillas. El trabajo con las vistas, fue relativamente sencillo gracias a las capacidades con las qué cuenta Django. Tal vez lo más complicado de este punto, fue lograr armar y entregar los datos de manera qué en las plantillas fuera sencillo mostrar y entender los datos por parte del usuario final de la aplicación web. Muy relacionado con el tema de los modulos, el timpo total de implemtación de las vista fue apróximadamente entre **8 y 10 horas**, teniendo en cuenta qué practicamente el tiempo de implementación de los modulos coincide con el de las vistas de cada aplicación, entendiendo por aplicación los modulos qué conforman el proyecto de la aplicación web. 

#### Implementación de registro y autenticación de usuarios

Como parte de los modulos que conforman el proyecto, quise implementar la posibilidad de qué un usuario se registrará en la aplicación, y de esta forma poder tener control sobre las ordenes y el usuario al qué pertenecen. A nivel de base de datos, un usuario puede generar muchas ordenes. En está implementación, trabajé aproximadamente entre unas **3 y 4 horas**. 

#### Realizando pruebas en Heroku 

El despliegue en Heroku fue de las actividades más complicadas, ya qué poca es la experiencia sobre el tema. Anteriormente había hecho un despliegue utilizando heroku, pero este se me hacía más complicado, dado qué en este caso hago uso de archivos estáticos como las plantillas, las hojas de estilos, etc. Además de la subida de archivos y condiguraciones del proyecto, el despliegue también implíca las pruebas que se realicen, por ejemplo, en muchas ocaciones mis vistas retornaban errores propios de Django qué debía solucionar para seguir con las pruebas, lo que implíca solucionar, actualizar el git y agregar los cambios a la rama remota qué gestiona el despliegue en Heroku. En este item, trabajé aproximadamente unas **3 horas** a la espera del tiempo adicional qué invierta en las ultimas pruebas antes de enviar esto. 

### Revertir Transacciones

Para revertir una transacción, se deben ingresar con:
 - usuario : manager
 - contraseña : commerce123

 ![](images_doc/login.png)


 Una vez dentro se despliega la siguiente interfaz

![](images_doc/reverted.png)

 En el momento en qué se da clic en revertir, la aplicación envía una solicitud a la Tpaga API. La respuesta de la operación se ve reflejada así:

 ![](images_doc/message.png)


### Endpoint a implementar

Un endopoint para implementar podría ser listar la información de las ordenes creadas por cada usuario en una ventana de tiempo. A partir de una fecha de inicio y una fecha de fin, mostar los detalles de cada orden, cómo sus productos, su estado y la cantidad de artículos por producto. 

### ¿Qué pueden mejorar?
Sobre lo positivo de la prueba, personalmente me gusto la presentación de la documentación. El uso del glosario ayuda a entender el contenido de cada solicitud realizada a la API. 

#### Para mejorar
- Hubiera sido genial qué cada elemento de la lista de purchase_items tuviera un campo dónde se pueda consgnar la cantidad de cada producto. 

- En la página principal de la documentación, muestran un diagrama con el flujo de la aplicación. El diagrama se llama "Diagrama de comunicación" y permite ver cómo se comunican los componentes del negocio en tiempo de ejecución. Personalmente le daría ese nombre, aunque igualmente cumple con el cometido de su nombre que es explicar el flujo de la aplicación. 

#### Recomendaciones

En lo personal, para el trabajo con Django recomiendo tres libros:

- Django, la guía definitiva: Desarrolla aplicaciones Web de forma rápida y sencilla usando Django. Adrian Holovaty y Jacob Kaplan-Moss

- Two Scoops of Django 1.11 Best Practices for Django. Daniel Roy Greenfeld y Audrey Roy Greenfeld
- Django RESTful web services. Gaston Hillar

Estos son los libros qué he utilizados como apoyo para desarrollar en Django. Otros materiales se pueden encontrar en [Medium](https://medium.com/). Esta es una página dónde profesionales de varias areas escriben sobre sus experiencias. Se encuentran artículos sobre desarrollo entre otras areas. 

En el tema de buenas prácticas, algo que intento aplicar siempre es hacer código que se entienda, de forma qué a la hora de compartirlo con la comunidad, cualquiera pueda entenderlo. Creo que esto es lo mas valioso de filosofías cómo el software libre: qué el código sea lo mas legible. 

Herramienta para alojar aplicaciones, sólo conozco Heroku. Existen otras cómo AWS, Digital Ocean. Existe otra herramienta quéno he visto muy referenciada qué se llama [D2C](https://d2c.io/). Permite conectarse con AWS, Google cloud, digital ocean. Para realizar despliegues  y pruebas locales a partir de repositorios, recomiendo docker. Se consigue muy buena documentación en internet. Dentro de su hub de aplicaciones se consiguen muchas herraminetas qué hacen sencillo el poder ejecutar aplicaciones de otros en nuestras máquinas. 

Una página qué recomiendo para el trabajo con vistas basadas en clases es [Classy Class-Based views](https://ccbv.co.uk/). Tienen información referente a las clases de las que heredan las vistas basadas en clases en django. Muy buena documentación. 

#### Para realizar pruebas con Docker,ejecutar los siguientes comandos :
1. git clone https://github.com/jsparadacelis/mini-commerce.git
2. cd mini-commerce
3. sudo docker-compose up
4. Entrar a http://127.0.0.1:8000/ desde el navegador

¡ Y listo !
