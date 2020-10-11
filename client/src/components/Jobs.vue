<template>
  <div>
    <nav class="navbar navbar-dark bg-dark">
        <a class="navbar-brand" href="#"><strong>Applicant Tracker</strong></a>
        <a class="nav-item nav-link" href="#" style="color:#fff;" v-if="is_logged_in" v-on:click="do_logout()">Logout</a>
    </nav>
    <login_view v-if="is_logged_in == false"> </login_view>
    <div v-else class="container">
    <br><h2>Job Dashboard</h2>
    <div class="row">
      <div class="col-md-4"></div>
      <div class="col-md-4"><b-button block v-b-modal.form_input v-if="is_recruiter" variant="primary">+ Add New Job</b-button></div>
      <div class="col-md-4"></div>
    </div>
    <hr>
    <div class="row">
        <table id='dtable' class="table table-hover table-bordered table-sm" width="100%" cellspacing=0 v-if="jobs">
        <thead class="thread-dark">
          <tr>
            <th scope="col">Job ID</th>
            <th scope="col">Title</th>
            <th scope="col">Company Name</th>
            <th scope="col">Location</th>
            <th scope="col">Creator</th>
            <th scope="col">Details</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(job, index) in jobs" v-bind:key="job.id">
            <td>{{job.id}}</td>
            <td>{{job.title}}</td>
            <td>{{job.company_name}}</td>
            <td>{{job.location}}</td>
            <td>{{job.creator}}</td>
            <td><center><b-button v-b-modal.form_modal variant="primary" v-on:click="update_modal(index)">More Info</b-button></center></td>
            <td v-if="is_recruiter">
              <center>
                <b-button variant="danger" v-on:click="delete_job(job.id)">Delete</b-button>
              </center>
            </td>
            <td v-else>
              <center>
                <b-button disabled variant="light" v-if="job.is_applied" >Applied</b-button>
                <b-button variant="success" v-else v-on:click="apply_job(job.id)">Apply</b-button>
              </center>
            </td>
          </tr>
        </tbody>
      </table>
      </div>
      <!-- modal for displaying details of the job -->
      <b-modal id="form_modal" size="lg" ok-only scrollable title="Job Info" v-if="modal_Data">
      <div class="form-group">
        <div class="p-1 row">
          <div class='col-md-4'><label>Job ID</label></div>
          <div class='col-md-8'>{{modal_Data.id}}</div>
        </div>
        <div class="p-1 row">
          <div class='col-md-4'><label>Job Title</label></div>
          <div class='col-md-8'>{{modal_Data.title}}</div>
        </div>
        <div class="p-1 row">
          <div class='col-md-4'><label>Company Name</label></div>
          <div class='col-md-8'>{{modal_Data.company_name}}</div>
        </div>
        <div class="p-1 row">
          <div class='col-md-4'><label>Job Location</label></div>
          <div class='col-md-8'>{{modal_Data.location}}</div>
        </div>
        <div class="p-1 row">
          <div class='col-md-4'><label>Job Creator</label></div>
          <div class='col-md-8'>{{modal_Data.creator}}</div>
        </div>
        <div class="p-1 row">
          <div class='col-md-4'><label>Job Description</label></div>
          <div class='col-md-8'>{{modal_Data.desc}}</div>
        </div>
      </div>
      </b-modal>

      <!-- modal for creating new Jobs for the recruited -->
      <b-modal size="lg" id="form_input" hide-footer scrollable title="Add new Job" v-if="is_recruiter">
        <form id="new_job">
          <div class="p-1 row">
            <div class='col-md-4'><label for="title">Job Title </label></div>
            <div class='col-md-8'><input type="text" class="form-control" name="title" id="title" required placeholder="Enter Job Title"></div>
          </div>
          <div class="p-1 row">
            <div class='col-md-4'><label for="c_name">Company Name </label></div>
            <div class='col-md-8'><input type="text" class="form-control" name="c_name" id="c_name" required placeholder="Enter Company Name"></div>
          </div>
          <div class="p-1 row">
            <div class='col-md-4'><label for="location">Job Location </label></div>
            <div class='col-md-8'><input type="text" class="form-control" name="location" id="location" required placeholder="Enter Job Location"></div>
          </div>
          <div class="p-1 row">
            <div class='col-md-4'><label for="desc">Job Description </label></div>
            <div class='col-md-8'><textarea class="form-control" name="desc" id="desc" rows="3" required placeholder="Enter Job Description"></textarea></div>
          </div>
          <div class="p-1 row">
            <div class='col'><center><b-button variant="success" v-on:click="create_job()">Submit</b-button></center></div>
            <div class='col'><center><b-button variant="secondary" v-on:click="form_reset('new_job')">Reset</b-button></center></div>
          </div>
        </form>
      </b-modal>
    </div>
  </div>
