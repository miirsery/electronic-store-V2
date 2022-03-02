export default function(instance) {
  return {
    signIn(payload) {
      let token = sessionStorage.getItem("tokenData");
      return instance.post("/api/user/token-create/", payload, {
        headers: {
          Authorization: `token ${token}`
        }
      });
    },
    signUp(payload) {
      return instance.post("api/auth/users/", payload);
    },
    logout() {
      return instance.delete("auth/logout/");
    }
  };
}
