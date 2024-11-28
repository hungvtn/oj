from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess
import json
from time import time, sleep

app = Flask(__name__)

# Danh sách trạng thái chấm bài
submission_status = []

# Hàm biên dịch mã nguồn
def compiler(name_problem):
    process = subprocess.run(['g++', f'{name_problem}.cpp', '-o', f't_{name_problem}'], 
                              capture_output=True, text=True)
    return process.stderr == ''

# Hàm chấm bài
def submit(path_folder, name_problem, time_limit):
    input_file = f"./test/{name_problem}/{path_folder}/{name_problem}.inp"
    output_file = f"{name_problem}.out"
    answer_file = f"./test/{name_problem}/{path_folder}/{name_problem}.out"

    # Ghi file input
    with open(input_file) as f:
        Input = f.readlines()
    with open(f"{name_problem}.inp", "w") as g:
        g.writelines(Input)

    # Chạy chương trình
    process = subprocess.Popen([f'./t_{name_problem}'], stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE, text=True)
    start_time = time()

    while True:
        if process.poll() is not None:
            break
        if time() - start_time > time_limit * 2:
            process.terminate()
            return 'TLE'
        sleep(0.1)

    # Đọc file output
    with open(output_file) as f:
        output = f.read().strip()
    with open(answer_file) as f:
        answer = f.read().strip()

    return 'AC' if output == answer else 'WA'

# Trang danh sách bài toán
@app.route("/")
def index():
    # Đọc danh sách bài toán từ file JSON
    with open('problems.json', 'r') as file:
        problems = json.load(file)
    return render_template("index.html", problems=problems)

# Trang bài toán cụ thể
@app.route("/<problem_name>", methods=['GET', 'POST'])
def problem(problem_name):
    if request.method == 'POST':
        # Lấy code từ form
        code = request.form.get('code')
        if not code.strip():
            submission_status.append({
                "problem": problem_name,
                "status": "No Code Provided",
                "score": "0.00",
                "time": "N/A"
            })
            return redirect(url_for('status'))

        # Lưu code vào file
        with open(f"{problem_name}.cpp", "w") as file:
            file.write(code)

        # Biên dịch
        if not compiler(problem_name):
            submission_status.append({
                "problem": problem_name,
                "status": "Compilation Error",
                "score": "0.00",
                "time": "N/A"
            })
            return redirect(url_for('status'))

        # Đọc thông tin chấm bài
        with open(f'test/{problem_name}/info.JSON') as file:
            info = json.load(file)
        point = info['point']
        time_limit = info['timeLimit']

        # Chấm bài
        scores = 0
        test_cases = [entry.name for entry in os.scandir(f'./test/{problem_name}') if 'test' in entry.name.lower()]
        num_tests = len(test_cases)

        for test in test_cases:
            result = submit(test, problem_name, time_limit)
            if result == 'AC':
                scores += 1

        final_score = float("{:.2f}".format(scores / num_tests * point))
        submission_status.append({
            "problem": problem_name,
            "status": "Accepted" if scores > 0 else "No AC",
            "score": f"{final_score} / {point}",
            "time": f"{len(test_cases) * time_limit:.2f}s"
        })
        return redirect(url_for('status'))

    return render_template("problem.html", problem_name=problem_name)

# Trang trạng thái
@app.route("/status")
def status():
    return render_template("status.html", submissions=submission_status)

if __name__ == "__main__":
    app.run(debug=True)
