FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y \
    netcat-openbsd \
    gcc \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivo de requisitos
COPY requirements.txt .

# Instala dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Copia e dá permissão ao script wait-for-it
COPY scripts/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
