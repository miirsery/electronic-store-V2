export default function(instance) {
  return {
    uploadPhoto(payload) {
      return instance.post("api/upload-photo/", payload);
    },
    updateProfile(payload) {
      return instance.patch("api/update-profile/", payload);
    },
  };
}