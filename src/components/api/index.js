import instance from "@/components/api/instance";
import authModule from "@/components/api/auth";
export default {
  auth: authModule(instance())
}