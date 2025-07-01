# Edwic.Dash
![image](https://github.com/user-attachments/assets/cc4f998c-a5bb-49e9-a80c-bbe3e20a9859)

---

## ⚡ One-liner для запуску

```bash
docker pull ghcr.io/tyom1ch/edwic-dash-alpha:latest && \
docker run -d -p 4173:4173 --name edwic-dash ghcr.io/tyom1ch/edwic-dash-alpha:latest
```

---

## 🚀 Відкривай у браузері

```
http://localhost:4173
```

---

### 📡 Щоб зайти з іншого пристрою у мережі

```
http://<IP_машини_де_запущено_контейнер>:4173
```

---

### 🛠️ Корисні команди

* Зупинити й видалити контейнер:

  ```bash
  docker stop edwic-dash && docker rm edwic-dash
  ```

* Перезапустити контейнер:

  ```bash
  docker restart edwic-dash
  ```

---
