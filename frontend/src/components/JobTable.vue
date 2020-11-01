<template>
  <div id="job-table">
    <p
      v-if="jobs.length < 1"
      class="empty-table"
    >
      No Jobs!, Try to create new :)
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
          <td v-if="editing === job.id">
            <input
              type="text"
              v-model="job.jobname"
            >
          </td>
          <td v-else>{{job.jobname}}</td>
          <td v-if="editing === job.id">
            <input
              type="text"
              v-model="job.description"
            >
          </td>
          <td v-else>{{job.description}}</td>
          <td v-if="editing === job.id">
            <input
              type="text"
              v-model="job.location"
            >
          </td>
          <td v-else>{{job.location}}</td>
          <td v-if="editing === job.id">
            <button class ='edit' @click="editJob(job)">Save</button>
            <button class = 'edit'
              @click="editing = null"
            >Cancel</button>
          </td>
          <td v-else>
            <button class ='edit' @click="editMode(job.id)">Edit</button>
            <button class ='del' @click="$emit('delete-job', job.id)">Delete</button>
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
    editMode(id) {
      this.editing = id
    },

    editJob(job) {
      if (job.jobname === '' || job.description === '' || job.location === '') return
      this.$emit('edit-job', job.id, job)
      this.editing = null
    }
  }
}
</script>

<style scoped>
button.edit{
  background: #2c3e50;
  border: 1px solid #2c3e50;
  margin: 0 0.5rem 0 0;
}

button.edit:hover,
button.edit:active,
button.edit:focus {
  background: #32a95d;
  border: 1px solid #32a95d;
}
button.del{
  background: #2c3e50;
  border: 1px solid #2c3e50;
  margin: 0 0.5rem 0 0;
}

button.del:hover,
button.del:active,
button.del:focus {
  background: #ac0d0d;
  border: 1px solid #ac0d0d;
}

input {
  margin: 0;
}

.empty-table {
  text-align: center;
}
</style>
