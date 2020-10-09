<template>
  <div class="container">
  <br><h2>Job Dashboard</h2>
  <hr>
      <table id='dtable' class="table table-hover table-bordered table-sm" width="100%" cellspacing=0 v-if="jobs">
      <thead class="thread-dark">
        <tr>
          <th scope="col">Job ID</th>
          <th scope="col">Title</th>
          <th scope="col">Company Name</th>
          <th scope="col">Location</th>
          <th scope="col">Creator</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="job in jobs" v-bind:key="job.id">
          <td>{{job.id}}</td>
          <td>{{job.title}}</td>
          <td>{{job.company_name}}</td>
          <td>{{job.location}}</td>
          <td>{{job.creator}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script>
  import axios from 'axios';

  export default {
    name: 'Jobs',
    data() {
      return {
        jobs: null,
      };
    },
    created: function() {
      axios
        .get('http://localhost:8000/api/jobs')
        .then(res => {
          this.jobs = res.data;
        })
    }
  }
</script>

<style>
  h3 {
    margin-bottom: 5%;
  }
</style>
