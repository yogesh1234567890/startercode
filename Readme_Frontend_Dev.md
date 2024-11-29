# **Please do not start before reading Master_Readme.md. and instructions provided below:**


# **Frontend Developer Assessment**

Welcome to the assessment for the Frontend Developer role! This project is designed to test your **technical skills**, **research ability**, and **UI/UX implementation expertise**. You will work on a single project that evaluates both your ability to use new libraries effectively and your skill in creating pixel-perfect, responsive user interfaces.

---

## **Objective**

The goal of this assessment is to:
1. **Test your ability to research and implement new libraries**, such as **React Flow** and **React DnD**, for building complex, functional components.
2. **Evaluate your UI/UX development skills** by recreating a provided Figma design with responsiveness and interactivity.
3. Understand your approach to **state management**, **context handling**, and **integrating mock data**.

---

## **Project Overview**

You will build a **Task and Relationship Management Tool** that has two key components:
1. **Database Diagramming Tool**:
   - Allows users to create, connect, and manage database tables visually using **React Flow**.
   - Implements global state using **Context API**.
2. **Pixel-Perfect UI Clone**:
   - Recreate a responsive UI based on a provided Figma design to demonstrate your **attention to detail** and **UI development skills**.

---

## **Key Features**

### **1. Database Diagramming Tool**

#### **Core Features**
- **Diagram Builder**:
  - Users can:
    - Add new tables (nodes) to a canvas.
    - Connect tables with lines to define relationships.
    - Edit table properties such as column names, data types, and constraints.

- **State Management**:
  - Use **Context API** to manage:
    - The list of tables and their properties.
    - Connections between tables.
    - Diagram state (e.g., zoom, pan).

- **Export and Save**:
  - Save the diagram as a JSON file.
  - Reload saved diagrams to resume editing.

#### **Custom UI Requirements**
- Add a **Sidebar**:
  - Manage table properties (e.g., rename, add/remove columns).
  - List all connections and allow users to edit/delete them.
- Add a **Toolbar**:
  - Include options like "Undo," "Redo," and "Export."
  - A button to switch between the diagram and table list views.

#### **Libraries**:
- Use **React Flow** for diagramming functionality.
- Use **Tailwind CSS** or any UI kit (e.g., Chakra UI, ShadCN) for styling.

---

### **2. Pixel-Perfect UI Clone**

#### **Core Features**
- Recreate the provided [Figma Design](https://www.figma.com/proto/PpWBQopL2PrIsAhDvOxCRa/HonestValue-Main-File?page-id=24%3A90&node-id=102-1405&node-type=frame&viewport=2518%2C2147%2C0.19&t=iHGEZAiMrFpuxZbu-1&scaling=min-zoom&content-scaling=fixed) using **Next.js or Vite**.
(Figma Link: https://www.figma.com/proto/PpWBQopL2PrIsAhDvOxCRa/HonestValue-Main-File?page-id=24%3A90&node-id=102-1405&node-type=frame&viewport=2518%2C2147%2C0.19&t=iHGEZAiMrFpuxZbu-1&scaling=min-zoom&content-scaling=fixed)
- Ensure **responsiveness**:
  - The UI should work seamlessly on mobile, tablet, and desktop screens (since figma does not have smaller screen design, we want to see your creativity on how you think it should be. Nothing too serious, but we want you to be independent thinker.).

#### **Mock Data Integration**
- Use JSON files to populate dynamic sections of the UI.
- Example: Display property details, comparisons, or user data dynamically.

#### **Customizations**
- Add subtle animations and transitions (e.g., hover effects, loading states) to enhance the user experience where you deem fit.
- Ensure **accessibility**:
  - Use semantic HTML, ARIA roles, and keyboard navigation where necessary.

#### **Styling**
- Use **Tailwind CSS** for styling or integrate with Chakra UI/ShadCN as needed.
- Match colors, fonts, and layout details exactly as provided in the design.

---

## **Deliverables**

1. **GitHub Repository**:
   - Push your code to a GitHub repository with clear and meaningful commit messages.
   - Include a `README.md` file with:
     - Project setup instructions.
     - An explanation of the libraries/tools you used and why.
     - Challenges faced and how you overcame them.

2. **Live Demo**:
   - Deploy the project to a hosting platform (e.g., Vercel, Netlify). or let us know how to run it locally.
   - Provide a live link to the hosted app (if not possible, provide a video demo).

3. **Screenshots**:
   - Include screenshots of the completed UI in your repository.

4. **Time Tracking**:
   - Maintain a log of the time spent on each task (e.g., research, development, testing).
   - Include this log in your repository as mentioned in the Master Readme.

---

## **Evaluation Criteria**

1. **Research and Implementation**:
   - How effectively did you use **React Flow** and **React DnD** to implement the diagramming tool?
   - Is the Context API used appropriately for state management?

2. **UI Development**:
   - Is the recreated Figma design pixel-perfect and responsive?
   - Are animations and transitions smooth and polished?

3. **Code Quality**:
   - Is your code modular, readable, and well-documented?
   - Did you follow best practices for React and state management?

4. **Creativity and Initiative**:
   - Have you added enhancements or features beyond the requirements?
   - Does your app look polished and professional?

5. **Functionality**:
   - Are all features working as expected?
   - Is the app bug-free?

---

## **Bonus Points** (not mandatory)

- Add real-time collaboration features using WebSockets.
- Implement advanced accessibility features (e.g., screen reader support).
- Add animations or creative visual effects to enhance the overall experience.

---

## **Good Luck!**

We’re excited to see your creativity and skills shine in this project. Feel free to use any libraries, tools, or frameworks you think will make your project stand out.

If you have any questions, feel free to reach out. Good luck, and happy coding! 🚀
