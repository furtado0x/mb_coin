# Usando a imagem Python oficial
FROM python:3.11-slim

# Definir variáveis de ambiente para o Poetry e Python
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="$POETRY_HOME/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && apt-get clean

# Instalar Poetry
RUN pip install --upgrade pip && pip install --no-cache-dir poetry

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do Poetry
COPY pyproject.toml poetry.lock ./

# Instalar as dependências do projeto usando o Poetry
RUN poetry install --no-root

# Copiar o código-fonte da aplicação
COPY . .
