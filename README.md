#Deben Agregar la multiplicación y la divisón

Validar que no se divida entre cero

Mejorar el menú usando while

usar try/except

Permitir miltiple usos hasta que seleccione la opción salir.

1 Paso a paso

Haga el fork del reposotiro deseado.

2 Clonar

git clone https://github.com/luarserna/calculadora_colab.git

3 Cree una rama con su nombre

git checkout -b sebas

4. Editas la calculadora

5. guarda
   
git add .

git commit "Agregar funciones"

6. Subiendo la rama
   
git push origin sebas

# Comandos Git basicos:

## comandos basicos de consola 

1. mkdir : Crear un directorio o carpeta
2. echo "bienvenidos a git" > ejemplo.py
3. cd : acceder a un directorio o carpeta 
    **Ejemplo:** cd documents
4. cd .. : Regresar a la carperta anterior 


## comandos basicos para el control de versiones git 

## **Inicializar Repositorio o clonar repositorio remoto**

### **Inicializar Repositorio local**

1. **Configutar git:** 

    git config --global user.name oscarmauriciogiraldo
    git config --global user.email oscardan@utp.edu.co

    **Nota :** Esta accion se hace si no se ha configutado previamente con el nombre de usuario y correo electronico, esto es escencial para realizar commits y el acceso al repositorio remoto

2. **git init:** Inicia un repositorio local
    Ejemplo: ubicado en el direcotorio en el que se requiere crear el repositorio
    abril la consola y ejecutar el comando:

    git init

    **Nota :** Esta accion solo se hace una vez para un repositorio que ya ha sido inicializado 

3. **git status:** Muestra el estado de los archivos editadosdel workspace del repositorio, ademas de informacion necesaria, como la rama en la que se encuentra el usuarioen ese momento.

4. **git ranch:** Muestra la rama en la cual se encuentra ubicado


5. **git add :** agrega los archivos al repositorio local o los cambios realizados sobre un archivo.

    **git add**: Se puede usar de dos formas:
    git add fileName / git add .
    - **git add fileName**: Agrega un archivo en espesifico al repositorio local
    - **git add .** : Agrega todos los archivos editados del workspace al repositorio.

6. **git commit:** toma un snapshot, es decir una foto de la version del code que se lleva hasta el momento para llevar un control de versiones.
    - **Ejemplo:** git commit -m "mi primer commit"

#### *Agregar repositorio remmoto:*

Se hace una conexion del repositorio local, al repositorio remoto.

7. **git add remote:** agregar o conectar el repositorio remoto:

    git remote add origin https://github.com/repo-remoto

#### *Subir los cambios al repositorio remoto*

8. **git push:** Direcciona los cambios al repositorio remoto, es decir al gitHub, gitLab o Cualquer herramienta que se este utilizando en el momento.

    **Ejemplos y Usuabilidad:**

    - **git push:** sube al repositorio remoto todos los cambios que se encuentran en el repositorio local.

    - **git push origin Master:** Sube al repositorio remoto solo los cambios que se encuentran en la rama Master local

    - **git push -u origin RamaName :** recomndable la opcion -u es para que sea unidireccional

### **Clonar repositorio remoto**

1. **git clone:** clona el repositorio remoto en un area de trabajo local, este se convierte entonces en un repositorio local con la coexión directa al repositorio remoto, por lo que para este caso ya no es necesario ejecutar los comandos:

    - *git init*
    - *git add remote origin*

   **Ejemplo**: git clone https://github.com/oscarmauriciogiraldo/project-BootCamp.git








 





 


8. git pull

11. git checkout -n rama-name




