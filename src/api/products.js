export default function(instance) {
  return {
    get(id) {
      return instance.get(`products/${id}`);
    },
    getAll() {
      return instance.get("products");
    }
  };
}