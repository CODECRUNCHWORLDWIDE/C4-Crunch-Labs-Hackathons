
# Install and Set Up Free Student License for Spring Boot, IntelliJ IDEA, and Postman

## 1. Install IntelliJ IDEA (with Free Student License)

### Step 1: Get a Free Student License
1. Go to the **JetBrains Student License** page: 👉 [https://www.jetbrains.com/community/education/#students](https://www.jetbrains.com/community/education/#students)
2. Click **Apply Now** and sign up with your university email (`.edu` or equivalent)
3. Verify your student status by either:
   - Using an official university email
   - Uploading a student ID or other proof of enrollment
4. Once verified, JetBrains will provide you with a free license for **IntelliJ IDEA Ultimate**

### Step 2: Install IntelliJ IDEA
1. Download IntelliJ IDEA from: 👉 [https://www.jetbrains.com/idea/download](https://www.jetbrains.com/idea/download)
2. Install **IntelliJ IDEA Ultimate** (or Community Edition if needed)
3. Open IntelliJ and log in with your **JetBrains Student License**

---

## 2. Install Spring Boot

### Step 1: Install Java Development Kit (JDK)
1. Download the latest **OpenJDK (Java 17 or 21 LTS)**: 👉 [https://adoptium.net/](https://adoptium.net/)
2. Install the JDK and set up environment variables (if needed)

### Step 2: Install Spring Boot CLI (Optional)
1. Download the Spring Boot CLI: 👉 [Spring Boot CLI Installation](https://docs.spring.io/spring-boot/docs/current/reference/html/getting-started.html#getting-started-installing-the-cli)
2. Use SDKMAN! (Recommended for installation):
sh
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install springboot

Verify the installation:
sh
spring --version

### Step 3: Set Up a Spring Boot Project in IntelliJ
1. Open IntelliJ IDEA and click New Project
2. Select Spring Boot from the list of frameworks
3. Choose dependencies (e.g., Spring Web, Spring Data JPA, etc.)
4. Click Finish to generate your project

## 3. Install Postman (API Testing)
1. Download Postman from: 👉 [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
2. Install and open Postman
3. Sign up for a free Postman Student Account (optional for more features): 👉 [https://www.postman.com/postman-student-program/](https://www.postman.com/postman-student-program/)

## Final Setup & Testing

✔ Verify Java & Spring Boot Installation:
sh
java -version
spring --version

✔ Run a Sample Spring Boot App:
sh
mvn spring-boot:run

✔ Test API with Postman:
1. Open Postman
2. Create a new request (GET, POST, etc.)
3. Enter http://localhost:8080/your-endpoint and test the API


