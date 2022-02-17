import instance from "@/api/instance";
import authModule from "@/api/auth";
import products from "@/api/products";
import catalog from "@/api/catalog";
export default {
  auth: authModule(instance),
  products: products(instance),
  catalog: catalog(instance)
}