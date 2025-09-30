# Usando Python com Alpine (leve)
FROM python:3.11-alpine

# Diretório de trabalho
WORKDIR /app

# Instalando dependências mínimas do sistema
RUN apk add --no-cache libffi-dev

# Copiar arquivos necessários
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código
COPY . .

# Expor a porta da aplicação
EXPOSE 3000

# Comando para rodar
CMD ["python", "app/app.py"]
