# **Please do not start before reading Master_Readme.md. and instructions provided below:**


# **Project: Sticky Notes Whiteboard with Dependencies**

---

## **Objective**

This project evaluates your **fullstack development** and **DevOps expertise**(Focus on DevOps). Your primary focus will be on setting up a **robust, secure, and automated DevOps pipeline** for deployment while building a functional application.

You will:
1. Build a **sticky notes whiteboard application** to demonstrate your frontend and backend development skills (Nothing too serious).
2. Set up and maintain a **CI/CD pipeline** to automate testing, building, and deployment processes.
3. Ensure secure handling of credentials, containerization, SSL configuration, and monitoring of the deployed application.

---

## **Project Overview**

### **Sticky Notes Whiteboard Application**
- Users can:
  1. Add, edit, and delete sticky notes on a canvas (Canvas of React Flow iteself).
  2. Connect notes to define dependencies using **React Flow**.
  3. Save and load the whiteboard as a reusable flow.

---

## **Primary DevOps Requirements**

### **1. CI/CD Pipeline**
Set up an automated pipeline using **GitHub Actions** that includes:
- **Pre-Commit and Pre-Push Hooks**:
  - Use **Husky** to implement hooks for:
    - Running linting tools (e.g., ESLint, Prettier).
    - Running basic unit tests.
    - Preventing commits or pushes if checks fail.
    - Setup custom actions runners to your ubuntu servers as non-root user
- **Pipeline Steps**:
  - Trigger the pipeline on every push and pull request to the `main` branch.
  - Steps:
    1. **Run Tests**:
        - Execute both frontend and backend unit tests.
    2. **Build**:
        - Build the application.
    3. **Security Checks**:
        - Include a step for scanning vulnerabilities (e.g., **npm audit** or **Trivy**).
    4. **Deploy**:
        - Deploy the application to the server (To know what servers/vps to use, refer to the master file).

### **2. Containerization**
- Use **Docker** to containerize the application:
  - Separate containers for:
    - **Frontend**: Serve the React application.
    - **Backend**: Host the APIs.
    - **Database**: Use SQLite or PostgreSQL in a container or use free postgres trial available online if available.
- Use **Docker Compose** to orchestrate the containers for local development and production.
- Apply best practices for container security:
  - Use lightweight images (e.g., `node:alpine`).
  - Avoid running containers as the root user.
  - Limit container privileges.

### **3. Credentials Management**
- Use **GitHub Secrets** to securely store:
  - Database credentials.
  - JWT secret keys.
  - Any other sensitive environment variables.
- **Local Setup**:
  - Use a `.env` file for local development but ensure it’s added to `.gitignore`.

### **4. Secure Deployment**
- Deploy the application to a **Ubuntu server** (e.g., AWS EC2, DigitalOcean or the one mentioned in the master read me).
- Use **Nginx** as a reverse proxy to serve the application.
- Enforce HTTPS:
  - Configure **Let’s Encrypt** for free SSL/TLS certificates.
  - Redirect all HTTP traffic to HTTPS.

### **5. Branch Protection**
- Protect the `main` branch:
  - Require CI checks to pass before merging pull requests.
  - Enable code review for all pull requests.

### **6. Monitoring and Logging**
- Implement basic logging for:
  - API requests (e.g., request time, status codes).
  - Errors for debugging.githu
- Monitoring (Optional):
  - Integrate **Prometheus** and **Grafana** or use cloud-native monitoring tools.

---

## **Development Requirements**

### **Frontend (Sticky Notes Whiteboard)**
1. **Whiteboard Interface**:
   - Use **React Flow** to:
     - Add sticky notes with customizable content.
     - Connect notes to define dependencies visually.
   - Enable drag-and-drop positioning for notes.

2. **Save and Load**:
   - Save the whiteboard (notes and connections) to the backend as a flow.
   - Fetch and render saved flows on the canvas.

3. **Styling**:
   - Use **Tailwind CSS** or any modern UI framework to create a clean and responsive(not mandatory) design.

### **Backend**
1. **API Endpoints**:
   - `POST /flows`: Save a new whiteboard flow.
   - `GET /flows`: Fetch all saved flows.
   - `GET /flows/:id`: Fetch a specific flow by ID.
   - `DELETE /flows/:id`: Delete a specific flow.

2. **Authentication**:
   - Implement token-based authentication using **JWT**.
   - Protect the endpoints to ensure only authenticated users can manage flows.

3. **Database**:
   - Use **SQLite** or **PostgreSQL** to store:
     - Flows: A JSON representation of notes and connections.
     - User authentication data.

---

## **Stretch Goals** (optional)
1. **Real-Time Collaboration**:
   - Use WebSockets to enable real-time updates for multiple users on the same whiteboard.
2. **Role-Based Access Control**:
   - Allow admins to manage all flows while users can manage only their own.
3. **Error Reporting**:
   - Integrate tools like **Sentry** for error tracking and reporting.

---

## **Deliverables**

1. **GitHub Repository**:
   - Include the entire codebase with separate folders for frontend and backend.
   - Add a `readme.md` file with:
     - CI/CD pipeline details.
     - Steps to set up and deploy the application locally and in production.
     - Explanation of any challenges and solutions implemented.

2. **Live Demo**:
   - Provide a public URL for the deployed application with HTTPS enabled.

3. **CI/CD Pipeline**:
   - Ensure the pipeline automates testing, building, and deployment.

4. **Documentation**:
   - Include detailed instructions in the `README.md` for:
     - Local setup.
     - API usage and endpoints.
     - DevOps practices followed.

5. **Time Log**:
    - Refer to master readme for timelog details

---

## **Evaluation Criteria**

### **1. Fullstack Development** (Less priority)
- Is the sticky notes whiteboard functional and intuitive?
- Are the APIs robust, secure, and well-documented?

### **2. DevOps Practices** (High priority)
- Is the CI/CD pipeline automated and reliable?
- Are containers well-organized and secure?
- Are SSL and credential management implemented effectively?
- Is the deployment process clearly documented and reproducible?

### **3. Code Quality**
- Is the code modular, maintainable, and readable?
- Are pre-commit hooks implemented effectively?

### **4. Creativity**
- Does the candidate go beyond basic requirements with enhancements?
- Is the UI polished and user-friendly?

---



## **Good Luck!**

