# 📹 LLMs-to-Agentic-AI: Content Creation and Publishing Automation

## 🚀 Overview

Welcome to **LLMs-to-Agentic-AI**, our innovative solution designed during the "From LLMs to Agentic AI" hackathon organized at ESSEC by Kryptosphere and Utopia. This project automates the creation and publication of high-quality contents tailored for businesses to effortlessly enhance their presence across social media platforms.

---

## 🎯 Project Vision

Creating engaging social media content regularly can be resource-intensive for companies. Our solution leverages powerful Large Language Models (LLMs) and advanced Agentic AI techniques to simplify content production, making it efficient, scalable, and accessible to businesses of any size.

---

## 🛠️ Project Architecture

Our architecture is built for scalability, modularity, and ease of use, encompassing:

### Frontend
- **React & TypeScript** for a responsive and dynamic UI
- Simple interfaces for users to input prompts, pictures, customize styles.
- Use of TailAdmin 

### Backend
- **Node.js & Express**: Manages data flows, handles API calls, and interacts seamlessly with AI services
- Secure REST API endpoints

### AI Module
- Utilizes **OpenAI's GPT Models** to transform prompts into detailed
- Employs **Agentic AI** logic to select relevant visuals, audio, and narration, fully automating p generation production

### Cloud Storage and Hosting
- **AWS S3** for storing prompts, metadatas and medias securely
- **CloudFront** for efficient delivery of media assets globally
- Managed via EC2 for streamlined cloud operations

### Database
- **MySQL** for storing and managing metadata, scripts, and user-generated content

---

## 🔧 Technologies & Tools

- **Frontend**: React, TypeScript
- **Backend**: Node.js, Express
- **Database**: MySQL
- **AI & ML**: OpenAI GPT-4 API
- **Media Processing**: FFmpeg
- **Cloud Services**: AWS (EC2, S3, CloudFront)
- **DevOps**: GitHub, Git, CI/CD pipelines
- **Deployment**: Docker

---

## ⚙️ Implementation Details

### 1. User Inputs
- Users submit prompts describing their desired content through a simple React interface.

### 2. AI-driven Script Generation
- Backend API calls OpenAI's GPT model to generate detailed scripts from prompts.

### 3. Automated media Creation
- Agentic AI selects visuals (stock footage, animations), background audio, and generates narration.

### 4. Cloud-based Storage & Management
- Generated content is stored securely in AWS S3 buckets.
- Each upload is tagged with a unique, incrementing `id_media` for efficient asset management.

### 5. Automatic Social Media Posting
- Integrated APIs for platforms like **LinkedIn** (maybe more to come), automating media posting along with relevant descriptions and hashtags.

---

## 🚩 Getting Started

### Step 1: Clone Repository
```bash
git clone https://github.com/Killianx256/LLMs-to-Agentic-AI.git
```
### Step 2: Install Dependencies
```bash
cd LLMs-to-Agentic-AI
npm install
```
### Step 3: Environment Setup
Create ```.env``` file and configure:
```
MISTRAL_API_KEY=<Your_OpenAI_API_Key>
MYSQL_URI=<Your_MySQL_URI>
AWS_ACCESS_KEY=<AWS_Access_Key>
AWS_SECRET_ACCESS_KEY=<AWS_Secret_Key>
LINKEDIN_CLIENT_ID=<Your_LinkedIn_Client_ID>
LINKEDIN_CLIENT_SECRET=<Your_LinkedIn_Client_Secret>
```

### Step 4: Run Application
```bash
npm run dev
```
Open your browser at http://localhost:3000

---

## 🌟 Features Roadmap

- Enhanced AI-driven customization (styles, tone, specific branding)
- Expanded integrations (Instagram Reels, YouTube Shorts)
- Advanced analytics dashboard

---

## 🤝 Contribution

Thanks to :

- Grégoire WORONIAK
- Lucas BARREZ
- Nicolas RENOIR
- Lucas LOPES

---

## 🙌 Credits & Acknowledgments

- **ESSEC, Kryptosphere, Utopia**: For organizing this inspiring hackathon
- **OpenAI**: Providing powerful AI models enabling advanced prompt
- **MistralAI**: Enhancing the model’s capabilities via Retrieval-Augmented Generation (RAG) for improved orchestration.
- **AWS**: Robust cloud infrastructure

---

🎉 Thank you for exploring our project! Feel free to reach out for any questions or collaborations!
