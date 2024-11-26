# Senior Design Report - CleverCollab

## Table of Contents
1. [Team Names and Project Abstract](#team-names-and-project-abstract)
2. [Project Description](#project-description)
3. [User Stories and Design Diagrams](#user-stories-and-design-diagrams)
    - [User Stories](#user-stories)
    - [Design Diagrams](#design-diagrams)
      - [Design D0](#design-D0)
      - [Design D1](#design-D1)
      - [Design D2](#design-D2)
      - [Design D3](#design-D3)
      - [Description of the Diagrams](#description-of-the-diagrams)
4. [Project Tasks and Timeline](#project-tasks-and-timeline)
    - [Task List](#task-list)
    - [Timeline](#timeline)
    - [Effort Matrix](#effort-matrix)
5. [ABET Concerns Essay](#abet-concerns-essay)
6. [PPT Slideshow (includes ABET Concerns)](#ppt-slideshow-includes-abet-concerns)
7. [Self-Assessment Essays](#self-assessment-essays)
8. [Professional Biographies](#professional-biographies)
9. [Budget](#budget)
10. [Appendix](#appendix)

## Team names and project abstract
- Team members: Arya Narke, Varad Parte, Daksh Prajapati, Jalin Solankee
- Advisor: Dr. Raj Bhatnagar
- [Link to our Biographies](Professional_Bios)
- **Project Abstract**: 
Our project, Autonomous AI Agents for Project Management Automation, harnesses AI to transform project management with automated task allocation and task prioritization, predictive analytics, and natural language processing. Leveraging Jira API calls via Python, the backend efficiently retrieves and processes project data, which is stored in MongoDB databases. Machine learning models analyze this data to predict delays and resource needs. An intuitive frontend in React.js provides real-time insights and interactive dashboards, while a GPT-powered chatbot interface answers queries from team members and project managers. This system empowers proactive project oversight, optimizing task allocation, progress tracking, and decision-making for enhanced productivity and efficiency.​

## Project Description
### Overview
This project aims to revolutionize project management using autonomous AI agents to automate task allocation, progress tracking, predictive analytics, and natural language interactions. These agents enhance efficiency by distributing tasks based on team members' skills and availability, providing real-time updates on project status, and offering predictive insights to foresee potential delays or issues. Our solution integrates AI into the project management workflow, creating a more streamlined and proactive approach to managing teams and tasks.

### Key Features
- **Automated Task Allocation**: AI agents assign tasks based on team members' expertise and availability, ensuring optimal resource management.
- **Real-Time Progress Tracking**: Live updates on task progress, team performance, and project status.
- **Predictive Analytics**: Machine learning models analyze current project data to predict potential delays or bottlenecks and suggest strategic adjustments.
- **NLP Chatbot for Queries**: A chatbot powered by GPT models allows managers and team members to ask questions about the project’s status, tasks, and potential risks. The chatbot can answer both simple and complex queries in natural language.
  
  #### Sample Queries:
  - For **Managers**:
    - "What are the key tasks that need to be done soon?"
    - "Who is working on task X?"
    - "Which tasks are likely to miss their deadlines based on current progress?"
    - "Are there any duplicated tasks?"
  - For **Team Members**:
    - "Which task should I prioritize?"
    - "Considering the time needed for each task, can I meet all my deadlines?"

### Technical Stack

#### Backend
- **Python**: Core programming language for building AI agents, backend logic, and chatbot functionality.
- **Machine Learning Models**: Used for predictive analytics, enabling the AI to forecast project outcomes and task delays.
- **OpenAI API**: Integrates GPT models to enable natural language processing for the chatbot, allowing users to ask questions and receive insights about the project.
- **Databases**: To store project data, tasks, and team information. Possible database solutions include:
  - **PostgreSQL**: For relational data storage.
  - **MongoDB**: For flexible and scalable document storage.
  
#### Frontend
- **React.js**: Provides a dynamic and responsive UI for project managers and team members. The frontend will offer features like:
  - Task overview dashboard.
  - Real-time project updates and insights.
  - Predictive analytics visualization.
  - Chatbot Interface: A clean, interactive interface for asking questions to the NLP-based AI chatbot.
- **Tailwind CSS**: Used for fast and responsive styling.
  
#### API Integration
- **RESTful APIs**: For communication between the frontend and backend. Ensures that project data, task updates, and predictive analytics are available in real-time.

## User Stories and Design Diagrams
### User Stories
#### User Profile - Project Manager
1. As a project manager, I want to view upcoming key tasks so that I can ensure the team meets deadlines.

2. As a project manager, I want to see which tasks are at risk of missing deadlines so that I can make adjustments proactively.

3. As a project manager, I want to assign tasks based on team members’ skills and availability so that I can optimize productivity.
   
#### User Profile - Team Member
1. As a team member, I want to view my highest-priority tasks based on importance and deadlines so that I can work on the most critical assignments first.

2. As a team member, I want to know if I can meet my deadlines based on my current progress so that I can adjust my workload if needed.

3. As a team member, I want to identify other team members with required skills for a specific task, and with some availability to help me navigate my task.

### Design Diagrams 
#### Design D0 (High-Level Overview) 

This diagram provides a basic overview of how the system operates at a high level:
- **Inputs:** 
   - Project/Task Data: Information related to tasks, deadlines, team member availability, etc.
   - User Queries: Requests from users (managers or team members) asking for project insights.
- **AI Agent:** Acts as the core of the system, processing these inputs.
- **Output:** 
   - The AI Agent responds to user queries with information such as task assignments, project status, or predictive insights on potential delays.

![alt text](Diagram_D0.png)

#### Design D1 (Subsystem Breakdown) 

This diagram expands upon the AI agent and divides it into core subsystems that handle specific operations:
- **Inputs:** 
   - Project/Task Data from project management boards and user queries.
- **Subsystems:**
   - **Trained Model:** Processes project data for task allocation, predictions, etc.
   - **Chatbot Interface:** Handles user interactions and translates queries.
   - **Predictive Analysis/ML Model:** Provides predictions and insights based on project data and queries asked.
- **Output:** 
   - Responses are generated for users, including status updates, task assignments, and potential risk forecasts.

![alt text](Diagram_D1.png)

#### Design D2 (Detailed Functional Breakdown) 

This is a more detailed version of Design D1, breaking down each component further:
- **Inputs:** 
   - Project/Task Data and user queries as before.
- **Subsystems:** 
   - **Predictive Analysis ML Model:** Handles data preprocessing, model training, and prediction generation.
   - **Trained Model:** Focuses on skill matching, task prioritization, predictions. Interacts with the chatbot interface. 
   - **Chatbot Interface:** Broken down into subcomponents such as query parsing, context matching, and response generation.
- **Output:**
   - The AI provides real-time responses to users, delivering status updates, task assignments based on skills, and predictive insights about potential risks.
   - Responses help managers and team members optimize task management and avoid delays.

![alt text](Diagram_D2.png)

Each diagram progressively elaborates on the system, with D2 providing a comprehensive look at the interaction between subsystems for task allocation, predictive analysis, and natural language processing.

## Project Tasks and Timeline
### Task List
#### Project: Autonomous AI Agents for Project Management Automation

##### **PHASE 1**
1. Investigate optimal machine learning models for predictive task analysis and forecasting delays.
Assigned to: **Jalin Solankee**

2. Research potential data preprocessing techniques for handling project/task data from the integrated project management boards (e.g., Trello, Jira).
Assigned to: **Varad Parte**

3. Design the chatbot interface for receiving and responding to user queries based on project data and predictive analytics.
Assigned to: **Daksh Prajapati**

4. Develop a data pipeline to integrate project/task data from project management boards into the AI agent system.
Assigned to: **Arya Narke**

##### **PHASE 2**
5. Implement the machine learning model for task prioritization based on deadlines, dependencies, and team members' availability.
Assigned to: **Arya Narke**

6. Test the task allocation module to ensure tasks are assigned based on skill matching and availability.
Assigned to: **Varad Parte**

7. Develop the OpenAI-based response generation module for natural language interaction with users.
Assigned to: **Daksh Prajapati**

8. Specify the data preprocessing techniques needed for predictive analysis to anticipate project delays.
Assigned to: **Jalin Solankee**

##### **PHASE 3**
9. Validate the trained AI model by running sample project data and ensuring accurate predictions of potential issues.
Assigned to: **Arya Narke**

10. Design a task allocation algorithm to match tasks with team members based on skill set and workload.
Assigned to: **Varad Parte**

11. Document the integration process of the chatbot interface with task prioritization and predictive analytics results.
Assigned to: **Daksh Prajapati**

12. Develop query parsing mechanisms for interpreting user prompts and directing queries to the appropriate modules (e.g., task allocation, predictive generation).
Assigned to: **Jalin Solankee**

##### **PHASE 4**
13. Test the overall system's ability to generate real-time project status updates and identify at-risk tasks.
Assigned to: **Arya Narke**

14. Refine the chatbot interface to improve user experience based on feedback from internal testing.
Assigned to: **Daksh Prajapati**

15. Implement context-matching logic for handling complex queries related to task dependencies and project status.
Assigned to: **Jalin Solankee**

16. Develop the predictive analysis module using historical project data to forecast potential delays and project risks.
Assigned to: **Varad Parte**

##### **PHASE 5**
17. Test the skill-based task allocation feature with sample user data to ensure proper matching and prioritization.
Assigned to: **Arya Narke**

18. Validate the system's accuracy in predicting project outcomes and flagging potential bottlenecks.
Assigned to: **Varad Parte**

19. Design the user interface for displaying task prioritization and progress tracking information to project managers and team members.
Assigned to: **Daksh Prajapati**

20. Document all API integrations, AI developments, etc. between the AI agent, project boards, and the OpenAI API.
Assigned to: **Jalin Solankee**

### Timeline
**Milestone, Timeline, and effort matrix**

### Effort Matrix

## ABET Concerns Essay
### Constraint Essay

In our project, several constraints impact the design and the possible solutions we can implement.

#### Economic Constraints

##### Budget and Resources
Since we are integrating technologies like machine learning models and GPT APIs, there are costs associated with API usage, cloud storage, and hosting. Our reliance on freeware or shareware might limit the scope of our project, especially when it comes to features like real-time updates or handling large datasets. If we are constrained by a limited budget, this could affect the quality and performance of the solution.

##### Funding
We are working with self-funded resources, which limits our access to premium services such as high-tier APIs or cloud infrastructure. This might impact our system's ability to handle large volumes of data efficiently.

#### Professional Constraints

##### Specialized Expertise
Our project requires expertise in advanced technologies like AI, machine learning, and natural language processing. While developing the project, we are gaining valuable knowledge and experience in these areas, which contributes to our professional growth. However, gaps in our expertise might slow down progress or present challenges in implementing certain features.

#### Ethical Constraints

##### Bias in AI Models
Since we are using AI and machine learning models, it is important for us to ensure that our algorithms do not introduce bias into task allocation or project predictions. If our models assign tasks unfairly, it could lead to an unbalanced workload or unequal task distribution among team members, which raises ethical concerns.

##### Transparency and Fairness
We need to ensure that our AI agents are transparent in their decision-making processes. Users should clearly understand how tasks are assigned and on what basis. If the decision-making process is opaque, it could lead to mistrust in the system, which could affect user adoption.

#### Security Constraints

##### Data Privacy
Our project involves handling sensitive project management data, which means we must prioritize data security and privacy. We are responsible for ensuring that all user data is securely stored and protected from unauthorized access. Additionally, we need to ensure that any external APIs or services we use comply with security standards to avoid exposing sensitive information.

## PPT Slideshow (includes ABET Concerns)
**Video Presentation**: [Senior Design-20241027_172629-Meeting Recording.mp4](https://mailuc-my.sharepoint.com/personal/narkean_mail_uc_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fnarkean%5Fmail%5Fuc%5Fedu%2FDocuments%2FRecordings%2FSenior%20Design%2D20241027%5F172629%2DMeeting%20Recording%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eb3944bf8%2Daa5e%2D4673%2Db69b%2D9c1cfb42d422)

**Slide Deck**: [Slide Deck](https://mailuc-my.sharepoint.com/:p:/g/personal/prajapdh_mail_uc_edu/EauuGWDS66NBnsKtTf9hCxUBd1RkEIg86fepzMMc6UQg2g?e=3xPsEd) 

## Self-Assessment Essay
1. [**Arya Narke**](https://github.com/solankeejalin24/CleverCollab/blob/main/Essays/Individual_Capstone_Assignment_narkean.pdf)
2. [**Varad Parte**](https://github.com/solankeejalin24/CleverCollab/blob/main/Essays/Individual%20Capstone%20Assignment_partevr.pdf)
3. [**Daksh Prajapati**]()
4. [**Jalin Solankee**](https://github.com/solankeejalin24/CleverCollab/blob/main/Essays/Individual_Capstone_Assignment_solankjp.pdf)
