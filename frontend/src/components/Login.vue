<template>
  <div class="login">

    <strong class="logo">Recruiter</strong> - U: recruiter@abc.in P: passw0rd
    <br>
    <strong class="logo">Candidate</strong> - U: candidate@abc.in P: passw0rd
    <el-card>
      <h2>Login</h2>
      <el-form
        class="login-form"
        :model="model"
        :rules="rules"
        ref="form"
        @submit.native.prevent="login"
      >
        <el-form-item prop="username">
          <el-input v-model="model.username" placeholder="Username" prefix-icon="fas fa-user"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="model.password"
            placeholder="Password"
            type="password"
            prefix-icon="fas fa-lock"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button
            :loading="loading"
            class="login-button"
            type="primary"
            native-type="submit"
            block
          >Login</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
// import Router from '../router'
export default {
  name: "login",
  data() {
    return {
      validCredentials: {
        recruiter:{
        username: "recruiter@abc.in",
        password: "passw0rd"
      },
      candidate:{
        username: "candidate@abc.in",
        password: "passw0rd"
      }
      },
      model: {
        username: "",
        password: ""
      },
      loading: false,
      rules: {
        username: [
          {
            required: true,
            message: "Username is required",
            trigger: "blur"
          },
          {
            min: 4,
            message: "Username length should be at least 5 characters",
            trigger: "blur"
          }
        ],
        password: [
          { required: true, message: "Password is required", trigger: "blur" },
          {
            min: 5,
            message: "Password length should be at least 5 characters",
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    simulateLogin() {
      return new Promise(resolve => {
        setTimeout(resolve, 800);
      });
    },
    async login() {
      let valid = await this.$refs.form.validate();
      if (!valid) {
        return;
      }
      this.loading = true;
      await this.simulateLogin();
      this.loading = false;
      if (
        this.model.username === this.validCredentials.recruiter.username &&
        this.model.password === this.validCredentials.recruiter.password ||
        this.model.username === this.validCredentials.candidate.username &&
        this.model.password === this.validCredentials.candidate.password
      ) {
        this.$message.success("Login successfull");
        if(this.model.username === this.validCredentials.recruiter.username){
          this.$router.push({ name: "Recruiter" }).catch(()=>{});
        }
        if(this.model.username === this.validCredentials.candidate.username){
          this.$router.push({ name: "Candidate" }).catch(()=>{});
        }


      } else {
        this.$message.error("Username or password is invalid");
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-button {
  width: 100%;
  margin-top: 40px;
}
.login-form {
  width: 290px;
}
.forgot-password {
  margin-top: 10px;
}
</style>
<style lang="scss"  >



//   body   {
//   margin: 0;
//   padding: 0;
//   background: #102a43;
//   background-size: contain;
// }

.login  {
  padding: 20px 20px;
  color: #000000;
  display: flex;
  flex-direction: column;
  align-items: center;

  .version {
    font-family: "Open Sans";
    padding: 0 10px;
    color: #000000;
    font-size: 12px;
    margin-top: 5px;
  }
}
.login {
  padding: 10px 20px;
  .logo {
    font-family: "Open Sans";
    letter-spacing: 3px;
    padding-top: 15px;
    padding-bottom: 15px;
  }
  .logo .part-2 {
    color: #000000;
  }
}
//
//
//










$teal: rgb(0, 124, 137);
.el-button--primary {
  background: $teal;
  border-color: $teal;

  &:hover,
  &.active,
  &:focus {
    background: lighten($teal, 7);
    border-color: lighten($teal, 7);
  }
}
.login .el-input__inner:hover {
  border-color: $teal;
}
.login .el-input__prefix {
  background: rgb(238, 237, 234);
  left: 0;
  height: calc(100% - 2px);
  left: 1px;
  top: 1px;
  border-radius: 3px;
  .el-input__icon {
    width: 30px;
  }
}
.login .el-input input {
  padding-left: 35px;
}
.login .el-card {
  padding-top: 0;
  padding-bottom: 30px;
}
h2 {
  font-family: "Open Sans";
  letter-spacing: 1px;
  font-family: Roboto, sans-serif;
  padding-bottom: 20px;
  padding-left: 95px;
  color: #000000;

}
a {
  color: $teal;
  text-decoration: none;
  &:hover,
  &:active,
  &:focus {
    color: lighten($teal, 7);
  }
}
.login .el-card {
  width: 340px;
  display: flex;
  justify-content: center;
}
</style>
