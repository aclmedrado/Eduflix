# Usar a imagem oficial do Python 3.9 slim
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências
COPY ./app/requirements.txt requirements.txt

# Instalar as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação
COPY ./app /app

# Expor a porta 8000 para o Gunicorn
EXPOSE 8000

# Comando para rodar a aplicação com Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]
