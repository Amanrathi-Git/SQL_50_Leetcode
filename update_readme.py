import os
import re

def extract_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    problem = re.search(r'-- Problem:\s*(.*)', content)
    difficulty = re.search(r'-- Difficulty:\s*(.*)', content)
    concept = re.search(r'-- Concept:\s*(.*)', content)
    link = re.search(r'-- Link:\s*(.*)', content)
    
    if problem and difficulty and concept and link:
        return {
            'problem': problem.group(1).strip(),
            'difficulty': difficulty.group(1).strip(),
            'concept': concept.group(1).strip(),
            'link': link.group(1).strip()
        }
    return None

def update_readme():
    sql_files = []
    for root, dirs, files in os.walk('.'):
        # Ignore hidden folders like .git and .github
        if '.git' in root or '.github' in root:
            continue
        for file in files:
            if file.endswith('.sql'):
                sql_files.append(os.path.join(root, file))
    
    problems_data = []
    for file in sql_files:
        data = extract_metadata(file)
        if data:
            problems_data.append(data)
    
    if not problems_data:
        print("No valid formatted .sql files found.")
        return

    table = "| Problem | Difficulty | Concept |\n"
    table += "|---|---|---|\n"
    for item in problems_data:
        diff = item['difficulty']
        diff_icon = "🟢 Easy" if diff.lower() == 'easy' else "🟡 Medium" if diff.lower() == 'medium' else "🔴 Hard" if diff.lower() == 'hard' else diff
        table += f"| [{item['problem']}]({item['link']}) | {diff_icon} | {item['concept']} |\n"
    
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    
    start_marker = "<!-- LEETCODE-LIST:START -->"
    end_marker = "<!-- LEETCODE-LIST:END -->"
    
    start_idx = readme.find(start_marker)
    end_idx = readme.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_readme = (
            readme[:start_idx + len(start_marker)] + "\n\n" +
            table + "\n" +
            readme[end_idx:]
        )
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_readme)
        print("README updated successfully.")
    else:
        print("Could not find marker tags in README.md")

if __name__ == "__main__":
    update_readme()
