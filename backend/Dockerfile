FROM python:3.11-slim

# Evita perguntas interativas e atualiza o sistema
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema necessárias ao mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && apt-get clean

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements.txt e instala dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando padrão para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
