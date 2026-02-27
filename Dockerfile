FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements1.txt
EXPOSE 5000
CMD ["python3", "-m", "src.website.app"]