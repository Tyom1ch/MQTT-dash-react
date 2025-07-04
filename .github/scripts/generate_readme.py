from google import genai
import subprocess
import os
import re

# =================================================================
# Взаємодія з Gemini API залишається без змін, як ви і просили
client = genai.Client()
# =================================================================

# --- РЕФАКТОРИНГ ЛОГІКИ GIT ---

def get_sorted_tags():
    """
    Повертає список всіх тегів, відсортованих за датою створення
    (від найновішого до найстарішого).
    """
    try:
        # Команда git tag сортує теги за датою їх створення у зворотному порядку
        tags_raw = subprocess.check_output(
            ["git", "tag", "--sort=-creatordate"]
        ).decode().strip()
        return tags_raw.split('\n')
    except subprocess.CalledProcessError:
        # Повертає порожній список, якщо тегів немає
        return []

def get_commits_between(old_tag, new_tag):
    """
    Отримує відформатований список комітів між двома тегами.
    """
    if old_tag:
        # Діапазон між старим і новим тегом
        command = ["git", "log", f"{old_tag}..{new_tag}", "--pretty=format:- %s"]
    else:
        # Якщо старого тега немає (перший реліз), беремо всі коміти до нового тега
        command = ["git", "log", new_tag, "--pretty=format:- %s"]
    
    try:
        return subprocess.check_output(command).decode().strip()
    except subprocess.CalledProcessError:
        return ""

# 1. Отримуємо всі теги, відсортовані за часом
all_tags = get_sorted_tags()

if not all_tags:
    print("Error: No tags found in the repository. Exiting.")
    exit(1) # Виходимо з помилкою, бо немає чого обробляти

# 2. Визначаємо поточний і попередній теги
current_tag = all_tags[0]
previous_tag = all_tags[1] if len(all_tags) > 1 else ""

print(f"-> Detected current tag: {current_tag}")
print(f"-> Detected previous tag: {previous_tag or 'None (first release)'}")

# 3. Отримуємо коміти, використовуючи надійні теги
commits = get_commits_between(previous_tag, current_tag)

# 4. Перевірка: якщо комітів немає, не турбуємо API
if not commits:
    print("-> No new commits found between tags. README will not be updated.")
    exit(0) # Виходимо успішно, бо це очікувана поведінка

print("\n--- Sending a list of commits to the API ---")
print(commits)
print("------------------------------------------\n")

# --- КІНЕЦЬ РЕФАКТОРИНГУ ---


# Формування промпту залишається без змін
prompt = f"""
Згенеруй changelog у форматі нижче, для тега {current_tag}.
Використовуй українську мову. Якщо тег не має змін, просто вкажи, що немає змін.
Не говори щось типу "Ось список змін", просто дай список змін у форматі, який я вказав нижче.
Структура така:

v.v.v - <короткий опис релізу одним словом.>
✨ Нові можливості (Added)
<тут перелік нових фіч>
♻️ Зміни (Changed)
<тут перелік змін>
🐛 Виправлення (Fixed)
<тут перелік багфіксів>
🧹 Внутрішні зміни (Housekeeping)
<внутрішні зміни, видалення сміття тощо>

Ось список комітів для аналізу:
{commits}
"""

# Взаємодія з Gemini API залишається без змін
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)

# Оновлення README.md залишається без змін
# (додано лише encoding для кращої сумісності з кирилицею)
with open("README.md", "r", encoding="utf-8") as f:
    old_content = f.read()

new_changelog = response.text.strip()

# Вставка нового changelog одразу після маркера (замінюємо всю секцію)
pattern = r"(<!-- CHANGELOG START -->)(.*?)(<!-- CHANGELOG END -->)"
# Додаємо заголовок до нового контенту
full_new_content = f"## {current_tag}\n\n{new_changelog}"
# Вставляємо новий контент і зберігаємо старий
replacement = f"\\1\n\n{full_new_content}\n\\2\\3"
# Якщо ви хочете повністю заміняти старий лог, використовуйте:
# replacement = f"\\1\n\n{full_new_content}\n\n\\3"

new_readme = re.sub(pattern, replacement, old_content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print("✅ README.md has been successfully updated.")