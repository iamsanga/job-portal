<template>
  <div  class="small-container">
    <nav>
    <router-link to="/received" >
      <h5>Received Applicants</h5></router-link>
    <router-link to="/"> <h5>Logout</h5></router-link>

  </nav>
  <br>
    <job-form @add-job="addJobs" />
    <job-table :jobs="jobs" @delete-job="deleteJob" @edit-job="editJob" />

  </div>

</template>

<script>
import JobTable from "@/components/JobTable.vue";
import JobForm from "@/components/JobForm.vue";

export default {
  name: "Recruiter",
  components: {
    JobTable,
    JobForm,
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
          "http://localhost:8081/jobs",
          {
          method: "GET"
          }
        );
        const data = await response.json();
        // console.log(data);
        this.jobs = data;
      } catch (error) {
        console.error(error);
      }
    },

    async addJobs(job) {
      try {
        const response = await fetch(
          "http://localhost:8081/jobs",
          {
            method: "POST",
            body: JSON.stringify(job)
            // headers: { "Content-type": "application/json; charset=UTF-8" },
          }
        );
        const data = await response.json();
        this.jobs = [...this.jobs, data];
      } catch (error) {
        console.error(error);
      }
    },

    async editJob(id, updatedJob) {
      try {
        const response = await fetch(
          `http://localhost:8081/jobs/${id}`,
          {
            method: "PUT",
            body: JSON.stringify(updatedJob),
            // headers: { "Content-type": "application/json; charset=UTF-8" },
          }
        );
        const data = await response.json();
        this.jobs = this.jobs.map((job) => (job.id === id ? data : job));
      } catch (error) {
        console.error(error);
      }
    },

    async deleteJob(id) {
      try {
        await fetch(`http://localhost:8081/jobs/${id}`, {
          method: "DELETE",
        });
        this.jobs = this.jobs.filter((job) => job.id !== id);
      } catch (error) {
        console.error(error);
      }
    },
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
