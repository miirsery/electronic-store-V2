export default {
  async load(action, errHandler) {
    try {
      await action();
    } catch (error) {
      if (errHandler) {
        errHandler();
      } else {
        console.log(error.response.data);
      }
    }
  },
};
