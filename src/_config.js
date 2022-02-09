export const process = {
  dev: true
};
export const site = {
  home: process.dev ? "http://localhost:8080/" : "https://www.google.com/"
};

export const app = {
  title: 'Shop',
};

export const links = [
  {
    title: "Home",
    alias: "home",
    url: "/"
  },
  {
    title: "Categories",
    alias: "categories",
    url: "/categories"
  }
];
