# 🚀 Python CI/CD Project (GitHub Actions)

---

# 🧠 Project Overview

This project demonstrates a **CI/CD pipeline for a Python application** using GitHub Actions.

The application performs **sales data analysis** using NumPy and validates functionality using automated tests.

---

# 📦 Project Structure

```
projects/python-cicd/
│
├── app.py              # Main application
├── utils.py            # Business logic
├── test_app.py         # Unit tests
├── requirements.txt    # Dependencies
```

---

# ⚙️ What This Project Does

* Processes sales data
* Calculates:

  * total sales
  * average
  * min / max
  * standard deviation
* Runs automated tests
* Executes CI pipeline on every push

---

# 🔄 CI/CD Workflow

```text
Code Push → GitHub Actions → Install Dependencies → Run Tests → Run App
```

---

# 🛠 Pipeline Explanation

Pipeline file: `.github/workflows/python.yml`

Steps:

1. Checkout code
2. Setup Python environment
3. Install dependencies (`numpy`, `pytest`)
4. Run tests
5. Execute application

---

# ▶️ How to Run Locally

```bash
cd projects/python-cicd
pip install -r requirements.txt
python app.py
```

---

# 🧪 Run Tests

```bash
pytest
```

---

# 🎯 Output Example

```
📊 Sales Analysis Report
------------------------------
total_sales: 2700
average_sales: 385.7
...
```

---

# 🚀 What This Demonstrates

* Python scripting
* CI/CD pipeline setup
* Automated testing
* Dependency management
* DevOps workflow understanding

---

# 🎯 Interview Talking Point

This project demonstrates how a Python application can be integrated with CI/CD pipelines to automate testing and execution on every code change.

---

