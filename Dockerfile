FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 1) зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) код бота (mini-app не копируем)
COPY src ./src

# делаем src пакетом (если файла нет в репо)
RUN sh -c "test -f src/__init__.py || touch src/__init__.py"

# чтобы import 'src.*' всегда работал
ENV PYTHONPATH=/app

# 3) запуск
CMD ["python", "-u", "-m", "src.main"]
