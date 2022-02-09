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
    title: "Catalog",
    alias: "catalog",
    url: "/catalog"
  },
  {
    // path: '/:PathMatch(.*)*',
    path: "/:CatchAll(.*)",
    name: "404",
  }
];
