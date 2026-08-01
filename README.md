# Pre-requisite Checks

## 1. Virtual Environment

* Ensure the **virtual environment (`.venv`) is not committed** to the Git repository.
* Add `.venv/` to the `.gitignore` file to prevent accidental commits.

## 2. Package Types

Before adding or importing a package, identify its type:

### Built-in Packages

* These are included with the Python installation.
* No separate installation is required.
* **Examples:** `json`, `os`, `logging`, `datetime`

### Third-party Packages

* These are provided by external organizations or open-source communities.
* They must be installed explicitly using `pip`.
* **Example:**

  ```bash
  pip install requests
  ```

### Custom Packages

* These are user-defined packages or modules created specifically for the project.
* Organize them properly within the project's package structure.

## 3. Dependency Management

* Maintain all third-party dependencies in a **`requirements.txt`** file.
* Example:

  ```text
  requests==2.34.2
  flask==3.0.3
  ```
* Install all dependencies using:

  ```bash
  pip install -r requirements.txt
  ```

## 4. Pipfile (Alternative to requirements.txt)

* A **`Pipfile`** can be used as an alternative to `requirements.txt`.
* It provides better dependency organization by separating packages into different categories.

### Example

**Development Packages**

* p1
* p2
* p3

**Testing Packages**

* p4
* p5

## 5. Package Usage

* Ensure that **application source code** uses only the required runtime dependencies (e.g., p1, p2, p3).
* Keep **testing dependencies** (e.g., p4, p5) separate from production dependencies.
* Avoid including unnecessary packages in the project to keep the application lightweight and maintainable.
