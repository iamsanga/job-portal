<template>
  <div  class="small-container">
    <nav>
      <router-link to="/recruiter" >
        <h5>Go Back</h5></router-link>
        <router-link to="/"> <h5>Logout</h5></router-link>
    </nav>
    <p
      v-if="jobs.length < 1"
      class="empty-table"
    >
      No Jobs Received!, Please check later :)
    </p>
    <table v-else>
      <thead>
        <tr>
          <th>Job Name</th>
          <th>Description</th>
          <th>Location</th>
          <th>Applicants</th>
        </tr>
      </thead>
      <tbody>
        <tr  :key="job.id"  v-for="job in jobs">

          <td>{{job.jobname}}</td>

          <td >{{job.description}}</td>

          <td>{{job.location}}</td>

          <td>{{job.applied}}</td>



        </tr>
      </tbody>
    </table>
  </div>

</template>

<script>

export default {
  name: "Received",
  components: {

  },
  data() {
    return {
      jobs: [],
    };
  },

  mounted() {
    this.getJobs();
  },

  methods: {
    async getJobs() {
      try {
        const response = await fetch(
          "http://localhost:8081/jobs/received",
          {
          method: "GET"
          }
        );
        const data = await response.json();
        // console.log(response);
        if (response.status == 200){
          this.jobs = data;
        }

      } catch (error) {
        console.error(error);
      }
    }


  },
};
</script>

<style>


.small-container {
  max-width: 680px;
}
</style>
