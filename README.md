# 🚀 Dockerized Flask + MySQL Without Docker Compose

This project demonstrates how I connected a Flask app and a MySQL database using **plain Docker commands**, step by step — no Docker Compose involved.

---

## 🔧 What I Did

- Wrote a `Dockerfile` to containerize the Flask app
- Used `requirements.txt` to install dependencies
- Set up a **custom Docker network** so containers could talk
- Ran a MySQL container manually
- Connected Flask to MySQL using `pymysql`

---

## 🐳 Commands I Used

### 1️⃣ Build Flask Image
```bash
docker build -t flask-app .

2️⃣ Create Docker Network

docker network create flask-net

3️⃣ Run MySQL Container

docker run -d \
  --name mysql-db \
  --network flask-net \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=testdb \
  -e MYSQL_USER=testuser \
  -e MYSQL_PASSWORD=testpass \
  mysql:5.7

4️⃣ Run Flask Container

docker run -d \
  --name flask-app \
  --network flask-net \
  -p 5000:5000 \
  flask-app


---

✅ Output

When visiting http://localhost:5000, you should see:

> ✅ Connected to MySQL from Flask!
