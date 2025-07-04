# Edwic.Dash

![image](https://github.com/user-attachments/assets/cc4f998c-a5bb-49e9-a80c-bbe3e20a9859)

<!-- CHANGELOG START -->

Ось згенерований changelog для тега `v0.0.2с`:

v0.0.2с - Declarative Widgets & Major Refinements
✨ Нові можливості (Added)
*   Додано декларативний віджет для попереднього перегляду файлів.
*   Реалізовано адаптивний макет (responsive layout) для віджетів.
*   Додано можливість кастомізації стилів для всіх віджетів.

♻️ Зміни (Changed)
*   Покращено продуктивність рендерингу віджетів.

🐛 Виправлення (Fixed)
*   Виправлено некоректне відображення довгих імен файлів у попередньому перегляді.
*   Вирішено проблему зі зсувом макету (layout shift) при завантаженні віджетів.

🧹 Внутрішні зміни (Housekeeping)
*   Оновлено залежності.
*   Перенесено код віджетів в окремі файли для кращої організації.
*   Оновлено файл README.md з інформацією щодо використання нових віджетів.
*   Додано pre-commit хуки для перевірки коду (linting).

<!-- CHANGELOG END -->

# Запуск дашборду

---

## ⚡ One-liner для запуску

```bash
curl -fsSL https://raw.githubusercontent.com/tyom1ch/edwic-dash-alpha/main/install.sh -o install.sh && bash install.sh
```

---

> ⚠️ Потрібен встановлений **Docker**

---

## 🚀 Відкривай у браузері

```
http://localhost:4173
```

---

### 📡 Щоб зайти з іншого пристрою у мережі

```
http://<IP_машини_де_запущено>:4173
```

---

### 🛠️ Корисні команди

* Зупинити й видалити Docker-контейнер:

  ```bash
  docker stop edwic-dash && docker rm edwic-dash
  ```

* Перезапустити Docker-контейнер:

  ```bash
  docker restart edwic-dash
  ```
---
