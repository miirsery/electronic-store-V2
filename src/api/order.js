export default function (instance) {
  return {
    sendOrder(payload) {
      return instance.post("order", payload);
    },
  };
}