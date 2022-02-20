export default function (instance) {
  return {
    sendOrder(payload) {
      return instance.post("orders", payload);
    },
  };
}