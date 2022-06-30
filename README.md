# **CNH Info Extract**
Projeto no qual tem como objetivo extrair as informações existentes em um documento de habilitação nacional (Brasil).
As informações que a aplicação extrairá são:
>- Nome
>- CPF
>- Documento de identidade
>- Orgão emissor
>- UF
>- Data de nascimento
>- Validade
>- 1º habilitação
>- Número do registro
>- Categoria

## **Info**
### **setup.py**
Script responsável por instalar todos os pacotes necessários para a aplicação.
### **library**
Pacote que contém todos os códigos necessários para a execução do programa.
### **test**
Pasta utilizada para testar se as instalações foram feitas corretamente.

## **Setup**
É recomendado que seja feita a instalação da demo dentro de um ambiente virtual. Para isso, execute o comando a seguir no terminal e em seguida ative o ambiente para instalar os pacotes da demo.
```
python3 -m venv "nome_do_ambiente"
source /path/to/"nome_do_ambiente"/bin/activate
```
Para preparar o ambiente para a execução da aplicação execute o script setup.py no terminal. Ele será responsável por instalar todos os pacotes necessários para a demo.
```
pip install .
```
Teste se os pacotes foram instalados corretamente. (Etapa não obrigatória)
```
python3 test/packages_test.py
```
## **Execução**
Para rodar a aplicação vá para library e execute o script run.py no terminal.
```
python3 library/run.py
```
Para alterar a entrada da câmera que será utilizada durante a aplicação utilize o comanda "--source" ao roda o script "run.py".
```
python3 library/run.py --source 2
```
*Caso apareça um erro da inicialização da câmera, altere o valor do source, a entrada da câmera que será utilizada pode ser diferente para cada caso.*

## **Dados**
Ao extrair as informações do documento será criado na mesma pasta do projeto um arquivo nomeado como "result.json", contendo todas as informações retiradas do documento.

*É importante resaltar que para uma demo o documento "result.json" será sempre reescrito quando for extraido novas informações, logo, os dados retirados dos documentos não serão guardados e apenas o último registro será salvo. Caso a aplicação não consiga extrair corretamente as informações de um campo expecífico o valor retornado será None para o campo.*

## **Dicas**
>- *Aproxime o documento o mais próximo da câmera em uso e espere que a imagem foque corretamente para uma leitura melhor das informações na imagem.*
>- *Evite tremer a câmera ou o documento. Deixe ambos o mais estático possível.*
>- *Posicione o documento o mais reto possível para uma melhor extração das informações.*
