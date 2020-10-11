# FastAPI-Applicant-Tracker
Simple Applicant Job tracker system using Python FastAPI &amp; Vue.js

## Backend
- Python 3.8
- FastAPI
- Pydantic

## Frontend
- Vue.js
- Axios
- VueCookies
- BootstrapVue

Currently, the client and the server are made to run on localhost on two different ports. FastAPI CORS is configured for the same purpose.

API Endpoints
- /api/jobs [GET]             -- list all jobs
- /api/job [POST]             -- Create new job
- /api/job/{job_id} [GET]     -- list the particular job
- /api/job/{job_id} [PUT]     -- Apply for a certain job (updating a job)
- /api/job/{job_id} [DELETE]  -- Delete the particular job

Ways to Improve:
- Proper Authentication - JWT (currently no authentication is used but the pageview is based on type of user connected - recruiter or candidate)
- Update the definition of User Modal and User Scheme with the data as needed.
- ORM modals & relationships need to be updated to make this more scalable.
- Add more endpoints to perform necessary activities with User Modal.
- Considering I am still a beginner in Vue.js, Frontend can be made even more better using Vue-router.
- Middleware can be re-defined for making this an advanced application.

Application working screenshots

- Login Page (no auth is programmed for simplicity use)\
![login Page](https://github.com/RSMuthu/FastAPI-Applicant-Tracker/blob/master/imgs/login_page.PNG)
- Candidate View Page (Based on the user selected on Login page)\
![Candidate Page](https://github.com/RSMuthu/FastAPI-Applicant-Tracker/blob/master/imgs/candidate_page.PNG)
- Modal view of a Job on Candidate's page\
![Job modal on Candidate's Page](https://github.com/RSMuthu/FastAPI-Applicant-Tracker/blob/master/imgs/job_modal.PNG)
- Recruiter View Page (Based on the user selected on Login Page)\
![Recruiter Page](https://github.com/RSMuthu/FastAPI-Applicant-Tracker/blob/master/imgs/recruiter_page.PNG)
- Modal View for entering new Job details on Recruiter's page
![New Job Modal view](https://github.com/RSMuthu/FastAPI-Applicant-Tracker/blob/master/imgs/new_job_modal.PNG)

This application is not deployed yet.\
**_Further, Shall work on the Deployment_**
