<template>
  <div id="job-table">
    <h1>Jobs Available:</h1>
    <p
      v-if="jobs.length < 1"
      class="empty-table"
    >
      No Jobs Found!, Please check later :)
    </p>
    <table v-else>
      <thead>
        <tr>
          <th>Job Name</th>
          <th>Description</th>
          <th>Location</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          :key="job.id"
          v-for="job in jobs"
        >

          <td>{{job.jobname}}</td>

          <td >{{job.description}}</td>

          <td>{{job.location}}</td>

          <td >

            <button class ='apply' v-if="!job.isApplied"
            @click="applyJob(job)"> Apply
           </button>
           <button class ="applied" v-else :disabled="true" > Applied
          </button>
            <!-- <p v-else> Applied </p> -->
          </td>

        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'job-table',
  props: {
    jobs: Array,
  },
  data() {
    return {
      editing: null,
    }
  },
  methods: {

    applyJob(job) {
       this.$emit('apply-job', job.id,job)
      // console.log(req)
      // if( req.detail === "Applied"){
      //   job.isApplied = true;
      // }
    }
  }
}
</script>

<style scoped>
button.apply{
  background: #2c3e50;
  border: 1px solid #2c3e50;
  margin: 0 0.5rem 0 0;
}
button.applied{
  background: #32a95d;
  border: 1px solid #32a95d;
  margin: 0 0.5rem 0 0;
}
button.apply:hover,
button.apply:active,
button.aplly:focus {
  background: #32a95d;
  border: 1px solid #32a95d;
}

input {
  margin: 0;
}

.empty-table {
  text-align: center;
}
</style>
