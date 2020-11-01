<template>
  <div id="job-form">
    <h1>Job Creation Dashboard</h1>
    <br />
    <form @submit.prevent="handleSubmit">
      <label>Job Name</label>
      <input
        ref="first"
        type="text"
        :class="{ 'has-error': submitting && invalidName }"
        v-model="job.jobname"
        @focus="clearStatus"
        @keypress="clearStatus"
      />
      <label>Description</label>
      <input
        type="text"
        :class="{ 'has-error': submitting && invalidDescription }"
        v-model="job.description"
        @focus="clearStatus"
      />
      <label>Location</label>
      <input
        type="text"
        :class="{ 'has-error': submitting && invalidLocation }"
        v-model="job.location"
        @focus="clearStatus"
      />
      <p v-if="error && submitting" class="error-message">
        ❗Please fill out all required fields
      </p>
      <p v-if="successful !== null " class="success-message">✅ Job successfully added</p>
      <button>Create</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "job-form",
  data() {
    return {
      error: false,
      submitting: false,
      successful: null,
      job: {
        jobname: "",
        description: "",
        location: "",
      },
    };
  },
  computed: {
    invalidName() {
      return this.job.jobname === "";
    },

    invalidDescription() {
      return this.job.description === "";
    },
    invalidLocation() {
      return this.job.location === "";
    },
  },
  methods: {
    handleSubmit() {
      this.clearStatus();
      this.submitting = true;

      if (this.invalidName || this.invalidDescription || this.invalidLocation) {
        this.error = true;
        return;
      }else {
        this.successful = true;
      }
      //
      this.$emit("add-job", this.job);

      this.$refs.first.focus();
      this.job = {
        jobname: "",
        description: "",
        location: "",
      };
      this.clearStatus();
      this.successfull = null;
      this.submitting = false;
    },

    clearStatus() {
      this.successfull = null;
      this.error = false;
    },
  },
};
</script>

<style scoped>
form {
  margin-bottom: 2rem;
}

[class*="-message"] {
  font-weight: 500;
}

.error-message {
  color: #d33c40;
}

.success-message {
  color: #32a95d;
}
</style>
