<template>
  <div  class="small-container">
    <nav>
    <router-link to="/"> <h5>Logout</h5></router-link>

    </nav>
  <br>
    <job-table :jobs="jobs"  @apply-job="applyJob" />

  </div>

</template>

<script>
import JobTable from "@/components/CandidateTable.vue";

export default {
  name: "Candidate",
  components: {
    JobTable,

  },
  data() {
    return {
      jobs: [],
      applied: false,
    };
  },

  mounted() {
    this.getJobs();
  },

  methods: {
    async getJobs() {
      try {
        const response = await fetch(
          "http://localhost:8081/jobs",
          {
          method: "GET"
          }
        );
        const data = await response.json();
        // console.log(data);
        this.jobs = data.map(
          x=>{
            x.isApplied = false;
            return x;
          });
      } catch (error) {
        console.error(error);
      }
    },

    async applyJob(id,job) {
      try {
        const response = await fetch(
          `http://localhost:8081/jobs/apply/${id}`,
          {
            method: "PUT"
            // headers: { "Content-type": "application/json; charset=UTF-8" },
          }
        );
         const data = await response.json();
         if (data.detail == "Applied"){
               job.isApplied= true
         }
         // console.log(data)

      } catch (error) {
        console.error(error);
      }
    }


  },
};
</script>

<style>
button {
  background: #2c3e50;
  border: 1px solid #2c3e50;
}

button:hover,
button:active,
button:focus {
  background: #32a95d;
  border: 1px solid #32a95d;
}

.small-container {
  max-width: 680px;
}
</style>
