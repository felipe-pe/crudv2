## Nome do projeto: AircraftDash

**Integrantes:** 

Beatriz Pama - 11914052

Felipe da Silva Pereira - 9276881


## Execução

1. Clone o repositório a alguma pasta local.

    ```
    git clone https://github.com/felipe-pe/crudv2.git
    ```

2. É recomendado criar um ambiente virtual usando `venv` utilizando o python (a depender do seu sistema operacional). Para isso, use o comando:

    ```
    cd crudv2
    python -m venv env
    ```

3. Depois, e ative o ambiente:

    ```
    .\env\bin\Activate.ps1
    ```
    
4. Faça as migrações do Django:

    ```
    cd controle_voos
    python manage.py makemigrations
    python manage.py makemigrations voos
    python manage.py migrate
    ```
5. Execute os testes:

    ```
    test
    ```

6. Para rodar o projeto, use os comandos:

    ```
    python manage.py runserver
    ```


7. Finalmente, para executar o sistema, acesse o link:

    http://localhost:8000/
