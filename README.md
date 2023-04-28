# eBuyme
O eBuyme é um site de simulação de e-commerce criado em django. 
### Preview
<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Homepage
</p>
<img src="https://user-images.githubusercontent.com/121815039/215379100-993a4c0f-f80c-4f30-b1c2-aa5d0d8055ed.jpg">
</td> 
<td width="50%">
<br>
<p align="center">
  Página do anúncio
</p>
<img src="https://user-images.githubusercontent.com/121815039/215379215-b991665e-b551-424b-8d0b-ab88a7b956c6.jpg">  
</td>
</table>



# Rodar localmente
### Clonando o repositório

--> Clone o repositório utilizando o comando abaixo:

```bash
git clone https://github.com/caamps/ebuyme.git
```


--> Entre na pasta onde estão localizados os arquivos:

```bash
cd eBuyme
```
--> Crie um ambiente virtual:

```bash
# Instalando o virtualenv
pip install virtualenv

# Criando o ambiente virtual
virtualenv envname
```
--> Ative o ambiente virtual:


```bash
envname\scripts\activate
```

--> Instale os requisitos:

```bash
pip install -r requirements.txt
```

### Configurações necessárias em settings.py
Para que o aplicativo funcione localmente, é necessário fazer as seguintes alterações no arquivo <b>settings.py</b> localizado na pasta eBuyme.
- [Cloudinary](https://cloudinary.com/): O projeto utiliza o cloudinary para armazenamento de uploads. Insira as credenciais da sua conta em: 
![image](https://user-images.githubusercontent.com/121815039/215380161-cad4a0a4-3a52-4e62-b8a9-499a2a801155.png)
- [Postgresql](https://www.postgresql.org/): O banco de dados utilizado é o postgresql. Insira as informações do seu banco de dados em: 
![image](https://user-images.githubusercontent.com/121815039/215380338-2f41c2d0-9530-4925-968e-501c9741a564.png)
- Verificação de email: O projeto conta com um sistema de envio de emails para verificação e alteração da senha. Insira as informações de um email
do serviço [Gmail](https://mail.google.com/mail/) válido em: <br/>
![image](https://user-images.githubusercontent.com/121815039/215380765-d619e0f3-bf91-47d9-b11c-d1830994165c.png)

Note que, caso a verificação em duas etapas esteja ativada, o serviço não funcionará. É necessário criar uma senha para o aplicativo em https://myaccount.google.com/security<br/>
--> A secret key utilizada foi gerada novamente e é diferente da utilizada em https://ebuyme.up.railway.app/


### Ativando o banco de dados
--> Para migrar as tabelas para seu banco de dados postgresql:
```bash
python manage.py migrate
```
O projeto é iniciado com 4 anúncios feitos por um usuário genérico, para fins de demonstração.

### Iniciando o site
--> Para iniciar o app, execute:

```bash
python manage.py runserver
```


### ⚠ Então, o servidor será iniciado em http://127.0.0.1:8000/





