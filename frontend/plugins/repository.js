import repositoryFactory from "~/api/repository";

export default (ctx, inject) => {
  // inject the repository in the context (ctx.app.$repository)
  // And in the Vue instances (this.$repository in your components)
  const factory = repositoryFactory(ctx.$axios);
  inject("executiveRepository", factory("/executives"));

  // You can reuse the repositoryWithAxios object:
  // inject("userRepository", repositoryWithAxios('/users'));
};
