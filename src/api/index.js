import instance from "@/api/instance";
import authModule from "@/api/auth";
import products from "@/api/products";
import catalog from "@/api/catalog";
import order from "@/api/order";
import user from "@/api/user";

export default {
  auth: authModule(instance),
  products: products(instance),
  catalog: catalog(instance),
  order: order(instance),
  user: user(instance)
};
