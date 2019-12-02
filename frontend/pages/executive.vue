<template>
  <v-layout column justify-center align-center>
    <div class="text-center">
      <span class="display-3">エグゼクティブになった!</span>
      <hr />
      <v-card-actions class="justify-center">
        <span>{{ executive.username }}</span>
      </v-card-actions>
    </div>
  </v-layout>
</template>

<script>
export default {
  async asyncData(ctx) {
    return {
      executive: await ctx.app.$executiveRepository.get(1).catch(error => {
        console.log(error);
        return {
          executive: {}
        };
      })
    };
  },
  data() {
    return {
      executive: {}
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