</template>


<script>
  import axios from 'axios';
  import Login from './Login.vue';

  export default {
    name: 'Jobs',
    components: {
      "login_view" : Login
      },
    data() {
      return {
        jobs: null,
        modal_Data: null,
        is_logged_in: null,
        is_recruiter: null
      };
    },
    created: function() {
      this.verify_auth();
      if (this.is_logged_in) {
        axios
          .get('http://localhost:8000/api/jobs')
          .then(res => {
            this.jobs = res.data;
          })
          .catch(error => console.log(error))
      }
    },
    methods: {
      update_modal: function(job_id) {
        // Update the modal dynamically
        this.modal_Data = this.jobs[job_id]
      },
      apply_job: function(data) {
        // for appling to the job.
        var post_data = {email: this.get_user_login()}
        axios
          .put('http://localhost:8000/api/job/' + data, post_data, { headers: { 'Authorization': `user `+this.get_user_login() }})
          .then(res => {
            alert(res.data.msg);
            location.href="/"
          })
          .catch(error => {
            console.log(error)
            alert("Error While Deleting the job !!");
          })
      },
      delete_job: function(id) {
        // for deleting the job.
        axios
          .delete('http://localhost:8000/api/job/' + id, { headers: { 'Authorization': `user `+this.get_user_login() }})
          .then(res => {
            alert(res.data.msg);
            location.href="/"
          })
          .catch(error => {
            console.log(error)
            alert("Error While Deleting the job !!");
          })
      },
      create_job: function() {
        // creates job - permitted only for recruiter
        var desc = document.getElementById('desc').value.trim();
        var loc = document.getElementById('location').value.trim();
        var c_name = document.getElementById('c_name').value.trim();
        var title = document.getElementById('title').value.trim();

        if (desc == "" || title == "" || location == "" || c_name == "") {
          alert ("Please Enter all information to create the job");
          return;
        }
        var post_data = {
          desc: desc,
          location: loc,
          company_name: c_name,
          title: title,
          creator: this.get_user_login()
        }
        axios
          .post('http://localhost:8000/api/job', post_data, { headers: { 'Authorization': `user `+this.get_user_login() }})
          .then(res => {
            alert("New Job created for " + res.data.title);
            location.href="/"
          })
          .catch(error => {
            console.log(error)
            alert("Error While Creating the job !!");
          })
      },
      form_reset: function(id) {
        // resets the modal form -- just a helper utility
        var form_obj = document.getElementById(id);
        //alert(id + " " + form_obj);
        form_obj.reset();
      },
      do_logout: function() {
        // helps to user to logout -- will clear off the cookie & reloads the page
        this.$cookies.remove("user")
        alert("User has logged out !");
        location.href="/"
      },
      verify_auth: function() {
        // verify if the user is logged in & if logged in, verifies if its a candidate or recruiter
        var user_data = this.$cookies.get("user")
        this.is_logged_in = (user_data != null)
        if (this.is_logged_in) {
          this.is_recruiter = user_data["is_recruiter"]
          this.is_logged_in = true
        }
      },
      get_user_login: function() {
        // get user id from the cookie.. id cookie has expired, it reloads the page
        var user = this.$cookies.get("user");
        if (user == null) {
          alert("Session has expired");
          location.href ="/"
        }
        return user['id']
      }
    }
  }
</script>

<style>
  h3 {
    margin-bottom: 5%;
  }
</style>
