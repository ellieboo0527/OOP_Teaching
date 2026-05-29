# OOP_Teaching

### Fork on GitHub

1. Open the teacher repository:

   https://github.com/BH4DKC/OOP_Teaching.git

2. Click **Fork** in the top-right corner.
3. Create the fork under your own GitHub account.
4. After forking, your repository link should look like:

   https://github.com/YOUR_USERNAME/OOP_Teaching.git


## Clone the Class Repository in PyCharm

1. Open **PyCharm**
2. On the welcome screen, click **Get from VCS**
3. In the URL box, paste:

   https://github.com/YOUR_USERNAME/OOP_Teaching.git

4. Choose a folder on your computer where you want to save the project
5. Click **Clone**
6. Wait for PyCharm to download and open the project

## Open and Run the Project

After cloning:

1. Look at the left project panel
2. Find the UNO project folder
3. Open `main.py`
4. Right-click `main.py`
5. Click **Run 'main'**

If PyCharm asks for a Python interpreter:

1. Choose **Add Interpreter**
2. Choose **Python 3**
3. Use the default virtual environment option
4. Click **OK**

## Pull Updates from GitHub

If the teacher updates the GitHub repository, you can download the newest version in PyCharm.

In PyCharm:

1. Go to the top menu
2. Click **Git**
3. Click **Pull**
4. Make sure the branch is `main`
5. Click **Pull**

This updates your local project with the newest files from GitHub.

## Push Your Changes

After committing:

1. Go to **Git**
2. Click **Push**
3. Click **Push** again

Push means: “Upload my saved changes to GitHub.”

## How to Get Teacher Updates After Forking

After you fork the teacher repository, your project has two versions:

- Teacher repository: `https://github.com/BH4DKC/OOP_Teaching.git`
- Your fork: `https://github.com/YOUR_USERNAME/OOP_Teaching.git`

If the teacher updates the starter code, you need to update your fork first.

### Step 1: Sync Your Fork on GitHub

1. Open your fork on GitHub.
2. Click **Sync fork**.
3. Click **Update branch**.

This copies the teacher's newest code into your fork.

### Step 2: Pull Updates in PyCharm

After syncing your fork:

1. Open the project in PyCharm.
2. Click **Git** at the top.
3. Click **Pull**.
4. Make sure the branch is `main`.
5. Click **Pull**.

This downloads the newest code from your fork into PyCharm.

### Important

Do not clone the teacher repository directly if you want to push your own work.

Use this workflow:

1. Fork the teacher repository.
2. Clone your own fork.
3. Make changes in PyCharm.
4. Commit your changes.
5. Push your changes to your fork.
6. If the teacher updates the starter code, sync your fork on GitHub and then pull in PyCharm.