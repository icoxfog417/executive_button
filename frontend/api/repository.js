// Provide nuxt-axios instance to use same configuration across the whole project
// I've used typical CRUD method names and actions here
export default $axios => resource => ({
  index() {
    if (process.env.BACKEND_HOST) {
      $axios.setHeader("X-Host-Override", process.env.BACKEND_HOST);
    }
    return $axios.$get(`${resource}`);
  },

  get(id) {
    if (process.env.BACKEND_HOST) {
      $axios.setHeader("X-Host-Override", process.env.BACKEND_HOST);
    }
    return $axios.$get(`${resource}/${id}`);
  },

  create(payload) {
    if (process.env.BACKEND_HOST) {
      $axios.setHeader("X-Host-Override", process.env.BACKEND_HOST);
    }
    return $axios.$post(`${resource}`, payload);
  },

  update(id, payload) {
    if (process.env.BACKEND_HOST) {
      $axios.setHeader("X-Host-Override", process.env.BACKEND_HOST);
    }
    return $axios.$post(`${resource}/${id}`, payload);
  },

  delete(id) {
    if (process.env.BACKEND_HOST) {
      $axios.setHeader("X-Host-Override", process.env.BACKEND_HOST);
    }
    return $axios.$delete(`${resource}/${id}`);
  }
});
