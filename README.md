# IT Revolution test task

## Project Description

In today's social media landscape, the need to share links is ubiquitous. However, many platforms impose constraints on post length, hindering effective link sharing. Addressing this challenge, our project aims to introduce the "Mini-Link" service, a solution for link shortening and enhanced user engagement.

### Key Features:

1. Simplified Interface: an intuitive interface for easy link creation and access to statistics.

2. Robust Database Management: storage of both shortened and original links for reliability and scalability.

3. Flexible Technology: utilization of diverse web technologies for adaptability and future-proofing.

4. Docker-Compose Integration: streamlined deployment and management for enhanced efficiency.

5. Transparent Collaboration: project code hosted on GitHub for transparency and collaboration.

Functionality:

- Link Management: efficient storage and redirection of shortened and original links.
  
- Statistical Insights: provision of insightful statistics on link popularity for user analysis.
  
- Link Creation: effortless generation of new shortened links to broaden content accessibility and reach.

## Running via Docker (it takes a time!)

1. Install / open Docker
2. Run `docker-compose up --build` at the terminal

## Running locally

### Backend

#### Installing using Github

Python 3.11+ is a must

1. Clone the repository in the terminal:
`git clone https://github.com/Nattalli/it-revolution-test-task.git`
2. Make the following command and populate it with required data:
`cp .env.example .env`
3. Create virtual env:
`python -m venv venv`
4. Setup virtual env:
    * On Windows: `venv\Scripts\activate`
    * On Linux or MacOS: `source venv/bin/activate`
5. Go to the `backend` folder: 
`cd backend`
6. And mark it as the source root 
7. Install requirements: `pip install -r requirements.txt`
8. Make migrations: `python manage.py migrate`
9. Now you can run it: `python manage.py runserver`

### Frontend

1. Go to the `frontend` folder:
   `cd frontend`
2. Install requirements: `npm i`
3. Run the frontend part: `npm run dev`
