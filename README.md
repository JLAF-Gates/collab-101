# Collab 101

A simple Python-based collaboration/demo project for working with tabular and geospatial data using **Pandas, GeoPandas, and NumPy**.

## 📋 Requirements

* Python 3.12+
* Git
* Windows / macOS / Linux
* GitHub account

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/JLAF-Gates/collab-101.git
cd collab-101
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\activate
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

Once activated, you should see:

```text
(.venv)
```

at the beginning of your terminal prompt.

### 4. Install dependencies

```bash
pip install pandas geopandas numpy
```

The project currently uses:

* **Pandas** – tabular data manipulation and analysis
* **GeoPandas** – geospatial data processing
* **NumPy** – numerical and array-based operations

## 📁 Project Structure

```text
collab-101/
│
├── .venv/              # Local Python virtual environment
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
│
└── ...                 # Project files and scripts
```

> The `.venv/` directory should not be committed to Git.

## 📦 Generate `requirements.txt`

After installing the dependencies:

```bash
pip freeze > requirements.txt
```

Other users can install the project's dependencies with:

```bash
pip install -r requirements.txt
```

## 🔄 Basic Git Workflow

Before starting work, make sure your local repository is up to date:

```bash
git pull
```

Check the current status:

```bash
git status
```

After creating or modifying files, stage your changes:

```bash
git add .
```

Commit your changes:

```bash
git commit -m "Describe your changes"
```

Push your changes:

```bash
git push
```

## 🌿 Collaboration Workflow

For collaborative development, **do not work directly on `main`**.

Instead, create a feature branch.

### 1. Update your local `main`

```bash
git checkout main
git pull origin main
```

### 2. Create a feature branch

Use a descriptive branch name:

```bash
git checkout -b feature/my-feature
```

For example:

```bash
git checkout -b feature/random-function
```

### 3. Make your changes

Create or modify your Python files.

Check what changed:

```bash
git status
```

Review the changes:

```bash
git diff
```

### 4. Stage the changes

```bash
git add .
```

Or stage a specific file:

```bash
git add random_demo.py
```

### 5. Commit the changes

```bash
git commit -m "Add random number function"
```

### 6. Push the branch to GitHub

For the first push:

```bash
git push -u origin feature/random-function
```

After the upstream branch has been established, you can simply use:

```bash
git push
```

## 🔀 Pull Request Workflow

After pushing your feature branch, create a **Pull Request (PR)** on GitHub.

The typical workflow is:

```text
main
  │
  ├── feature/random-function
  │        │
  │        ├── Make changes
  │        ├── git add .
  │        ├── git commit
  │        └── git push
  │
  └── Pull Request
           │
           └── Review
                │
                └── Merge → main
```

### Create a Pull Request

After pushing your branch:

```bash
git push -u origin feature/random-function
```

Go to the repository on GitHub.

1. Open the **Pull requests** tab.
2. Click **New pull request**.
3. Select:

   * **Base:** `main`
   * **Compare:** `feature/random-function`
4. Review the changes.
5. Add a title and description.
6. Create the Pull Request.
7. Request a review from your collaborator.
8. Address any requested changes.
9. Merge the Pull Request once it has been approved.

> The Pull Request is where collaborators can review, discuss, and approve changes before they are merged into `main`.

## 🔀 Merge a Pull Request

The preferred approach for this demo is to merge the Pull Request through GitHub.

Once the Pull Request is approved:

```text
feature/random-function
          │
          │ Pull Request
          ▼
        Review
          │
          ▼
       Approved
          │
          ▼
      Merge to main
```

After the Pull Request is merged, the changes become part of the `main` branch.

## 🔄 Update Your Local `main` After a Merge

After a Pull Request has been merged into `main`, switch back to your local `main` branch:

```bash
git checkout main
```

Pull the latest changes:

```bash
git pull origin main
```

You can then create another feature branch:

```bash
git checkout -b feature/another-feature
```

## 🧹 Delete a Completed Feature Branch

After the Pull Request has been merged, you can delete the local feature branch:

```bash
git branch -d feature/random-function
```

You can also delete the remote branch:

```bash
git push origin --delete feature/random-function
```

> GitHub may also provide a **Delete branch** button after the Pull Request is merged.

## 🔍 Useful Git Commands

### Check current branch

```bash
git branch
```

### Switch branches

```bash
git checkout main
```

or:

```bash
git switch main
```

### Create and switch to a new branch

```bash
git checkout -b feature/my-feature
```

or:

```bash
git switch -c feature/my-feature
```

### View all branches

```bash
git branch -a
```

### Check repository status

```bash
git status
```

### View commit history

```bash
git log --oneline
```

### View changes

```bash
git diff
```

### Pull the latest changes

```bash
git pull origin main
```

### Push changes

```bash
git push
```

### Check remote repository

```bash
git remote -v
```

## 🧪 Verify the Environment

You can verify that the required packages are installed by running:

```bash
python -c "import pandas, geopandas, numpy; print('Environment ready!')"
```

If successful, the terminal should display:

```text
Environment ready!
```

## 📌 Recommended Collaboration Rules

1. **Do not commit directly to `main`.**
2. Create a feature branch for your work.
3. Use descriptive branch names.
4. Make small and meaningful commits.
5. Pull the latest `main` before starting new work.
6. Push your feature branch to GitHub.
7. Create a Pull Request.
8. Have another collaborator review the changes.
9. Merge the Pull Request into `main`.
10. Pull the updated `main` branch before starting your next task.

### Recommended Branch Naming

```text
feature/<feature-name>
fix/<issue-name>
docs/<documentation-name>
refactor/<change-name>
```

Examples:

```text
feature/random-function
feature/geospatial-analysis
fix/data-loading-error
docs/update-readme
refactor/data-processing
```

## 📝 Example Collaboration Scenario

Suppose a collaborator wants to add a random number function.

### Start from the latest `main`

```bash
git checkout main
git pull origin main
```

### Create a feature branch

```bash
git checkout -b feature/random-function
```

### Add the Python code

```text
random_demo.py
```

### Commit the changes

```bash
git add random_demo.py
git commit -m "Add random number function"
```

### Push the branch

```bash
git push -u origin feature/random-function
```

### Create a Pull Request

On GitHub:

```text
feature/random-function
          ↓
     Pull Request
          ↓
        Review
          ↓
       Approved
          ↓
    Merge into main
```

### Get the merged changes

```bash
git checkout main
git pull origin main
```

The `random_demo.py` file is now available in the local `main` branch.

## 📄 License

This project is intended for demonstration and collaborative development purposes.
