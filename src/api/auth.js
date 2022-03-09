export default function (instance) {
  return {
    signIn(payload) {
      return instance.post("api/user/token-create/", payload);
    },
    signUp(payload) {
      return instance.post("api/auth/users/", payload);
    },
    getInfo() {
      return instance.get("api/user/user-auth/");
    }
  };
}
