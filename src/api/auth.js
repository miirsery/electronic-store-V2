import axios from "axios";

export default function(instance) {
  return {
    signIn(payload) {
      return instance.post("api/user/token-create/", payload);
    },
    signUp(payload) {
      return instance.post("api/auth/users/", payload);
    },
    test() {
      return instance.get("api/user/user-auth/")
    },
    logout() {
      // return instance.delete("auth/logout/");
      return axios.get("https://jsonplaceholder.typicode.com/users");
    }
  };
}
