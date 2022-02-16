import axios from "axios";

const instance = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com",
  withCredentials: true,
  headers: {
    accept: "application/json"
  }
});
export default instance