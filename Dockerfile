
#1. Base Image 
FROM python:3.12-slim

#2. Set working directory
WORKDIR /app

#3. Copy requiremnt first 
COPY requirement.txt .

#4. Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

#5. copy rest of app
COPY . .  

#6. EXPOSE Flask port
EXPOSE  5050

#7.RUN APP
CMD ["python", "app.py"]
