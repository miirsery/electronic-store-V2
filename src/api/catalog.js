export default function (instance) {
  return {
    get(id) {
      return instance.get(`catalog/${id}`);
    },
    getAll() {
      return instance.get("catalog");
    },
  };
}
