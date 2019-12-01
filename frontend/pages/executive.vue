<template>
  <v-layout column justify-center align-center>
    <div class="text-center">
      <span class="display-3">エグゼクティブになった!</span>
      <hr />
      <v-card-actions class="justify-center">
        <span>{{ executive.title }}</span>
      </v-card-actions>
    </div>
  </v-layout>
</template>

<script>
export default {
  async asyncData(ctx) {
    /*
    return {
        executive: await ctx.app.$executiveRepository.index()
    } */
  },
  data() {
    return {
      executive: { title: "huga" }
    };
  },
  methods: {
    async beExecutive() {
      const result = await this.$executiveRepository.create({
        title: "clicked"
      });
    }
  }
};
</script>
