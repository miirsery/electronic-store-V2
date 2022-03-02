import axios from "axios";

export default function(instance) {
  return {
    signIn(payload) {
      let token = sessionStorage.getItem("tokenData").replace(/['"«»]/g, "");
      return instance.post("/api/user/token-create/", payload, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });
    },
    signUp(payload) {
      return instance.post("api/auth/users/", payload);
    },
    logout() {
      // return instance.delete("auth/logout/");
      return axios.get("https://jsonplaceholder.typicode.com/users");
    }
  };
}
